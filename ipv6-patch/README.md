# IPv6 客户端查看增强补丁（基于上游 v7.0.1）

本目录提供一份**基于 `chjspp520/room-elves-card` v7.0.1 最新版**的可复现补丁，让「iKuai 全览」把 `sensor.ikuai_lan_hosts` 的 `ipv6_entries` 真正列出来并可点开查看，而不是只在提示里显示「另有 N 台 IPv6 终端未并入列表」。

> 上游 v7.0.1 已自行内置 iKuai 4.0 `{code, results}` 信封兼容，且 `hacs.json` 已移除 `content_in_root`；本补丁**不重复这两处改动**，只针对 v7.0.1 仍缺失的 IPv6 终端能力。

## 一、v7.0.1 现状与问题

集成已把 IPv6 终端明细放在 `sensor.ikuai_lan_hosts.attributes.ipv6_entries`，但 v7.0.1 的 `_ikuaiAllClientHint()` 只做提示：

```js
Array.isArray(i.ipv6_entries) && i.ipv6_entries.length &&
  n.push("另有 " + i.ipv6_entries.length + " 台 IPv6 终端未并入列表")
```

结果：IPv6 终端在卡片里看不到、点不开，也没有连接详情；纯 IPv6 环境下客户端列表直接早退为空。

## 二、补丁内容（四层，均只改渲染层）

所有改动都是对压缩 bundle 的**锚点唯一校验 + 纯文本替换**，不触碰解析层、IPv4 四页签、插件系统与上游内置逻辑。

| 层 | 脚本 | 内容 |
|---|---|---|
| 1 | `tools/1_ipv6_clients.py` | 去掉「IPv4 列表为空就早退」；把 `ipv6_entries` 分组列入主列表、纳入重绘指纹；修掉 IPv4 为空时 `a[0]` 抛错的隐患；计数与提示文案同步；点击行弹出 IPv6 详情 |
| 2 | `tools/2_units_connections.py` | 上行/下行为实时速率、累计上下行与今日累计为累计字节，按 1024 进制换算为 B/KB/MB/GB（速率带 `/s`）；已带单位的文本不重复换算；新增「查看连接详情」区块 |
| 3 | `tools/3_recalibrate.py` | 按爱快 4.0 实机抓包校准 `monitor_lanipv6` 载荷；IPv6 地址展开为完整 8 段带前导零、GUA 优先跳过 `fe80:`；连接卡片补域名、协议/线路汇总字段 |
| 4 | `tools/4_display_fix.py` | IPv6 详情与连接详情的 kv 改为两列单对布局，值自动换行不再被省略号截断；弹窗放宽；补齐 30+ 集成原始字段中文标签 |

### 连接详情接口（爱快 4.0 实机校准）

```
POST /Action/call
{"func_name":"monitor_lanipv6","action":"show",
 "param":{"TYPE":"conn,conn_num","ip":"<完整8段IPv6>","proto":"all","interface":"all","limit":""}}
```

- 参数名只有 `ip` 有效（`ipv6` / `ipv6_addr` 返回空）；
- `ip` 需完整 8 段带前导零，压缩格式下 `conn_num` 汇总为 0；
- 响应为 4.0 信封 `{code, message, results}`，`results` 含 `conn` / `conn_num` / `protocol_stats` / `interface_stats`；
- `conn` 行字段：`protocol` `status` `dst_addr` `src_port` `dst_port` `forward_addr` `app_name` `interface` `total_up` `total_down` `domain`。

## 三、目录文件

| 文件 | 说明 |
|---|---|
| `room-elves-card.js` | 打好补丁的成品（基于官方 v7.0.1 release 附件 4,595,608 B） |
| `room-elves-card.js.gz` | 同内容 gzip（level 9、无时间戳，可复现） |
| `tools/apply_all.py` | 一键复现：输入官方 v7.0.1 附件 → 输出上述两个文件 |
| `tools/1_*.py` ~ `4_*.py` | 四层独立补丁脚本，逐个校验锚点唯一 |
| `tests/test_*.py` | 四套回归测试（170 项断言） |

SHA-256：

| 文件 | 大小 | SHA-256 |
|---|---|---|
| `room-elves-card.js` | 4,610,272 B | `608e89a481689c0b77580aa34fc01e9654269f52466b2f35e75494d8a319d3c4` |
| `room-elves-card.js.gz` | 1,138,476 B | `4b8bdc5a4da12c8e13072abc9c68e06e23f38157a9bd5a6bb9fa0135a89c4f31` |

## 四、自己复现

从 [上游 v7.0.1 release](https://github.com/chjspp520/room-elves-card/releases/tag/v7.0.1) 下载 `room-elves-card.js`，然后：

```bash
python tools/apply_all.py ./官方-room-elves-card.js ./dist
```

脚本会校验基线、依次应用四层补丁、`node --check`、生成 `.gz` 并打印哈希，结果应与上表一致。

运行回归测试（需要 node）：

```bash
CARD_JS=./room-elves-card.js python tests/test_v6.py
CARD_JS=./room-elves-card.js python tests/test_patch3.py
CARD_JS=./room-elves-card.js python tests/test_patch4.py
CARD_JS=./room-elves-card.js python tests/test_patch5.py
```

## 五、验证结果

| 项 | 结果 |
|---|---|
| `node --check` | PASS |
| `test_v6.py` / `test_patch3.py` / `test_patch4.py` / `test_patch5.py` | 22 / 41 / 51 / 56 项，共 **170 项断言全 PASS** |
| 真实浏览器 360px 窄屏 computed style | IPv6 值列 127px → 317px，`white-space:normal` / `text-overflow:clip` 生效；IPv4 弹窗仍为原 `nowrap+ellipsis`，未受影响 |
| 载荷离线校验 | 3 组地址均生成完整 8 段带前导零 `ip`，参数键与实机一致；单位换算 `1048576 → 1 MB`、`2048 → 2 KB/s` |
| 爱快 4.0 实机校准 | 同一套载荷此前在真机 6 台 IPv6 终端上取到 16 条真实连接、全部 `code=0`；本目录另做离线载荷比对，确认与实机校准版逐字段一致 |
| `.gz` 解压回读 | 与 `.js` 逐字节相等 |
| 一键脚本复现 | 输出与目录内成品逐字节一致 |

## 六、为什么以「补丁 + 成品」形式提交

上游仓库没有构建前源码（`src/`），根目录 `room-elves-card.js` 是旧版快照，正式分发走 release 附件。因此这里提供可直接使用的成品 + 可复现补丁脚本 + 完整说明；若手上有构建前源码，按 `tools/` 里四层替换对应到 `_ikuaiAllClientHint` / `_ikuaiAllBuildV6Row` 等位置即可合并。

## 七、部署与回退

覆盖 `config/www/community/room-elves-card/` 下的 `room-elves-card.js` 与 `room-elves-card.js.gz`（HA 优先返回 `.gz`，两个都要换），浏览器 Ctrl+Shift+R 强刷。回退直接取回官方 v7.0.1 release 附件覆盖即可；本补丁不写入任何配置。

> 说明：仓库主分支原有的 `hacs.json`、`README.md` 等文件本 PR 一律不改动，全部内容新增在 `ipv6-patch/` 目录下，因此不会产生合并冲突。测试样例中的 IPv6 均为 RFC 3849 文档保留地址 `2001:db8::/32`。
