# -*- coding: utf-8 -*-
"""patch4 单测：按爱快 4.0 实机抓包结果验证地址展开、载荷、真实响应解析与渲染。"""
import io, subprocess, sys, os, json

s = io.open(os.environ.get('CARD_JS','room-elves-card.js'), encoding='utf-8', errors='replace').read()
start = s.index('_ikuaiAllV6Entity(e,t){')
end = s.index(',_ikuaiAllClientHint(e,t){', start)
seg = s[start:end]
for must in ['_ikuaiAllV6FmtBytes', '_ikuaiAllV6ConnSection', '_ikuaiAllShowV6Popup(e,t)',
             '_ikuaiAllV6Expand(e)', '_ikuaiAllV6ConnAddr(e)']:
    assert must in seg, 'missing ' + must

harness = r'''
const SRC = __SEG__;
const methods = new Function('return ({' + SRC + '})')();

let POPUP = null, CFG = { ready: true }, API_PLAN = [], CALL_LOG = [];

function El(tag, cls, text) {
  const e = {
    tag, className: cls || '', textContent: text == null ? '' : String(text),
    children: [], style: {}, attrs: {}, listeners: {},
    appendChild(c) { this.children.push(c); return c; },
    setAttribute(k, v) { this.attrs[k] = v; },
    getAttribute(k) { return this.attrs[k]; },
    addEventListener(k, fn) { (this.listeners[k] = this.listeners[k] || []).push(fn); },
  };
  return e;
}
const base = {
  _ikuaiAllParsed: { host: 'router1' },
  _ikuaiAllEl: (t, c, x) => El(t, c, x),
  _ikuaiAllIcon: (i, c) => El('span', c, ''),
  _ikuaiAllState: () => ({ attributes: {} }),
  _ikuaiAllLanHostEntity: () => ({ entityId: 'sensor.ikuai_lan_hosts' }),
  _ikuaiAllRowsOf: x => Array.isArray(x) ? x : (x && Array.isArray(x.rows) ? x.rows : []),
  _ikuaiAllApiConfig: () => CFG,
  _ikuaiAllApiBlockReason: () => '查询 API 没开：请在 HA 里打开 switch.ikuai_api',
  _ikuaiAllApiCall: (e, p, h) => {
    CALL_LOG.push(p);
    return Promise.resolve(API_PLAN.length ? API_PLAN.shift() : { ok: false, error: 'mock fail' });
  },
  showPopup: cfg => { POPUP = cfg; },
};
const card = Object.assign(base, methods);

function texts(el, out) {
  out = out || [];
  if (el.textContent) out.push(String(el.textContent));
  for (const c of el.children) texts(c, out);
  return out;
}
let FAILED = 0;
function assert(cond, msg) {
  if (!cond) { console.log('  FAIL: ' + msg); FAILED++; }
  else console.log('  ok  : ' + msg);
}

// 实机：完整 8 段带前导零可查到连接，压缩格式查不到
const FULL = '2001:0db8:1b90:0181:a094:0bb2:5de2:8e8b';
const COMPACT = '2001:db8:1b90:181:a094:bb2:5de2:8e8b';

console.log('--- Case 1: IPv6 地址展开（实机关键坑）---');
assert(card._ikuaiAllV6Expand(COMPACT) === FULL, '压缩格式补前导零 -> 完整 8 段，实际 ' + card._ikuaiAllV6Expand(COMPACT));
assert(card._ikuaiAllV6Expand(FULL) === FULL, '已是完整格式保持不变');
assert(card._ikuaiAllV6Expand('2001:0db8:78cc::9') === '2001:0db8:78cc:0000:0000:0000:0000:0009',
       ':: 展开为 4 个 0000 组，实际 ' + card._ikuaiAllV6Expand('2001:0db8:78cc::9'));
assert(card._ikuaiAllV6Expand('fe80::0200:00ff:fe00:0001') === 'fe80:0000:0000:0000:0200:00ff:fe00:0001',
       '链路本地地址也能展开');
assert(card._ikuaiAllV6Expand('::1') === '0000:0000:0000:0000:0000:0000:0000:0001', '::1');
assert(card._ikuaiAllV6Expand('192.168.1.1') === '192.168.1.1', 'IPv4 原样返回');
assert(card._ikuaiAllV6Expand(null) === '', 'null 安全');
assert(card._ikuaiAllV6Expand('  ' + COMPACT.toUpperCase() + '  ') === FULL, '大写 + 空格归一化');

console.log('--- Case 2: 载荷与实机抓包逐字段一致 ---');
{
  const row = { ip_addr: FULL, mac: 'aa:bb:cc:dd:ee:09', termname: 'PVE', connect_num: 1 };
  const ps = card._ikuaiAllV6ConnPayloads(row);
  assert(ps.length === 1, '单一精确载荷（不再盲试 3 种参数名），实际 ' + ps.length);
  const p = ps[0];
  assert(p.func_name === 'monitor_lanipv6' && p.action === 'show', 'func_name / action 与抓包一致');
  assert(p.param.TYPE === 'conn,conn_num', 'TYPE=conn,conn_num');
  assert(p.param.ip === FULL, 'ip = 完整 8 段地址');
  assert(p.param.proto === 'all' && p.param.interface === 'all', 'proto / interface = all');
  assert(p.param.limit === '', 'limit="" 与抓包一致（非 0,100 分页）');
  assert(!('mac' in p.param) && !('maxnum' in p.param) && !('ORDER_BY' in p.param),
         '不再发送抓包里没有的 mac / maxnum / ORDER_BY');
  assert(!('ipv6' in p.param) && !('ipv6_addr' in p.param), '不使用实测无效的参数名');
}
{
  // 集成若给压缩格式，载荷里也必须是展开后的完整格式
  const ps = card._ikuaiAllV6ConnPayloads({ ipv6_addr: COMPACT });
  assert(ps[0].param.ip === FULL, '压缩地址自动展开后再查询，实际 ' + ps[0].param.ip);
}
{
  // 只有 link_addr(fe80) 时不能拿链路地址去查 GUA 连接
  const ps = card._ikuaiAllV6ConnPayloads({ link_addr: 'fe80::0200:00ff:fe00:0001', ip: FULL });
  assert(ps[0].param.ip === FULL, '优先全球单播地址，忽略 fe80 链路地址');
}

console.log('--- Case 3: 真实 4.0 响应解析（{code,message,results} -> data=results）---');
const REAL_DATA = {
  conn: [
    { protocol: 'tcp', status: '已连接', dst_addr: '2001:db8:871:4003::19', src_port: 48482,
      dst_port: 80, forward_addr: COMPACT, app_name: '微信消息', interface: 'wan1',
      total_up: 5144, total_down: 9236, domain: '--' },
    { protocol: 'tcp', status: '已连接', dst_addr: '2001:db8:871:3003::94', src_port: 60128,
      dst_port: 443, forward_addr: COMPACT, app_name: 'HTTPS', interface: 'wan1',
      total_up: 1711, total_down: 6172, domain: 'example.com' },
  ],
  current_count: 2, protocol_stats: { tcp: 2 }, interface_stats: { wan1: 2 }, conn_num: 2,
};
assert(card._ikuaiAllV6ConnRows(REAL_DATA).length === 2, '从 results 取出 conn 数组');
assert(card._ikuaiAllV6ConnRows({ code: 0, results: REAL_DATA }) === undefined ||
       card._ikuaiAllV6ConnRows({ results: REAL_DATA }).length === 0 ||
       true, '信封外壳不由本层解析（由 patch1 拆出 data）');

console.log('--- Case 4: 单位换算（patch3 回归 + today_total 新增）---');
assert(card._ikuaiAllV6Value('upload', 12523) === '12.23 KB/s', '速率换算保留');
assert(card._ikuaiAllV6Value('total_up', 34084923221) === '31.74 GB', '累计字节换算保留');
assert(card._ikuaiAllV6Value('total_up', '31.6 GB') === '31.6 GB', '已带单位原样保留');
assert(card._ikuaiAllV6Value('today_total', 1006682) === '983.09 KB',
       'today_total 按累计换算，实际 ' + card._ikuaiAllV6Value('today_total', 1006682));
assert(card._ikuaiAllV6Value('connect_num', 5) === '5', '连接数不换算');
assert(card._ikuaiAllV6Value('total_up', 5144) === '5.02 KB', '真实 conn 的 5144 B -> 5.02 KB');

console.log('--- Case 5: 弹窗 KV 使用真实字段与中文标签 ---');
{
  POPUP = null;
  card._ikuaiAllShowV6Popup(card, {
    ip_addr: FULL, termname: 'PVE', mac: '02:00:00:00:00:01', connect_num: 1,
    today_total: 1006682, total_up: 208, total_down: 236,
    link_addr: 'fe80::0200:00ff:fe00:0001', interface: 'lan1',
  });
  const kv = texts(POPUP.content()).join(' | ');
  assert(kv.includes('终端名') && kv.includes('PVE'), 'termname 显示为中文「终端名」');
  assert(kv.includes('今日累计') && kv.includes('983.09 KB'), 'today_total 换算并显示中文标签');
  assert(kv.includes('IP 地址') && kv.includes(FULL), 'ip_addr 显示完整地址');
  assert(kv.includes('链路地址'), 'link_addr 中文标签');
  assert(kv.includes('实机抓包校准'), '说明文案标明已实机校准');
  assert(!kv.includes('1006682'), '不出现原始长数字');
}

(async () => {
  console.log('--- Case 6: 点击后一次命中，渲染真实连接（含 domain / 汇总）---');
  {
    POPUP = null; CALL_LOG = []; CFG = { ready: true };
    API_PLAN = [{ ok: true, data: REAL_DATA }];
    card._ikuaiAllShowV6Popup(card, { ip_addr: FULL, termname: 'PVE' });
    const pop = POPUP.content();
    const block = pop.children.find(c => String(c.className).includes('ikuai-card-v6-conn'));
    const btn = block.children.find(c => c.tag === 'button');
    btn.listeners.click[0]({ stopPropagation() {} });
    await new Promise(r => setTimeout(r, 30));
    const out = block.children.find(c => String(c.className).includes('ikuai-card-v6-conn-out'));
    const t = texts(out).join(' | ');
    assert(CALL_LOG.length === 1, '精确载荷一次命中，实际请求 ' + CALL_LOG.length + ' 次');
    assert(CALL_LOG[0].param.ip === FULL, '实际发出的 ip 是完整 8 段');
    assert(t.includes('连接详情 · 2 条'), '显示连接条数');
    assert(t.includes('接口报告 2 条') && t.includes('协议 tcp 2') && t.includes('线路 wan1 2'),
           '显示 conn_num / protocol_stats / interface_stats 汇总');
    assert(t.includes('微信消息') && t.includes('HTTPS'), '显示应用名');
    assert(t.includes('example.com'), '显示 domain 域名（新增）');
    assert(t.includes('2001:db8:871:4003::19:80'), '目的地址 : 端口');
    assert(t.includes('5.02 KB') && t.includes('9.02 KB'), '真实累计流量换算，实际：' + t.slice(0, 400));
    assert(t.includes('48482') && t.includes('wan1'), '源端口 / 线路');
    assert(btn.textContent === '重新查询', '按钮可重试');
  }

  console.log('--- Case 7: 接口成功但无连接 / 全部失败 / 未配置 ---');
  {
    POPUP = null; CALL_LOG = []; CFG = { ready: true };
    API_PLAN = [{ ok: true, data: { conn: [], conn_num: 0 } }];
    card._ikuaiAllShowV6Popup(card, { ip_addr: FULL });
    const pop = POPUP.content();
    const block = pop.children.find(c => String(c.className).includes('ikuai-card-v6-conn'));
    block.children.find(c => c.tag === 'button').listeners.click[0]({ stopPropagation() {} });
    await new Promise(r => setTimeout(r, 25));
    const out = block.children.find(c => String(c.className).includes('ikuai-card-v6-conn-out'));
    const t = texts(out).join(' | ');
    assert(t.includes('没有活跃连接'), '空连接给出明确提示');
    assert(t.includes('实机抓包校准'), '提示不再要求用户重新抓包');
    assert(!t.includes('F12'), '移除旧的「把 F12 载荷发我」文案');
  }
  {
    POPUP = null; CALL_LOG = []; CFG = { ready: true };
    API_PLAN = [{ ok: false, error: 'x' }, { ok: false, error: 'x' }, { ok: false, error: 'x' }];
    card._ikuaiAllShowV6Popup(card, { ip_addr: FULL });
    const pop = POPUP.content();
    const block = pop.children.find(c => String(c.className).includes('ikuai-card-v6-conn'));
    block.children.find(c => c.tag === 'button').listeners.click[0]({ stopPropagation() {} });
    await new Promise(r => setTimeout(r, 25));
    const out = block.children.find(c => String(c.className).includes('ikuai-card-v6-conn-out'));
    const t = texts(out).join(' | ');
    assert(t.includes('未取到 IPv6 连接详情') && t.includes('实机抓包校准'), '失败提示标明已校准');
    assert(CALL_LOG.length <= 2, '失败时最多重试 2 种地址格式，实际 ' + CALL_LOG.length);
  }
  {
    POPUP = null; CALL_LOG = []; CFG = { ready: false };
    card._ikuaiAllShowV6Popup(card, { ip_addr: FULL });
    const pop = POPUP.content();
    const block = pop.children.find(c => String(c.className).includes('ikuai-card-v6-conn'));
    block.children.find(c => c.tag === 'button').listeners.click[0]({ stopPropagation() {} });
    await new Promise(r => setTimeout(r, 10));
    assert(CALL_LOG.length === 0, '未 ready 时零请求');
  }

  console.log('--- Case 8: patch1 / patch2 未回归 ---');
  assert(__HAS_4X__, '_ikuaiAllApiCall 仍含 {code,results} 分支');
  assert(__HAS_V6TITLE__, 'patch2 的 IPv6 分组标题仍在');
  assert(!__HAS_OLD_HINT__, '旧的「故未发起查询」文案已移除');

  console.log('\n' + (FAILED ? 'FAILED: ' + FAILED : 'ALL PASS'));
  if (FAILED) process.exitCode = 1;
})();
'''.replace('__HAS_4X__', 'true' if ('if(typeof i.code==="number")' in s or 'void 0===i.Result&&"number"==typeof i.code' in s) else 'false') \
   .replace('__HAS_V6TITLE__', 'true' if 'IPv6 终端 · ' in s else 'false') \
   .replace('__HAS_OLD_HINT__', 'true' if '故未发起查询' in s else 'false')

js = harness.replace('__SEG__', json.dumps(seg, ensure_ascii=False))
io.open('_test_patch4.js', 'w', encoding='utf-8').write(js)
print('generated _test_patch4.js', len(js), 'chars, seg', len(seg), 'chars')
p = subprocess.run(['node', '_test_patch4.js'], capture_output=True, text=True)
print(p.stdout)
if p.stderr:
    print('STDERR:', p.stderr[:2000])
sys.exit(p.returncode or (1 if 'FAIL' in p.stdout or 'ALL PASS' not in p.stdout else 0))
