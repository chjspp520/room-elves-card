# -*- coding: utf-8 -*-
"""patch5：修复 IPv6 终端详情 / 连接详情弹窗里长值被省略号截断的问题。

只作用于 IPv6 弹窗的 kv 容器（新增 ikuai-card-kv-v6 类）与连接详情卡片
（已有 ikuai-card-v6-conn-card 类）；IPv4 弹窗和其他卡片完全不动。

改动：
  1. 这两处 kv 由「四列两对」改为「两列单对」，值占满右侧整行；
  2. 值不再 nowrap / ellipsis / overflow:hidden，改为可换行完整显示；
  3. 弹窗略微放宽，补齐集成原始字段的中文标签；
  4. 连接详情卡片加轻量分隔，长列表更易读。
"""
import io, hashlib

FN = 'room-elves-card.js'
s = io.open(FN, encoding='utf-8', errors='replace').read()
orig_len = len(s)
reps = []


def rep(tag, old, new):
    n = s.count(old)
    assert n == 1, '%s: anchor count = %d (expect 1)' % (tag, n)
    reps.append((tag, old, new, len(old), len(new)))


# ---- 1) CSS：两列单对 + 值自动换行、不再省略号截断 ----
CSS_ANCHOR = '.ikuai-card-kv-v.is-wide{grid-column:2/-1}'
CSS_NEW = CSS_ANCHOR + (
    '.ikuai-card-kv-v6,.ikuai-card-v6-conn-card'
    '{grid-template-columns:minmax(0,auto) minmax(0,1fr);align-items:start;gap:4px 10px}'
    '.ikuai-card-kv-v6 .ikuai-card-kv-k,.ikuai-card-v6-conn-card .ikuai-card-kv-k'
    '{white-space:normal;overflow-wrap:anywhere;line-height:1.45;padding:1px 0}'
    '.ikuai-card-kv-v6 .ikuai-card-kv-v,.ikuai-card-v6-conn-card .ikuai-card-kv-v'
    '{white-space:normal;overflow:visible;text-overflow:clip;overflow-wrap:anywhere;'
    'word-break:break-word;line-height:1.45;padding:1px 0}'
    '.ikuai-card-v6-conn-card{padding:6px 0;border-bottom:1px solid var(--room-popup-divider,#00000014)}'
)
rep('[1] CSS 两列单对 + 值换行不截断', CSS_ANCHOR, CSS_NEW)

# ---- 2) IPv6 弹窗 kv 容器挂上专属类 ----
POP_OLD = 'const o=this._ikuaiAllEl("div","ikuai-card-kv"),l=(e,t,i)=>{'
POP_NEW = 'const o=this._ikuaiAllEl("div","ikuai-card-kv ikuai-card-kv-v6"),l=(e,t,i)=>{'
rep('[2] IPv6 弹窗 kv 加 ikuai-card-kv-v6', POP_OLD, POP_NEW)

# ---- 3) 弹窗宽度略放宽，让长 IPv6 少折行 ----
W_OLD = 'width:460px;max-width:92vw'
W_NEW = 'width:520px;max-width:94vw'
rep('[3] 弹窗宽度 460->520 / 92vw->94vw', W_OLD, W_NEW)

# ---- 4) 补齐集成原始字段的中文标签（截图里大量英文键名）----
L_OLD = 'link_addr:"链路地址",id:"ID"};return t[e]||e}'
L_ADD = (',ac_gid:"接入组",apmac:"AP MAC",bssid:"BSSID",channel:"信道",'
         'client_typeid:"终端类型",device_icon:"设备图标",device_type:"设备类型",'
         'dtalk_name:"备注名",enc:"加密方式",frequencies:"频段",'
         'static_status:"静态分配",uplink_addr:"上联 MAC",uplink_dev:"上联设备",'
         'vendor_icon:"厂商图标",vlan_id:"VLAN",webid:"Web ID",'
         'connect_status:"连接状态",link_local:"链路本地地址",global_addr:"全球单播地址",'
         'forward_addr:"外网地址",dst_addr:"目的地址",dst_port:"目的端口",src_port:"源端口",'
         'app_name:"应用",protocol:"协议",status:"状态",'
         'total_up_bytes:"累计上行",total_down_bytes:"累计下行",'
         'today_up:"今日上行",today_down:"今日下行",'
         'client_count:"终端数",ipv6_count:"IPv6 终端数",'
         'connect_time:"连接时长",conn_time:"连接时长",'
         'upload_bytes:"累计上行",download_bytes:"累计下行"')
L_NEW = 'link_addr:"链路地址",id:"ID"' + L_ADD + '};return t[e]||e}'
rep('[4] 中文字段标签补齐（30+ 个原始键）', L_OLD, L_NEW)

# ---- 5) 说明文案补一句「长值已可完整显示」 ----
H_OLD = '连接详情走 monitor_lanipv6，已按爱快 4.0 实机抓包校准。'
H_NEW = '连接详情走 monitor_lanipv6，已按爱快 4.0 实机抓包校准。长地址 / 域名 / 时间戳会自动换行完整显示，不再截断。'
rep('[5] 弹窗说明补「不再截断」', H_OLD, H_NEW)

for tag, old, new, lo, ln in reps:
    s = s.replace(old, new, 1)
    print('  %-42s %6d -> %6d chars (+%d)' % (tag, lo, ln, ln - lo))

assert len(s) > orig_len
io.open(FN, 'w', encoding='utf-8', newline='').write(s)
print('replacements =', len(reps))
print('%d -> %d chars (+%d)' % (orig_len, len(s), len(s) - orig_len))
print('sha256 =', hashlib.sha256(s.encode('utf-8')).hexdigest())
