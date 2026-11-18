# 插件API契约 — 房间精灵插件宿主（v1.x）

> **本文是契约，不是教程**：每个 API 的语义、生命周期、错误边界、频率限制都在这里定死。
> 上手教程看《插件开发指南.md》；实现原理看《插件宿主设计.md》。
> **纪律**：本文与实现不符视为实现 bug —— 两者必须同步修改，且属于对外承诺。

---

## 1. 契约版本规则

| 档 | 语义 | 递增时机 | 引入内核 |
|---|---|---|---|
| `1.0` | 稳定基线 | — | v7.0.0 |
| `1.1` | 向后兼容新增（新 ctx 成员 / 新可选参数） | 只加不改 | v7.0.0.2 |
| `1.2` | 向后兼容新增：实体订阅（`entitiesOf` 声明式 + `ctx.watch` 动态）+ `onHass` 实体过滤 | 只加不改 | v7.0.0.5 |
| `1.3` | 向后兼容新增：`ctx.media`（媒体查看器 —— 图片/视频全屏查看，与内置卡同一份实现） | 只加不改 | v7.0.1.108 |
| `2.0` | 破坏性变更（改签名 / 改语义 / 删成员） | 下一大版本 | （未定，随 v8.x） |

- **内核支持区间**：`['1.0', '1.1']` —— 插件声明此区间内的档即可加载；声明 `2.0` 及以上 → 拒绝，
  控制台 `E_API_VERSION` 并 toast「插件 X 需要房间精灵 vX 以上」；
- **兼容承诺**：`1.x` 内**不删除、不改语义**，只新增；`2.0` 发布时给至少一个大版本的过渡期；
- **存量兼容**：插件写整数 `apiVersion: 1` 视为 `'1.0'`（v7.0.0 存量不受影响）；
- **运行时查询**：`RoomElves.apiVersion`（内核支持的最高档，当前 `'1.3'`）、
  `RoomElves.apiSupported`（支持区间数组）。

---

## 2. 生命周期（五个阶段）

```
加载 → 注册 → 渲染 → 更新 → 销毁
```

### 2.1 加载

- 触发：页面加载后（顶层 `ensureLoaded`）或任意主卡 `setConfig` 看到 `plugins`；
- **300ms 防抖**（抗 YAML 编辑器逐字输入）+ **串行加载**（清单内一个接一个）；
- 双通道：`import(url)` 失败 → 退化为 `<script src>`；
- 失败：本会话不再自动重试（`FAILED`），**并从清单移除**；控制台 `E_LOAD_FAILED` / `E_LOAD_TIMEOUT`（10s）；
- **框架保证**：同一 URL 只执行一次（`LOADED` 去重）；成功后控制台打印
  `[room-elves] 插件 <type> 来自 <路径>，拥有控制设备的权限`。
- **插件必须**：在模块顶层（或 script 顶层）同步调用 `RoomElves.defineCard(...)` 至少一次；
  只 import 不注册 = 什么都不会发生。

### 2.2 注册（`defineCard`）

- 校验顺序：`render` 函数存在 → `apiVersion` 语义档 → `type` 非空 → 重名（`E_TYPE_EXISTS` 拒绝，不覆盖）；
- 成功 → 入注册表 → 通知"等待此 type 的占位"（`flushWaiters`）；
- **框架保证**：`type` 归一（`my_solar_card` ≡ `my-solar-card`，大小写不敏感）；重复注册**不覆盖**。

### 2.3 渲染（`render(ctx, container, config)`）

- 触发：三种形态（`standalone_type` / `popup_card` / `cards` 混排）都经过
  `_createCardElementInner → renderIfHandled`；
- **可能多次执行**：主卡重建、弹窗重开、配置变更都会重新 `render` —— **不要**在模块顶层保存
  DOM 引用或"已初始化"标记；每次 render 都是全新的一次；
- 错误边界：`render` 抛错 → 该卡位置显示"插件渲染失败：`<type>`"占位，**不影响页面其它部分**；
  控制台 `E_RENDER` 带堆栈；
- `config`：用户 YAML 透传（**不含** `popup_position` / `width` 等弹窗参数，它们由弹窗层消费）。

### 2.4 更新

- `ctx.onHass(fn)`：hass 推送时回调。**rAF 合并 + 单闸门** —— 心跳场景每秒十余次推送，
  回调**每帧最多一次**，且两次回调之间可能聚合了多次状态变化。**不要**假设"一次回调 = 一次推送"；
- `ctx.theme.onChange(fn)`：主题切换时回调（5 套主题任意切换都会触发）；
- 隐藏的卡片**仍然收到**回调（P0 不做可见性过滤，P1 计划中）。

### 2.5 销毁（`ctx._destroy`，框架内部）

三重触发之一满足即销毁：① 根元素移出文档**且超过 15 秒宽限期**（防弹窗"先建后插"误杀），
在下一次 hass 广播时判定；② 主卡显式 `disposeAllWithin`；③ 弹窗关闭回收。

销毁时框架依次执行：onHass 监听清空 → theme 反订阅 → **本实例创建的所有图表 `destroy()`** →
`timers.clearAll()` → 关闭本实例弹窗 → 从活跃表删除。

**插件必须**：不要在 render 之外的地方另起"逃逸"的定时器（直接 `setInterval`）——
框架只回收 `ctx.timers` 里登记的。

---

## 3. API 条目

> 约定：所有方法的 `this` 无意义（都是闭包函数）；"返回 null"指严格 `null`（不是 undefined 抛错）。

### 3.1 `ctx.frame` — 界面骨架

| 方法 | 语义 | 错误边界 |
|---|---|---|
| `createCardHeader(host, title, accent)` / `(host, opts)` | 整卡头部（唯一入口）。返回**句柄** `{el, right, tabs, set, refresh, destroy}` —— **不是节点**，append 时必须 `.el` | `host` 非 Node → 抛错；`tabs.items` 为空 → 不建页签 |
| `createSection(host, opts)` | 区块。返回句柄 `{el, head, body, left, right, set, refresh, expand, collapse, isCollapsed, destroy}` | 同上 |
| `createTabBar(host, opts)` | 主选项卡 + 面板。返回句柄 `{el, tabs, applyTab, switchTo, getActive, destroy}`；`adopt:true` 接管既有 DOM，`adoptTabs:false` 只接管面板 | `items.length < minPages(默认2)` → 整条隐藏 |
| `createSegTabs(host, opts)` | 分段选项卡。返回句柄 `{el, get, apply, switchTo, refresh, setItems, destroy}`；**`apply` 只同步不回调**，`switchTo` 才回调；空字符串 key 合法（"全部"）；角标颜色跟状态走（不支持 badgeColor） | 点击禁用项不切换；`setActive` 传不在清单里的 key 直接忽略 |
| `presets.text/pill/icon/button/progress` | 右插槽小控件；值可传函数（框架脏检查） | — |

**频率限制**：无。但页签/分段的 DOM 由框架持有，插件不要绕过句柄直接改 `.re-tab` 内部。

### 3.2 `ctx.accent` — 主色

| 方法 | 语义 |
|---|---|
| `apply(root, {accent})` | 把 `--re-accent*` 变量写到 root（幂等：同根重复调用复用句柄）。返回句柄或 null |
| `resolve(v)` | 解析命名色 / hex / `auto`（读 HA `--primary-color`）→ `#rrggbb` |
| `themeOf(root)` | 逐级向上（含穿 shadow 边界）找 `theme-*` 类 → `'light'|'dark'|…` |

### 3.3 `ctx.theme` — 主题

| 方法 | 语义 |
|---|---|
| `current()` | 当前主题名（`'light'` / `'dark'` / `'black'` / `'darkgray'` / `'transparent'`） |
| `vars(name?)` | 该主题的**全部变量**（key 带 `--room-` 前缀）。给 canvas/ECharts 取色用 |
| `apply(root, name?)` | 把一套主题变量**手动写到 root**（内联，优先级最高）。⚠️ 会把这块区域锁死在该主题 —— 只用于独立 shadowRoot |
| `onChange(fn)` | 订阅切换；返回反订阅函数；卡片断开时框架自动取消 |

**频率**：`onChange` 每次切换触发一次（无合并）。

### 3.4 `ctx.hass` / `ctx.onHass` / `ctx.watch`

- `ctx.hass` 是 **getter**，永远返回最新引用 —— 不要存快照；
- `onHass(fn, opts?)`：
  - **不带 `opts.entities`** → 全量广播：任何 hass 推送都触发（rAF 合并，每帧 ≤ 1 次）；
  - **带 `opts.entities: [ids]`** → 引用级过滤：只有清单内实体变化（state 对象引用变化，与 HA
    "更新才换引用"的语义一致）才触发；**首次广播必然触发**（快照为空）；
  - **错误边界**：回调抛错被捕获 + `console.warn`，不影响其它插件；
- `watch(...ids)`（1.2）：把实体登记进宿主主卡的 `_entitySubscriptions`（与内置卡同语义，
  让主卡的订阅集/事件流知道插件关心什么）。
  ⚠️ **必须在 `render` 里调用** —— 主卡每次重建会重新收集订阅集，框架不会替插件保留；
- **频率限制**：rAF 合并 → 每帧最多一次；重活自己 `ctx.timers.raf` 再合并；
- **典型组合**：`render` 里 `ctx.watch(...ids)` + `ctx.onHass(fn, { entities: ids })`。

### 3.4.2 实体订阅：声明式 `entitiesOf`（推荐）+ 动态 `ctx.watch`

主卡维护一个**实体订阅集**（`_entitySubscriptions`）：主卡渲染过滤与事件流的"相关实体"清单，
每次主卡重建会**重新收集**。插件有两种方式把实体送进去：

**① 声明式（推荐）—— `defineCard({ entitiesOf: (config) => ids })`**

```js
RoomElves.defineCard({
  type: 'my-solar-card',
  entitiesOf: (config) => [
    config.power_entity, config.today_entity, ...(config.extra_entities || [])
  ],
  render(ctx, container, config) { ... }
});
```

- 主卡收集订阅时**自动调用**（`_collectCardEntities` 的插件分支）——插件 config 里的实体
  随主卡重建自动进/出集合，**插件无须自己调任何东西**；
- 返回值：字符串或字符串数组；无域前缀的（如 `'bad'`）被过滤；抛错被吞（返回 `[]`，不影响主卡）；
- 典型形态：`popup_card` 弹窗里的插件卡**不在**主卡订阅收集流程（动态弹窗）——
  这类场景靠 §2.4 的全量广播即可，或用 `ctx.watch` 补登记。

**② 动态 —— `ctx.watch(...ids)`**

运行时才知道的实体（用户在下拉里选了一个新实体、数据接口返回的关联实体）用 `ctx.watch(id)`
登记进**宿主主卡**的订阅集。⚠️ 必须能在主卡重建后再次调用 —— 通常放在 `render` 里
（依赖 config 的部分改用 ①），或放在"用户选择变化"的回调里（选择变化会触发 render 重跑）。

**分工**：config 里写死的 → ①；运行时发现的 → ②。

- 对比口径是 **state 对象引用**（`hass.states[id] !== 上次引用`），不是 state 值字符串 ——
  与主卡 `_lastEntityStates` 同口径，也是 HA 的真实行为（实体更新才换引用）；
- 过滤快照按**插件实例**维护；`render` 重建不会清快照（同一实例的 DOM 重建不影响）；
  卡片销毁后重建 = 新实例 = 快照为空 = 首次广播触发一次。

### 3.5 `ctx.timers`

`setTimeout` / `setInterval` / `requestAnimationFrame` / `clearTimeout` / `clearInterval` / `clearAll`。
**全部实例级**：卡片销毁时 `clearAll()`。回调里抛错不影响其它定时器（逐个隔离）。

### 3.6 `ctx.cache` / `ctx.fetch`

**cache**（全局共享 —— 与主卡、其它插件同一份）：

| 方法 | 语义 |
|---|---|
| `get(key, subKey)` | 过 TTL（5 分钟）返回 `undefined`；命中返回存入的值（**同一引用**，别原地改） |
| `set(key, subKey, value)` | 写入；容量上限 200 条（惰性裁剪一半） |
| `clear(key?)` | 清单组 / 全清 |

**fetch**（**永不 reject**；失败一律返回 `null`）：

| 方法 | 成功返回 | 失败返回 |
|---|---|---|
| `json(url, init?, ttlMs?)` | **解析后的 data**（JSON.parse 结果） | `null`（HTTP 错 / 超时 / 解析失败） |
| `text(url, init?, ttlMs?)` | 响应**文本** | `null` |
| `get(url, ttlMs?)` | data（等价 json 的 GET 简写） | `null` |
| `jsonRaw(url, init?, ttlMs?)` | 信封 `{ok, status, data, timeout?}` | 信封（`ok:false`）—— 需要状态码时用 |
| `textRaw(url, init?, ttlMs?)` | 信封 `{ok, status, text}` | 同上 |

**频率限制（框架自动做，插件无需重复做）**：

- **同刻合并**：同 URL 的并发请求只发一次（跨卡片共享在途）；
- **短时复用**：显式传 `ttlMs` 时，该窗口内同 URL 直接返回缓存文本（各自 parse，不共享对象引用）；
- **超时兜底**：20 秒（`jsonRaw` 的信封里 `timeout: true` 标记）。

### 3.7 `ctx.select` — 下拉

`create(opts)` → 组件实例（`{get, set, destroy…}`，与主卡 `_createSelect` 同一实现）。
普通下拉给 `options`；动态下拉给 `loadOptions: async () => options`（每次打开重新取）。
**错误边界**：内核 `_createSelect` 不存在时返回 `null`（1.x 实际不会发生）。
**生命周期**：下拉弹层挂在宿主 shadowRoot；同一 `owner`（插件实例）打开新的会自动关旧的；
卡片断开时随 `timers`/弹窗回收体系清理。

### 3.8 `ctx.popup` — 弹窗 / 气泡 / 日历 / 确认框

| 方法 | 语义 | 返回 |
|---|---|---|
| `show(opts)` | 通用弹窗（`content` 可为函数 = 延迟构建） | `{close}` |
| `bubble(opts)` | 气泡（`target` 锚点、自动翻边、弹性动画） | `{bubble, close}` |
| `calendar(entityId, date, onPick, rect?, apiOptions?)` | 日历；`entityId` 传 `''` = 纯日期选择 | — |
| `confirm(title, message, onConfirm, onCancel?)` | 确认框 | — |

**错误边界**：弹窗内部抛错由框架捕获（不白屏）；`onClose` 回调保证触发（含 Esc / 遮罩）。
**频率限制**：同一实例同时只开一个弹窗（新开会关旧的，z-index 互斥由 owner 管理）。

### 3.9 `ctx.actions` — 统一动作系统

`execute(tapAction, options?)` → `Promise<boolean> | void`。
支持 action：`toggle` / `set_value` / `loop_assign` / `process_execute` / `quick-action` /
`more-info` / `navigate` / `call-service` / `popup_card` / `card`。
**副作用**：每次执行自动写后端操作记录（`user_actions` 表）—— 插件**禁止**绕过它直接
`hass.callService` 操作设备（会丢埋点）。

### 3.10 `ctx.chart` — 历史图表

`create(opts)` → 句柄 `{el, load, destroy, …}`（与主卡 `createHistoryChart` 完全一致）。
四个宿主回调由框架注入（fetchHistory → WebSocket 历史、loadEcharts → 共享实例、
getState → hass 当前值、createSelect → 实例下拉）。**销毁**：句柄登记在实例上，
卡片断开时框架统一 `destroy()`；插件提前不要时也可自己调。

### 3.11 `ctx.el` / `ctx.clear`

- `el(tag, className?, text?, props?)`：`props` 约定 —— `style` 传对象（`Object.assign(node.style)`）、
  `onclick` / `onXxx` 传函数（addEventListener）、其余 `setAttribute`（`undefined` 跳过）；
- `clear(node)`：移除全部子节点。

### 3.13 `ctx.media` — 媒体查看器（图 / 视频）

**入口**：`ctx.media.open(opts) → { close } | null`

在插件里点开一张图或一段视频：**打开即全屏**，底部常驻工具条
（标题 · 文件名 · `1/N` · 倍率 · 下载 · 退出全屏 · 关闭），
双击 / 捏合 / 滚轮缩放，左右滑或 ← → 翻页，点画面黑底关闭。
与内置卡（叮咚门铃 / 通知中心附件）**同一份实现**（`infra/media-viewer.js`），观感一致。

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `url` | string | ✅ | 打开时停在哪个地址 |
| `list` | `Array<{url, kind?, time?, file?}>` | — | 连续浏览链；不传 = 单张 |
| `kind` | `'video' \| 'image'` | — | `list` 内逐项用；顶层只在单张时有意义 |
| `time` | string | — | 有值时标题按该时刻显示 |
| `file` | string | — | 文件名（也用作下载默认名） |
| `title` | string | — | 单张时的标题 |
| `onFullscreenChange` | `(on: boolean) => void` | — | 进出全屏回调（收起插件自己的信息区） |

**行为约定**：

- `host` 由框架注入（内部用主卡的 `showPopup` / `_timers`），插件**不要**传，传了会被覆盖；
- 返回 `null` 表示无法打开（宿主缺少 `showPopup`）—— 插件应降级（如 `ctx.popup.show`）；
- **下载按钮**只在「`/api/` 开头且非 `camera_proxy_stream`」的直链上出现，外链自动隐藏；
- 弹窗被同 `className` 的替换、或卡片断开时，框架自动收尾（移除 `keydown`、停止视频、还原全屏内联样式）。

```js
const ref = ctx.media.open({
  url: first.url,
  list: photos.map(p => ({ url: p.url, kind: p.video ? 'video' : 'image', time: p.time })),
  title: '今日抓拍',
  onFullscreenChange: (on) => { infoEl.hidden = on; }
});
if (!ref) ctx.popup.show({ content: () => ctx.el('img', '', '', { src: first.url }) });
```

> 契约版本：**1.3 起提供**（未声明 `apiVersion: '1.3'` 的插件仍可调用，
> 但那是"用到较新能力"—— 建议声明 1.3 以在旧内核上得到明确报错）。

---

### 3.12 `ctx.styles` / 其它

- `injectFrame(root)`：注入框架 CSS 到独立 shadowRoot —— **1.1 现状为空操作**
  （主卡内嵌场景样式已继承；独立 shadowRoot 属 P1）；
- `RoomElves.utils.el`：与 `ctx.el` 相同（供模块顶层建占位用）。

---

## 4. 稳定性承诺

**冻结面（破坏 = 2.0）**：

1. `window.RoomElves` 顶层成员：`defineCard` / `load` / `loadAll` / `plugins.{list,add,reset}` /
   `pluginTypes` / `frame` / `accent` / `theme` / `cache` / `apiVersion` / `apiSupported` / `version`；
2. `defineCard` 参数：`type` / `name` / `apiVersion` / `render(ctx, container, config)` / `getCardSize` / `entitiesOf(config)`（1.2）；
3. `ctx` 门面**方法名与语义**（本文 §3 全部条目）；
4. 错误码：`E_LOAD_FAILED` / `E_LOAD_TIMEOUT` / `E_API_VERSION` / `E_TYPE_EXISTS` / `E_RENDER` /
   `E_DEF_INVALID` / `E_TAG_INVALID`；
5. 主题变量名：`--room-*`（17 个通用变量）与 `--re-accent*`（见开发指南 4.2）。

**非承诺（可变）**：

- ctx 内部实现（stub / 原型借用方式）；
- `.re-*` **类名结构**（CSS 变量名是承诺，类名 DOM 结构可能重构）；
- 控制台日志的具体格式（`拥有控制设备的权限` 这句文案的措辞可调）；
- `FRAME_CSS` 注入方式。

---

## 5. 已知限制（1.x 现状，写插件时绕开）

| 限制 | 说明 | 计划 |
|---|---|---|
| 无热卸载 | ESM 模块一旦加载无法移除；升级插件 = 刷新页面 | 不会做（浏览器限制） |
| `styles.injectFrame` 空操作 | 插件应直接挂在主卡 shadowRoot 内（样式继承） | P1 支持独立 shadowRoot |
| 隐藏卡片仍收到 onHass | 后台标签页插件回调照跑（插件自己节流） | P1 做可见性跳过 |
| `render` 抛错无局部重试 | 只能等下一次整卡重建 | 评估中 |
| 插件清单不上云端 | 换浏览器/设备要重新声明 `plugins` | P2 同步后端 |
| 无沙箱 | 插件 = 页面内任意代码（见责任声明） | 不会做（与"复用全部能力"矛盾） |
