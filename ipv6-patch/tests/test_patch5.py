# -*- coding: utf-8 -*-
"""patch5 单测：验证 IPv6 弹窗长值不再被截断、中文标签补齐、旧功能未回归。"""
import io, subprocess, sys, json, os, tempfile

SRC = os.environ.get('CARD_JS','room-elves-card.js')
s = io.open(SRC, encoding='utf-8', errors='replace').read()

# ---------- 静态 CSS / 源码断言 ----------
print('--- Case 1: 新增 CSS 规则存在且能覆盖原截断规则 ---')
ORIG_TRUNC = ('.ikuai-card-kv-v{min-width:0;color:var(--room-primary-text,#333);'
              'text-overflow:ellipsis;white-space:nowrap;font-size:11.5px;overflow:hidden}')
NEW_GRID = '.ikuai-card-kv-v6,.ikuai-card-v6-conn-card{grid-template-columns:minmax(0,auto) minmax(0,1fr)'
NEW_VAL = ('.ikuai-card-kv-v6 .ikuai-card-kv-v,.ikuai-card-v6-conn-card .ikuai-card-kv-v'
           '{white-space:normal;overflow:visible;text-overflow:clip;overflow-wrap:anywhere;'
           'word-break:break-word')
NEW_KEY = '.ikuai-card-kv-v6 .ikuai-card-kv-k,.ikuai-card-v6-conn-card .ikuai-card-kv-k{white-space:normal'


def chk(cond, msg, results):
    print(('  ok  : ' if cond else '  FAIL: ') + msg)
    results.append(bool(cond))


R = []
chk(ORIG_TRUNC in s, '原全局 .ikuai-card-kv-v 截断规则仍在（IPv4 弹窗不受影响）', R)
chk(NEW_GRID in s, '新规则：两列单对 grid-template-columns', R)
chk(NEW_VAL in s, '新规则：值 white-space:normal / overflow:visible / text-overflow:clip / wrap', R)
chk(NEW_KEY in s, '新规则：键允许换行', R)
chk(s.index(NEW_VAL) > s.index(ORIG_TRUNC), '新规则位于原截断规则之后（层叠覆盖生效）', R)
chk('.ikuai-card-v6-conn-card{padding:6px 0;border-bottom:' in s, '连接卡片分隔线', R)
chk(s.count('ikuai-card-kv-v6') >= 3, '新类名被 CSS 与 JS 引用', R)

print('--- Case 2: 仅 IPv6 路径挂载新类，IPv4 弹窗保持原样 ---')
chk('const o=this._ikuaiAllEl("div","ikuai-card-kv ikuai-card-kv-v6"),l=(e,t,i)=>{' in s,
    'IPv6 弹窗 kv 容器带 ikuai-card-kv-v6', R)
chk('const l=this._ikuaiAllEl("div","ikuai-card-kv"),c=(e,t,i,n)=>{' in s,
    'IPv4 弹窗 kv 容器仍为原始 ikuai-card-kv（未改）', R)
chk('"ikuai-card-kv ikuai-card-v6-conn-card"' in s, '连接详情卡片沿用 ikuai-card-v6-conn-card', R)

print('--- Case 3: 弹窗尺寸 / 说明文案 ---')
chk('width:520px;max-width:94vw' in s, '弹窗宽度 520px / 94vw', R)
chk('长地址 / 域名 / 时间戳会自动换行完整显示，不再截断' in s, '说明文案标注不再截断', R)

# ---------- 运行时 DOM 断言 ----------
start = s.index('_ikuaiAllV6Entity(e,t){')
end = s.index(',_ikuaiAllClientHint(e,t){', start)
seg = s[start:end]
for must in ['_ikuaiAllV6Label(e){', '_ikuaiAllShowV6Popup(e,t){', '_ikuaiAllV6ConnCard(e,t)',
             '_ikuaiAllV6ConnSection(e,t,i){', '_ikuaiAllV6Value(e,t)']:
    assert must in seg, 'segment missing ' + must

HARNESS = r'''
const SRC = __SEG__;
const methods = new Function('return ({' + SRC + '})')();
let POPUP = null, CFG = { ready: true }, API_PLAN = [], CALL_LOG = [];

function El(tag, cls, text) {
  return {
    tag, className: cls || '', textContent: text == null ? '' : String(text),
    children: [], style: {}, attrs: {}, listeners: {},
    appendChild(c) { this.children.push(c); return c; },
    setAttribute(k, v) { this.attrs[k] = v; },
    getAttribute(k) { return this.attrs[k]; },
    addEventListener(k, fn) { (this.listeners[k] = this.listeners[k] || []).push(fn); },
  };
}
const base = {
  _ikuaiAllParsed: { host: 'router1' },
  _ikuaiAllEl: (t, c, x) => El(t, c, x),
  _ikuaiAllIcon: (i, c) => El('span', c, ''),
  _ikuaiAllState: () => ({ attributes: {} }),
  _ikuaiAllLanHostEntity: () => ({ entityId: 'sensor.ikuai_lan_hosts' }),
  _ikuaiAllRowsOf: x => Array.isArray(x) ? x : (x && Array.isArray(x.rows) ? x.rows : []),
  _ikuaiAllApiConfig: () => CFG,
  _ikuaiAllApiBlockReason: () => '查询 API 没开',
  _ikuaiAllApiCall: (e, p, h) => {
    CALL_LOG.push(p);
    return Promise.resolve(API_PLAN.length ? API_PLAN.shift() : { ok: false, error: 'mock fail' });
  },
  showPopup: cfg => { POPUP = cfg; },
};
const card = Object.assign(base, methods);

function walk(el, out) { out = out || []; out.push(el); for (const c of el.children) walk(c, out); return out; }
function texts(el) { return walk(el).map(x => String(x.textContent)); }
function hasClass(el, c) { return String(el.className || '').split(/\s+/).includes(c); }
let FAILED = 0;
function assert(c, m) { if (!c) { console.log('  FAIL: ' + m); FAILED++; } else console.log('  ok  : ' + m); }

// 截图里被截断的典型字段
const FULL = '2001:0db8:1b90:0181:a094:0bb2:5de2:8e8b';
const ROW = {
  ip_addr: FULL, mac: '02:00:00:00:00:0f', comment: 'Home Assistant',
  termname: 'Home Assistant', hostname: 'Home Assistant',
  client_vendor: 'Home Assistant', client_model: '智能家居', client_type: 'Unknown',
  connect_num: 7, upload: 0, download: 0, today_total: 176800000,
  total_up: 497980000, total_down: 1040000000, interface: 'lan1',
  uptime: '2026-11-11 08:23:41', timestamp: '2026-11-11 08:23:41',
  auth_type: 0, channel: '1,155', client_typeid: '155214001', device_icon: '1,155',
  id: 2, link_addr: 'fe80::0200:00ff:fe00:0002', reject: 2, signal: 0,
  static_status: 0, uplink_addr: '02:00:00:00:00:94', uplink_dev: 'iKuai',
  vendor_icon: '2,214', vlan_id: 0, webid: '', ac_gid: 0,
};

console.log('--- Case 4: 弹窗 DOM 结构（长值完整、容器带新类）---');
POPUP = null;
card._ikuaiAllShowV6Popup(card, ROW);
const root = POPUP.content();
const all = walk(root);
const kvContainer = all.find(x => String(x.className).includes('ikuai-card-kv-v6'));
assert(!!kvContainer, '弹窗含 ikuai-card-kv-v6 容器');
const vals = all.filter(x => hasClass(x, 'ikuai-card-kv-v'));
const keys = all.filter(x => hasClass(x, 'ikuai-card-kv-k'));
assert(vals.length > 0 && vals.length === keys.length,
       'KV 成对渲染，键 ' + keys.length + ' / 值 ' + vals.length);
assert(texts(root).includes(FULL), '完整 8 段 IPv6 原样保留在 DOM（不再被截断成 ...）');
assert(!texts(root).some(t => t.includes('...')), 'DOM 文本中没有省略号截断');
assert(vals.every(v => v.attrs.title === v.textContent), '每个值仍带完整 title（桌面悬停可用）');
assert(kvContainer && !String(kvContainer.className).includes('ikuai-card-v6-conn-card'),
       '主 KV 容器与连接详情卡片类名未混淆');

console.log('--- Case 5: 截图里的英文字段已补中文标签 ---');
const label = k => card._ikuaiAllV6Label(k);
const pairs = {
  ac_gid: '接入组', channel: '信道', client_typeid: '终端类型',
  device_icon: '设备图标', static_status: '静态分配', uplink_addr: '上联 MAC',
  uplink_dev: '上联设备', vendor_icon: '厂商图标', vlan_id: 'VLAN', webid: 'Web ID',
  bssid: 'BSSID', apmac: 'AP MAC', enc: '加密方式', frequencies: '频段',
  link_local: '链路本地地址', global_addr: '全球单播地址',
};
for (const k of Object.keys(pairs)) assert(label(k) === pairs[k], k + ' -> ' + pairs[k]);
const kvText = texts(root).join(' | ');
assert(kvText.includes('接入组') && kvText.includes('信道') && kvText.includes('VLAN'),
       '弹窗实际渲染出中文字段名');
assert(!kvText.includes('ac_gid') && !kvText.includes('client_typeid'),
       '弹窗不再出现裸英文键名');

console.log('--- Case 6: 原有中文标签 / 单位换算未回归 ---');
for (const [k, v] of Object.entries({termname:'终端名', today_total:'今日累计',
                                     total_up:'累计上行', uprate:'上行速率',
                                     link_addr:'链路地址', id:'ID'}))
  assert(label(k) === v, k + ' -> ' + v);
assert(card._ikuaiAllV6Value('total_up', 34084923221) === '31.74 GB', '累计字节换算');
assert(card._ikuaiAllV6Value('upload', 12523) === '12.23 KB/s', '速率换算');
assert(card._ikuaiAllV6Value('today_total', 1006682) === '983.09 KB', 'today_total 换算');
assert(kvText.includes('176.8') || kvText.includes('168.6'), '今日累计已换算为 MB');

console.log('--- Case 7: 连接详情卡片结构与长值 ---');
const CONN = {
  protocol: 'tcp', status: '已连接', app_name: '中国联通营业厅',
  domain: 'client.example.com', dst_addr: '2001:0db8:0b00::19', dst_port: 80,
  src_port: 41368, forward_addr: FULL, interface: 'wan1',
  total_up: 3940000, total_down: 12750000,
};
const cc = card._ikuaiAllV6ConnCard(card, CONN);
const ccAll = walk(cc);
assert(hasClass(cc, 'ikuai-card-v6-conn-card'), '连接卡片带专属类（新 CSS 生效）');
assert(hasClass(cc, 'ikuai-card-kv'), '连接卡片仍是 kv 网格');
assert(texts(cc).includes('client.example.com'), '域名完整保留');
const ccVals = ccAll.filter(x => hasClass(x, 'ikuai-card-kv-v'));
assert(ccVals.every(v => v.attrs.title === v.textContent), '连接卡片每个值带完整 title');
assert(texts(cc).some(t => t.includes('3.76 MB') || t.includes('12.16 MB')), '累计流量已换算');

console.log('--- Case 8: patch4 载荷 / 地址展开未回归 ---');
const ps = card._ikuaiAllV6ConnPayloads(ROW);
assert(ps.length === 1, '单一精确载荷');
assert(ps[0].func_name === 'monitor_lanipv6' && ps[0].param.TYPE === 'conn,conn_num', '实机载荷');
assert(ps[0].param.ip === FULL, 'ip 为完整 8 段');
assert(card._ikuaiAllV6Expand('2001:0db8:78cc::9') === '2001:0db8:78cc:0000:0000:0000:0000:0009',
       ':: 展开');
assert(texts(root).join(' ').includes('不再截断'), '说明文案含「不再截断」');

console.log(FAILED === 0 ? '\nALL PASS' : '\n' + FAILED + ' FAILED');
process.exit(FAILED === 0 ? 0 : 1);
'''

js = HARNESS.replace('__SEG__', json.dumps(seg, ensure_ascii=False))
tmp = os.path.join(tempfile.gettempdir(), '_test_patch5.js')
io.open(tmp, 'w', encoding='utf-8').write(js)
print('--- 运行时 DOM 断言 ---')
p = subprocess.run(['node', tmp], capture_output=True, text=True, encoding='utf-8', errors='replace')
print(p.stdout, end='')
if p.stderr:
    print('STDERR:', p.stderr[:1500])
runtime_ok = (p.returncode == 0)

print()
print('=== 总计 ===')
print('  静态断言:', sum(R), '/', len(R), '通过')
print('  运行时  :', 'ALL PASS' if runtime_ok else 'FAILED')
ok = all(R) and runtime_ok
print('  RESULT  :', 'PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
