# -*- coding: utf-8 -*-
"""patch3 单测：单位换算、弹窗渲染、IPv6 连接详情查询与渲染。"""
import io, subprocess, sys, os, json

s = io.open(os.environ.get('CARD_JS','room-elves-card.js'), encoding='utf-8', errors='replace').read()
start = s.index('_ikuaiAllV6Entity(e,t){')
end = s.index(',_ikuaiAllClientHint(e,t){', start)
seg = s[start:end]
assert '_ikuaiAllV6FmtBytes' in seg and '_ikuaiAllV6ConnSection' in seg
assert '_ikuaiAllShowV6Popup(e,t)' in seg

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
function assert(cond, msg) {
  if (!cond) { console.log('  FAIL: ' + msg); process.exitCode = 1; }
  else console.log('  ok  : ' + msg);
}

console.log('--- Case 1: 单位换算（字节 / 速率 / 已带单位 / 非流量字段）---');
assert(card._ikuaiAllV6Value('upload', 12523) === '12.23 KB/s', 'upload 12523 B/s -> 12.23 KB/s，实际 ' + card._ikuaiAllV6Value('upload', 12523));
assert(card._ikuaiAllV6Value('download', '16768') === '16.38 KB/s', 'download 16768 -> 16.38 KB/s');
assert(card._ikuaiAllV6Value('total_up', 34084923221) === '31.74 GB', 'total_up 34084923221 -> 31.74 GB，实际 ' + card._ikuaiAllV6Value('total_up', 34084923221));
assert(card._ikuaiAllV6Value('total_down', 0) === '0 B', 'total_down 0 -> 0 B');
assert(card._ikuaiAllV6Value('total_up', '31.6 GB') === '31.6 GB', '已带单位的累计值原样保留');
assert(card._ikuaiAllV6Value('upload', '12.23 KB/s') === '12.23 KB/s', '已带单位的速率原样保留');
assert(card._ikuaiAllV6Value('connect_num', 5) === '5', '连接数不换算');
assert(card._ikuaiAllV6Value('hostname', 'Phone-v6') === 'Phone-v6', '文本字段不换算');
assert(card._ikuaiAllV6Value('uprate', 2048) === '2 KB/s', 'uprate 也按速率换算');
assert(card._ikuaiAllV6Value('total_up_bytes', 1073741824) === '1 GB', 'total_up_bytes 按累计换算');
assert(card._ikuaiAllV6Value('obj', { a: 1 }) === '{"a":1}', '对象转 JSON');
assert(card._ikuaiAllV6Value('x', null) === '', 'null 返回空');
assert(card._ikuaiAllV6FmtBytes(1536) === '1.5 KB', '1536 B -> 1.5 KB');
assert(card._ikuaiAllV6FmtBytes(1073741824) === '1 GB', '1073741824 B -> 1 GB');
assert(card._ikuaiAllV6FmtBytes(1099511627776) === '1 TB', '1 TiB -> 1 TB');

console.log('--- Case 2: 弹窗 KV 渲染使用换算后的值 ---');
{
  POPUP = null;
  const row = {
    ipv6_addr: '2001:0db8:78cc::1', mac: 'aa:bb:cc:dd:ee:01', hostname: 'Phone-v6',
    connect_num: 5, upload: 12523, download: 16768,
    total_up: 34084923221, total_down: 98765432,
  };
  card._ikuaiAllShowV6Popup(card, row);
  const pop = POPUP.content();
  const kv = texts(pop).join(' | ');
  assert(kv.includes('31.74 GB'), '详情显示换算后的累计上行');
  assert(kv.includes('12.23 KB/s'), '详情显示换算后的上行速率');
  assert(!kv.includes('34084923221'), '详情不再出现原始长数字');
  assert(kv.includes('IPv6 地址') && kv.includes('累计上行') && kv.includes('累计下行'), '中文标签仍在');
  assert(kv.includes('1024 进制换算'), '提示说明口径');
  const connBlock = pop.children.find(c => String(c.className).includes('ikuai-card-v6-conn'));
  assert(!!connBlock, '弹窗内新增「查看连接详情」区块');
  const btn = connBlock && connBlock.children.find(c => c.tag === 'button');
  assert(!!btn && btn.textContent === '查看连接详情', '按钮文案正确');
}

console.log('--- Case 3: IPv6 连接查询载荷（patch4 已按实机抓包校准为单一精确载荷）---');
{
  const row = { ip_addr: '2001:0db8:78cc:0000:0000:0000:0000:0009', mac: 'aa:bb:cc:dd:ee:09' };
  const ps = card._ikuaiAllV6ConnPayloads(row);
  assert(ps.length === 1, '单一精确载荷');
  assert(ps[0].func_name === 'monitor_lanipv6' && ps[0].action === 'show', '走 monitor_lanipv6 / show');
  assert(ps[0].param.TYPE === 'conn,conn_num', 'TYPE=conn,conn_num');
  assert(ps[0].param.ip === '2001:0db8:78cc:0000:0000:0000:0000:0009', 'ip 为完整 8 段地址');
  assert(!('mac' in ps[0].param) && !('ipv6' in ps[0].param), '不再发送实机载荷里没有的参数');
}

(async () => {
  console.log('--- Case 4: 点击后查询并渲染连接详情（单载荷一次命中）---');
  {
    POPUP = null; CALL_LOG = []; CFG = { ready: true };
    API_PLAN = [
      { ok: true, data: { conn: [
        { protocol: 'TCP', status: '已连接', app_name: 'HTTPS', dst_addr: '2001:db8:f100:13::b6',
          dst_port: 8080, src_port: 45934, forward_addr: '2001:db8:3f0:8202::1',
          total_up: 1073741824, total_down: 2684354560, interface: 'wan1' },
      ] } },
    ];
    const row = { ipv6_addr: '2001:0db8:78cc::9', mac: 'aa:bb:cc:dd:ee:09' };
    card._ikuaiAllShowV6Popup(card, row);
    const pop = POPUP.content();
    const block = pop.children.find(c => String(c.className).includes('ikuai-card-v6-conn'));
    const btn = block.children.find(c => c.tag === 'button');
    btn.listeners.click[0]({ stopPropagation() {} });
    await new Promise(r => setTimeout(r, 30));
    const out = block.children.find(c => String(c.className).includes('ikuai-card-v6-conn-out'));
    const t = texts(out).join(' | ');
    assert(CALL_LOG.length === 1, '精确载荷一次命中，实际请求 ' + CALL_LOG.length + ' 次');
    assert(t.includes('连接详情 · 1 条'), '显示连接条数');
    assert(t.includes('TCP') && t.includes('已连接'), '显示协议 / 状态');
    assert(t.includes('2001:db8:f100:13::b6:8080'), '显示目的地址 : 端口');
    assert(t.includes('1 GB') && t.includes('2.5 GB'), '连接累计上下行也换算单位，实际：' + t);
    assert(t.includes('45934') && t.includes('wan1'), '显示源端口 / 线路');
    assert(btn.textContent === '重新查询', '查询完成后按钮可重试');
  }

  console.log('--- Case 5: 全部候选失败时给出明确提示 ---');
  {
    POPUP = null; CALL_LOG = []; CFG = { ready: true };
    API_PLAN = [
      { ok: false, error: 'x' }, { ok: false, error: 'x' }, { ok: false, error: 'x' },
    ];
    card._ikuaiAllShowV6Popup(card, { ipv6_addr: '2001:db8:1::1' });
    const pop = POPUP.content();
    const block = pop.children.find(c => String(c.className).includes('ikuai-card-v6-conn'));
    const btn = block.children.find(c => c.tag === 'button');
    btn.listeners.click[0]({ stopPropagation() {} });
    await new Promise(r => setTimeout(r, 30));
    const out = block.children.find(c => String(c.className).includes('ikuai-card-v6-conn-out'));
    const t = texts(out).join(' | ');
    assert(CALL_LOG.length <= 2, '最多尝试 2 种地址格式');
    assert(t.includes('未取到 IPv6 连接详情') && t.includes('实机抓包校准'), '失败提示标明已按实机校准');
  }

  console.log('--- Case 6: 未配置查询 API 时不发请求 ---');
  {
    POPUP = null; CALL_LOG = []; CFG = { ready: false };
    card._ikuaiAllShowV6Popup(card, { ipv6_addr: '2001:db8:1::2' });
    const pop = POPUP.content();
    const block = pop.children.find(c => String(c.className).includes('ikuai-card-v6-conn'));
    const btn = block.children.find(c => c.tag === 'button');
    btn.listeners.click[0]({ stopPropagation() {} });
    await new Promise(r => setTimeout(r, 10));
    const out = block.children.find(c => String(c.className).includes('ikuai-card-v6-conn-out'));
    assert(CALL_LOG.length === 0, '未 ready 时零请求');
    assert(texts(out).join('|').includes('switch.ikuai_api'), '显示配置提示');
  }

  console.log('--- Case 7: 4.0 信封分支与 patch2 文案仍在 ---');
  assert(__HAS_4X__, '_ikuaiAllApiCall 仍含 {code,results} 分支');
  assert(__HAS_V6TITLE__, 'patch2 的 IPv6 分组标题仍在');
  assert(!__HAS_OLD_HINT__, '旧的「故未发起查询」文案已替换');
})();
'''.replace('__HAS_4X__', 'true' if ('if(typeof i.code==="number")' in s or 'void 0===i.Result&&"number"==typeof i.code' in s) else 'false') \
   .replace('__HAS_V6TITLE__', 'true' if 'IPv6 终端 · ' in s else 'false') \
   .replace('__HAS_OLD_HINT__', 'true' if '故未发起查询' in s else 'false')

js = harness.replace('__SEG__', json.dumps(seg, ensure_ascii=False))
io.open('_test_patch3.js', 'w', encoding='utf-8').write(js)
print('generated _test_patch3.js', len(js), 'chars, seg', len(seg), 'chars')
p = subprocess.run(['node', '_test_patch3.js'], capture_output=True, text=True)
print(p.stdout)
if p.stderr:
    print('STDERR:', p.stderr[:2000])
sys.exit(p.returncode or (1 if 'FAIL' in p.stdout else 0))
