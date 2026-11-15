# -*- coding: utf-8 -*-
"""在 v6.14.72-patch1（已含 iKuai 4.0 信封兼容）基础上叠加 IPv6 客户端查看。

只改渲染层，不动 _ikuaiAllApiCall 的 4.0 分支。
"""
import io, os, shutil, sys

BASE = 'base_patch1.js'
OUT = 'room-elves-card.js'

if not os.path.exists(BASE):
    shutil.copyfile(OUT, BASE)

s = io.open(BASE, encoding='utf-8', errors='replace').read()
orig_len = len(s.encode('utf-8'))

# v7.0.1 基线：上游已内置 iKuai 4.0 {code,results} 信封兼容，本补丁不再重复插入
assert s.count('void 0===i.Result&&"number"==typeof i.code') == 1, \
    '基线不是 v7.0.1（缺少上游内置的 4.0 信封兼容分支）'


METHODS = r'''_ikuaiAllV6Entity(e,t){const i=t||e&&e.host||null;return this._ikuaiAllLanHostEntity(i)},
_ikuaiAllV6HostState(e,t){const i=this._ikuaiAllV6Entity(e,t);return i?this._ikuaiAllState(i.entityId)||{attributes:{}}:{attributes:{}}},
_ikuaiAllV6Entries(e,t){const i=this._ikuaiAllV6HostState(e,t);return this._ikuaiAllRowsOf(i.attributes&&i.attributes.ipv6_entries)},
_ikuaiAllV6Addr(e){const t=e||{},i=["ipv6_addr","ipv6addr","ip6addr","ip_addr","ip","addr","address","ipv6","ip6","link_addr","link_local","global_addr","ipv6_ip"];for(let n=0;n<i.length;n++){const a=t[i[n]];if(null!=a&&""!==a&&"object"!=typeof a&&String(a).indexOf(":")>=0)return String(a)}for(let n=0;n<i.length;n++){const a=t[i[n]];if(null!=a&&""!==a&&"object"!=typeof a)return String(a)}return""},
_ikuaiAllV6Name(e){const t=e||{},i=["comment","hostname","name","client_device","client_model","username","dtalk_name"];for(let n=0;n<i.length;n++){const a=t[i[n]];if(null!=a&&""!==a&&"Unknown"!==a&&"未知"!==a&&"object"!=typeof a)return String(a)}return this._ikuaiAllV6Addr(e)||"未知设备"},
_ikuaiAllV6Fp(e){try{return JSON.stringify(e||{})}catch(t){return String(e)}},
_ikuaiAllV6Text(e){if(null==e)return"";if("object"==typeof e){try{return JSON.stringify(e)}catch(t){return String(e)}}return String(e)},
_ikuaiAllV6Label(e){const t={ipv6_addr:"IPv6 地址",ipv6addr:"IPv6 地址",ip6addr:"IPv6 地址",ip_addr:"IP 地址",ip:"IP 地址",addr:"地址",address:"地址",mac:"MAC",hostname:"主机名",comment:"备注",name:"名称",client_device:"设备",client_model:"型号",client_type:"系统",connect_num:"连接数",upload:"上行",download:"下行",total_up:"累计上行",total_down:"累计下行",uptime:"上线时长",timestamp:"时间戳",reject:"已拒绝",interface:"接口",ssid:"SSID",apname:"AP",signal:"信号",username:"用户名",auth_type:"认证方式",link_addr:"链路地址",id:"ID"};return t[e]||e},
_ikuaiAllBuildV6Row(e,t){const i=t||{},n=this._ikuaiAllEl("div","ikuai-card-row ikuai-card-client-row ikuai-card-v6-row");n._ikuaiV6=i,n.appendChild(this._ikuaiAllEl("div","ikuai-card-client-dot on"));const a=this._ikuaiAllEl("div","ikuai-card-row-main"),o=this._ikuaiAllEl("div","ikuai-card-client-title");o.appendChild(this._ikuaiAllEl("span","ikuai-card-client-name",this._ikuaiAllV6Name(i)));const r=this._ikuaiAllEl("span","ikuai-card-client-badge","IPv6");r.style.color="var(--room-primary-text,#333)",r.style.background="#00000010",o.appendChild(r),a.appendChild(o);const s=[],l=this._ikuaiAllV6Addr(i),c=String(i.mac||"");l&&s.push({text:l,cls:"is-mono"}),c&&s.push({text:c,cls:"is-mono"}),i.connect_num&&s.push({text:"连接 "+i.connect_num,cls:"is-num"}),(i.client_device||i.client_model)&&s.push({text:[i.client_device,i.client_model].filter(e=>e&&"Unknown"!==e).join(" "),cls:""});const d=this._ikuaiAllEl("div","ikuai-card-client-meta");for(let u=0;u<s.length;u++)u&&d.appendChild(this._ikuaiAllEl("span","ikuai-card-client-meta-sep","·")),d.appendChild(this._ikuaiAllEl("span","ikuai-card-client-meta-part"+(s[u].cls?" "+s[u].cls:""),s[u].text));a.appendChild(d),n.appendChild(a),n.addEventListener("click",t=>{t.stopPropagation(),this._ikuaiAllShowV6Popup(e,i)});return n},
_ikuaiAllShowV6Popup(e,t){const i=t||{},n=this._ikuaiAllEl("div","ikuai-card-client-pop"),a=this._ikuaiAllEl("div","ikuai-card-client-pop-head");a.appendChild(this._ikuaiAllIcon("mdi:ip-network","ikuai-card-client-pop-icon")),a.appendChild(this._ikuaiAllEl("div","ikuai-card-client-pop-title",this._ikuaiAllV6Name(i))),n.appendChild(a);const o=this._ikuaiAllEl("div","ikuai-card-kv"),l=(e,t,i)=>{o.appendChild(this._ikuaiAllEl("div","ikuai-card-kv-k",e));const n=this._ikuaiAllEl("div","ikuai-card-kv-v"+(i?" "+i:""),t);n.setAttribute("title",t),o.appendChild(n)},r=Object.keys(i),s=["ipv6_addr","ipv6addr","ip6addr","ip_addr","ip","addr","address","mac","hostname","comment","name","client_device","client_model","client_type","connect_num","upload","download","total_up","total_down","uptime","timestamp"];r.sort((e,t)=>{const i=s.indexOf(e),n=s.indexOf(t);return(i<0?999:i)-(n<0?999:n)||String(e).localeCompare(String(t))});for(let u=0;u<r.length;u++){const t=r[u],n=this._ikuaiAllV6Text(i[t]);if(n)l(this._ikuaiAllV6Label(t),n,/addr|mac|ip|address/i.test(t))}n.appendChild(o),n.appendChild(this._ikuaiAllEl("div","ikuai-card-hint","数据来自 sensor.ikuai_lan_hosts 的 ipv6_entries；字段随爱快固件版本（含 4.x）不同，此处按集成原样展示。IPv4 应用流量 / 连接明细不适用于 IPv6 终端，故未发起查询。")),this.showPopup({content:()=>n,className:"ikuai-card-client-popup",style:"width:460px;max-width:92vw;max-height:84vh;max-height:84dvh;overflow:auto;border-radius:20px;padding:16px",showOverlay:!0,showBackground:!0,popupPosition:"center"})}'''


REPLACES = [
    # A) 去掉「IPv4 列表为空就早退」，否则纯 IPv6 环境下看不到任何终端
    (
        'body:t=>{if(!a.length)return void t.appendChild(this._ikuaiAllEl("div","ikuai-card-hint","当前没有在线终端"));let r=()=>{};',
        'body:t=>{let r=()=>{};if(!a.length)t.appendChild(this._ikuaiAllEl("div","ikuai-card-hint","当前没有在线 IPv4 终端"));',
        'A_earlyreturn',
    ),
    # B) 刷新函数内取 IPv6 明细，并纳入重绘指纹
    (
        'r=()=>{const t=this._ikuaiAllLanHosts(e._ikuaiAllParsed||i,n)||[],r=this._ikuaiAllSortClients(e,t),l=this._ikuaiAllClientSortState(e),c=["s:"+l.key+l.dir,String(r.length)];',
        'r=()=>{const t=this._ikuaiAllLanHosts(e._ikuaiAllParsed||i,n)||[],r=this._ikuaiAllSortClients(e,t),l=this._ikuaiAllClientSortState(e),c=["s:"+l.key+l.dir,String(r.length)],v6=this._ikuaiAllV6Entries(e._ikuaiAllParsed||i,n)||[],v6a=this._ikuaiAllV6HostState(e._ikuaiAllParsed||i,n).attributes||{};c.push("v6#"+v6.length+"#"+v6.map(e=>this._ikuaiAllV6Fp(e)).join("~"));',
        'B_r_head',
    ),
    # C) 主列表之后追加 IPv6 分组；同时修掉 a[0] 在 IPv4 为空时会抛错的隐患
    (
        'o.textContent="";for(let t=0;t<r.length;t++)o.appendChild(this._ikuaiAllBuildClientRow(e,r[t]));this._ikuaiAllClientSweep(e,o);const p=this._ikuaiAllClientHint(t,this._ikuaiAllState(a[0].entity.entityId));',
        'o.textContent="";for(let t=0;t<r.length;t++)o.appendChild(this._ikuaiAllBuildClientRow(e,r[t]));if(v6.length){const h=this._ikuaiAllEl("div","ikuai-card-hint ikuai-card-v6-title","IPv6 终端 · "+v6.length+" 台"+(v6a.ipv6_truncated?"（集成已截断）":""));h.style.marginTop="8px",h.style.fontWeight="600",o.appendChild(h);for(let u=0;u<v6.length;u++)o.appendChild(this._ikuaiAllBuildV6Row(e,v6[u]))}this._ikuaiAllClientSweep(e,o);const p=this._ikuaiAllClientHint(t,this._ikuaiAllV6HostState(e._ikuaiAllParsed||i,n));',
        'C_render',
    ),
    # D) 提示文案：从「未并入列表」改为「已列出」，并覆盖只有计数没有明细的情况
    (
        'Array.isArray(i.ipv6_entries)&&i.ipv6_entries.length&&n.push("另有 "+i.ipv6_entries.length+" 台 IPv6 终端未并入列表"),i.truncated&&n.push("列表被集成截断")',
        'Array.isArray(i.ipv6_entries)&&i.ipv6_entries.length&&n.push("下方已列出 "+i.ipv6_entries.length+" 台 IPv6 终端"),i.ipv6_truncated&&n.push("IPv6 列表被集成截断"),"number"==typeof i.ipv6_count&&i.ipv6_count>0&&!Array.isArray(i.ipv6_entries)&&n.push("集成报告 "+i.ipv6_count+" 台 IPv6 终端，但未提供明细 ipv6_entries"),i.truncated&&n.push("列表被集成截断")',
        'D_hint',
    ),
    # E) 计数：IPv4 为 0 但 IPv6 有终端时不再显示「0 台」
    (
        'if(!o.length)return"0 台";',
        'if(!o.length){const v=this._ikuaiAllV6Entries(n,a);return v.length?"IPv6 "+v.length+" 台":"0 台"}',
        'E_count',
    ),
    # F) 在客户端方法区插入新增方法
    (
        '},_ikuaiAllClientHint(e,t){',
        '},' + METHODS + ',_ikuaiAllClientHint(e,t){',
        'F_insert',
    ),
]

for old, new, name in REPLACES:
    cnt = s.count(old)
    if cnt != 1:
        print('ANCHOR FAIL', name, 'count=', cnt)
        sys.exit(1)
    s = s.replace(old, new, 1)
    print('applied', name, '+%d bytes' % (len(new.encode('utf-8')) - len(old.encode('utf-8'))))

b = s.encode('utf-8')
io.open(OUT, 'wb').write(b)
print()
print('base bytes ', orig_len)
print('patch2 bytes', len(b), 'delta', len(b) - orig_len)
print('upstream v7.0.1 4.0 envelope branch kept:', s.count('void 0===i.Result&&"number"==typeof i.code'))
print('v6 methods:', s.count('_ikuaiAllV6'), 'v6 row:', s.count('_ikuaiAllBuildV6Row'))
