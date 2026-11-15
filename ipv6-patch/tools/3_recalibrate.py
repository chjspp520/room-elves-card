# -*- coding: utf-8 -*-
"""patch4：按爱快 4.0 实机抓包校准 IPv6 连接详情接口。

实机抓包结论（爱快 4.0 路由后台，iKuai OS V4）：
  POST /Action/call
  {"func_name":"monitor_lanipv6","action":"show",
   "param":{"TYPE":"conn,conn_num","ip":"<完整8段IPv6>","proto":"all","interface":"all","limit":""}}
  resp {"code":0,"message":"Success","results":{"conn":[...],"current_count":2,
        "protocol_stats":{"tcp":2},"interface_stats":{"wan1":2},"conn_num":2}}

  * 参数名只有 ip 有效；ipv6 / ipv6_addr 返回 code=0 但 conn 为空。
  * ip 必须是完整 8 段带前导零的地址；压缩格式（省零、::）实测 conn_num=0。
  * conn 行真实字段：protocol status dst_addr src_port dst_port forward_addr
    app_name interface total_up total_down domain。
  * 4.0 信封 {code,message,results} 已被 patch1 正确解析，data=results。
"""
import io, hashlib, sys

PATH = 'room-elves-card.js'
s = io.open(PATH, encoding='utf-8', errors='replace').read()
orig_len = len(s)
n = 0


def rep(old, new, tag):
    global s, n
    c = s.count(old)
    assert c == 1, '%s: anchor count=%d (expect 1)' % (tag, c)
    s = s.replace(old, new, 1)
    n += 1
    print('  [%d] %s  (%d -> %d chars)' % (n, tag, len(old), len(new)))


# ---- 1. 地址展开 + 连接地址选择 + 精确载荷 ----
OLD_PAYLOADS = ('_ikuaiAllV6ConnPayloads(e){const t=this._ikuaiAllV6Addr(e)||"",'
                'i=String((e||{}).mac||""),n=["ip","ipv6","ipv6_addr"],a=[];'
                'for(let r=0;r<n.length;r++){const o={TYPE:"conn,conn_num",interface:"all",'
                'proto:"all",maxnum:500,limit:"0,100",ORDER_BY:"",ORDER:""};'
                'o[n[r]]=t,i&&(o.mac=i),a.push({func_name:"monitor_lanipv6",action:"show",'
                'param:o})}return a},')

NEW_METHODS = r'''
_ikuaiAllV6Expand(e){const t=String(null==e?"":e).trim().toLowerCase().split("%")[0];if(t.indexOf(":")<0||t.indexOf(".")>=0)return String(null==e?"":e).trim();const a=t.split("::");if(a.length>2)return t;const r=a.length>1?(a[0]?a[0].split(":"):[]):[],i=a.length>1?(a[1]?a[1].split(":"):[]):[],o=a.length>1?r.length+i.length:t.split(":").length;if(o>8)return t;const c=8-o,l=[];for(let d=0;d<c;d++)l.push("0");const u=a.length>1?r.concat(l,i):t.split(":");if(8!==u.length)return t;const h=[];for(let d=0;d<8;d++){const f=String(u[d]||"").replace(/[^0-9a-f]/g,"");if(!f||f.length>4)return t;h.push(("0000"+f).slice(-4))}return h.join(":")},
_ikuaiAllV6ConnAddr(e){const t=e||{},i=["ip_addr","ipv6_addr","ipv6addr","ip6addr","ip","addr","address","ipv6","ip6","global_addr","ipv6_ip","forward_addr","link_addr","link_local"],n=this._ikuaiAllV6Addr(t)||"";for(let a=0;a<i.length;a++){const r=t[i[a]];if(null!=r&&""!==r&&"object"!=typeof r){const o=String(r).trim();if(o.indexOf(":")>=0&&0!==o.toLowerCase().indexOf("fe80:"))return this._ikuaiAllV6Expand(o)}}return this._ikuaiAllV6Expand(n)},
_ikuaiAllV6ConnPayloads(e){const t=this._ikuaiAllV6ConnAddr(e)||"",i=this._ikuaiAllV6Addr(e)||"",n={TYPE:"conn,conn_num",ip:t,proto:"all",interface:"all",limit:""},a=[{func_name:"monitor_lanipv6",action:"show",param:n}];if(i&&i!==t){const r=this._ikuaiAllV6Expand(i);if(r&&r!==t)a.push({func_name:"monitor_lanipv6",action:"show",param:Object.assign({},n,{ip:r})})}return a},
'''.strip('\n')

rep(OLD_PAYLOADS, NEW_METHODS, '载荷：单 ip 参数 + 地址展开 + 与抓包一致的 param')

# ---- 2. 连接卡片补 domain 域名 ----
rep('a("协议 / 状态",[r,o].filter(Boolean).join(" · ")),a("应用",l),a("目的地址",',
    'a("协议 / 状态",[r,o].filter(Boolean).join(" · ")),a("应用",l),'
    'a("域名",this._ikuaiAllV6ConnField(i,["domain","host","hostname","dname"])),a("目的地址",',
    '连接卡片补 domain 域名')

# ---- 3. 成功提示加入接口汇总字段 ----
rep('if(v.length){a.textContent="重新查询",o=!1,r.appendChild(this._ikuaiAllEl("div","ikuai-card-hint","连接详情 · "+v.length+" 条（monitor_lanipv6），累计流量已换算单位"));',
    'if(v.length){const w=g&&g.data||{},A=[],B=Number(w.conn_num),C=w.protocol_stats,D=w.interface_stats,'
    'E=x=>{if(!x||"object"!=typeof x)return"";const y=Object.keys(x);return y.slice(0,4).map(z=>z+" "+x[z]).join(" / ")};'
    'if(isFinite(B))A.push("接口报告 "+B+" 条");if(E(C))A.push("协议 "+E(C));if(E(D))A.push("线路 "+E(D));'
    'a.textContent="重新查询";o=!1;'
    'r.appendChild(this._ikuaiAllEl("div","ikuai-card-hint","连接详情 · "+v.length+" 条（monitor_lanipv6，累计流量已换算单位）"+(A.length?" · "+A.join(" · "):"")));',
    '成功提示接入 conn_num / protocol_stats / interface_stats')

# ---- 4. 失败提示改为已实机校准的文案 ----
rep('h?"接口返回成功，但该终端当前没有连接记录":"未取到 IPv6 连接详情（已尝试 "+p.length+" 种参数）。爱快该接口可能与预期不同：可在路由 Web 后台「状态监控 → IPv6 → 终端详情」查看；把浏览器 F12 网络面板里那条请求的载荷发我，即可精确适配。"',
    'h?"接口已按爱快 4.0 实机抓包校准（monitor_lanipv6），返回成功但该终端当前没有活跃连接；若只看到 fe80:: 链路地址，说明暂无全球单播地址。":"未取到 IPv6 连接详情（已尝试 "+p.length+" 种地址格式）。接口 monitor_lanipv6 / TYPE=conn,conn_num 已按爱快 4.0 实机抓包校准；请确认 switch.ikuai_api 已开启，且该终端在「状态监控 → IPv6 终端监控」里存在全球单播地址。"',
    '失败提示更新为实机校准说明')

# ---- 5. today_total 等真实累计字段纳入换算 ----
rep('/^(total_up|total_down|total_up_bytes|total_down_bytes|up_bytes|down_bytes|upload_bytes|download_bytes|up_total|down_total|bytes_up|bytes_down|total_upload|total_download)$/i.test(String(e||""))',
    '/^(total_up|total_down|total_up_bytes|total_down_bytes|up_bytes|down_bytes|upload_bytes|download_bytes|up_total|down_total|bytes_up|bytes_down|total_upload|total_download|today_total|today_up|today_down|today_bytes)$/i.test(String(e||""))',
    '换算字段补 today_total（集成 ipv6_entries 真实字段）')

# ---- 6. 地址字段优先级：ip_addr（真实 GUA 字段名）提前，link_addr 靠后 ----
rep('_ikuaiAllV6Addr(e){const t=e||{},i=["ipv6_addr","ipv6addr","ip6addr","ip_addr","ip","addr","address","ipv6","ip6","link_addr","link_local","global_addr","ipv6_ip"];',
    '_ikuaiAllV6Addr(e){const t=e||{},i=["ip_addr","ipv6_addr","ipv6addr","ip6addr","ip","addr","address","ipv6","ip6","global_addr","ipv6_ip","link_addr","link_local"];',
    '地址优先级：ip_addr 提前、link_addr 后置')

# ---- 7. 名称字段补 termname（集成真实字段） ----
rep('_ikuaiAllV6Name(e){const t=e||{},i=["comment","hostname","name","client_device","client_model","username","dtalk_name"];',
    '_ikuaiAllV6Name(e){const t=e||{},i=["comment","termname","hostname","name","client_device","client_model","username","dtalk_name"];',
    '名称字段补 termname')

# ---- 8. 中文标签补真实字段 ----
rep('connect_num:"连接数",upload:"上行"',
    'termname:"终端名",today_total:"今日累计",uprate:"上行速率",downrate:"下行速率",domain:"域名",client_vendor:"终端厂商",client_model:"设备型号",interface:"接口",uptime:"上线时长",connect_num:"连接数",upload:"上行"',
    '中文标签补 termname / today_total / domain 等')

# ---- 9. 弹窗说明文案：明确单位口径 + 连接详情已实机校准 ----
rep('数据来自 sensor.ikuai_lan_hosts 的 ipv6_entries；字段随爱快固件版本（含 4.x）不同。上行 / 下行为实时速率（字节/秒）、累计上行 / 下行为累计字节，已按 1024 进制换算为 KB / MB / GB（速率带 /s，与爱快后台口径一致）。',
    '数据来自 sensor.ikuai_lan_hosts 的 ipv6_entries（整行字段按集成原样展示）。上行 / 下行为实时速率（字节/秒）、累计上下行与今日累计为累计字节，均按 1024 进制换算为 KB / MB / GB（速率带 /s，与爱快后台口径一致）。连接详情走 monitor_lanipv6，已按爱快 4.0 实机抓包校准。',
    '弹窗说明更新为实机校准口径')

# ---- 10. 排序优先字段补充 ----
rep('s=["ipv6_addr","ipv6addr","ip6addr","ip_addr","ip","addr","address","mac","hostname","comment","name","client_device","client_model","client_type","connect_num","upload","download","total_up","total_down","uptime","timestamp"];',
    's=["ip_addr","ipv6_addr","ipv6addr","ip6addr","ip","addr","address","mac","comment","termname","hostname","name","client_device","client_model","client_vendor","client_type","connect_num","upload","download","uprate","downrate","today_total","total_up","total_down","interface","uptime","timestamp"];',
    '弹窗字段排序补真实字段')

io.open(PATH, 'w', encoding='utf-8', newline='').write(s)
print('\nreplacements=%d  %d -> %d chars (+%d)' % (n, orig_len, len(s), len(s) - orig_len))
for k in ['_ikuaiAllV6Expand(e)', '_ikuaiAllV6ConnAddr(e)', '"domain","host"',
          '接口报告 ', 'today_total|today_up', '已按爱快 4.0 实机抓包校准']:
    print('  %-40s %d' % (k, s.count(k)))
PY = None
