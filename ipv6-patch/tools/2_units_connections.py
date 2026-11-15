# -*- coding: utf-8 -*-
"""patch3: IPv6 详情单位换算 + IPv6 连接详情查询。"""
import io, sys

PATH = 'room-elves-card.js'
b = io.open(PATH, 'rb').read()
s = b.decode('utf-8')

M = []
M.append(r'''_ikuaiAllV6Num(e){if("number"==typeof e)return isFinite(e)?e:null;if("string"!=typeof e)return null;const t=e.trim();return t&&/^\d+(?:\.\d+)?$/.test(t)&&isFinite(Number(t))?Number(t):null}''')
M.append(r'''_ikuaiAllV6FmtBytes(e){const t=this._ikuaiAllV6Num(e);if(null===t||t<0)return"";if(0===t)return"0 B";const i=["B","KB","MB","GB","TB","PB"];let n=0,a=t;for(;a>=1024&&n<i.length-1;)a/=1024,n++;const r=a.toFixed(2);return String(parseFloat(r))+" "+i[n]}''')
M.append(r'''_ikuaiAllV6FmtRate(e){const t=this._ikuaiAllV6FmtBytes(e);return t?t+"/s":""}''')
M.append(r'''_ikuaiAllV6RateKey(e){return/^(upload|download|uprate|downrate|up_rate|down_rate|upload_rate|download_rate|up_speed|down_speed|tx_rate|rx_rate)$/i.test(String(e||""))}''')
M.append(r'''_ikuaiAllV6BytesKey(e){return/^(total_up|total_down|total_up_bytes|total_down_bytes|up_bytes|down_bytes|upload_bytes|download_bytes|up_total|down_total|bytes_up|bytes_down|total_upload|total_download)$/i.test(String(e||""))}''')
M.append(r'''_ikuaiAllV6HasUnit(e){return"string"==typeof e&&/\d\s*[KMGTP]?B(?:\/s)?\s*$/i.test(e)}''')
M.append(r'''_ikuaiAllV6Value(e,t){if(null==t)return"";if("object"==typeof t)return this._ikuaiAllV6Text(t);if(this._ikuaiAllV6HasUnit(t))return String(t);const i=this._ikuaiAllV6Num(t);if(null!==i){if(this._ikuaiAllV6BytesKey(e))return this._ikuaiAllV6FmtBytes(i);if(this._ikuaiAllV6RateKey(e))return this._ikuaiAllV6FmtRate(i)}return this._ikuaiAllV6Text(t)}''')
M.append(r'''_ikuaiAllV6ConnPayloads(e){const t=this._ikuaiAllV6Addr(e)||"",i=String((e||{}).mac||""),n=["ip","ipv6","ipv6_addr"],a=[];for(let r=0;r<n.length;r++){const o={TYPE:"conn,conn_num",interface:"all",proto:"all",maxnum:500,limit:"0,100",ORDER_BY:"",ORDER:""};o[n[r]]=t,i&&(o.mac=i),a.push({func_name:"monitor_lanipv6",action:"show",param:o})}return a}''')
M.append(r'''_ikuaiAllV6ConnRows(e){if(!e||"object"!=typeof e)return[];const t=["conn","conn6","data","connections","list","conn_data"];for(let i=0;i<t.length;i++)if(Array.isArray(e[t[i]]))return e[t[i]];return[]}''')
M.append(r'''_ikuaiAllV6ConnField(e,t){const i=e||{},n=t||[];for(let a=0;a<n.length;a++){const r=i[n[a]];if(null!=r&&""!==r&&"object"!=typeof r)return String(r)}return""}''')
M.append(r'''_ikuaiAllV6ConnCard(e,t){const i=t||{},n=this._ikuaiAllEl("div","ikuai-card-kv ikuai-card-v6-conn-card");let m=0;const a=(k,v)=>{if(null==v||""===v)return;m++,n.appendChild(this._ikuaiAllEl("div","ikuai-card-kv-k",k));const o=this._ikuaiAllEl("div","ikuai-card-kv-v",v);o.setAttribute("title",v),n.appendChild(o)},r=this._ikuaiAllV6ConnField(i,["protocol","proto","app_proto"]),o=this._ikuaiAllV6ConnField(i,["status","state","conn_state","connect_status"]),l=this._ikuaiAllV6ConnField(i,["app_name","app","protocol_name"]),c=this._ikuaiAllV6ConnField(i,["dst_addr","dest_addr","dst_ip","dest_ip","dest","remote_addr","addr","address"]),d=this._ikuaiAllV6ConnField(i,["dst_port","dest_port","dport","remote_port"]),p=this._ikuaiAllV6ConnField(i,["src_port","sport","local_port","source_port"]),u=this._ikuaiAllV6ConnField(i,["forward_addr","wan_addr","nat_addr","src_addr","pub_addr","outer_addr"]),h=this._ikuaiAllV6ConnField(i,["total_up","up_bytes","upload_bytes","up_total","bytes_up"]),f=this._ikuaiAllV6ConnField(i,["total_down","down_bytes","download_bytes","down_total","bytes_down"]),g=this._ikuaiAllV6ConnField(i,["interface","iface","line","wan_name"]);a("协议 / 状态",[r,o].filter(Boolean).join(" · ")),a("应用",l),a("目的地址",c||d?(c||"—")+(d?":"+d:""):""),a("源端口",p),a("外网地址",u),a("线路 / 接口",g),a("累计上行 / 下行",h||f?(h?this._ikuaiAllV6Value("total_up",h):"—")+" / "+(f?this._ikuaiAllV6Value("total_down",f):"—"):""),m||n.appendChild(this._ikuaiAllEl("div","ikuai-card-hint","（该连接无可显示字段）"));return n}''')
M.append(r'''_ikuaiAllV6ConnSection(e,t,i){const n=this._ikuaiAllEl("div","ikuai-card-v6-conn"),a=this._ikuaiAllEl("button","ikuai-card-api-refresh","查看连接详情");a.setAttribute("type","button"),a.style.marginTop="10px",a.style.width="100%",a.style.padding="8px",a.style.borderRadius="12px",a.style.cursor="pointer";const r=this._ikuaiAllEl("div","ikuai-card-v6-conn-out");let o=!1;const l=(e&&e._ikuaiAllParsed||{}).host||null,c=()=>{if(o)return;o=!0,a.textContent="查询中…",r.textContent="";const d=this._ikuaiAllApiConfig(e,l);if(!d.ready){a.textContent="查看连接详情",o=!1,r.appendChild(this._ikuaiAllEl("div","ikuai-card-hint",this._ikuaiAllApiBlockReason(d)));return}const p=this._ikuaiAllV6ConnPayloads(t);let h=!1;const u=f=>{if(f>=p.length){a.textContent="重新查询",o=!1,r.appendChild(this._ikuaiAllEl("div","ikuai-card-hint",h?"接口返回成功，但该终端当前没有连接记录":"未取到 IPv6 连接详情（已尝试 "+p.length+" 种参数）。爱快该接口可能与预期不同：可在路由 Web 后台「状态监控 → IPv6 → 终端详情」查看；把浏览器 F12 网络面板里那条请求的载荷发我，即可精确适配。"));return}this._ikuaiAllApiCall(e,p[f],l).then(g=>{const v=g&&g.ok?this._ikuaiAllV6ConnRows(g.data):[];if(v.length){a.textContent="重新查询",o=!1,r.appendChild(this._ikuaiAllEl("div","ikuai-card-hint","连接详情 · "+v.length+" 条（monitor_lanipv6），累计流量已换算单位"));for(let y=0;y<Math.min(v.length,50);y++)r.appendChild(this._ikuaiAllV6ConnCard(e,v[y]));return}g&&g.ok&&(h=!0),u(f+1)}).catch(()=>u(f+1))};u(0)};a.addEventListener("click",c),n.appendChild(a),n.appendChild(r),i.appendChild(n)}''')

A = '\n_ikuaiAllShowV6Popup(e,t){'
B = 'const t=r[u],n=this._ikuaiAllV6Text(i[t]);if(n)l(this._ikuaiAllV6Label(t),n,/addr|mac|ip|address/i.test(t))'
C = 'n.appendChild(o),n.appendChild(this._ikuaiAllEl("div","ikuai-card-hint","数据来自 sensor.ikuai_lan_hosts 的 ipv6_entries；字段随爱快固件版本（含 4.x）不同，此处按集成原样展示。IPv4 应用流量 / 连接明细不适用于 IPv6 终端，故未发起查询。")),this.showPopup({'
C_NEW = 'n.appendChild(o),n.appendChild(this._ikuaiAllEl("div","ikuai-card-hint","数据来自 sensor.ikuai_lan_hosts 的 ipv6_entries；字段随爱快固件版本（含 4.x）不同。上行 / 下行为实时速率（字节/秒）、累计上行 / 下行为累计字节，已按 1024 进制换算为 KB / MB / GB（速率带 /s，与爱快后台口径一致）。")),this._ikuaiAllV6ConnSection(e,i,n),this.showPopup({'

for name, anchor in [('A', A), ('B', B), ('C', C)]:
    n = s.count(anchor)
    print('anchor', name, 'count=', n)
    if n != 1:
        sys.exit('anchor %s not unique' % name)

s = s.replace(A, '\n' + ',\n'.join(M) + ',\n_ikuaiAllShowV6Popup(e,t){', 1)
s = s.replace(B, 'const t=r[u],n=this._ikuaiAllV6Value(t,i[t]);if(n)l(this._ikuaiAllV6Label(t),n,/addr|mac|ip|address/i.test(t))', 1)
s = s.replace(C, C_NEW, 1)

out = s.encode('utf-8')
io.open(PATH, 'wb').write(out)
print('old bytes', len(b), 'new bytes', len(out), 'delta', len(out) - len(b))
print('new methods', len(M))
for k in ['_ikuaiAllV6FmtBytes', '_ikuaiAllV6Value', '_ikuaiAllV6ConnSection', '_ikuaiAllV6ConnCard', 'monitor_lanipv6']:
    print('  %-28s %d' % (k, s.count(k)))
