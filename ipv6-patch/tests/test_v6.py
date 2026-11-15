# -*- coding: utf-8 -*-
"""抽出补丁后的客户端方法区，用轻量 DOM stub 在 node 里跑逻辑单测。"""
import io, subprocess, sys, os

s = io.open(os.environ.get('CARD_JS','room-elves-card.js'), encoding='utf-8', errors='replace').read()
start = s.index('_ikuaiAllClientCountText(e,t,i){')
end = s.index(',_ikuaiAllClientSortState(e){', start)
seg = s[start:end]
assert 'if(v6.length)' in seg and '_ikuaiAllV6Entries' in seg and '_ikuaiAllBuildV6Row' in seg
assert seg.count('，') >= 0

harness = r'''
const SRC = __SEG__;
const methods = new Function('return ({' + SRC + '})')();

let ATTRS = {}, V4 = [], POPUP = null, SECTION = null;

function El(tag, cls, text) {
  const e = {
    tag, className: cls || '', textContent: text == null ? '' : String(text),
    children: [], style: {}, attrs: {}, listeners: {},
    appendChild(c) { this.children.push(c); return c; },
    setAttribute(k, v) { this.attrs[k] = v; },
    getAttribute(k) { return this.attrs[k]; },
    addEventListener(k, fn) { (this.listeners[k] = this.listeners[k] || []).push(fn); },
    querySelectorAll(sel) {
      return this.children.filter(c => String(c.className).includes('ikuai-card-client-row'));
    },
  };
  return e;
}

const base = {
  _ikuaiAllParsed: { host: 'router1' },
  _ikuaiAllEl: (t, c, x) => El(t, c, x),
  _ikuaiAllIcon: (i, c) => El('span', c, ''),
  _ikuaiAllState: () => ({ attributes: ATTRS }),
  _ikuaiAllLanHostEntity: () => ({ entityId: 'sensor.ikuai_lan_hosts' }),
  _ikuaiAllRowsOf: x => Array.isArray(x) ? x : (x && Array.isArray(x.rows) ? x.rows : []),
  _ikuaiAllLanHosts: () => V4,
  _ikuaiAllSortClients: (e, t) => (t || []).slice(),
  _ikuaiAllClientSortState: () => ({ key: 'name', dir: 1 }),
  _ikuaiAllClientSortBar: () => El('div', 'ikuai-card-sortbar', ''),
  _ikuaiAllBuildClientRow: (e, t) => El('div', 'ikuai-card-row ikuai-card-client-row', 'V4:' + t.name),
  _ikuaiAllClientSweep: () => {},
  _ikuaiAllBind: () => {},
  _ikuaiAllClientName: (e, t) => t.name,
  _ikuaiAllBool: () => true,
  _ikuaiAllMacSwitches: () => ({}),
  _ikuaiAllSection: (e, t, cfg) => { SECTION = cfg; return {}; },
  showPopup: cfg => { POPUP = cfg; },
};

const card = Object.assign(base, methods);

function runCase(name, attrs, v4) {
  ATTRS = attrs; V4 = v4; POPUP = null; SECTION = null;
  const root = El('div', '', '');
  card._ikuaiAllBuildClientSection(card, root, card._ikuaiAllParsed, 'router1', v4);
  const body = El('div', '', '');
  SECTION.body(body);
  const list = body.children.find(c => String(c.className).includes('ikuai-card-client-list'));
  const hint = body.children.find(c => String(c.className) === 'ikuai-card-hint' && c !== list);
  return { body, list, hint, count: SECTION.count() };
}

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

const V6_4X = [
  { ipv6_addr: '2001:0db8:78cc::1', mac: 'aa:bb:cc:dd:ee:01', hostname: 'Phone-v6', connect_num: 5, client_device: 'iPhone' },
  { ipv6_addr: '2001:0db8:78cc::2', mac: 'aa:bb:cc:dd:ee:02', hostname: 'Pad-v6', connect_num: 2 },
  { ip_addr: 'fe80::3', mac: 'aa:bb:cc:dd:ee:03', comment: 'NAS-v6', connect_num: 9 },
];
const V4_ROWS = [
  { entry: { ip_addr: '192.168.1.2', mac: '11:22:33:44:55:01' }, entity: { entityId: 'sensor.ikuai_lan_hosts' }, allowSwitch: null, name: 'PC' },
  { entry: { ip_addr: '192.168.1.3', mac: '11:22:33:44:55:02' }, entity: { entityId: 'sensor.ikuai_lan_hosts' }, allowSwitch: null, name: 'TV' },
];

console.log('--- Case A: iKuai 4.0，IPv4 2 台 + IPv6 3 台 ---');
{
  const r = runCase('A', {
    count: 2, ipv4_count: 2, ipv6_count: 3, detail_count: 2,
    entries: [{}, {}], ipv6_entries: V6_4X, speed_limited: 0,
  }, V4_ROWS);
  assert(r.list.children.length === 6, '列表 = 2 行 IPv4 + 1 个 IPv6 标题 + 3 行 IPv6');
  const title = r.list.children.find(c => String(c.className).includes('ikuai-card-v6-title'));
  assert(!!title && title.textContent.includes('IPv6 终端 · 3 台'), '分组标题显示 3 台');
  const v6rows = r.list.children.filter(c => String(c.className).includes('ikuai-card-v6-row'));
  assert(v6rows.length === 3, '3 行 IPv6 终端');
  const t = texts(v6rows[0]).join('|');
  assert(t.includes('Phone-v6') && t.includes('2001:0db8:78cc::1') && t.includes('IPv6'), '行内显示名称 / IPv6 地址 / IPv6 标签');
  assert(String(r.hint.textContent).includes('下方已列出 3 台 IPv6 终端'), '提示从「未并入列表」改为「已列出」');
  assert(r.count.includes('在线 2') && r.count.includes('IPv6 3'), '计数 = ' + r.count);
  v6rows[0].listeners.click[0]({ stopPropagation() {} });
  assert(!!POPUP, '点击 IPv6 行弹出详情');
  const pop = POPUP.content();
  const kv = texts(pop).join('|');
  assert(kv.includes('IPv6 地址') && kv.includes('2001:0db8:78cc::1'), '详情含中文标签与 IPv6 地址');
  assert(kv.includes('MAC') && kv.includes('主机名'), '详情含 MAC / 主机名');
  assert(kv.includes('ipv6_entries'), '详情注明数据来自 ipv6_entries');
}

console.log('--- Case B: 纯 IPv6 环境（IPv4 列表为空）---');
{
  const r = runCase('B', {
    count: 0, ipv4_count: 0, ipv6_count: 2, entries: [], ipv6_entries: V6_4X.slice(0, 2),
  }, []);
  assert(r.list.children.length === 3, 'IPv4 为空时不再早退，仍渲染 1 标题 + 2 行');
  assert(r.count === 'IPv6 2 台', '计数不再显示「0 台」，实际 = ' + r.count);
  assert(texts(r.body).join('|').includes('当前没有在线 IPv4 终端'), '给出 IPv4 为空提示');
}

console.log('--- Case C: 3.x / 旧集成，无 IPv6 属性 ---');
{
  const r = runCase('C', { count: 2, entries: [{}, {}], detail_count: 2 }, V4_ROWS);
  assert(r.list.children.length === 2, '只渲染 2 行 IPv4，无 IPv6 分组');
  assert(!texts(r.body).join('|').includes('IPv6 终端'), '不出现 IPv6 分组标题');
  assert(!String(r.hint.textContent).includes('IPv6'), '提示里没有 IPv6 文案');
  assert(r.count === '在线 2', '计数 = ' + r.count);
}

console.log('--- Case D: 只有 ipv6_count，没有明细 ---');
{
  const r = runCase('D', { count: 1, ipv6_count: 7, entries: [{}] }, V4_ROWS.slice(0, 1));
  assert(r.list.children.length === 1, '不渲染空 IPv6 分组');
  assert(String(r.hint.textContent).includes('集成报告 7 台 IPv6 终端，但未提供明细'), '提示集成未给明细');
}

console.log('--- Case E: IPv6 明细被集成截断 ---');
{
  const r = runCase('E', {
    count: 2, ipv6_count: 120, entries: [{}, {}], ipv6_entries: V6_4X, ipv6_truncated: true,
  }, V4_ROWS);
  const title = r.list.children.find(c => String(c.className).includes('ikuai-card-v6-title'));
  assert(title.textContent.includes('集成已截断'), '分组标题提示截断');
  assert(String(r.hint.textContent).includes('IPv6 列表被集成截断'), '提示列表被截断');
}

console.log('--- Case F: 4.0 信封补丁未被动到 ---');
assert(__HAS_4X__, '_ikuaiAllApiCall 仍含 {code,results} 分支');
'''.replace('__HAS_4X__', 'true' if ('if(typeof i.code==="number")' in s or 'void 0===i.Result&&"number"==typeof i.code' in s) else 'false')

import json
js = harness.replace('__SEG__', json.dumps(seg, ensure_ascii=False))
io.open('_test_v6.js', 'w', encoding='utf-8').write(js)
print('generated _test_v6.js', len(js), 'chars, seg', len(seg), 'chars')
p = subprocess.run(['node', '_test_v6.js'], capture_output=True, text=True)
print(p.stdout)
if p.stderr:
    print('STDERR:', p.stderr[:2000])
sys.exit(p.returncode or (1 if 'FAIL' in p.stdout else 0))
