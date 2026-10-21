

<img width="430" height="932" alt="1" src="https://github.com/user-attachments/assets/8d854761-0073-4f19-9f3b-0e7f14485919" />
<img width="470" height="1002" alt="1" src="https://github.com/user-attachments/assets/f1525554-3592-44c1-855c-464b1b3e40ad" />

# Room Elves Card - 房间精灵卡片 完整使用说明(适用于v6.6.0及其以前的版本)

# Room Elves Card - 房间精灵卡片 完整使用说明



## 一、卡片简介

**Room Elves Card**（房间精灵卡片）是一款功能极为强大的 Home Assistant 自定义卡片，旨在将一个房间（或全屋）的所有设备状态与控制能力集中到一张卡片中，实现"一卡掌控全家"的智能家居体验。

> **作者声明**：[电力卡片](https://github.com/chjspp520/electricity-info-card)、[HA 数据统一存储系统](https://github.com/chjspp520/ha_data_store)、[ESXi Control](https://github.com/chjspp520/esxi_control)、[iKuai 集成](https://github.com/chjspp520/ikuai)、[飞牛 fnOS 集成](https://github.com/chjspp520/fnos) 均由 **chjspp520** 制作维护。
>
> **免责声明**：作者仅提供软件功能，不对数据泄露提供安全保障。数据安全由用户自行负责，使用本软件即代表接受本条款（适用法律以所在地为准）。

### 核心特性

- **30+ 种设备卡片类型支持**：灯光（单灯/灯组）、空调、插座/开关、耗材/电池、暖气/新风机、媒体播放器（支持后台播放/api 列表）、窗帘（单层/双层）、晾衣架（机械仿真拖拽）、风扇、通用设备、动态图标、时间轴、情景模式、快捷操作、按钮组、用户卡片、天气、健康数据、传感器、开关、选择器、数字输入、滑块、文本、按钮、图片、仪表图/进度条/柱状图/曲线图/环形图/饼图/热力图/日历图/混合图表等
- **丰富的弹出控制面板**：每种设备类型都有专属弹窗——灯光面板支持亮度/色温调节、按房间分组、批量开关；空调面板可调温度/模式/风速；窗帘面板支持百分比滑块控制、单双层切换；晾衣架面板带机械仿真拖拽和收藏位置；情景模式支持执行进度展示和状态验证
- **两种显示模式**：
  - **普通模式**：左侧显示房间名称和传感器数据，右侧显示设备操作按钮，适合单房间展示
  - **头部模式（head）**：所有按钮铺满卡片，顶部可显示概览栏（灯光/空调/插座/耗材/环境/人员/能耗统计），适合放在页面顶部作为全屋控制中心
- **通用动作系统（tap_action）**：统一的动作引擎覆盖所有可点击位置，支持 `toggle`（自动推断服务切换开关）、`set_value`（智能推断服务设置目标值）、`loop_assign`（循环赋值：每次点击把实体推进到值序列下一个值）、`process_execute`（流程执行：按步骤序列依次执行多实体操作，支持每步独立延时）、`quick-action`（快捷操作/情景模式）、`more-info`、`navigate`、`call-service`、`popup_card`、`card`（弹出设备内置控制弹窗）等 12 种动作类型，`toggle` 和 `set_value` 还支持多实体批量操作
- **选项卡系统**：弹窗内支持选项卡分组，具备图标、高亮、自动跳转、条件过滤（display_only）、禁用、角标、分组归属（belong）等高级功能，支持按楼层/区域分组展示；**选项卡之间支持左右滑动切换**（跟手拖动 + 松手吸附 + 高亮跟手）
- **左右滑动（全场景统一）**：弹窗选项卡、头部多页按钮、各卡片自己的分页（多房间 / 多用户 / 多档位 / 多数据集）都支持左右滑动，手感一致；纵向滚动仍归浏览器，起点落在按钮 / 输入框 / 日期导航上不算翻页，页面里的横向滚动区会主动让路；只有一页时不启用；**无需任何配置**（详见「八-A、左右滑动」）
- **程序扩展坞（Dock）**：从屏幕右侧滑入的快捷启动栏，支持头部模式全部按钮类型和动作系统，点击触发按钮展开/收起
- **独立卡片模式（Standalone）**：将单个设备控制面板直接作为一张卡片使用，支持空调、窗帘、媒体、晾衣架、图表等 20+ 种独立卡片类型
- **三张卡片已从"外置独立卡片"并入内建（内部子卡片）**：**温湿度面板**（`wenshidu`）、**设备回放**（`replay`）、**定时精灵**（`timer`）原先各自是**在本卡片之外单独安装的独立卡片**（`wenshidu-card.js` / `device-replay-card.js` / `timer-control-card.js`），现已**整体并入房间精灵卡片**，成为它的**内部子卡片** —— 独立 custom element 已退役（不再单独注册），改由本卡片以 `standalone_type: wenshidu / replay / timer` 直接内置渲染，也能作为 `type: wenshidu / replay / timer` 按钮嵌进按钮网格；配置写法见 6.42 / 6.40 / 6.41，实现位于 `modules/cards/wenshidu.js` / `device-replay.js` / `timer-control.js`（引擎内封在各自 Element 里，只对卡片原型暴露少数方法）
- **多页模式（头部模式）**：用 `buttons_2` / `buttons_3` … 把按钮分到多页，**左右滑动切换页面**（跟手拖动 + 松手吸附 + 圆点高亮跟手），底部圆点指示当前页；桌面端也可用滚轮翻页
- **图表卡片系统**：内置 10 种图表类型——仪表图（纯 SVG）、进度条（纯 CSS）、柱状图（纯 CSS）、曲线图/环形图/饼图/南丁格尔玫瑰图/热力图/日历图/混合图表（ECharts），以及插座功率流向桑基图
- **飞牛 fnOS 全实体卡片（`fnos`）**：把一台飞牛 NAS **整台装进一张卡** —— 只配一个聚合实体（默认 `sensor.fnos_all_entities`，不配也用它兜底）就自动认设备与角色（**不写死任何实体 id**），顶层五个页签（主机 / 存储 / Docker / 虚拟机 / 应用）：主机含指标格、网络与磁盘 IO、系统信息、存储概况、服务开关与重启 / 关机；存储页列出存储池与硬盘；Docker 页一行一个容器（启停 / 重启）；虚拟机页含电源 / 重启 / 强制关机 / 打开远程；应用页汇总文件·相册·影视。依赖 [fnos 集成](https://github.com/chjspp520/fnos)，配置见 6.37
- **个人账单卡片（`bill`）**：把 ha_data_store 的账单数据画成一张卡——概览（环形图 + 来源占比条 + 年度 / 月度收支 + 最近 N 日）、分析（四张环形图 + 月度趋势 + 支付时刻 + 对方排行）、日历（格子分两行写"收 / 支" + 年月选择）、查询（条件可折叠 + 汇总（合计行"有哪个显示哪个"，不计收支也摆得出来）+ 排序条 + 涉及年筛选）、历史（历史今日 / 历史本月）**五个选项卡**，并支持在**一个窗口里一路下钻**（年 → 月 → 日 → 时 → 那一个小时的账单）；明细行的字段还能直接点着去查询。配置见 6.45
- **iKuai 全实体卡片（`ikuai_card`）**：把一台爱快路由器**整台装进一张卡** —— 只配一个聚合实体（默认 `sensor.ikuai_all_entities`）就自动认设备与角色（**不写死任何实体 id**），顶层四个页签（路由 / Docker / 虚拟机 / 日志），路由页再分六个子页签（网络 / 线路 / DHCP / 客户端 / 本地认证 / 设置）；虚拟机带远程控制台与画面预览。配置见 6.46
- **叮咚门铃卡片（`dingdong`）**：只配一个「实体清单」实体，就把一台叮咚（移康 eques）门铃装进一张卡 —— 抓拍 / 实时 / 反转三态画面 + 按天回看的事件·抓拍·录像混合时间轴 + 跨天双向时间轴 + 设置 + 诊断；不写死实体 id（按「域 + 后缀」从清单反查角色）。依赖 `eques_dingdong` 集成，配置见 6.47
- **平面户型图**：支持 JSON 坐标数据的平面户型图渲染，实时显示各房间人员占用状态，拖动时间轴可回溯历史活动
- **人员/天气/导航**：用户卡片支持多人头像布局（当前登录用户大头像居中）、在/离家状态检测、实时定位、高德地图导航路线规划、多地区天气预报（支持和风天气 API 与 HA 实体双数据源）
- **情景模式**：一键执行预定义操作列表，支持气泡选择/直接执行模式、延时执行、执行进度实时展示、状态验证、执行历史记录，服务调用自动推断（覆盖 light/climate/cover/fan/media_player/vacuum/lock/automation/script 等所有域）。还可作为统一卡片类型（`type: action`）或 `tap_action: quick-action` 在弹窗、title_entities 等任意位置使用
- **自动弹窗（auto_open_entity）**：当指定实体变为 on 时自动打开弹窗，支持延迟弹出和自动关闭，适合告警联动场景
- **HA 数据统一存储系统集成**：顶层配置 `api_base_url` 和 `key`，所有请求历史数据走该路径，支持健康数据、天气、历史图表、时间轴等场景
- **配置共享**：通过 `config_id` / `from_config_id` 在多个卡片间共享按钮配置和弹窗布局，支持 `tabs_config` 组合引用
- **自定义外观**：支持自定义卡片尺寸、背景色、圆角、主题切换（亮/暗/时间/跟随系统），按钮图标/颜色/动画均可配置，CSS 变量覆盖扩展
- **动画与交互**：图标支持 shake/rotate/blink/breathe/jump/random-move 等动画效果，点击反馈、状态过渡动画、光晕特效等

---

## 二、如何安装

### 方式一：HACS 安装（推荐）

1. 确保已安装 [HACS]。
2. 在 HACS → 前端模块 → 右上角三点菜单 → "自定义存储库"中，添加存储库地址：`https://github.com/chjspp520/room-elves-card`。
3. 搜索并安装 `Room Elves Card`，安装后刷新页面即可在仪表盘的自定义卡片中找到。

### 方式二：手动安装

1. 将文件 `room-elves-card.js` 放入 Home Assistant 配置目录下的 `www` 文件夹中（如果没有 `www` 文件夹，请手动创建一个）。
2. 在 HA 侧边栏的"配置" → "仪表盘" → 右上角三点菜单 → "资源"中，添加一个 JavaScript 模块资源，路径填 `/local/room-elves-card.js`。添加后刷新页面即可找到。

### 推荐搭配卡片 & 依赖

以下是与本卡片配套使用的推荐卡片和依赖集成：

> ⚠️ 下面列出的集成，**卡片本身不含数据采集，缺集成就没有数据**。其中 `ha_data_store` 属于**深度依赖集成**（历史 / 播放列表 / 健康数据等多处共用，**不专属某一张卡片**）；其余三个各对应一张卡片：
> `esxi_control` → `esxi`（ESXi 虚拟化）· `ikuai` → `ikuai_card`（iKuai 全实体卡）· `fnos` → `fnos`（飞牛 fnOS 全实体卡）。

- **HA 数据统一存储系统** ([ha_data_store](https://github.com/chjspp520/ha_data_store)) — ⚠️ **深度依赖集成（不绑定单张卡片）**。本卡片已深度适配该集成，通过其 API 接口读取历史数据、播放列表（媒体卡片）、健康数据等，多处功能共用，**建议优先安装配置**。它同时是 `type: bill` 个人账单卡片的必需集成（需 v5.0.0 及以上），见 6.45。
- **ESXi Control** ([esxi_control](https://github.com/chjspp520/esxi_control)) — ⚠️ **`type: esxi` 卡片的必需集成**。为每台主机 / 虚拟机 / 数据存储 / 许可证建实体，并生成聚合实体 `sensor.esxi_all_entities`；**没装集成时 ESXi 卡片没有数据**（只显示提示），安装见 6.44。
- **iKuai 集成** ([ikuai](https://github.com/chjspp520/ikuai)) — ⚠️ **`type: ikuai_card` 卡片的必需集成**。为整台爱快（系统 / 线路 / DHCP / 客户端 / Docker / 虚拟机 / 日志…）建实体，并生成聚合实体 `sensor.ikuai_all_entities`；**没装集成时爱快卡片没有数据**，安装见 6.46。注意**不是**旧的 `ikuai_router` 集成。
- **飞牛 fnOS 集成** ([fnos](https://github.com/chjspp520/fnos)) — ⚠️ **`type: fnos` 卡片的必需集成**。为整台飞牛（主机 / 存储 / Docker / 虚拟机 / 文件·相册·影视）建实体，并生成聚合实体 `sensor.fnos_all_entities`；**没装集成时飞牛卡片没有数据**（只显示提示），安装与配置见 6.37。
- **电力卡片** ([electricity-info-card](https://github.com/chjspp520/electricity-info-card)) — 家庭用电信息展示卡片，支持功率、电量、电费等多维度数据

---

## 三、快速上手

### 最简单的卡片 - 显示一个房间

```yaml
type: custom:room-elves-card
room_name: 客厅
entities:
  - entity: sensor.temperature
  - entity: sensor.humidity
buttons:
  - type: lights
    card:
      - entity: light.living
        name: 主灯
```

把这个配置复制到 HA 仪表盘，添加一个"手动模式"卡片，粘贴进去即可！

### 进阶示例 - 带多种设备

```yaml
type: custom:room-elves-card
room_name: 我的房间
head: true
theme: time
entities:
  - entity: sensor.temperature
    name: 温度
  - entity: sensor.humidity
    name: 湿度
buttons:
  - type: lights
    icon: mdi:lightbulb-group
    card:
      - entity: light.main
        name: 主灯
      - entity: light.night
        name: 夜灯
    per_line: 2
  - type: ac
    entity: climate.room
  - type: socket
    entity: switch.desk
    name: 书桌插座
  - type: dynamic_icon
    icon: mdi:window-closed
    rules:
      - condition:
          entity: binary_sensor.window
          operator: '=='
          value: 'on'
        icon: mdi:window-open
        color: '#3498db'
person:
  - main_entity: binary_sensor.motion
    rooms:
      房间: binary_sensor.motion
    width: 500px
overview:
  - type: environment
    rooms:
      户外:
        temperature: sensor.outdoor_temp
        humidity: sensor.outdoor_hum
```

---

## 四、基础配置结构

配置采用层级结构，最外层定义卡片的全局行为和外观，内层通过`style`、`entities`、`person`、`automation`、`overview`、 `buttons（头部模式才可配置该项）`等字段组织具体功能。

### 卡片的两大模式

卡片的布局由 `head` 字段决定，两种模式在视觉和功能上有显著差异：

| 特性 | 普通模式 (`head: false`) | 头部模式 (`head: true`) |
|------|--------------------------|-------------------------|
| **布局** | 左右分栏：左侧传感器 + 右侧按钮 | 按钮按网格铺满整张卡片 |
| **传感器** | 显示在卡片左侧（`entities`） | 不显示左侧传感器区域 |
| **概览栏** | ❌ 不支持 | ✅ 顶部显示全屋态势概览 |
| **按钮排列** | 右侧自动流式排列 | CSS Grid 网格，支持跨行跨列（`row_column`） |
| **网格控制** | 无 | `head_columns`（列数）、`head_rows`（行数） |
| **适用场景** | 单房间卡片，展示该房间传感器和设备 | 全屋控制中心，放在页面顶部总览全局 |

> 💡 **选择建议**：如果你只想管理一个房间，使用普通模式即可；如果你想在页面顶部放一张"全屋控制中心"卡片，同时总览所有房间的灯光、空调、人员、能耗等状态，请使用头部模式。

### 头部模式布局详解

头部模式下，卡片采用 **CSS Grid 网格布局**，按钮铺满整个卡片区域，支持灵活的跨行跨列控制。

#### 基本结构

```
┌──────────────────────────────────────────────────────────┐
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐   │
│  │ 按钮1 │ │ 按钮2 │ │ 按钮3 │ │ 按钮4 │ │ 按钮5 │ │ 按钮6 │   ← 网格排列
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘   │
│  ┌────────────────────┐ ┌──────┐ ┌──────────────────────┐│
│  │   按钮7 (2行3列)    │ │ 按钮8 │ │   按钮9 (1行4列)     ││  ← 支持跨行跨列
│  │                    │ └──────┘ │                      ││
│  └────────────────────┘          └──────────────────────┘│
├──────────────────────────────────────────────────────────┤
│  [公告栏 notice]                                          │  ← 公告通知（可选）
│  [概览栏 overview]                                        │  ← 概览
└───────────────────────────────────────────────────────────┘
```

#### 网格列数与行数

通过 `head_columns` 和 `head_rows` 控制网格的列数和行数：

```yaml
head: true
head_columns: 6                       # 网格列数，默认 6 列
head_rows: auto                       # 网格行数，默认 auto（自动撑开）
```

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `head_columns` | `number` | `6` | 网格列数，决定一行最多放几个按钮 |
| `head_rows` | `string` | `auto` | 网格行数，`auto` 表示根据按钮数量自动撑开 |

#### 按钮跨行跨列（row_column）

每个按钮可以通过 `row_column` 字段指定它在网格中占几行几列，格式为 `'序号,行数-列数'`：

```yaml
head: true
head_columns: 6

buttons:
  - type: lights
    card:
      - entity: light.living_ceiling
    row_column: '1,2-3'               # 序号1，占2行3列（大按钮）
  - type: ac
    card:
      - entity: climate.living
    row_column: '2,1-2'               # 序号2，占1行2列
  - type: media
    entity: media_player.tv
    row_column: '3,1-4'               # 序号3，占1行4列（横条）
  - entity: switch.plug               # 没有 row_column 会自动排列（占1行1列）
```

**`row_column` 格式说明：**

| 格式 | 含义 | 示例 |
|------|------|------|
| `'序号,行数-列数'` | 指定按钮占几行几列 | `'1,2-3'` = 序号1，占2行3列 |

**常见布局示例：**

| row_column | 效果 | 适用场景 |
|------------|------|----------|
| `'1,1-1'` | 1×1 标准小按钮 | 普通开关、插座 |
| `'1,2-2'` | 2×2 方形大按钮 | 灯光组、情景模式 |
| `'1,2-3'` | 2×3 宽高大按钮 | 用户卡片（含头像/天气） |
| `'1,1-2'` | 1×2 横向双宽 | 空调、窗帘 |
| `'1,1-4'` | 1×4 横条 | 媒体设备 |
| 不配置 | 自动排列（1×1） | 插座、独立开关等 |

> **序号**只决定排列顺序，不决定最终位置。系统会自动检测碰撞，优化布局。

#### 头部模式完整配置示例

```yaml
type: custom:room-elves-card
head: true
head_columns: 6
room_name: 全屋控制中心
style:
  width: 100%
notice:
  style:
    - width: 100%
    - height: 30px
  scroll: true
  items:
    - content: "{{iif(is_state('device_tracker.spp_39', 'not_home'), '不在家', '在家')}}"
    - content: "当前温度：{{state_attr('weather.home', 'forecast.0.temperature')}}℃"
overview:
  - type: environment
    rooms:
      户外:
        temperature: sensor.outdoor_temp
        humidity: sensor.outdoor_hum
  - type: person
    rooms:
      客厅: binary_sensor.living_motion
    person:
      - entity: person.zhangsan
        name: 张三
  - type: energy
    utilities:
      电力:
        entity: sensor.electricity_meter
        power: sensor.electricity_power
      空调:
        level: 2                    # 电力下的二级子集
        icon: mdi:air-conditioner
        content: >-
          今日：{{ states('sensor.ac_daily') | float(0) | round(1) }}kWh
      新风:
        level: 2                    # 电力下的二级子集
        icon: mdi:air-filter
        content: >-
          今日：{{ states('sensor.fan_daily') | float(0) | round(1) }}kWh
buttons:
  - type: user
    persons:
      - entity: person.zhangsan
        at_home: device_tracker.zhangsan_phone
    row_column: '1,2-3'
  - type: scene_mode
    scenes:
      - name: 离家
        actions:
          - entities:
              全屋灯: light.all_lights
            value: "off"
    row_column: '2,2-3'
  - type: lights
    card:
      - entity: light.living_ceiling
        name: 客厅灯
    row_column: '3,1-2'
  - type: ac
    card:
      - entity: climate.living
        name: 客厅空调
    row_column: '4,1-2'
  - type: curtain
    entity: cover.living_curtain
    row_column: '3,1-2'
  - type: socket
    card:
      - entity: switch.plug1
        name: 插座1
      - entity: switch.plug2
        name: 插座2
    row_column: '5,1-4'
person:
  - main_entity: binary_sensor.living_motion
    rooms:
      客厅: binary_sensor.living_motion
automation:
  - entity: automation.good_morning
    name: 早安
  - entity: automation.good_night
    name: 晚安
```

#### 头部多屏模式（多页滑动）

当 `head: true` 且按钮数量超过一页时，可以通过 `buttons_2`、`buttons_3`…… 等配置将按钮分到多个页面，**左右滑动即可切换页面**（跟手拖动 + 松手吸附；底部圆点指示当前页，拖动越过半屏时高亮就跟手过去）。桌面端也可以直接把**纵向滚轮**转成翻页。机制与其它选项卡完全一致，见「八-A、左右滑动」。

```yaml
head: true
head_columns: 6               # 第1页列数
head_columns_2: 4             # 第2页列数（可选，默认继承 head_columns）

buttons:                      # 第1页按钮
  - type: lights
    card:
      - entity: light.living_ceiling
  - type: ac
    card:
      - entity: climate.living

buttons_2:                    # 第2页按钮
  - type: curtain
    entity: cover.living_curtain
  - type: media
    entity: media_player.tv
    row_column: '1,1-3'       # 第2页也支持 row_column
```

**配置说明：**

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `buttons` | `array` | 必填 | 第1页按钮列表 |
| `buttons_2` | `array` | 无 | 第2页按钮列表 |
| `buttons_3` | `array` | 无 | 第3页按钮列表（支持无限多页） |
| `head_columns` | `number` | `6` | 第1页网格列数 |
| `head_columns_2` | `number` | 同 `head_columns` | 第2页独立列数 |

**多屏模式特性：**

| 特性 | 说明 |
|------|------|
| **滑动切换** | 横向整屏滑动，滚动捕捉（scroll-snap），支持触屏拖拽和鼠标滚轮 |
| **底部指示器** | 圆点显示当前页位置，点击圆点可直接跳转到对应页 |
| **每页独立列数** | 通过 `head_columns_N` 为每页设置不同网格列数 |
| **按钮排列** | 每页按钮独立排列，`row_column` 分别生效 |
| **概览栏/公告栏** | 仅在首页（Page 0）显示，切换页面时随首页一起滑动消失 |
| **页内按钮更新** | 实时状态更新覆盖所有页面，翻页后按钮状态已是最新 |

**完整示例：两页布局**

```yaml
head: true
head_columns: 6
head_columns_2: 3              # 第二页用大按钮，3列布局

buttons:
  - type: lights
    card:
      - entity: light.living_room
        name: 客厅灯
    row_column: '1,2-3'
  - type: ac
    entity: climate.living
    row_column: '2,2-3'
  - type: curtain
    entity: cover.bedroom_curtain
    row_column: '3,2-3'
  - type: media
    entity: media_player.tv
    row_column: '4,1-3'
  - type: scene_mode
    name: 全关
    scenes:
      - name: 全关
        actions:
          - entities:
              全屋灯: light.living_room
            value: "off"
    row_column: '5,1-3'

buttons_2:                     # 第二页：设备详情
  - type: sensor
    name: 温湿度
    entity: sensor.temperature
    row_column: '1,2-2'
  - type: sensor
    name: 湿度
    entity: sensor.humidity
    row_column: '1,3-3'
  - type: dynamic_icon
    name: 空气质量
    entity: sensor.air_quality
    icon: mdi:air-filter
    row_column: '2,1-3'
```

### 完整配置示例

```yaml
type: custom:room-elves-card       # 固定写法，告诉 HA 使用这张卡片
room_name: 客厅                     # 房间名称，会显示在卡片上
mode: grouped                       # 显示模式，保持 grouped 即可
head: false                         # 是否启用头部模式（true=启用，false=普通模式）
theme: light                        # 主题设置（见后文）
show_animation: true                # 是否让按钮上的图标有动画效果
style:                              # 自定义卡片外观（尺寸、颜色等）
  width: 350px                      # 卡片宽度
  height: auto                      # 卡片高度（auto=自动）
  background: 'rgba(255,255,255,0.9)'  # 背景颜色
  border-radius: 20px               # 圆角大小
entities:                           # 传感器列表（在普通模式下显示在左侧）
  - entity: sensor.temperature        # 实体ID
    name: 温度                        # 显示名称
    icon: mdi:thermometer             # 显示图标
buttons:                            # 按钮配置（这是卡片最重要的部分）
  - type: lights                      # 按钮类型
    card:
      - entity: light.living_room
        name: 主灯
person:                             # 人员在传感器（卡片左下角，点击弹出活动弹窗）
  - main_entity: binary_sensor.living_motion  # 主传感器
    icon: mdi:motion-sensor
    rooms:                                    # 各房间传感器映射
      客厅: binary_sensor.living_motion
      卧室: binary_sensor.bedroom_motion
    room_point_from: /local/point.json        # 平面图坐标数据文件
    width: 600px                              # 弹窗宽度
automation:                         # 自动化开关（卡片底部右侧，点击弹出控制面板）
  - entity: automation.good_morning     # 自动化实体ID
    name: 早安模式                       # 显示名称
  - entity: automation.away_mode
    name: 离家模式
overview:                           # 概览栏（⚠️ 仅 head 模式可用，非 head 模式无效）
  - type: environment                    # 环境概览：显示各房间温湿度
    rooms:
      户外:
        temperature: sensor.outdoor_temp
        humidity: sensor.outdoor_hum
      客厅:
        temperature: sensor.living_temp
        humidity: sensor.living_hum
  - type: person                         # 人员概览：显示在家人员与房间占用
    rooms:
      客厅: binary_sensor.living_motion
      卧室: binary_sensor.bedroom_motion
    person:
      - entity: person.zhangsan
        name: 张三
  - type: energy                         # 能耗概览：显示用电量、功率、余额
    utilities:
      电力:
        entity: sensor.electricity_meter
        power: sensor.electricity_power
        cost_entity: sensor.balance
      空调:
        level: 2                          # 电力下的二级子集
        icon: mdi:air-conditioner
        content: >-
          今日：{{ states('sensor.ac_daily') | float(0) | round(1) }}kWh
  - type: weather                        # 天气概览：显示天气预报
    entity: sensor.he_feng_tian_qi
  - type: right-col                      # 自定义右列（右侧窄列）：一行一个 content，支持模板 + HTML
    items:
      - icon: mdi:thermometer
        name: 客厅
        content: >-
          {{ states('sensor.living_temp') }}℃/{{ states('sensor.living_hum') }}%
      - icon: mdi:flash
        name: 今日
        content: >-
          {{ states('sensor.today_energy') | float(0) | round(1) }}kWh
    tap_action:
      action: navigate
      navigation_path: /lovelace/energy
```

### 顶层配置项说明

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `type` | ✅ | `string` | — | 固定为 `custom:room-elves-card` |
| `room_name` | ❌ | `string` | 无 | 房间名称，显示在卡片左上角。头部模式下也会作为卡片标识 |
| `mode` | ❌ | `string` | `grouped` | 卡片布局模式，保持 `grouped` 即可 |
| `head` | ❌ | `boolean` | `false` | 是否启用头部模式。`false` = 普通模式（左侧传感器 + 右侧按钮），`true` = 头部模式（按钮按网格铺满，顶部显示概览栏） |
| `head_columns` | ❌ | `number` | `6` | ⚠️ **仅 head 模式可用**。网格列数，决定一行最多放几个按钮 |
| `head_rows` | ❌ | `string` | `auto` | ⚠️ **仅 head 模式可用**。网格行数，`auto` 表示根据按钮数量自动撑开 |
| `primary_update_interval` | ❌ | `number` | `10` | ⚠️ **仅 head 模式可用**。primary 文本更新间隔（秒）。默认 10 秒，设为 `0` 表示实时更新（约每 2 秒），自定义秒数则按配置值更新 |
| `theme` | ❌ | `string` | `light` | 主题风格，可选 `light` / `dark` 或自定义主题名 |
| `show_animation` | ❌ | `boolean` | `true` | 是否启用按钮图标动画效果（如空调旋转、灯光呼吸等）。设为 `false` 禁用所有动画 |
| `icon_animation` | ❌ | `string` | 无 | **全局默认图标动画**。仅对未单独设置 `icon_animation` 的按钮生效，不覆盖单按钮配置。可选值：`shake` / `rotate` / `blink` / `breathe` / `jump` / `random-move` / `none`（详见动画效果） |
| `style` | ❌ | `object` | 无 | 自定义卡片外观，支持 `width`、`height`、`background`、`border-radius` 等 CSS 属性 |
| `entities` | ❌ | `array` | `[]` | 传感器数据列表，普通模式下显示在卡片左侧，支持温度、湿度、CO2、PM2.5 等任意传感器实体（详见第五节） |
| `buttons` | ❌ | `array` | `[]` | 按钮配置列表，卡片核心功能区域。支持 20+ 种按钮类型（灯光、空调、插座、耗材、窗帘、晾衣架、情景模式等），每种类型有专属弹窗控制面板（详见第六节） |
| `person` | ❌ | `array` | `[]` | 人员在传感器配置，卡片左下角显示人体感应小按钮，点击弹出活动弹窗（含实时状态、时间轴、活动统计、平面户型图）（详见第九节） |
| `automation` | ❌ | `array` | `[]` | 自动化开关列表，卡片底部右侧显示小图标，点击弹出控制面板统一管理所有自动化的启用/禁用（详见第十节） |
| `overview` | ❌ | `array` | `[]` | ⚠️ **仅 head 模式可用**，非 head 模式下配置无效。全屋设备态势概览栏，显示在卡片顶部，支持环境（温湿度）、人员（在家状态）、能耗（用电/功率/余额）、天气（多城市预报）、自定义右列（`right-col`）等类型。灯光/空调/插座/耗材概览在 head 模式下自动统计，无需手动配置（详见第十一节） |
| `notice` | ❌ | `object` | 无 | ⚠️ **仅 head 模式可用**，公告栏配置。显示在概览栏上方，支持模板文本和实体状态两种内容类型，多条内容时支持自动滚动（详见第十一节之公告栏） |

### 配置组织逻辑

卡片的功能模块按"显示位置"组织：

**普通模式 (`head: false`)：**
```
┌─────────────────────────────────────────┐
│  room_name                              │
├──────────┬──────────────────────────────┤
│          │                              │
│ entities │         buttons              │
│ 传感器区  │        设备按钮区             │
│ (左侧)   │         (右侧)                │
│          │                              │
├──────────┴──────────────────────────────┤
│ [person][automation]                    │  
└─────────────────────────────────────────┘
```

**头部模式 (`head: true`)：**
```

┌──────────────────────────────────────────────────────────┐
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐   │
│  │ 按钮1│  │ 按钮2│ │ 按钮3│ │ 按钮4│  │ 按钮5│ │ 按钮6│   │← 网格排列
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘   │
│  ┌────────────────────┐ ┌──────┐ ┌──────────────────────┐│
│  │   按钮7 (2行3列)    │ │ 按钮8 │ │   按钮9 (1行4列)     ││  ← 支持跨行跨列
│  │                    │ └──────┘ │                      ││
│  └────────────────────┘          └──────────────────────┘│
├──────────────────────────────────────────────────────────┤
│  [公告栏 notice]                                          │  ← 公告通知（可选）
│  [概览栏 overview]                                        │  ← 全屋态势概览
└───────────────────────────────────────────────────────────┘

```

> **注意：**
> - YAML 配置对缩进非常敏感，请使用 2 个空格作为缩进，不要使用 Tab 键。
> - `overview` 概览栏仅在 `head: true` 时生效。如果 `head: false`（普通模式），即使配置了 `overview` 也不会显示。
> - 灯光/空调/插座/耗材的概览会在 head 模式下自动统计，无需额外配置；环境、人员、能耗、天气概览需要手动配置。
> - `entities`、`person`、`automation` 在两种模式下均可使用，但 `entities` 的传感器数据仅在普通模式下显示在左侧。

### 独立卡片模式（standalone）

除了将多种设备聚合到一张卡片的常规用法，房间精灵卡片还支持**独立卡片模式**——将单个设备控制面板直接作为一张卡片使用，无需配置按钮网格。

### 适用场景

- 只需要控制单个设备（如一台空调、一扇窗帘），不需要房间聚合视图
- 在仪表盘中混合使用其他卡片，只需某一种设备的专属控制面板
- 想把空调/窗帘等控制面板放到不同位置，而非集中在一个房间卡片内

### 基本配置

只需添加 `standalone_type` 字段，卡片会自动跳过按钮渲染，直接显示对应设备的控制界面：

```yaml
type: custom:room-elves-card
standalone_type: ac              # 设备类型
entity: climate.living           # 实体 ID
name: 客厅空调                    # 显示名称（可选）
```

### 支持的设备类型

> **其中 `replay`（设备回放）/ `timer`（定时精灵）/ `wenshidu`（温湿度面板）三张，原先是在本卡片之外单独安装的独立卡片**（`device-replay-card.js` / `timer-control-card.js` / `wenshidu-card.js`），现已**整体并入房间精灵卡片**成为**内部子卡片**：独立 custom element 不再注册，配置改成本卡片的写法（分别见 6.40 / 6.41 / 6.42）。也就是说，用这三张现在**只需要房间精灵卡片本身**，不必再另装一张卡片。

> ⚠️ **下表里 `esxi` / `ikuai_card` / `bill` / `fnos` 四张卡依赖外部集成，必须先自行安装，否则卡片没有数据**：
> [`esxi_control`](https://github.com/chjspp520/esxi_control) · [`ikuai`](https://github.com/chjspp520/ikuai) ·
> [`ha_data_store`](https://github.com/chjspp520/ha_data_store)（v5.0.0+，个人账单） ·
> [`fnos`](https://github.com/chjspp520/fnos)（飞牛 fnOS 全实体卡片）。
> 安装方式与依赖细节见各自小节（6.37 / 6.44 / 6.45 / 6.46），**光装房间精灵卡片本身不够**。

**常规设备类型：**

| `standalone_type` | 说明 | 实体域 |
|-------------------|------|--------|
| `ac` | 空调控制面板（温度/模式/风速/摆风/使用统计） | `climate` |
| `curtain` | 窗帘控制面板（百分比滑块/双层/开合模式） | `cover` |
| `media` | 媒体控制面板（开关/播放控制） | `media_player` |
| `clothes_dryer` | 晾衣架控制面板（拖拽/收藏位置/灯光联动） | `cover` / `switch` |
| `nas` | NAS 服务器状态卡片（硬盘状态/电源控制/温度风扇） | HP iLO 集成实体 |
| `printer` | 打印机用量统计卡片（设备状态 / 日历热力图 / 墨量 / 累计统计 / 用墨占比环形图） | `sensor` |
| `entities_health` | 实体健康状态卡片（按房间/按状态展示全屋实体在线离线情况） | `sensor` |
| `daily_report` | 今日家庭日报卡片（summary 日报/状态横幅/关键指标） | `sensor` |
| `replay` | 设备回放卡片（户型图 + 设备时间轴，可播放/拖拽/选日期） | 任意（用 `entities:` 配置回放设备，见 6.40） |
| `timer` | 定时精灵卡片（延时/定时执行设备动作，含任务列表与历史） | 任意（后端 `sensor.ha_data_store_timer`，见 6.41） |
| `wenshidu` | 温湿度面板卡片（时间轴回放 + 温度/湿度两张户型图 + 3D 视图 + 历史曲线） | 任意（用 `rooms:` + `entities:` 配置，见 6.42） |
| `overview` | 概览面板卡片（把概览弹窗内容直接渲染成常显卡片） | 无（用顶层 `overview:` 配置） |
| `scene_mode` | 情景模式卡片（情景列表常显，点击就地执行并显示进度） | 无（用顶层 `scenes:` 配置） |
| `esxi` | ESXi 虚拟化卡片（主机状态 / 虚拟机批量操作 / 屏幕墙三选项卡）**⚠️ 需先装 `esxi_control` 集成** | `esxi_control` 集成实体（聚合实体 `sensor.esxi_all_entities`，回退 `sensor.entities`，见 6.44） |
| `bill` | 个人账单卡片（概览 / 分析 / 日历 / 查询 / 历史五选项卡 + 窗口内下钻图表）**⚠️ 需先装 `ha_data_store` v5.0.0+** | ha_data_store 账单接口（配 `api_base_url` + `key`，见 6.45） |
| `ikuai_card` | iKuai 全实体卡片（路由 / Docker / 虚拟机 / 日志四页签，只配一个聚合实体即认全设备）**⚠️ 需先装 `ikuai` 集成** | 新集成 `ikuai` 的聚合实体 `sensor.ikuai_all_entities`（见 6.46） |
| `fnos` | 飞牛 fnOS 全实体卡片（主机 / 存储 / Docker / 虚拟机 / 应用五页签，只配一个聚合实体即认全设备）**⚠️ 需先装 [`fnos`](https://github.com/chjspp520/fnos) 集成** | 飞牛 fnOS 集成的聚合实体 `sensor.fnos_all_entities`（见 6.37） |
| `sensor` | 传感器卡片（数值显示） | `sensor` |
| `switch` | 开关卡片 | `switch` / `input_boolean` |
| `select` | 选择下拉卡片 | `select` / `input_select` |
| `number` | 数字输入卡片 | `number` / `input_number` |
| `button` | 按钮卡片 | 任意 |
| `slider` | 滑块卡片 | `number` / `input_number` |
| `usage` | 用量卡片（电费/水费等） | `sensor` |
| `usage_calendar` | 使用量日历卡片（日历视图 + 年/月/日 ECharts 图表） | 任意 |

**图表类型（基于 ECharts / SVG）：**

| `standalone_type` | 说明 | 渲染引擎 |
|-------------------|------|---------|
| `chart` / `chart_line` | 曲线趋势图 | ECharts |
| `chart_gauge` | 仪表图 | 纯 SVG |
| `chart_progress` | 进度条图 | 纯 CSS |
| `chart_bar` | 柱状图 | 纯 CSS |
| `chart_pie` | 圆角环形图 | ECharts |
| `chart_pie_full` | 完整饼图 | ECharts |
| `chart_heatmap` | 日历热力图 | ECharts |
| `chart_calendar` | 日历图 | ECharts |
| `chart_mixed` | 混合图表 | ECharts |
| `chart_nightingale` | 南丁格尔玫瑰图 | ECharts |
| `chart_scatter` | 散点图 | ECharts |

> ⚠️ **ECharts 依赖**：使用 ECharts 渲染的图表类型需要 `echarts.min.js`。卡片优先加载本地文件 `www/pobaby_package/js/echarts.min.js`，若不存在则自动从 CDN 加载。

### 配置示例

**空调独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: ac
entity: climate.bedroom
name: 卧室空调
```

**使用量日历独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: usage_calendar
api:
  entity: climate.keting_ac_keting_ac
title: 客厅空调用电量日历
show_title: false
width: 400px
show_popup: true
calc_value_choose: value
units: "°,h"
series: "用量,时长"
```

> 💡 `api_base_url` 和 `key` 省略时自动从顶层配置继承（如有）。

**温湿度面板独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: wenshidu
card_width: 440px
default_main_room: 客厅          # 主房间：时间轴渐变按它的温度着色
main_entities:
  客厅:
    temperature: sensor.keting_wendu
rooms:                           # 户型图的房间多边形（SVG points 坐标）
  - id: 客厅
    name: 客厅
    points: 68,283 253,283 253,229 311,229 311,331 273,331 273,508 128,509 128,353 68,352
    labelX: "206"
    labelY: "311"
    dataX: "190"
    dataY: "330"
entities:                        # 每个房间的温湿度实体
  客厅:
    temperature: sensor.keting_wendu
    humidity: sensor.keting_shidu
temp_colors:
  16-20: "#3498db"
  20-25: "#2ecc71"
  25-30: "#f39c12"
  30-32: "#e74c3c"
```

> 完整字段（多房间、字体、单位显隐、3D、外部 API 数据源等）见 6.42。

**设备回放独立卡片**

把「户型图 + 设备时间轴」做成可播放的一天回放（内部子卡片，无需另装卡片）：

```yaml
type: custom:room-elves-card
standalone_type: replay
card_width: 500                     # 设计基准宽度（实际随容器等比缩放）
floorplan_height: 400               # 户型图高度
background_image: /local/pobaby_package/floorplan/1f.png
entities:                           # 回放设备列表（坐标按 card_width 基准书写）
  - entity: light.ke_ting
    name: 客厅-大灯
    x: 0
    y: 0
    image_url: /local/pobaby_package/device/ke_ting_on.png
    image_scale: 100
  - entity: climate.ke_ting
    name: 客厅-空调
    x: 300
    y: 100
    image_url: /local/pobaby_package/device/kong_tiao.png
    image_scale: 30
    rotation: 90
```

> 设备项字段（坐标 / 图标 / 缩放 / 旋转 / 传感器气泡 / 轨道等）与顶层字段见 6.40。

**ESXi 虚拟化独立卡片**

```yaml
# 最省事：只给聚合实体
type: custom:room-elves-card
standalone_type: esxi
entity: sensor.esxi_all_entities     # 默认就是它（旧环境自动回退 sensor.entities）
name: 虚拟化

# 需要收窄范围时再加（都是可选项）
# hosts: 主机                         # 只保留这些主机
# vms: Windows 10                    # 只保留这些虚拟机
# exclude: ESXi 统计                  # 排掉集成的兜底设备
# show_screen: true                  # 是否生成「屏幕」页签
# show_refresh: true                 # 头部「立即刷新数据」按钮
# show_sync: true                    # 「主机配置」里的「同步（重载集成）」
# confirm_power_off: false           # 关机不二次确认
```

> ⚠️ 需先安装 [`esxi_control`](https://github.com/chjspp520/esxi_control) 集成；高度由内容决定，卡片自带 3 秒值级刷新。完整字段见 6.44。

**个人账单独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: bill
name: 个人账单
api_base_url: http://192.168.1.100:8123/api/ha_data_store/
key: 你的KEY
page_size: 20                        # 明细分页每页条数（默认 20）
recent_days: 7                       # 概览「最近 N 日」天数（默认 7）
# source: 微信                       # 初始来源筛选（可省）
# direction: 支出                    # 初始收支方向筛选（可省）
```

> ⚠️ 需先安装 [`ha_data_store`](https://github.com/chjspp520/ha_data_store) **v5.0.0+** 并开好账单接口生成 Key；**无轮询** —— 只在打开卡片 / 切到未取过数的页 / 点刷新 / 换查询条件时取数。完整字段见 6.45。

**iKuai 全实体独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: ikuai_card
entity: sensor.ikuai_all_entities    # 默认就是它，可省
name: 爱快
accent: auto                         # 主色：命名色 / hex / auto / 实体驱动
width: 760px                         # 卡片基准宽度（弹窗里用 popup_width）
# confirm_power_off: true            # 关机类操作是否二次确认（默认开）
```

> ⚠️ 需先安装 [`ikuai`](https://github.com/chjspp520/ikuai) 集成；**只配一个聚合实体**即可认全路由 / Docker / 虚拟机 / 日志，高度 `auto`、自带 3 秒值级刷新（不参与独立模式的 1 秒轮询）。完整页签与字段见 6.46。

**飞牛 fnOS 全实体独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: fnos
entity: sensor.fnos_all_entities     # 默认就是它，可省（被占号时自动识别 _2 后缀）
name: 飞牛 fnOS
icon: mdi:nas
accent: "#26a69a"                    # 主色（可省）
popup_width: 900px                   # 弹窗宽度（卡片形态下不生效，可省）
# confirm_power: true                # 重启 / 关机 / 强制关机是否二次确认（默认 true）
```

> ⚠️ 需先安装 [飞牛 fnOS 集成](https://github.com/chjspp520/fnos)；**只配一个聚合实体**即可认全主机 / 存储 / Docker / 虚拟机 / 应用，高度 `auto`、自带 3 秒值级刷新。完整页签与字段见 6.37。

**窗帘独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: curtain
entity: cover.living_room_curtain
name: 客厅窗帘
```

**晾衣架独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: clothes_dryer
entity: cover.clothes_dryer
name: 阳台晾衣架
```

**媒体独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: media
entity: media_player.living_room_tv
name: 客厅电视
```

**曲线图独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: chart_line
entity: sensor.living_room_temperature
name: 客厅温度趋势
hours_to_show: 24
```

**仪表图独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: chart_gauge
entity: sensor.living_room_humidity
name: 客厅湿度
```

**进度条图独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: chart_progress
entity: sensor.cpu_usage
name: CPU 使用率
```

**柱状图独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: chart_bar
entity: sensor.daily_power_consumption
name: 每日用电量
```

**环形图独立卡片**

```yaml
type: custom:room-elves-card
standalone_type: chart_pie
entity: sensor.power_distribution
name: 用电分布
```

**概览面板独立卡片**

把「全屋态势」概览弹窗的内容（微气候 / 全屋能耗 / 人在 / 设备概览 / 实体健康 等）直接渲染成一张常显卡片，配置沿用概览弹窗同一套 `overview:` 列表：

```yaml
type: custom:room-elves-card
standalone_type: overview
overview:
  - type: environment
    name: 环境
    icon: mdi:thermometer-water
    rooms:
      户外:
        temperature: sensor.ketingwaiyangmian_wendu
        humidity: sensor.ketingwaiyangmian_shidu
      客厅:
        temperature: sensor.keting_wendu
        humidity: sensor.keting_shidu
  - type: person
    name: 人在
    icon: mdi:run
    rooms:
      客厅: binary_sensor.keting_renzai
    person:
      - name: Alix
        entity: device_tracker.ip15_94
  - type: overview_device
    icon: mdi:server
    name: 服务器开启数量
    condition: 'on'
    entities:
      - entity: binary_sensor.192_168_1_90
        name: Exsi
    tap_action:
      card_config:
        from_config_id: fuwuqi
        get_type: all
  - type: entities_health
    entity: sensor.hashu_ju_tong_yi_cun_chu_xi_tong_frontend_card_entities_health
    name: 实体健康
    icon: mdi:heart-pulse
```

> **说明：**
> - 与头部模式共用同一份 `overview:` 配置格式，各子项含义见「概览弹窗」章节。
> - 刷新由 hass 推送驱动（概览相关实体变化即更新），不轮询；内容与弹窗完全同源（同一套渲染 + 同一套实时更新链路）。
> - **灯 / 空调 / 插座 / 耗材** 四张概览卡片的数据来自房间 `buttons` 配置，面板形态下没有 `buttons` → 不会出现；其余（微气候 / 全屋能耗 / 人在 / 天气 / 设备概览 / 自动化管理 / 实体健康）均正常。
> - `recently-used`（常用）是概览**行**上的入口按钮，不属于弹窗内容，因此面板形态下不显示。
> - 面板内的 `from_config_id` 引用在点击时从全局配置仓库解析，需要页面上**其他卡片**已注册该 `config_id`（例如同一看板的头部模式卡片）。
> - 居住动态卡片右侧的户型图与弹窗同口径：房间几何来自 `room_point_from`（未配置时用默认路径 `/local/pobaby_package/point/point.json`）加载后合并的数据。

**情景模式卡片**

把情景模式气泡的内容直接渲染成一张常显卡片，配置沿用按钮里 `type: scene_mode` 的同一套 `scenes:` 列表：

```yaml
type: custom:room-elves-card
standalone_type: scene_mode
width: 400px
entity: input_text.scene_mode          # 执行历史写入的实体（可选）
verify_timeout: 10
scenes:
  - name: 睡眠模式（关闭全屋灯光）
    icon: mdi:bed-clock
    icon_color: '#006e54'
    confirm: true
    actions:
      - name: 全屋灯光
        value: 'off'
        entities:
          客厅_大灯: light.keting_dadeng
          厨房_大灯: light.chufang
          主卧_吸顶灯: light.zhuwo_xidingdeng
      - name: 小卫插座
        select: true
        value: 'off'
        entities:
          小卫插座: switch.xiaoweishengjian_chazuo
  - name: 开始远程工作
    icon: mdi:remote-desktop
    confirm: true
    actions:
      - entity: switch.giot_cn_1165554495_v61ksm_on_p_2_1
        value: 'on'
        name: 开机
        confirm_entity: sensor.iot_cn_2026036605_pw6u1_electric_power_p_3_2
        confirm_value: '>10'
        confirm_time: 5
      - entity: switch.xian_shi_qi
        value: 'off'
        name: 显示器
```

> **说明：**
> - 与按钮 `type: scene_mode` 共用同一套 `scenes:` 格式（`actions` / `entities` / `value` / `select` / `confirm` / `fold` / `delay` / `confirm_entity` / `confirm_value` / `confirm_time` 语义完全一致）。
> - 卡片形态**始终是列表模式**（等价于气泡的 `mode: bubble`）：卡片没有"点击按钮"这一动作，否则只配一个情景时会被判为直接执行、渲染瞬间就跑掉。
> - 点击某个情景 → 勾选项生效 → 卡片内容就地切成进度面板（执行中 / 验证中 / 逐项结果）→ 5 秒后自动回到情景列表；执行结果写入 `entity`（`input_text`）。
> - 实时刷新由 hass 推送驱动（动作角标"已开启/总数"、设备明细的 on 状态、执行历史行），不需要轮询。
> - 展开/折叠：`fold: true` 可让该情景的动作列表默认收起（`expand_all` 当前无实现）。

### 透传配置

`standalone_type` 和 `entity` 之外的所有配置字段会自动透传给内部卡片，可以像在 `buttons` 中一样使用各设备类型的专属配置：

```yaml
type: custom:room-elves-card
standalone_type: ac
entity: climate.living
name: 客厅空调
current_temperature: sensor.living_temperature    # 当前温度传感器
power_display_entity: sensor.ac_power            # 功率显示实体
show_usage: true                                  # 显示使用统计
```

> **注意：** 独立卡片模式与普通/头部模式互斥。配置了 `standalone_type` 后，`head`、`buttons`、`entities` 等字段均无效。例外：`standalone_type: overview` 用顶层 `overview:` 配置面板内容；`standalone_type: scene_mode` 用顶层 `scenes:` 配置情景列表。

---

## 五、添加传感器数据区域（entities）

在普通模式下，卡片左侧会显示房间的传感器数据，比如温度、湿度等。

```yaml
entities:
  - entity: sensor.living_room_temperature   # 温度传感器实体
    name: 室内温度                            # 显示的名称
    icon: mdi:thermometer                     # 显示的图标
  - entity: sensor.living_room_humidity
    name: 湿度
    icon: mdi:water-percent
  - entity: sensor.co2
    name: CO2
    icon: mdi:molecule-co2
  - entity: sensor.pm25
    name: PM2.5
    icon: mdi:air-filter
```

每个实体还可以配置点击动作：
```yaml
  - entity: sensor.temperature
    name: 温度
    tap_action:
      action: more-info              # 点击弹出详细信息
```

### 全局 entities 点击动作（entities_tap_action）

可以为所有实体配置一个全局点击动作，当实体未单独配置 `tap_action` 时自动生效（相当于默认值）。同时也作为平面户型图数据的存储位置。

```yaml
entities:
  - entity: sensor.living_room_temperature
    name: 室内温度

entities_tap_action:                  # 全局配置，所有实体共用
  action: more-info
```

> 实体自身的 `tap_action` 优先级高于 `entities_tap_action`。即实体单独配置了 `tap_action` 时，使用自身的配置；未配置时回退到全局 `entities_tap_action`。

> 找实体 ID 的方法：在 HA 的"开发者工具" → "状态"中，可以看到所有可用的实体。

---

## 六、按钮配置详解（核心功能）

`buttons` 是卡片最重要的配置，每个按钮可以控制一种或一组设备。

> **分页与滑动**：按钮分到多页（`buttons_2` / `buttons_3` …）或弹窗里分了选项卡时，**都支持左右滑动切换** —— 规则与支持范围见「八-A、左右滑动」。

> **`icon_text` 通用支持**：所有按钮类型（含 `type: button`、独立按钮、设备分组等）均支持 `icon_text` 配置项，
> 用于在图标右上角显示一个斜三角徽章文字。支持 `preset_xx` 预设映射（如 `preset_state`、`preset_ac`、`preset_fan`、`preset_humidifier`、`preset_qweather`、`preset_media`）
> 和 Jinja2 模板语法。当不配置 `icon_text` 时不显示该斜三角。详见各类型配置表和 22.4 节。

**buttons 支持两种格式：**

**格式一：标准数组格式（推荐）**

```yaml
buttons:
  - type: lights
    card:
      - entity: light.living_room
        name: 主灯
  - type: ac
    entity: climate.living
```

**格式二：对象格式（快捷写法）**

当需要将多个实体按类型快速分组时，可以键名作为 type、值作为 card 数组：

```yaml
buttons:
  lights:                               # 键名作为 type
    - entity: light.living_room          # 直接写 card 数组的内容
      name: 客厅灯
    - entity: light.bedroom
      name: 卧室灯
  socket:                               # 多个 type 可混用
    - entity: switch.plug1
      name: 插头1
```

两种格式可以混用，卡片会自动合并处理。

### 6.1 灯光组 (type: lights)

用于控制一组灯（如一个房间里的所有灯）。点击按钮切换开关状态，长按弹出灯光控制面板（可调节亮度、色温）。

```yaml
buttons:
  - type: lights
    icon: mdi:lightbulb-group              # 默认显示的图标
    on_icon: mdi:lightbulb-group           # 灯开启时的图标
    off_icon: mdi:lightbulb-group-off      # 灯关闭时的图标
    on_color: '#f1c40f'                   # 灯开启时图标的颜色
    off_color: '#95a5a6'                  # 灯关闭时图标的颜色
    card:                                  # 这个组里有哪些灯
      - entity: light.living_ceiling        # 灯的实体ID
        name: 天花灯                        # 灯的名称
        room: 客厅                          # 所属房间（用于弹窗分组）
        global_exception: true   # 全关/全开/取反时跳过此实体
        # ── 收藏快捷按钮（可选，在滑块下方显示快捷圆点）──
        collect_brightness:                # 收藏亮度（百分比）
          - name: 夜灯
            brightness: 20%
          - name: 阅读
            brightness: 50%
          - name: 明亮
            brightness: 80%
        collect_colour_temperature:        # 收藏色温（Kelvin）
          - name: 暖光
            colour_temperature: 2000
          - name: 自然光
            colour_temperature: 5000
          - name: 冷光
            colour_temperature: 6500
        collect_colors:                    # 收藏颜色（HEX色值）
          - name: 红
            color: '#ff0000'
          - name: 绿
            color: '#00ff00'
          - name: 蓝
            color: '#0000ff'
      - entity: light.living_floor_lamp
        name: 落地灯
        room: 客厅
    group_lights_by_room: true             # 在弹窗中按房间分组显示
    show_badge: true                       # 显示已开启的灯的数量角标
    per_line: 2                            # 弹窗中每行显示几个灯
    close_time: 300                        # 自动关闭倒计时（秒），0=不自动关闭
```

**灯光组专用配置项：**

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `close_time` | `number` | `0` | 弹窗自动关闭倒计时（秒）。设为 `0` 时不自动关闭，设为 `300` 表示 300 秒后自动关闭弹窗 |
| `group_lights_by_room` | `boolean` | `false` | 弹窗中是否按 `room` 字段分组显示灯光，各房间独立区域展示 |
| `show_duration` | `boolean` | `false` | 按钮上是否显示已开启时长 |

**card 子项配置项：**

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `room` | `string` | 无 | 所属房间（用于弹窗按房间分组） |
| `global_exception` | `boolean` | `false` | `true` 时，在弹窗中使用"全关"/"全开"/"取反"等批量操作时**跳过**此实体。适用于不想被批量控制的设备（如安防灯、常亮夜灯等） |
| `collect_brightness` | `array` | 无 | 收藏亮度快捷按钮列表，每个子项含 `name`（显示名称）和 `brightness`（亮度百分比，如 `20%` 或 `50`） |
| `collect_colour_temperature` | `array` | 无 | 收藏色温快捷按钮列表，每个子项含 `name`（显示名称）和 `colour_temperature`（色温值，单位 Kelvin，如 `2000` = 暖光，`6500` = 冷光） |
| `collect_colors` | `array` | 无 | 收藏颜色快捷按钮列表，每个子项含 `name`（显示名称）和 `color`（HEX 色值，如 `'#ff0000'`） |

**收藏快捷按钮说明：**

收藏快捷按钮显示在灯光弹窗控制面板的滑块下方，以圆点形式展示，点击即可快速切换到预设值：

- **`collect_brightness`**：收藏亮度，圆点内用黄色渐变填充百分比表示亮度高低。配置后即使设备不支持亮度调节也会显示
- **`collect_colour_temperature`**：收藏色温，圆点颜色根据色温值自动计算（暖光偏橙、冷光偏蓝）。配置后即使设备不支持色温调节也会显示
- **`collect_colors`**：收藏颜色，圆点直接使用配置的 HEX 色值填充

> 三个收藏属性均可配置在 `type: lights` 的 `card` 子项上（每盏灯独立配置），也可配置在 `type: light` 单灯的顶层。配置在 `type: lights` 顶层时，会自动向下透传到所有 `card` 子项（子项自身未配置时使用顶层配置）。

> `global_exception` 同样适用于 `type: socket` 的 card 子项。此配置项仅在灯光/插座等聚合按钮的弹窗批量操作中生效，不影响单个按钮的点按操作。

### 6.2 单灯 (type: light)

控制单个灯。功能与灯光组类似，但只控制一个设备。同样支持 `collect_brightness`、`collect_colour_temperature`、`collect_colors` 收藏快捷按钮。

```yaml
  - type: light
    entity: light.bedroom_light             # 灯的实体ID
    name: 卧室灯
    on_color: '#f1c40f'
    off_color: '#95a5a6'
    show_duration: true                     # 显示已开启时长
    close_time: 600                         # 自动关闭倒计时（秒），0=不自动关闭
    # ── 收藏快捷按钮（可选，配置方式与 lights 的 card 子项一致）──
    collect_brightness:
      - name: 夜灯
        brightness: 20%
      - name: 明亮
        brightness: 80%
    collect_colour_temperature:
      - name: 暖光
        colour_temperature: 2000
      - name: 冷光
        colour_temperature: 6500
    collect_colors:
      - name: 红
        color: '#ff0000'
      - name: 蓝
        color: '#0000ff'
```

### 6.3 空调 (type: ac)

显示空调状态，点击弹出空调控制面板（调温、模式、风速）。图标会根据运行模式自动变化（雪花=制冷、太阳=制热、水滴=除湿、风扇=吹风），并带有旋转动画。

---
### 三种使用方式

#### 方式一：独立卡片（standalone_type）

```yaml
type: custom:room-elves-card
standalone_type: ac
entity: climate.living_room
name: 客厅空调
power_entity: sensor.living_ac_energy_yearly
power_display_entity: sensor.living_ac_power
humidity_entity: sensor.living_room_humidity
current_temperature: sensor.living_room_temp
width: 400px
page_1: both_page                         # 第二页：日历使用统计 + 图表
api_base_url: /api/ha_data_store/         # 日历图表 API 地址（可选）
key: your_api_key                         # API 密钥（可选）
```

#### 方式二：单个按钮（buttons 中使用单设备）

单台空调直接在顶层配置 `entity`，无需 `card` 数组，**不显示角标**：

```yaml
buttons:
  - type: ac
    entity: climate.living_room
    name: 客厅空调
    room: 客厅
    power_entity: sensor.living_ac_energy_yearly
    power_display_entity: sensor.living_ac_power
    humidity_entity: sensor.living_room_humidity
    current_temperature: sensor.living_room_temp
    width: 400px
```

#### 方式三：聚合多设备（buttons 中使用 card 数组）

多台空调使用 `card` 数组配置，按钮上**显示角标**（已开启数量）：

```yaml
buttons:
  - type: ac
    show_badge: true
    card:
      - entity: climate.living_room
        name: 客厅空调
        room: 客厅
        power_entity: sensor.living_ac_energy_yearly
        power_display_entity: sensor.living_ac_power
      - entity: climate.bedroom
        name: 卧室空调
        room: 卧室
        power_entity: sensor.bedroom_ac_energy_yearly
```

> **角标说明：** 单台空调（使用 `entity` 字段）不显示角标；多台空调（使用 `card` 数组）时按钮上显示已开启的数量。

**多空调组顶部信息栏 + 用电合计日历（v5.3.3）：**

多台空调（`card` 数组）的弹出窗口**顶部**会显示一条**一句话信息栏**（整行可点击），形如：

```
2台运行中 · 总功率 850w · 今日 3.2kWh · 5.1h
```

- **运行台数**：当前开启的空调数量；**0 台时显示「没有正在运行的」**
- **总功率**：Σ 各台 `power_display_entity` 当前值 —— **< 1000W 显示 `xxw`（取整），≥ 1kW 显示 `x.xkW`**
- **今日**：当日各台用电量合计（`x.xkWh`）· 当日运行时长合计（`x.xh`，含正在运行空调的实时时长）

> **显示值为 0 的项一律不显示**：`今日 0.0kWh` / `0.0h` 这类没有信息量的片段会整段消失，例如全天没开机时信息栏就是 `没有正在运行的 · 总功率 15w`。

信息栏**背景色随第一台开启空调的模式**变化（全部关闭时用默认浅色背景）。未配置 `power_display_entity` 时隐藏「总功率」；未配置 `power_entity` 时「今日」段里只显示时长。

点击信息栏弹出的**合计日历**有两种形态，**默认就是「使用量日历卡片（多实体）」**，不需要配置：

| 形态 | 何时使用 | 说明 |
|------|----------|------|
| **使用量日历卡片（多实体）**（默认） | 不配置 | 直接内嵌 [6.35 使用量日历卡片](#635-使用量日历卡片-type-usage_calendar) 的**多实体聚合**形态：日历 / 历史 / 年 / 月 / 日 / 洞察**六个选项卡**、时段全景图与下钻、日历格子「N 台」角标、分设备甘特图等全部复用 |
| 原内置合计日历 | `ac_calendar_card: old` | 本卡片自己实现的单页合计日历（月网格 + 年/月/历史），见下方小节 |

**默认形态的内部自动配置**（不用手写 `api` / `entities`）：

| 项 | 来源 |
|------|------|
| `api.entities` | 空调组内每台空调的 `entity`（后端记录的就是这批实体），名字沿用各台的 `name` |
| `api_base_url` / `api.key` | 空调组节点 → 组内空调 → 卡片顶层配置，逐级回退 |
| `title` | 「组名 + 用电量日历」，如「全屋空调用电量日历」 |
| 展示项 | `width: 100%`、`show_popup: true`、`calc_value_choose: value`（第二个数值显示**时长**）、`data_value_color: #00a381`、`calc_value_color: #c85179`、`units: °,h`、`series: 用量,时长`、`decimals: 1,2` |

```yaml
buttons:
  - type: ac
    name: 全屋空调
    # ac_calendar_card: old          # ← 只有想用回原内置合计日历才加这一行
    card:
      - entity: climate.keting_ac_keting_ac
        name: 客厅空调
      - entity: climate.zhuwo_xxx
        name: 主卧空调
```

**`ac_calendar_card` 取值：**

| 取值 | 形态 |
|------|------|
| 不配（默认）/ `usage` / `usage_calendar` | 使用量日历卡片（多实体） |
| `old` / `builtin` / `legacy` | 原内置合计日历 |

也可以写**对象形式**微调使用量日历卡片（不写 `type` 即为该形态），除 `type` 外的键会透传给卡片配置：

```yaml
    # 宽度 620px 的弹窗 + 200 度月度预算 + 单位换成 kWh
    ac_calendar_card: { width: 620px, monthly_budget: 200, units: "kWh,元" }
    # 对象形式要用原内置合计日历
    ac_calendar_card: { type: old }
```

> 位置优先级：空调组节点 → 组内第一台空调 → 卡片顶层配置（与 `api_base_url` 同口径）。
> 对象形式的 `width` 决定**弹窗宽度**；不写时默认**沿用空调组的 `width`**（未配置时退回 `min(560px, 92vw)`）。

**原内置合计日历（`ac_calendar_card: old`）：**

- **宽度**遵循空调组 `width` 配置，高度 420px
- 含**月视图网格 + 年 / 月 / 历史**图表 tab，数据为多台空调**按天/按年累加合计**
- 日历网格固定同时显示**用电量 + 时长**；未配置 `power_entity` 时只显示时长
- **当日**正在运行的空调会通过 `device_history` 补充实时运行时长/用电量并累加
- 点击日历单元格弹出气泡：**左栏信息**（开机次数/运行台数/总用电/总时长/用电最多）+ **右栏饼图**（轮换显示用电量/时长，自动轮换 + 点击切换）+ **下方分设备明细**（仅当天有数据的空调，带色点标注）

> 💡 未配置 `power_entity`（用电量实体）时，原内置合计日历的信息栏、日历、饼图、年/月/历史图表中所有涉及用电量的部分都会自动隐藏，仅保留时长维度。

**配置字段说明：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ❌ | `string` | 无 | 空调 climate 实体 ID（单设备时必填） |
| `name` | ❌ | `string` | 无 | 空调名称 |
| `room` | ❌ | `string` | 无 | 空调所在房间（用于按房间分组） |
| `power_entity` | ❌ | `string` | 无 | 年累计用电量 sensor 实体 ID |
| `power_display_entity` | ❌ | `string` | 无 | 当前功率 sensor 实体 ID |
| `humidity_entity` | ❌ | `string` | 无 | 湿度 sensor 实体 ID |
| `current_temperature` | ❌ | `string` | 无 | 室温 sensor 实体 ID |
| `icon` | ❌ | `string` | 自动 | 自定义图标（默认随模式变化） |
| `width` | ❌ | `string` | `auto` | 弹窗宽度 |
| `popup_position` | ❌ | `string` | `null` | 弹窗位置 |
| `page_1` | ❌ | `string` | 无 | 第二页类型。`power_page`=只显示用电量；`duration_page`=只显示使用时长；`both_page`=同时显示用电量和时长。配置后卡片变为左右滑动双页模式，左页为控制面板，右页为日历使用统计 + 年/月/历史图表 |
| `api_base_url` | ❌ | `string` | 继承顶层 | API 数据接口地址，用于日历图表数据查询。不配置时自动从顶层配置继承 |
| `key` | ❌ | `string` | 继承顶层 | API 密钥，不配置时自动从顶层配置继承 |
| `mode_buttons` | ❌ | `array` | 无 | 自定义模式按钮列表（见 6.3.1） |
| `fan_buttons` | ❌ | `array` | 无 | 自定义风速按钮列表（见 6.3.2） |
| `swing_buttons` | ❌ | `array` | 无 | 自定义摆风按钮列表（见 6.3.3） |
| `swing_select` | ❌ | `string` | 无 | 摆风下拉模式（见 6.3.3.2）。`true`=两行都用下拉；`vertical`=仅垂直用下拉；`horizontal`=仅水平用下拉；`both`=两行都用下拉 |
| `swing_select_labels` | ❌ | `object` | 无 | 自定义摆风选项显示名称（见 6.3.3.2）。`{ vertical: {off:'关',...}, horizontal: {off:'关',...} }` |
| `hide` | ❌ | `string/array` | 无 | 隐藏指定摆风档位（见 6.3.3.3）。支持模式名（如 `swing_upper`）或特殊值 `swing_horizontal_modes`（隐藏整行水平摆风） |
| `features` | ❌ | `array` | 无 | 功能按钮列表（见 6.3.4） |

---

#### 6.3.1 自定义模式按钮 (mode_buttons)

**配置值支持三种形式：**

| 配置值 | 行为 |
|--------|------|
| 不配置 / `mode_buttons: emoji` | 内置 emoji 预设（关`关` / 制冷`❄️` / 制热`🔥` / 除湿`💧` / 送风`🌀` / 自动`A`），无动画 |
| `mode_buttons: icon` | 内置图标预设（mdi 图标 + 动画），制冷/制热/送风/自动旋转，除湿呼吸 |
| 数组 `[{...}, {...}]` | 完全自定义（支持 toggle / mode 两种类型，支持 animation 字段） |

**快捷用法：一行切换图标模式**

```yaml
mode_buttons: icon       # 使用内置图标预设（带动画）
# 或
mode_buttons: emoji      # 使用内置 emoji 预设（等于不配置）
```

**自定义场景：** 部分空调的模式值非标准，或通过 `select.*` 实体控制；或需要自定义图标/顺序/子集。配置数组后可完全自定义模式按钮列表，支持两种类型：

**类型 1：`toggle` —— 通过外部实体控制模式**（适配非标空调）

```yaml
mode_buttons:
  - type: toggle
    switch_entity: select.xiaomi_ac_hvac_mode       # select 实体
    switch_name: 制冷
    icon: mdi:snowflake
    toggle_attribute: current_option
    toggle_value: cool
  - type: toggle
    switch_entity: select.xiaomi_ac_hvac_mode
    switch_name: 制热
    icon: mdi:fire
    toggle_attribute: current_option
    toggle_value: heat
```

**类型 2：`mode` —— 映射到 `climate.set_hvac_mode`**（用于自定义文本/顺序/子集）

下面示例覆盖空调全部 6 种标准模式，可直接复制使用：

```yaml
mode_buttons:
  - type: mode
    name: 关闭
    value: 'off'
    icon: mdi:power-off
  - type: mode
    name: 制冷
    value: cool
    icon: mdi:snowflake
  - type: mode
    name: 制热
    value: heat
    icon: mdi:weather-sunny
  - type: mode
    name: 除湿
    value: dry
    icon: mdi:water
  - type: mode
    name: 送风
    value: fan_only
    icon: mdi:fan
  - type: mode
    name: 自动
    value: auto
    icon: mdi:autorenew
```

> 💡 **图标速查表（空调模式推荐 mdi 图标）：**
>
> | 模式 | value | 推荐图标 | 备选图标 |
> |------|-------|---------|---------|
> | 关闭 | `off` | `mdi:power-off` | `mdi:air-conditioner` |
> | 制冷 | `cool` | `mdi:snowflake` | `mdi:snowflake-variant` |
> | 制热 | `heat` | `mdi:weather-sunny` | `mdi:fire` / `mdi:radiator` |
> | 除湿 | `dry` | `mdi:water` | `mdi:water-percent` / `mdi:drop` |
> | 送风 | `fan_only` | `mdi:fan` | `mdi:fan-spin` / `mdi:wind` |
> | 自动 | `auto` | `mdi:autorenew` | `mdi:cached` / `mdi:shuffle` |


> 💡 **类型可混用**：同一组 `mode_buttons` 可同时包含 `toggle` 和 `mode` 类型。

**mode_buttons 子项字段：**

| 字段 | toggle 类型 | mode 类型 | 说明 |
|------|:----------:|:--------:|------|
| `type` | ✅ `toggle` | ✅ `mode` | 按钮类型 |
| `switch_entity` | ✅ | ❌ | 外部控制实体 ID（select/switch/input_select/light 等） |
| `value` / `mode` | ❌ | ✅ | climate `hvac_mode` 值（缺省时回退到 `name`） |
| `name` | ❌ | ❌ | 按钮显示文本（不配置 `icon` 时使用） |
| `switch_name` | ❌ | ❌ | 显示文本别名（优先级高于 `name`） |
| `icon` | ❌ | ❌ | 图标（`mdi:` 开头），配置后优先显示图标 |
| `animation` | ❌ | ❌ | 激活态动画：`rotate`（旋转）/ `breathe`（呼吸）。仅当前模式按钮播放 |
| `toggle_attribute` | ❌ | ❌ | 判断激活态的属性名（select 用 `current_option`） |
| `toggle_value` | ❌ | ❌ | 属性值等于此值时按钮高亮 |
| `service` | ❌ | ❌ | 自定义 climate 服务（高级用法） |
| `data` | ❌ | ❌ | 自定义服务数据（高级用法，JSON 对象） |

---

#### 6.3.2 自定义风速按钮 (fan_buttons)

**默认行为：** 不配置 `fan_buttons` 时，从 climate 实体的 `fan_modes` 属性自动生成风速按钮，文本走内置映射表（`auto`→`A`、`low`→`低`、`high`→`强` 等）。

**自定义场景：** 不同品牌空调的风速值差异较大，部分通过 `select.*` 实体而非 `fan_mode` 属性控制。配置 `fan_buttons` 后可完全自定义按钮列表，支持两种类型：

**类型 1：`toggle` —— 通过外部实体控制风速**（适配小米等非标空调）

```yaml
fan_buttons:
  - type: toggle
    switch_entity: select.xiaomi_ac_fan_level          # select 或 switch 实体
    switch_name: 静音                                   # 按钮显示文本（不配置 icon 时使用）
    icon: mdi:volume-low                                # 可选，配置后优先显示图标
    toggle_attribute: current_option                   # select 实体使用 current_option
    toggle_value: mute                                  # 当前选项等于此值时按钮高亮
  - type: toggle
    switch_entity: select.xiaomi_ac_fan_level
    switch_name: 中
    toggle_attribute: current_option
    toggle_value: medium
```

**类型 2：`fan` —— 映射到 `climate.set_fan_mode`**（用于自定义文本/顺序/子集）

```yaml
fan_buttons:
  - type: fan
    name: 自动风                                        # 按钮显示文本
    value: auto                                         # 对应 climate fan_mode 值
    icon: mdi:fan-auto                                  # 可选
  - type: fan
    name: 强劲
    value: high
    icon: mdi:fan-speed-3
```

> 💡 **类型可混用**：同一组 `fan_buttons` 可同时包含 `toggle` 和 `fan` 类型，分别处理非标和标准风速控制。

**fan_buttons 子项字段：**

| 字段 | toggle 类型 | fan 类型 | 说明 |
|------|:----------:|:--------:|------|
| `type` | ✅ `toggle` | ✅ `fan` | 按钮类型 |
| `switch_entity` | ✅ | ❌ | 外部控制实体 ID（select/switch/input_select/light 等） |
| `value` / `fan_mode` | ❌ | ✅ | climate `fan_mode` 值（缺省时回退到 `name`） |
| `name` | ❌ | ❌ | 按钮显示文本（不配置 `icon` 时使用） |
| `switch_name` | ❌ | ❌ | 显示文本别名（优先级高于 `name`） |
| `icon` | ❌ | ❌ | 图标（`mdi:` 开头），配置后优先显示图标 |
| `animation` | ❌ | ❌ | 激活态动画：`rotate`（旋转）/ `breathe`（呼吸）。仅当前模式按钮播放 |
| `toggle_attribute` | ❌ | ❌ | 判断激活态的属性名（select 用 `current_option`） |
| `toggle_value` | ❌ | ❌ | 属性值等于此值时按钮高亮 |
| `service` | ❌ | ❌ | 自定义 climate 服务（高级用法） |
| `data` | ❌ | ❌ | 自定义服务数据（高级用法，JSON 对象） |

---

#### 6.3.3 自定义摆风按钮 (swing_buttons)

**默认行为：** 不配置 `swing_buttons` 时，自动从 climate 实体属性生成摆风按钮：

- **垂直摆风**（`swing_modes`）：符号统一用 `↑` + CSS 旋转角度表达导风板位置，`swing_*`（摆动档）会自动注上 "摆动" 角标。`off` → `⊘`，`full` → `⇆`。
- **水平摆风**（`swing_horizontal_modes`）：当实体同时有 `swing_horizontal_modes` 属性时，自动展开为双行布局（垂直 + 水平，各行自带"垂直""水平"标签）。符号同样用 `↑` + 旋转角度（不同角度区间）。`off` → `⊘`，`full` → `⇆`。

符号与角度完全按 `swing_modes` / `swing_horizontal_modes` 的值从内置映射表自动匹配，无需手动配置。

**自定义场景：** 部分空调的摆风角度通过 `select.*` 实体控制（如小米天幕风/地毯风等定点摆风），无法通过 `swing_mode` 表达。配置 `swing_buttons` 后会**追加**到默认按钮之后。

```yaml
swing_buttons:
  - type: toggle
    switch_entity: select.xiaomi_ac_vertical_angle
    switch_name: ⥔                                      # 天幕风（上定格）
    toggle_attribute: current_option
    toggle_value: 上定格（天幕风）
  - type: toggle
    switch_entity: select.xiaomi_ac_vertical_angle
    switch_name: ↑
    toggle_attribute: current_option
    toggle_value: 偏上定格-定向1
  - type: toggle
    switch_entity: select.xiaomi_ac_vertical_angle
    switch_name: ⥙                                      # 地毯风（下定格）
    toggle_attribute: current_option
    toggle_value: 下定格（地毯风）
    icon: mdi:arrow-down-bold                           # 可选
```

> 💡 **追加模式：** `swing_buttons` 会追加到默认 `swing_modes` 按钮之后，不会替换。如果你希望完全自定义（隐藏默认摆风按钮），可在 climate 实体上清空 `swing_modes` 属性，或忽略此提示直接全部用自定义按钮。

**swing_buttons 子项字段：** 与 `fan_buttons` 的 `toggle` 类型完全一致，`type` 支持 `toggle`（外部实体）和 `fan`（映射到 `climate.set_swing_mode`）。

---

##### 6.3.3.1 水平摆风双行布局

当气候实体的属性中同时存在 `swing_modes` 和 `swing_horizontal_modes` 时，摆风区域自动切换为**双行布局**：

- **垂直行**（上）：显示 `swing_modes` 中的档位，"垂直"标签
- **水平行**（下）：显示 `swing_horizontal_modes` 中的档位，"水平"标签
- 原来单行时的"摆风："标签自动隐藏（各行已有自己的轴标签）

双行布局**无需任何额外配置**，系统自动检测实体的 `swing_horizontal_modes` 属性并渲染。

```yaml
# 示例实体属性（自动检测，无需配置）
# swing_modes: off, full, fixed_upper, fixed_upper_middle, ...
# swing_horizontal_modes: off, full, left, left_center, center, right_center, right
```

---

##### 6.3.3.2 下拉模式 (swing_select / swing_select_labels)

当摆风档位较多时，可以将按钮切换为下拉选择器（`<select>`），下拉框占用 3 个按钮位置。

**swing_select 的取值：**

| 值 | 行为 |
|---|---|
| 不配置 | 全部使用按钮（默认） |
| `true` | 两行都使用下拉 |
| `vertical` | 仅垂直行使用下拉 |
| `horizontal` | 仅水平行使用下拉 |
| `both` | 两行都使用下拉（等同 `true`） |

**自定义下拉选项名称 (swing_select_labels)：**

```yaml
swing_select: both

swing_select_labels:
  vertical:
    off: "关"
    full: "上下扫风"
    fixed_upper: "最上"
    fixed_upper_middle: "偏上"
    fixed_middle: "中间"
    fixed_lower_middle: "偏下"
    fixed_lower: "最下"
  horizontal:
    off: "关"
    full: "左右扫风"
    left: "最左"
    center: "居中"
    right: "最右"
```

> 💡 下拉模式下 `<option>` 不支持 CSS transform 旋转，显示的是内置符号文本（↑ → ↓ ◀ ▶ 等）。

---

##### 6.3.3.3 隐藏指定摆风档位 (hide)

隐藏不需要的摆风档位或整行水平摆风。

```yaml
# 隐藏水平摆风整行（摆风区域退回单行布局，仅显示垂直摆风）
hide: swing_horizontal_modes

# 隐藏多个特定档位（逗号分隔字符串或数组均可）
hide: swing_upper, swing_upper_middle, swing_middle, swing_lower_middle, swing_lower

# 同时隐藏整行 + 特定档位
hide:
  - swing_horizontal_modes
  - fixed_lower
```

---

##### 6.3.3.4 摆风符号映射表

垂直和水平摆风统一使用 `↑` 符号 + CSS 旋转角度，从同一个中心映射表取值。

**垂直摆风（swing_modes）：**

| 模式值 | 符号 | 旋转角度 | 视觉 |
|---|---|---|---|
| `off` | `⊘` | — | 关闭 |
| `full` | `⇆` | — | 全范围扫风 |
| `fixed_upper` / `top` | `↑` | 30° | 偏上 |
| `fixed_upper_middle` | `↑` | 60° | 更偏上 |
| `fixed_middle` / `middle` | `↑` | 90° | → 水平（中间） |
| `fixed_lower_middle` | `↑` | 120° | 偏下 |
| `fixed_lower` / `bottom` | `↑` | 150° | 更偏下 |
| `swing_upper` | `↑`（摆动角标） | 30° | 上区摆动 |
| `swing_upper_middle` | `↑`（摆动角标） | 60° | 偏上区摆动 |
| `swing_middle` | `↑`（摆动角标） | 90° | 中区摆动 |
| `swing_lower_middle` | `↑`（摆动角标） | 120° | 偏下区摆动 |
| `swing_lower` | `↑`（摆动角标） | 150° | 下区摆动 |

> `fixed_*` 表示**定格**（导风板固定在一个角度），`swing_*` 表示**摆动**（导风板在该区间内来回扫风）。

**水平摆风（swing_horizontal_modes）：**

| 模式值 | 符号 | 旋转角度 | 视觉 |
|---|---|---|---|
| `off` | `⊘` | — | 关闭 |
| `full` | `⇆` | — | 全范围左右扫风 |
| `left` | `↑` | 240° | 指向左 |
| `left_center` | `↑` | 210° | 偏左 |
| `center` | `↑` | 180° | ↓ 居中 |
| `right_center` | `↑` | 150° | 偏右 |
| `right` | `↑` | 120° | 指向右 |

**兼容旧协议（非标空调）：**

| 模式值 | 符号 | 旋转角度 | 说明 |
|---|---|---|---|
| `MIDDLE1` | `↑` | 30° | 部分空调的中间档位1 |
| `MIDDLE2` | `↑` | 60° | 部分空调的中间档位2 |
| `MIDDLE3` | `↑` | 90° | 部分空调的中间档位3 |
| `SWING` | `⇆` | — | 通用摆动 |
| `AUTO` | `A` | — | 自动 |

---

#### 6.3.4 功能按钮 (features)

**用途：** 在空调面板底部显示附加功能开关（睡眠/辅热/干燥/节能/声音等），支持 `switch.*` 标准实体和 `select.*` 选项实体。

```yaml
features:
  - type: toggle
    switch_entity: switch.xiaomi_ac_sleep_mode
    switch_name: 睡眠
    icon: mdi:power-sleep
  - type: toggle
    switch_entity: switch.xiaomi_ac_heater
    switch_name: 辅热
    icon: mdi:fire
  - type: toggle
    switch_entity: switch.xiaomi_ac_eco
    switch_name: 节能
    icon: mdi:sprout
  - type: toggle
    switch_entity: select.xiaomi_ac_sound_mode          # select 实体也支持
    switch_name: 声音
    icon: mdi:music-circle
    toggle_attribute: current_option
    toggle_value: 'on'
```

**features 子项字段：** 与 `fan_buttons` 的 `toggle` 类型完全一致。

---

#### 6.3.5 完整配置示例（四种自定义按钮联合使用）

```yaml
- type: ac
  entity: climate.ceshi
  name: 虚拟空调
  humidity_entity: sensor.keting_shidu
  power_entity: sensor.ke_ting_kong_diao_nian_yong_dian_liang
  power_display_entity: sensor.esp_meter_power
  popup_position: clone_button_down
  width: 400px

  # 自定义模式（映射到 climate.set_hvac_mode，带动画）
  mode_buttons:
    - type: mode
      name: 关闭
      value: 'off'
      icon: mdi:power-off
    - type: mode
      name: 制冷
      value: cool
      icon: mdi:snowflake
      animation: rotate
    - type: mode
      name: 自动
      value: auto
      icon: mdi:autorenew
      animation: rotate

  # 自定义风速（通过 select 实体控制）
  fan_buttons:
    - type: toggle
      switch_entity: select.xiaomi_ac_fan_level
      switch_name: 静
      toggle_attribute: current_option
      toggle_value: mute
    - type: toggle
      switch_entity: select.xiaomi_ac_fan_level
      switch_name: 中
      toggle_attribute: current_option
      toggle_value: medium
    - type: fan                                      # 标准风速映射，可混用
      name: 自动
      value: auto

  # 自定义摆风（追加到默认 swing_modes 之后）
  swing_buttons:
    - type: toggle
      switch_entity: select.xiaomi_ac_vertical_angle
      switch_name: ⥔
      toggle_attribute: current_option
      toggle_value: 上定格（天幕风）
    - type: toggle
      switch_entity: select.xiaomi_ac_vertical_angle
      switch_name: ⥙
      toggle_attribute: current_option
      toggle_value: 下定格（地毯风）

  # 功能按钮
  features:
    - type: toggle
      switch_entity: switch.xiaomi_ac_sleep_mode
      switch_name: 睡眠
      icon: mdi:power-sleep
    - type: toggle
      switch_entity: switch.xiaomi_ac_heater
      switch_name: 辅热
      icon: mdi:fire
    - type: toggle
      switch_entity: switch.xiaomi_ac_eco
      switch_name: 节能
      icon: mdi:sprout
```

> 💡 **icon 与 name 优先级：** 四类自定义按钮（`mode_buttons`/`fan_buttons`/`swing_buttons`/`features`）均遵循统一规则——配置 `icon`（`mdi:` 开头）时优先显示图标，未配置则显示 `name` 或 `switch_name` 文本。

### 6.4 插座/开关 (type: socket)

控制插座或开关型设备（如智能插座、墙壁开关等）。

```yaml
  - type: socket
    icon: mdi:power-socket-au
    card:
      - entity: switch.living_room_plug      # 插座实体ID
        name: 客厅插座
      - entity: switch.tv_plug
        name: 电视插座
        room: 客厅
        global_exception: true   # 全关/全开/取反时跳过此实体
    show_badge: true
    per_line: 2
    shwo_sankey: false                       # 是否显示功率流向桑基图（需ECharts）
```

### 6.5 耗材/电池 (type: consumables)

显示电池电量、滤芯寿命等耗材的剩余量。当低于设定阈值时自动告警。

```yaml
  - type: consumables
    icon: mdi:battery
    card:
      - entity: sensor.door_lock_battery
        name: 门锁电池
        group: 门锁
      - entity: sensor.temp_sensor_battery
        name: 温湿度计
        group: 传感器
    tabs:                                     # 也可用选项卡模式分组
      - name: 门锁
        rows:
          - row: 1
            items:
              - entity: sensor.door_lock_battery
                name: 门锁电池
```

电池图标会根据剩余量自动变化（满电→绿色，低电→红色），同时按钮上显示最低剩余量数字。

### 6.6 媒体播放器 (type: media)

媒体播放器控制中心。支持播放控制、后台播放、播放列表管理（通过 API 接口获取，依赖 HA 数据统一存储系统）、多页面选项卡（`tabs` 自由布局）。

```yaml
  - type: media
    name: 播放器                          # 显示名称
    entity: media_player.xxx               # 媒体设备实体（必填，向后兼容 media_entity）
    icon: mdi:music
    conversation_entity: sensor.xxx_conversation  # 对话记录传感器（可选，对话时显示对话图标）
    width: 440px                          # 弹窗宽度（可选，如 430px / 90%）
    popup_position: clone_button_down      # 弹窗位置
    cover_animation: true                 # 封面 CD 旋转动画（默认 true）
    api_base_url: xxxxxxxxxx              # API 地址（可选，默认使用顶层 api_base_url）
    key: xxxxxxxxxxxx                     # API 密钥（可选，默认使用顶层 key）
    user: 小屁孩,妈妈,爸爸                # 播放列表按用户分组（可选，逗号分隔或数组）
    default_page: 控制中心                # 默认显示的页面（可选，值为 tab.name，不配则默认"本地播放"）
    player_page_label: 本地播放           # "本地播放"页标签文案（可选，默认"本地播放"）

    # ── 顶层页面选项卡（可选，每个 tab 是一个独立页面，内部用自由布局组织内容）──
    tabs:
      - name: 控制中心                    # 选项卡名称（同时作为 default_page 的匹配值）
        icon: mdi:toggle-switch-variant   # 选项卡图标（可选）
        rows:                             # 自由布局行配置（与原 free_layout 同结构）
          - row: 1
            per_line: 2
            title: 控制中心
            show_title: false
            items:
              - type: sensor
                entity: sensor.xxx_conversation
                name: 语音控制记录
                show_conversation: true
              - type: switch
                entity: switch.xxx_mute
                name: MIC静音
      - name: 云音乐
        icon: mdi:music-box-multiple
        rows:
          - row: 1
            per_line: 1
            items:
              - type: url                 # URL 嵌入卡片（替代原 xiaomusic_url 顶层字段）
                xiaomusic_url: http://192.168.1.12:58090/static/default/index.html
```

**页面模型：**

弹窗顶部为 pill 风格的页面切换栏，基于 `tabs` 动态生成：

- **第 0 项固定为"本地播放"页**（内置播放器：封面/进度/播放列表，不可在 `tabs` 中配置）
- **后续为 `tabs` 中配置的自定义页面**，每个页面用 `rows` 自由布局组织内容
- 页面切换通过点击顶部 pill 完成，切换有 80ms 淡入淡出过渡

**配置项：**

| 字段 | 必填 | 类型 | 默认值 | 说明 |
|------|------|------|--------|------|
| `tabs` | ❌ | `array` | `[]` | 顶层页面选项卡数组，每项含 `name`/`icon`/`rows` |
| `default_page` | ❌ | `string` | `本地播放` | 默认显示的页面，值为 tab 的 `name`，匹配不到时回退到"本地播放" |
| `player_page_label` | ❌ | `string` | `本地播放` | "本地播放"页的标签文案 |
| `user` | ❌ | `string\|array` | — | 播放列表按用户分组，逗号分隔字符串或数组 |

**tabs 每项结构：**

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| `name` | ✅ | `string` | 选项卡名称（同时作为 `default_page` 的匹配值） |
| `icon` | ❌ | `string` | 选项卡图标，默认 `mdi:view-dashboard-outline` |
| `rows` | ❌ | `array` | 自由布局行配置（`row`/`per_line`/`title`/`show_title`/`items`） |

**功能说明：**

| 功能 | 说明 |
|------|------|
| 播放控制 | 封面/歌名/歌手展示、进度条、播放/暂停、上一曲/下一曲、音量调节 |
| 后台播放 | 支持后台播放模式，通过 API 接口获取播放列表和状态 |
| 播放列表管理 | 播放列表通过 HA 数据统一存储系统 API 接口获取，支持多用户分 Tab、多列表展开/收起 |
| 媒体库浏览 | 点击「从媒体库添加」浏览 HA 媒体源，选歌添加到当前播放列表 |
| 文件夹批量 | 媒体库中点击文件夹 `[+ 全部]`，选择目标列表或新建列表后添加全部音乐 |
| 播放全部 | 每个播放列表头部有「播放全部」按钮 |
| 多页面选项卡 | 配置 `tabs` 后顶部出现多个页面 pill，可自由布置传感器/开关/按钮/URL 等任意卡片 |
| 默认页面 | 通过 `default_page` 指定打开弹窗时默认显示的页面 |
| 删除列表 | 播放列表头部 `🗑` 按钮删除整个列表 |
| 删除单曲 | 展开列表后每曲右侧 `✕` 按钮删除 |

**交互方式：**

- 顶部 pill 切换页面（"本地播放" + 各自定义页），pill 溢出时可横向滚动
- "本地播放"页内部按 `user` 配置生成用户切换 Tab（小屁孩/妈妈/爸爸），用于切换不同用户的播放列表
- 播放列表默认折叠，点击头部展开/收起
- 点击「从媒体库添加」打开 HA 媒体库浏览器，支持目录树导航、单曲添加、文件夹批量添加
- Tab / 播放列表切换后状态保持（`activeTabIndex`/`activePlaylistIndex` 持久化，`activePageIndex` 不持久化——每次打开按 `default_page` 决定）

**URL 嵌入卡片（type: url）：**

在 `tabs[].rows[].items` 中使用 `type: url` 用 iframe 嵌入外部网页（替代原 `xiaomusic_url` 顶层字段）：

| 字段 | 必填 | 类型 | 默认值 | 说明 |
|------|------|------|--------|------|
| `url` | ❌ | `string` | — | 嵌入的 URL（与 `xiaomusic_url` 互为别名） |
| `xiaomusic_url` | ❌ | `string` | — | `url` 的别名，向后兼容 |
| `height` | ❌ | `string` | `800px` | iframe 高度 |
| `sandbox` | ❌ | `string` | `allow-scripts allow-same-origin allow-forms allow-popups` | iframe sandbox 属性 |
| `allowfullscreen` | ❌ | `bool` | `true` | 是否允许全屏 |

**动态图标自动启用（图标 + 颜色 + 动画随播放状态联动）：**

当 `type: media` 按钮未配置 `on_icon` / `off_icon` / `on_color` / `off_color` 时，自动套用 `media_player` 动态图标预设，图标、颜色、动画随实体状态实时变化，同时右上角斜三角自动显示状态文字（`icon_text: preset_media`）。播放控制弹窗等全部专属能力不受影响。

| state | 图标 | 颜色 | 动画 | 角标文字 |
|-------|------|------|------|---------|
| `playing` | `mdi:speaker-play` | 绿 `#4caf50` | breathe | 放 |
| `paused` | `mdi:speaker-pause` | 青 `#26c6da` | — | 停 |
| `idle` | `mdi:speaker-stop` | 浅蓝灰 `#90a4ae` | — | 闲 |
| `standby` | `mdi:speaker` | 深灰 `#607d8b` | — | 候 |
| `on` | `mdi:speaker` | 蓝 `#42a5f5` | breathe | 开 |
| `off` | `mdi:speaker-off` | 灰 `#7f8c8d` | — | 关 |

**对话状态检测（conversation_entity）：**

配置 `conversation_entity` 后，当该实体值变化时表示正在对话，动态图标临时切换为对话图标，对话结束后恢复媒体状态图标。适用于小爱音箱等带语音对话记录传感器的设备。

| 属性 | 说明 |
|------|------|
| 图标 | `mdi:speaker-message` |
| 颜色 | 紫 `#9c27b0` |
| 动画 | breathe |
| 持续时间 | 值停止变化后 3 秒恢复 |

**工作原理（防抖模式）：**
- `conversation_entity` 值变化 → 立即显示对话图标，重置 3 秒计时器
- 值持续变化（长时间对话）→ 计时器不断重置，对话图标持续显示
- 值停止变化 3 秒后 → 计时器到期，恢复 `entity` / `media_entity` 状态对应的媒体图标

```yaml
  - type: media
    name: 播放器
    entity: media_player.xiaomi_oh2p_dac5_play_control
    conversation_entity: sensor.xiaomi_oh2p_dac5_conversation   # 对话记录传感器
    # ... 其他配置
```

> - 首次加载只缓存值不触发，避免页面打开就显示对话图标
> - `conversation_entity` 已自动纳入实体订阅，状态变化即可触发图标更新
> - `conversation_entity` 与 `tabs` 中展示同一实体互不冲突（一个用于图标判断，一个用于内容展示）
> - 仅在动态图标模式（未配 `on_icon`/`off_icon`）下生效

> - 也可显式配置 `preset: media_player` 覆盖默认预设，或配置 `on_icon` / `off_icon` 回退到手动二态模式
> - 若需自定义角标文字，配置 `icon_text` 即可覆盖自动的 `preset_media`
> - 实体配置项推荐使用 `entity`，旧配置的 `media_entity` 仍完全兼容（两者任一存在即生效，`entity` 优先）

> 💡 **依赖说明**：播放列表管理功能依赖 [HA 数据统一存储系统](https://github.com/chjspp520/ha_data_store/releases)，需先在 HA 中安装并配置好 API 地址和密钥。

#### 6.6.1 语音对话记录气泡（show_conversation）

在 `free_layout` 的任意 `items` 卡片上配置 `show_conversation: true`，点击该卡片即可弹出**仿微信聊天界面**的语音对话历史气泡。数据通过顶层 `api_base_url` 和 `key` 调用 `type=xiaoai_history` 接口获取，对话时间使用返回数据的 `conv_time` 字段。

**配置项：**

| 字段 | 必填 | 类型 | 默认值 | 说明 |
|---|---|---|---|---|
| `show_conversation` | ✅ | `bool` | — | 开启对话气泡功能 |
| `entity` | ✅ | `string` | — | 对话记录实体 ID（如 `sensor.xxx_conversation`），作为 API 的 `entity_id` 参数 |
| `command_entity` | ❌ | `string` | — | 指令下发实体 ID（如 `text.xxx_execute_text_directive`），配置后在气泡底部显示输入框，可手动输入指令通过 `text.set_value` 发送给小爱 |
| `quick_input` | ❌ | `string[]` | — | 快捷指令列表。仅在配置了 `command_entity` 时生效，在发送按钮右侧显示快捷输入按钮（⚡），点击弹出列表，选定某项直接发送该指令 |
| `conversation_page_days` | ❌ | `number` | `7` | 每次分页加载的天数 |
| `conversation_max_height` | ❌ | `string` | `60vh` | 气泡最大高度，超出滚动 |
| `conversation_width` | ❌ | `string\|number` | `90%` | 气泡宽度（数字按 px，字符串原样使用），最大不超过 500px |

**配置示例：**

```yaml
buttons:
  - type: media
    name: 播放器
    entity: media_player.xxx
    api_base_url: /api/ha_data_store/
    key: your_api_key
    free_layout:
      - row: 1
        per_line: 1
        title: 语音控制记录
        items:
          - entity: sensor.xxx_conversation
            type: sensor
            name: 语音控制记录
            icon: mdi:account-voice
            show_conversation: true          # 必填，开启聊天气泡功能
            command_entity: text.xxx_execute_text_directive  # 可选，开启底部指令输入框
            quick_input:                     # 可选，快捷指令列表（需配合 command_entity）
              - 关闭客厅大灯
              - 关闭餐厅吊灯和壁灯
              - 打开客厅大灯
            conversation_page_days: 7        # 可选，每次加载天数，默认 7
            conversation_max_height: 60vh    # 可选，气泡最大高度，默认 60vh
            conversation_width: 90%          # 可选，气泡宽度，默认 90%
```

**功能说明：**

- **加载方向**：最新对话显示在底部（iMessage/微信标准），向上滚动自动加载更早 7 天的数据
- **数据排序**：按 `conv_time` 正序排列（最旧在顶，最新在底）
- **时间分隔**：相邻两条对话间隔超过 5 分钟或日期不同时插入时间分隔线，今天显示 `HH:MM`，昨天显示 `昨天 HH:MM`，更早显示 `MM-DD HH:MM`
- **用户头像**：自动匹配当前登录 HA 用户（`hass.user.id` ↔ `person.*` 实体的 `user_id`），使用其 `entity_picture` 作为右侧"我"的头像，匹配不到时降级为 `mdi:account` 图标
- **AI 头像**：使用 `mdi:robot` 图标
- **指令下发**：配置 `command_entity` 后，气泡底部显示输入框，回车或点击发送按钮通过 `text.set_value` 服务将指令写入 `command_entity`；发送后乐观插入本地消息并延迟 3 秒刷新对话列表拉取真实回复
- **快捷输入**：配置 `quick_input` 数组（需配合 `command_entity`）后，发送按钮右侧出现 ⚡ 快捷输入按钮，点击弹出快捷指令列表，选定某项直接发送该指令
- **触发范围**：`show_conversation` 可配置在任意 `type` 的 item 上（`sensor`/`text`/`switch`/`button` 等），配置后会**覆盖**该卡片原有的点击行为（`stopPropagation`）
- **API 接口**：`GET {api_base_url}query?type=xiaoai_history&key={key}&entity_id={entity}&start={YYYY-MM-DD}&end={YYYY-MM-DD}`，返回 JSON 中 `data.rows` 数组含 `user_text`（用户语句）、`ai_text`（AI 回复）、`conv_time`（对话时间）等字段
- **错误处理**：首次加载失败显示"加载失败 + 重试按钮"；加载更多失败仅显示临时"加载失败"提示行，不影响已有内容；无更早数据时显示"没有更早的对话了"

> ⚠️ **覆盖原生点击**：在 `switch`/`button` 等有原生动作（toggle/调用服务）的卡片上配置 `show_conversation: true` 后，原生点击动作会被覆盖。如需保留原动作，请使用独立的 `sensor`/`text` 类型卡片承载对话功能。

#### 6.6.2 小爱对话记录卡片 (type: xiaoai_conversation)

`xiaoai_conversation` 是独立的对话记录卡片类型，直接渲染仿微信聊天界面，展示语音对话历史。与 6.6.1 的 `show_conversation` 气泡不同，它**不需要点击触发**，本身即是对话界面，可作为卡片直接放入网格 / free_layout items，也可通过通用 `tap_action.action: popup_card` 作为弹窗弹出。

**两种使用方式：**

- **直接渲染**：作为 `type: xiaoai_conversation` 卡片放入 `items`，直接显示完整聊天界面
- **作为弹窗**：在任意按钮上配置 `tap_action.action: popup_card`，`card` 内填写 `type: xiaoai_conversation`，点击按钮弹出聊天界面（复用通用弹窗系统，支持 `popup_position` / `width`）

**配置项：**

| 字段 | 必填 | 类型 | 默认值 | 说明 |
|---|---|---|---|---|
| `type` | ✅ | `string` | — | 固定 `xiaoai_conversation` |
| `entity` | ⚠️ | `string` | — | 对话记录实体 ID。**单对话模式必填**；多对话模式下填在 `multiple_conversations` 子项中 |
| `command_entity` | ❌ | `string` | — | 命令下发实体 ID，单对话模式使用；多对话模式下填在子项中 |
| `play_text_entity` | ❌ | `string` | — | 播报实体 ID，单对话模式使用；多对话模式下填在子项中 |
| `quick_input` | ❌ | `string[]` | — | 快捷指令列表。**多对话模式下作为共用快捷输入**，与各子项的专属快捷输入合并显示（专属在前，共用在后） |
| `multiple_conversations` | ❌ | `object[]` | — | **多对话模式**：配置多组对话的数组。启用后**顶层 `entity` / `command_entity` / `play_text_entity` 将被忽略**（设了会报 warning）。每个子项字段见下表 |
| `conversation_page_days` | ❌ | `number` | `7` | 每次分页加载的天数。多对话模式下各子项可单独覆盖 |
| `conversation_max_height` | ❌ | `string\|number` | — | 聊天内容区高度（如 `500px`），超出时列表内部滚动；不配置时由内容撑开 |
| `conversation_width` | ❌ | `string\|number` | — | 卡片宽度（数字按 px，字符串原样使用如 `90%`/`400px`）；弹窗模式下建议 `100%` 自适应弹窗宽度 |
| `name` | ❌ | `string` | `语音对话记录` | 标题栏显示的名称（多对话模式下自动显示为"与 {活跃名称} 聊天"） |
| `icon` | ❌ | `string` | `mdi:account-voice` | 标题栏图标（仅元数据，卡片本身不显示图标） |

**`multiple_conversations` 子项字段：**

| 字段 | 必填 | 类型 | 默认值 | 说明 |
|---|---|---|---|---|
| `name` | ✅ | `string` | — | 对话名称，显示在 tab 按钮上，标题栏显示"与 {name} 聊天" |
| `entity` | ✅ | `string` | — | 对话记录实体 ID，作为 API 的 `entity_id` 参数 |
| `icon` | ❌ | `string` | `mdi:account-voice` | 对话图标，显示在 tab 按钮和标题栏 |
| `command_entity` | ❌ | `string` | — | 命令下发实体 ID，配置后该对话 tab 才显示发送按钮 |
| `play_text_entity` | ❌ | `string` | — | 播报实体 ID，配置后该对话 tab 才显示播报按钮 |
| `quick_input` | ❌ | `string[]` | — | 该对话的**专属快捷输入**。与顶层 `quick_input`（共用）合并显示，专属在前、共用在后 |
| `conversation_page_days` | ❌ | `number` | 继承顶层值 | 该对话的分页加载天数，不配置则使用顶层 `conversation_page_days` |

> 📌 **command_entity vs play_text_entity**：两者均为 text 实体，通过 `text.set_value` 写入。`command_entity` 让小爱执行指令（产生对话记录，发送后乐观插入消息并延迟刷新）；`play_text_entity` 让小爱 TTS 朗读（不产生对话记录，仅 Toast 提示"已播报"）。两者可同时配置，输入区会显示两个独立按钮，共享同一输入框。

> 📌 **多对话模式行为**：输入区在任一子项配置了 `command_entity` 或 `play_text_entity` 时即显示。切换 tab 时输入区的按钮、placeholder 和快捷输入列表会自动切换到当前活跃对话的配置。数据按 tab 独立缓存和分页加载。

**方式一：直接渲染（放入 free_layout items）**

```yaml
buttons:
  - type: media
    name: 播放器
    entity: media_player.xxx
    api_base_url: /api/ha_data_store/
    key: your_api_key
    tabs:
      - name: 音响
        icon: mdi:toggle-switch-variant
        rows:
          - row: 1
            per_line: 1
            title: 控制中心
            items:
              - type: xiaoai_conversation
                name: 语音控制记录
                entity: sensor.xxx_conversation
                command_entity: text.xxx_execute_text_directive   # 可选，命令发送
                play_text_entity: text.xxx_play_text               # 可选，TTS 播报
                icon: mdi:account-voice
                conversation_page_days: 7
                conversation_max_height: 400px                     # 可选，列表高度，超出滚动
                conversation_width: 400px                          # 可选，卡片宽度
                quick_input:                                       # 可选，快捷指令（需配合 command_entity）
                  - 关闭客厅大灯
                  - 关闭餐厅吊灯和壁灯
                  - 打开客厅大灯
```

**方式二：作为弹窗（tap_action.action: popup_card）**

在任意按钮上配置 `tap_action`，点击后用通用弹窗弹出对话界面：

```yaml
buttons:
  - name: 语音控制记录
    icon: mdi:account-voice
    tap_action:
      action: popup_card
      popup_position: top          # 可选，弹窗位置：top/bottom/center 等
      width: 400px                 # 可选，弹窗宽度
      card:                        # 单个对象（非数组）
        type: xiaoai_conversation
        name: 语音控制记录
        entity: sensor.xxx_conversation
        command_entity: text.xxx_execute_text_directive
        play_text_entity: text.xxx_play_text
        conversation_page_days: 7
        conversation_max_height: 500px
        conversation_width: 100%   # 弹窗模式下建议 100%，自适应弹窗宽度
        quick_input:
          - 关闭客厅大灯
          - 关闭餐厅吊灯和壁灯
          - 打开客厅大灯
    api_base_url: /api/ha_data_store/   # 顶层配置 API 地址
    key: your_api_key
```

> ⚠️ **popup_card 的 card 是单个对象**：`tap_action.card` 应为单个 cardConfig 对象（非数组），因为弹窗内部调用 `createCardElement(cardConfig)` 创建单张卡片。

**方式三：多对话模式（multiple_conversations）**

适用于家里有多台小爱音箱的场景，一个卡片同时管理多台设备的对话记录，标题栏显示 tab 按钮可切换：

```yaml
buttons:
  - type: media
    name: 智能管家
    entity: media_player.xxx
    api_base_url: /api/ha_data_store/
    key: your_api_key
    tabs:
      - name: 语音控制
        icon: mdi:account-voice
        rows:
          - row: 1
            per_line: 1
            title: 小爱对话记录
            items:
              - type: xiaoai_conversation
                name: 小爱对话
                conversation_page_days: 7
                conversation_max_height: 500px
                conversation_width: 100%
                # 多对话配置——配置后忽略顶层的 entity / command_entity / play_text_entity
                multiple_conversations:
                  - name: 客厅小爱
                    icon: mdi:account-voice
                    entity: sensor.xiaomi_living_room_conversation
                    command_entity: text.xiaomi_living_room_cmd
                    play_text_entity: text.xiaomi_living_room_tts
                    quick_input:                     # 专属快捷输入（显示在共用前面）
                      - 关闭客厅大灯
                      - 打开客厅大灯
                  - name: 2楼小爱
                    icon: mdi:account-voice
                    entity: sensor.xiaomi_2f_conversation
                    command_entity: text.xiaomi_2f_cmd
                    play_text_entity: text.xiaomi_2f_tts
                # 共用快捷输入（专属在前，共用在后合并）
                quick_input:
                  - 关闭所有灯
                  - 离家模式
```

**功能说明：**

- **直接渲染**：卡片本身即聊天界面，不设 `conversation_max_height` 时由内容撑开（无滚动）；设了则在指定高度内列表滚动
- **弹窗模式**：由通用 `popup_card` 动作系统用 `showPopup` 包裹，`popup_position` 控制弹窗位置，`width` 控制弹窗宽度；建议卡片 `conversation_width: 100%` 自适应弹窗
- **输入区**：配置了 `command_entity` 或 `play_text_entity` 任意一个即显示输入区
  - 蓝色发送按钮（`mdi:send`）：发送命令到 `command_entity`，乐观插入本地消息 + 延迟 3 秒刷新列表
  - 绿色播报按钮（`mdi:volume-high`）：发送文本到 `play_text_entity`，TTS 朗读，仅 Toast 提示"已播报"
  - 回车键默认发送命令（未配 `command_entity` 时发送播报）
  - 快捷输入（⚡）按钮：仅 `command_entity` 配置时显示，选定快捷项直接发送命令
- **数据加载**：最新对话在底部，向上滚动自动加载更早 `conversation_page_days` 天的数据
- **多对话模式**（`multiple_conversations`）：
  - header 分为两行：标题行显示"与 {name} 聊天" + 图标，下方 tab 行显示所有对话按钮
  - 点击 tab 按钮切换对话，数据独立缓存和分页，切换回已加载的 tab 即时恢复列表和滚动位置
  - 输入区按钮和 placeholder 随当前活跃 tab 切换，只显示该对话支持的按钮
  - 快捷输入合并规则：当前 tab 的 `quick_input`（专属）在前 + 顶层 `quick_input`（共用）在后
  - 有命令下发后自动重置该 tab 的缓存，3 秒后重新加载获取最新回复
- **与 show_conversation 气泡的关系**：`xiaoai_conversation` 是独立卡片类型（直接渲染/弹窗），`show_conversation` 是给其他类型卡片附加的点击气泡行为。两者复用同一套对话 UI 和数据加载逻辑

---

### 6.7 用户卡片 (type: user)

在卡片中嵌入用户信息卡片，显示家庭成员的头像、在/离家状态、位置、天气、导航等信息。通过 `persons` 配置支持**多人模式**，也可以只配置一个人实现单人场景。

---

#### 通用配置

```yaml
  - type: user
    persons:                                     # 家庭成员列表（必填）
      - entity: person.zhangsan                    # person 实体
        at_home: device_tracker.ip15_94            # 在家实体
        location: sensor.15pro_geocoded_location   # 地址文本 + 坐标
        phone_wifi: sensor.15pro_ssid              # 手机 WiFi（可选）
        phone_battery: sensor.15pro_battery_state  # 电池状态（可选）
        phone_battery_level: sensor.15pro_battery_level # 电量（可选）

    # ── 导航（可选）──
    navigation:
      amap_web_key: 你的高德Web端Key           # 高德 Web 端 Key（地图/导航）
      home_coordinates: 116.397428,39.90923     # 家庭经纬度

    # ── 天气（可选，支持多地区 + API）──
    weather:
      - name: 西安市                              # 地区名称（显示在 Tab 上）
        entity: sensor.he_feng_xi_an              # 和风天气 HA 实体（优先）
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx  # API 地址（降级）
      - name: 汉中市
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx  # 仅 API

    # ── 手机信息（可选，仅当 persons 成员未配独立 phone 字段时的降级配置）──
    phone:
      wifi: sensor.xxx_wifi                     # WiFi 名称
      battery: sensor.xxx_battery               # 电池状态（charging/ discharging）
      battery_level: sensor.xxx_battery_level   # 电池电量（0-100）

    # ── 位置显示控制（可选，默认 true）──
    # 支持在 location 对象内设置 show_location 来控制是否显示距离/时间信息
    # 也支持外部 location.show_location（布尔值或 input_boolean 实体 ID）
```

---

#### 配置示例

适合家庭/多人场景，最多配置 **5 个家庭成员**。卡片中**当前登录 HA 的用户头像居中突出**（大头像），其余成员以**小头像**按上/左/右/下环绕布局。匹配逻辑：`person.xxx.attributes.user_id === hass.user.id`。

```yaml
  - type: user
    persons:
      - entity: person.zhangsan                       # person 实体（头像/姓名/登录匹配）
        at_home: device_tracker.ip15_94                # 在家实体（detect 头像彩色/灰度）
        location: sensor.15pro_geocoded_location       # 地址文本 + 坐标（HA 移动端自动解析）
        phone_wifi: sensor.15pro_ssid                  # 手机 WiFi（可选）
        phone_battery: sensor.15pro_battery_state      # 电池状态（可选）
        phone_battery_level: sensor.15pro_battery_level # 电量（可选）

      - entity: person.lisi
        at_home: device_tracker.lisi_phone
        location: sensor.lisi_geocoded_location

      - entity: person.wangwu
        at_home: device_tracker.wangwu_phone
        # 不配 location 时，从 device_tracker 属性或 person→device_trackers 获取坐标

    navigation:
      amap_web_key: 你的高德Web端Key
      home_coordinates: 116.397428,39.90923

    weather:
      - name: 西安市
        entity: sensor.he_feng_xi_an
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx
      - name: 汉中市
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx
```

**天气配置说明：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `name` | ❌ | `string` | 地区名称，显示在 Tab 切换按钮上 |
| `entity` | ❌ | `string` | 和风天气 HA 实体 ID（优先使用） |
| `api_base_url` | ❌ | `string` | 和风天气 API 地址（实体无数据时降级使用） |

**数据源优先级：** `entity` > `api_base_url`。同时配置时优先用实体数据，实体无数据则降级到 API。

**API 数据缓存：** 从 API 获取的数据会缓存 30 分钟，避免频繁请求。打开弹窗时如果缓存过期会自动刷新。

**旧格式兼容：** 仍支持旧的单地区格式 `weather: { entity: sensor.xxx }`。

**天气配置格式支持三种写法：**

```yaml
# 写法1：标准数组格式（推荐）
weather:
  - name: 西安市
    entity: sensor.he_feng_xi_an
    api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx
  - name: 汉中市
    api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx

# 写法2：对象键名作为地区名
weather:
  - 西安市:
      entity: sensor.he_feng_xi_an
      api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx
  - 汉中市:
      api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx

# 写法3：旧格式（单地区，向后兼容）
weather:
  entity: sensor.he_feng_xi_an
```

**每个 person 成员字段说明：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `entity` | ✅ | `person.xxx` | 头像/姓名/`user_id` 均从此实体自动获取 |
| `at_home` | ✅ | `device_tracker.xxx` | `home` → 在家 / 其他 → 离家。控制头像边框颜色 + 灰度滤镜 |
| `location` | ❌ | `sensor.xxx_geocoded_location` | HA 移动端自动解析的地址文本；坐标从 `attributes.Location[lat, lon]` 读取 |
| `phone_wifi` | ❌ | `sensor.xxx_ssid` | 手机当前连接的 WiFi 名（弹窗头部显示） |
| `phone_battery` | ❌ | `sensor.xxx_battery_state` | 手机电池状态（`charging` / `discharging`） |
| `phone_battery_level` | ❌ | `sensor.xxx_battery_level` | 手机电池电量百分比（0-100） |

> `at_home` 为必填。仅凭 `person.state` 无法判断是否在家（可能是 `company` 等 zone 名称），只有 `device_tracker.state === 'home'` 能准确判断。

**位置坐标获取优先级（`location` 未配置时的降级）：**
1. `location` 实体 → `attributes.Location` 数组
2. `at_home` (device_tracker) → `attributes.latitude / longitude`
3. `person` 实体的 `attributes.device_trackers` → 遍历其中各 device_tracker

**卡片布局效果：** 当前登录用户头像居中（大头像），其余成员的小头像环绕四周。连线颜色反映在/离家状态：🟢 绿=在家，⚪ 灰=离家（灰度滤镜）。

**弹窗布局效果：** 所有成员头像在头部并排显示，当前用户高亮（稍大+白色外圈），各自显示"在线/离线"状态胶囊。地址区域显示焦点用户的位置。地图上以不同颜色标记所有人的坐标，带导航路线规划。

**小头像点击：** 点击任意小头像，弹窗切换为该成员专属的定位/导航/详情页。

### 6.9 健康 (type: health)

显示健康数据入口，点击弹出健康数据控制面板。数据通过 HA 数据统一存储系统 API 接口获取，顶层配置的 `api_base_url` 和 `key` 自动生效。

```yaml
  - type: health
    name: 健康档案                        # 显示名称
    icon: mdi:heart-pulse
    primary: 健康                         # 按钮下方文字
    user: CM,CHJ,SPP                      # 家庭成员（逗号分隔）
    popup_position: clone_button_down
    width: 430px
```

### 6.10 动态图标 (type: dynamic_icon)

动态图标是最灵活的按钮类型。可以根据实体的不同状态，自动切换图标、颜色和动画。多条规则同时匹配时可以循环显示，也可以始终显示第一条匹配的规则。适合用来做"状态监控中心"——一个按钮同时监控多个设备或传感器，哪个出问题就亮哪个。

#### 基础用法

```yaml
  - type: dynamic_icon
    icon: mdi:bell                          # 默认图标（无规则匹配时显示）
    color: '#74787c'                        # 默认颜色
    rules:                                  # 规则列表
      - condition:                           # 规则1：门开了
          entity: binary_sensor.front_door
          operator: '=='
          value: 'on'
        icon: mdi:door-open
        color: '#2ecc71'
        animation: shake
      - condition:                           # 规则2：温度>30度
          entity: sensor.temperature
          operator: '>'
          value: '30'
        icon: mdi:thermometer-alert
        color: '#e74c3c'
        animation: blink
    loop_display: true                      # 多条规则匹配时循环显示
    display_time: 3                         # 每条规则显示几秒
    show_badge: true                        # 显示匹配条件的规则数量
```

##### 轮播模式 (primary: dynamic)

动态图标还支持**轮播模式** —— 不依赖条件评估，所有规则按顺序循环展示。每条规则独立显示图标、颜色、动画、`primary` 文本和右上角斜三角文字（`icon_text`）。适合需要轮播展示多条信息（如不同电表读数）的场景。

```yaml
  - type: dynamic_icon
    primary: dynamic                  # 启用轮播模式
    display_time: 3                   # 每条规则显示秒数（默认3秒）
    tap_action:                       # 点击动作（顶层全局配置）
      action: more-info
      entity: sensor.ele
    rules:
      - primary: "{{ states('sensor.ele') }}￥"           # 按钮下方文字，支持模板
        icon: mdi:transmission-tower-import
        icon_text: "502"                                   # 右上斜三角文字，支持模板
        color: "#e60033"
        animation: blink
      - primary: "{{ states('sensor.gas') }}￥"
        icon: mdi:transmission-tower-import
        icon_text: "602"
        color: "#007b43"
```

**轮播模式特点：**

| 特点 | 说明 |
|------|------|
| `condition` 忽略 | 所有规则无条件轮流显示，不评估条件 |
| 不显示 badge | 轮播模式下自动隐藏角标 |
| 始终为开启状态 | 按钮以 `.on` 样式显示，不受 onCount 影响 |
| `icon_text` | 图标右上角斜三角区域显示文本，支持 Jinja2 模板和 `preset_xx` 预设，颜色跟随规则 color |
| `primary` 在规则内 | 每条规则独立定义按钮下方文字，跟随轮播实时刷新 |
| `tap_action` 优先级 | 顶层 > 规则级 > 默认 toggle-all。顶层未配时使用当前轮播规则的 `tap_action`（详见下方说明） |

#### 顶层配置项

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `type` | ✅ | `string` | — | 固定为 `dynamic_icon` |
| `icon` | ❌ | `string` | `mdi:help-circle` | 默认图标，无规则匹配时显示 |
| `color` | ❌ | `string` | `#74787c` | 默认图标颜色，无规则匹配时使用 |
| `on_color` | ❌ | `string` | `#2ecc71` | 有规则匹配时的光晕颜色（用于按钮阴影效果） |
| `off_color` | ❌ | `string` | `#e74c3c` | 无规则匹配时的光晕颜色 |
| `rules` | ✅ | `array` | `[]` | 规则列表，每条规则含 `condition` + 显示属性 |
| `loop_display` | ❌ | `boolean` | `true` | 多条规则匹配时是否循环显示。`false` 时始终显示第一条匹配的规则 |
| `display_time` | ❌ | `number` | `3` | 循环显示时每条规则显示的秒数 |
| `show_badge` | ❌ | `boolean` | `true` | 是否显示角标（满足条件的实体数量，去重计数）。轮播模式下自动隐藏 |
| `badge_entity` | ❌ | `string` | 无 | 自定义角标实体，优先级高于自动统计。实体值非 0/unavailable/unknown 时显示 |
| `primary` | ❌ | `string` | 无 | 按钮下方文字，支持模板语法。设为 `dynamic` 时启用轮播模式（见轮播模式说明）。需要完整 Jinja2 语法时配合 `server_explain: true`（详见第十七节）。非轮播模式时由 `_updateDockTriangles` 管理，与 `icon_text` 互不干扰 |
| `server_explain` | ❌ | `boolean` | `false` | `true` 时将 `primary` 模板发送到 HA 后端渲染（仅限 `expand()` 等 HA 独有函数） |
| `preset` | ❌ | `string` | 无 | 预设规则名称，自动生成 `rules`。详见下方"预设规则"章节 |
| `entity` | ❌ | `string` | 无 | 预设规则使用的实体 ID，与 `preset` 配合使用 |
| `tap_action` | ❌ | `object` | 无 | 自定义点击动作（不配置时点击默认弹出第一个匹配规则实体的 more-info）。**轮播模式优先使用顶层配置**，顶层未配时使用当前轮播规则的 `tap_action`（每条规则可独立定义） |
| `name` | ❌ | `string` | 无 | 按钮名称，用于 Tab 高亮匹配（当弹窗含选项卡时，按 `rule.name === tab.name` 自动高亮） |

#### rules 子项配置

每条规则由 `condition`（条件）和显示属性组成。轮播模式下 `condition` 忽略，所有规则参与轮播。

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `condition` | ❌ | `object` | — | 条件配置（单一条件或复合条件）。轮播模式下忽略 |
| `icon` | ❌ | `string` | 顶层 `icon` | 匹配时显示的图标 |
| `color` | ❌ | `string` | 顶层 `color` | 匹配时图标的颜色。支持 **Jinja2 模板语法**（如 `"{{ states('sensor.color') }}"`）和 **CSS 命名色**（如 `red`/`yellow`/`green`）。模板输出 hex（如 `#e60033`）或命名色均可 |
| `animation` | ❌ | `string` | 无 | 匹配时的动画效果 |
| `primary` | ❌ | `string` | 无 | 按钮下方文字，支持模板语法。**轮播模式必填**，每条规则独立显示。非轮播模式下也支持，由 `_updateDockTriangles` 统一管理 |
| `icon_text` | ❌ | `string` | 无 | 图标右上角斜三角文字，支持 **Jinja2 模板**和 **`preset_xx` 预设**（如 `preset_state`、`preset_ac`、`preset_fan`、`preset_humidifier`、`preset_qweather`、`preset_media`）。**所有按钮类型均支持**，不限于 dynamic_icon。不配置时不显示斜三角 |
| `tap_action` | ❌ | `object` | 无 | 当前规则的点击动作（仅轮播模式生效，顶层未配置时使用）。支持 `card_config.from_config_id` 引用已注册的弹窗配置 |
| `card_params` | ❌ | `object` | 无 | 运行时参数，合并到弹出卡片的配置中。key/value 由目标卡片定义，纯透传。`from_config_id` 解析时此字段会被保留 |
| `initial_tab` | ❌ | `string` | 无 | 播放到该规则时，将值合并到弹出卡片的 `initial_tab` 字段（如 `"1"`）。目标卡片在 `setConfig` 中读取并跳转到对应视图。**无需 `from_config_id`，顶层 `tap_action.card` 直接配置卡片也可用** |
| `name` | ❌ | `string` | 无 | 规则名称，用于弹窗 Tab 高亮匹配（与 tab 的 name 对应时自动高亮） |

> **轮播模式点击动作（tap_action）优先级**：
> 1. **顶层 `tap_action`**（配置在 `rules` 同级）— 始终使用，忽略规则内的配置
> 2. **规则级 `tap_action`**（顶层未配时）— 跟随轮播切换，每条规则可独立定义点击动作
> 3. **默认 `toggle-all`** — 顶层和规则级都未配置时回退
>
> 规则级 `tap_action` 支持 `card_config.from_config_id` 引用已注册的弹窗配置，轮播到该规则时自动解析为完整动作：
>
> ```yaml
>   - type: dynamic_icon
>     primary: dynamic
>     display_time: 3
>     # 未配顶层 tap_action → 使用规则级
>     rules:
>       - primary: "{{ states('sensor.ele') }}元"
>         icon: mdi:transmission-tower
>         icon_text: 电
>         tap_action:
>           card_config:
>             from_config_id: ele_config      # 轮播到此规则时弹出电费配置
>       - primary: "{{ states('sensor.gas') }}元"
>         icon: mdi:gas-burner
>         icon_text: 气
>         tap_action:
>           card_config:
>             from_config_id: gas_config      # 轮播到此规则时弹出燃气配置
> ```
>
> 如需所有规则统一点击动作，在顶层配置 `tap_action` 即可覆盖所有规则级配置。
>
> **`card_params` — 运行时参数透传**：在规则级 `tap_action` 中可通过 `card_params` 传递额外参数给弹出卡片，key/value 完全由目标卡片定义。
> `from_config_id` 解析时 `card_params` 会被保留，最终合并到卡片配置中。
>
> ```yaml
> rules:
>   - primary: "电费{{...}}元"
>     icon_text: 电
>     tap_action:
>       card_config:
>         from_config_id: ele       # 引用已注册卡片配置
>       card_params:                # ← 运行时透传参数
>         initial_tab: "1"          #   目标卡片读取此字段做导航
>         theme_variant: dark       #   可传任意 key/value
> ```
>
> 目标卡片在 `setConfig` 中读取 `config.initial_tab` 即可使用。
>
> **`initial_tab` — 快速跳转（无需 `from_config_id`）**：当顶层 `tap_action.card` 直接配置卡片（不引用）时，可在规则中通过 `initial_tab` 指定跳转目标，轮播切换时自动注入到卡片配置：
>
> ```yaml
>   - type: dynamic_icon
>     primary: dynamic
>     rules:
>       - primary: "电费{{...}}元"
>         icon_text: 电
>         initial_tab: "1"           # ← 规则级，直接指定跳转到视图1
>       - primary: "燃气{{...}}元"
>         icon_text: 气
>         initial_tab: "2"           # ← 跳转到视图2
>     tap_action:                    # 顶层配置卡片（只配一次）
>       action: popup_card
>       card:
>         type: custom:electricity-info-card
>         multiclass:
>           "1": { utility_type: ele, ... }
>           "2": { utility_type: gas, ... }
> ```
>
> 目标卡片在 `setConfig` 中读取 `config.initial_tab` 并导航到对应视图。
>
> **`icon_text` 通用支持**：所有按钮类型（含 `type: button`、独立按钮、设备分组等）均支持 `icon_text`，支持 `preset_state`/`preset_ac`/`preset_fan`/`preset_humidifier`/`preset_qweather`/`preset_media` 预设和 Jinja2 模板语法。当不配置 `icon_text` 时不显示右上角斜三角。详见 22.4 节。
>
> **显示属性的两种写法**：`icon`/`color`/`animation` 可以写在规则顶层（与 `condition` 同级），也可以写在 `condition` 内部（与 `entity`/`operator` 同级）。顶层优先级更高。这在复合条件中特别有用，可以避免属性重复：

```yaml
# 写法1：属性与 condition 同级（推荐）
- condition:
    entity: binary_sensor.front_door
    operator: '=='
    value: 'on'
  icon: mdi:door-open
  color: '#2ecc71'

# 写法2：属性在 condition 内部（适合复合条件统一设置样式）
- condition:
    logic: and
    conditions:
      - entity: binary_sensor.door
        operator: '=='
        value: 'on'
      - entity: sensor.temperature
        operator: '>'
        value: '25'
    icon: mdi:door-open          # 在 condition 内部
    color: '#e74c3c'
```

#### condition 条件配置

##### 单一条件

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ✅ | `string` | — | 实体 ID |
| `operator` | ❌ | `string` | `==` | 比较运算符（见下表） |
| `value` | ✅ | `string`/`array` | — | 目标值，数组表示 OR（匹配任一即可） |
| `attribute` | ❌ | `string` | 无 | 比较实体的属性值而非状态值。支持简写（如 `temperature` 自动解析为 `attributes.temperature`）或完整路径（如 `attributes.brightness`） |

**条件支持的操作符：**

| 操作符 | 说明 | 示例 |
|-------|------|------|
| `==` / `===` | 等于 | `value: 'on'` |
| `!=` / `!==` | 不等于 | `value: 'off'` |
| `>` | 大于（数值比较） | `value: '30'` |
| `<` | 小于（数值比较） | `value: '10'` |
| `>=` | 大于等于 | `value: '60'` |
| `<=` | 小于等于 | `value: '20'` |
| `contains` / `include` | 包含（大小写不敏感） | `value: '异常'` |
| `between` | 在范围内 | `value: '20,30'` 或 `value: [20, 30]` |

**单一实体多状态值匹配：**

一个实体可能有多种状态都需要触发同一规则（如空调的 `cool`、`heat`、`dry` 都算"运行中"），有三种方式实现：

**方法1：value 数组（推荐）** — 最简洁，一个条件匹配多个值

```yaml
# 空调处于以下任一状态时图标旋转
- condition:
    entity: climate.living
    operator: '=='
    value: ['cool', 'heat', 'dry', 'fan_only']   # 匹配其中任意一个
  icon: mdi:air-conditioner
  color: '#3498db'
  animation: rotate

# 人员在家或在工作地点
- condition:
    entity: person.zhangsan
    operator: '=='
    value: ['home', 'company']
  icon: mdi:account-check
  color: '#2ecc71'
```

**方法2：多条规则** — 每种状态独立一条规则，可设置不同的图标/颜色/动画

```yaml
# 不同状态显示不同图标
- condition:
    entity: climate.living
    operator: '=='
    value: 'cool'
  icon: mdi:snowflake
  color: '#3498db'
- condition:
    entity: climate.living
    operator: '=='
    value: 'heat'
  icon: mdi:fire
  color: '#e74c3c'
- condition:
    entity: climate.living
    operator: '=='
    value: 'dry'
  icon: mdi:water-off
  color: '#9b59b6'
```

**方法3：contains 包含** — 状态值中包含某关键词即匹配

```yaml
# 状态文本中包含"异常"即匹配
- condition:
    entity: sensor.device_status
    operator: contains
    value: '异常'
  icon: mdi:alert-circle
  color: '#e74c3c'
  animation: blink
```

> **三种方法对比：** 方法1 最简洁，适合多值统一处理；方法2 可以为每个状态定制不同的视觉表现；方法3 适合模糊匹配场景。`value` 数组支持所有操作符（`==`、`!=`、`>`、`<` 等），数组中每个值独立与实体值比较，任一匹配即为真。

**attribute 属性比较：**

```yaml
# 比较灯光亮度属性
- condition:
    entity: light.living_room
    attribute: brightness              # 等价于 attributes.brightness
    operator: '>'
    value: '200'
  icon: mdi:lightbulb-on
  color: '#f1c40f'

# 比较温度传感器属性
- condition:
    entity: climate.living
    attribute: temperature             # 等价于 attributes.temperature
    operator: '>'
    value: '26'
  icon: mdi:thermometer-alert
  color: '#e74c3c'
```

> 不配置 `attribute` 时，比较的是实体的 `state` 值；配置 `attribute` 后，比较的是实体对应属性的值。

##### 复合条件（AND/OR）

当需要同时满足多个条件时，使用复合条件。复合条件支持嵌套。

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `logic` | ❌ | `string` | `and` | 逻辑关系：`and`（所有条件都满足）或 `or`（任一条件满足） |
| `conditions` | ✅ | `array` | — | 子条件列表，每个子项为单一条件或嵌套的复合条件 |

**AND 示例（所有条件必须同时满足）：**

```yaml
- condition:
    logic: and
    conditions:
      - entity: binary_sensor.front_door
        operator: '=='
        value: 'on'
      - entity: sensor.temperature
        operator: '>'
        value: '25'
  icon: mdi:door-open
  color: '#e74c3c'
  animation: blink
```

**OR 示例（任一条件满足即可）：**

```yaml
- condition:
    logic: or
    conditions:
      - entity: binary_sensor.front_door
        operator: '=='
        value: 'on'
      - entity: binary_sensor.back_door
        operator: '=='
        value: 'on'
  icon: mdi:door-open
  color: '#e74c3c'
```

**嵌套复合条件（AND + OR 混合）：**

```yaml
- condition:
    logic: and
    conditions:
      - entity: sensor.humidity
        operator: '>'
        value: '70'
      - condition:                    # 嵌套的 OR 条件
          logic: or
          conditions:
            - entity: binary_sensor.window
              operator: '=='
              value: 'on'
            - entity: sensor.temperature
              operator: '>'
              value: '30'
  icon: mdi:water-percent
  color: '#3498db'
  animation: breathe
```

#### 动画效果

匹配规则时可为图标添加动画效果，让异常状态更加醒目。

| 动画名 | 别名 | 效果 | 适用场景 |
|--------|------|------|----------|
| `shake` | — | 左右晃动（2秒周期） | 告警、异常状态 |
| `rotate` | — | 360度持续旋转（2秒线性） | 加载中、运行中 |
| `blink` | `flash` | 闪烁（1秒周期，透明度变化） | 严重告警、需立即关注 |
| `breathe` | — | 呼吸缩放（2秒周期，大小变化） | 正常运行、在线状态 |
| `jump` | — | 上下跳动（1.5秒周期） | 提醒、新消息 |
| `random-move` | `random_move` | 小范围随机移动（3秒周期） | 趣味效果、宠物追踪 |

> 不配置 `animation` 时图标静止显示。

---

### 通用按钮动画配置 (`icon_animation`)

> 适用于普通按钮类型（lights / switch / socket / curtain / heater / device / consumables / media 等），**不覆盖**空调（ac）和动态图标（dynamic_icon）已有的独立动画机制。

**全局默认（批量设置）：** 支持直接写动画名，也支持实体 ID 动态控制：

```yaml
type: custom:room-elves-card
icon_animation: input_select.icon_animation_mode   # 读取实体的 state 作为动画名
buttons:
  - type: lights
    card:
      - entity: light.living_room
  - type: sockets
    card:
      - entity: switch.plug
```

也可以直接写动画名，所有未单独配置的按钮统一使用该动画：

```yaml
icon_animation: breathe
```

**单按钮覆盖（不随全局变动）：**

```yaml
buttons:
  - type: lights
    icon_animation: rotate   # 此按钮单独使用旋转动画
    card:
      - entity: light.living_room
  - type: curtain
    icon_animation: none     # 此按钮关闭动画
    entity: cover.curtain
  - type: switch
    # 不配置 icon_animation → 继承全局 breathe
    entity: switch.plug
```

**优先级：按钮级 `icon_animation` > 全局 `icon_animation` > 硬编码默认（shake）**

> 全局 `icon_animation` 仅对**未单独配置** `icon_animation` 的按钮生效，批量设置时不会覆盖单个设置。

#### 角标（badge）说明

动态图标的角标默认显示**满足条件的实体数量**（去重计数）：

- 自动统计所有 `rules` 中条件满足的实体，多个规则引用同一实体只计一次
- `show_badge` 默认为 `true`，设为 `false` 可隐藏角标
- 角标值为 0 时不显示

**使用 `badge_entity` 自定义角标：**

```yaml
  - type: dynamic_icon
    icon: mdi:bell
    badge_entity: sensor.unread_messages     # 用传感器值作为角标
    rules:
      - condition:
          entity: binary_sensor.alert
          operator: '=='
          value: 'on'
        icon: mdi:bell-ring
        color: '#e74c3c'
```

> `badge_entity` 优先级高于自动统计。配置了 `badge_entity` 后，角标值取该实体的 state（非 0/unavailable/unknown 时显示）。

#### 循环显示机制

当多条规则同时匹配时，图标会按规则顺序循环切换显示：

- `loop_display: true`（默认）：按 `display_time` 间隔循环显示所有匹配的规则
- `loop_display: false`：始终只显示第一条匹配的规则，不循环
- `display_time`：循环间隔秒数，默认 3 秒

```yaml
# 示例：3个告警同时触发时，每2秒切换显示一个
loop_display: true
display_time: 2
```

#### 点击交互

- **未配置 `tap_action`**：点击按钮弹出第一个匹配规则实体的 more-info 详情面板
- **配置了 `tap_action`**：执行指定动作，支持所有 tap_action 类型（`more-info`、`toggle`、`call-service`、`navigate`、`popup_card`、`card` 等）

```yaml
  - type: dynamic_icon
    icon: mdi:shield-home
    tap_action:
      action: more-info
      entity: alarm_control_panel.home     # 点击弹出指定实体的详情
    rules:
      - condition:
          entity: binary_sensor.front_door
          operator: '=='
          value: 'on'
        icon: mdi:door-open
        color: '#e74c3c'
        animation: blink
```

> **`color` 支持 Jinja2 模板和 CSS 命名色**。模板中可以直接返回 `red`/`yellow`/`green` 等命名色，按钮背景色会自动从该颜色减淡计算。适用于用 `input_select` 或传感器动态控制图标颜色：
>
> ```yaml
>   - type: dynamic_icon
>     primary: dynamic
>     display_time: 3
>     rules:
>       - primary: "{{ states('sensor.ele') | float | round(0) }}元"
>         icon: mdi:transmission-tower
>         icon_text: 电
>         color: "{% set s = states('sensor.ele') | float(0) %}{% if s < 20 %}red{% elif s <= 50 %}yellow{% else %}green{% endif %}"
>         animation: blink
>       - primary: "{{ states('sensor.gas') | float | round(0) }}元"
>         icon: mdi:gas-burner
>         icon_text: 气
>         color: "{% set s = states('sensor.gas') | float(0) %}{% if s < 50 %}#e60033{% elif s <= 80 %}orange{% else %}red{% endif %}"
>         animation: breathe
> ```
>
> **`icon_text` 非轮播模式支持**：当 `loop_display: false` 时，`icon_text` 同样可以显示。右上角斜三角徽章会在匹配的规则有 `icon_text` 时自动出现，`color` 和 `icon_text` 均支持 Jinja2 模板语法。

#### 预设规则 (preset)

当 `dynamic_icon` 需要匹配的是一组已知状态（如天气状况、空调模式），可以不用手动写十几条 `rules`，而是使用预设：指定 `preset` 名称和 `entity`，系统自动生成 `rules`。用户仍可在 `rules` 中手写部分规则覆盖预设值。

> **⚠️ 重要**：使用 `preset` 时必须同时指定 `entity`（预设用它生成每条规则的 `condition.entity`）。

```yaml
  - type: dynamic_icon
    entity: weather.qweather_pro_lian_hu_weather  # 必填
    preset: qweather                              # 自动展开 16 条天气规则
    loop_display: false
    show_badge: false
    primary: |
      {{state_attr('weather.qweather_pro_lian_hu_weather', 'condition_cn')}}
    tap_action:
      action: popup_card
      card:
        type: custom:qweather-card
        entity: weather.qweather_pro_lian_hu_weather
```

等价于手写 16 条 `rules`（每条自动注入 `condition.entity`、`icon`、`icon_text`、`color`、`animation`）。

> **`preset: qweather` 与 `preset: weather` 的区别**：
> - `weather` / `metno`：匹配实体 `state` 的 HA 标准条件字符串（`sunny`、`cloudy`、`rainy` 等）
> - `qweather`：匹配实体 `attributes.qweather_icon` 的 QWeather 数值代码（`"104"`=阴、`"306"`=中雨等），覆盖 60+ 种天气代码，自动生成全部规则
>
> **通用 attribute 覆盖**：部分预设（如 `qweather`）有默认匹配的 attribute 字段。可通过 `condition.attribute` 覆盖为其他属性，甚至用于其他非天气场景：
> ```yaml
>   - type: dynamic_icon
>     entity: weather.hefeng_home
>     preset: qweather
>     condition:
>       attribute: condition_cn        # 改为匹配中文说明字段
> ```
> 预设未定义默认 attribute 时（如 `weather`、`ac`），`condition.attribute` 也可手动添加，改变匹配字段为实体属性而非 state。

##### 预设列表

| 预设名称 | 适用场景 | 匹配字段 | 条件键值 | 说明 |
|---------|---------|---------|---------|------|
| `qweather` | 天气 | `attributes.qweather_icon` | 100 晴 / 104 阴 / 306 中雨 / 400 小雪 / 501 雾 / 999 未知 等 60+ 数值码 | 专为和风天气自定义集成设计，读取 `qweather_icon` 属性匹配，不受 HA 语言翻译影响。图标颜色按天气特征定制（雷→黄闪、暴雨→深蓝发抖、雪→白蓝旋转） |
| `weather` / `metno` | 天气 | `state` | `clear-day` `sunny` `cloudy` `partlycloudy` `fog` `hail` `lightning` `lightning-rainy` `pouring` `rainy` `snowy` `snowy-rainy` `windy` `exceptional` `clear-night` `clear` | 覆盖 HA 标准天气状态。`icon_text` 统一为单字（晴/夜/阴/云/雾…），适合右上角三角徽章 |
| `ac` / `aircon` / `climate` / `hvac` | 空调 (HVAC) | `state` | `off` `idle` `cool` `heat` `dry` `fan_only` `auto` | 匹配 climate 实体的 hvac_mode 状态。关闭时图标为 `mdi:air-conditioner` |
| `fan` / `circulation_fan` / `circ_fan` | 循环扇 | `state` | `off` `直吹风` `自然风` `智能风` `睡眠风` | 匹配 fan 实体的状态或 `preset_mode` 属性。模式值通常在 `preset_mode` 属性中，需配合 `condition.attribute: preset_mode`。关闭时图标为 `mdi:fan` |
| `humidifier` / `humid` | 加湿器 | `state` | `off` `恒湿` `睡眠` `强力` | 匹配 humidifier 实体的状态或 `mode` 属性。模式值可能在 `mode` 属性中，需配合 `condition.attribute: mode`。关闭时图标为 `mdi:fan` |
| `media_player` / `media` / `mp` | 媒体播放器 | `state` | `playing` `paused` `idle` `standby` `on` `off` | 匹配 media_player 实体的 state 状态。播放→`mdi:speaker-play`(绿)、暂停→`mdi:speaker-pause`(青)、空闲→`mdi:speaker-stop`(浅蓝灰)、待机/开启→`mdi:speaker`(深灰/蓝)、关闭→`mdi:speaker-off`(灰) |
| `kettle` / `yang_sheng_hu` | 养生壶 | `state` | `待机中` `烹饪中` `预约中` `保温中` `空闲中提壶` `烹饪中提壶` `预约中提壶` `保温中提壶` `错误` `升级中` `烹饪完成` | 匹配养生壶实体的中文 state 状态。烹饪→`mdi:kettle-steam`(红 shake)、保温→`mdi:thermometer-chevron-up`(橙 breathe)、提壶状态→图标 outline 版 + jump 动画、错误→`mdi:alert-circle`(红 blink)、升级→`mdi:cloud-download`(蓝 rotate)、完成→`mdi:check-circle`(绿 breathe) |

##### 用户自定义覆盖

如果预设中某个状态的图标/颜色不符合预期，可以手动写 `rules` 来覆盖——`rules` 有值时预设不会展开：

```yaml
  - type: dynamic_icon
    entity: climate.ke_ting
    preset: ac
    # 手动覆盖部分规则
    rules:
      - condition:
          value: cool
        icon: mdi:snowflake
        icon_text: ❄
        color: "#00bfff"
        animation: rotate
```

> 预设文件存放在 `modules/presets/dynamic-icon-presets.js`。添加新预设只需在该文件定义映射表并在 `PRESET_REGISTRY` 注册即可。

##### 循环扇 / 加湿器预设示例

```yaml
# 循环扇 — 模式在 preset_mode 属性中
- type: dynamic_icon
  entity: fan.xiaomi_smartfan
  preset: fan
  condition:
    attribute: preset_mode          # 覆盖默认 state，改为匹配 preset_mode 属性
  tap_action:
    action: more-info

# 加湿器 — 模式在 mode 属性中
- type: dynamic_icon
  entity: humidifier.bedroom
  preset: humidifier
  condition:
    attribute: mode                 # 覆盖默认 state，改为匹配 mode 属性
  tap_action:
    action: more-info
```

##### 媒体播放器预设示例

```yaml
# 媒体播放器 — 动态图标联动（图标+颜色+文字随播放状态变化）
- type: dynamic_icon
  entity: media_player.ke_ting_yin_xiang
  preset: media_player             # 自动展开 6 条规则：playing/paused/idle/standby/on/off
  primary: 音响
  tap_action:
    action: more-info

# 仅 icon_text 文字预设（适用于 media 按钮类型，图标/颜色由动态图标预设控制）
# 注：type: media 未配 on_icon/off_icon 时会自动套用 media_player 预设，
#     图标/颜色/动画/角标文字全部联动，无需显式写 preset
- type: media
  entity: media_player.wo_de_yin_xiang
  name: 音响
  # icon_text: preset_media          # 已自动启用，如需自定义可覆盖

# 养生壶 icon_text 预设（配合 preset: kettle 使用）
# 返回两个字的中文状态文字（待机/烹饪/预约/保温/提壶/错误/升级/完成）
- type: dynamic_icon
  entity: sensor.养生壶_工作状态
  preset: kettle
  # icon_text: preset_kettle         # 已自动启用
  primary: "{{ state('sensor.养生壶_工作状态') }}"
```

#### Tab 高亮联动

当动态图标按钮配置了弹窗（通过 `tap_action` 弹出含选项卡的弹窗），可以利用 `rule.name` 与 `tab.name` 的对应关系实现 Tab 自动高亮：

- 如果 `rule.name` 与某个 `tab.name` 相同，且该规则条件满足，则对应 Tab 自动高亮
- Tab 自身的 `entity` + `entity_value` 配置优先级更高

```yaml
  - type: dynamic_icon
    icon: mdi:home
    tap_action:
      action: popup_card
      # ... 弹窗配置含 tabs
    rules:
      - name: 门锁                        # 与 tab.name 匹配
        condition:
          entity: binary_sensor.front_door
          operator: '=='
          value: 'on'
        icon: mdi:door-open
        color: '#e74c3c'
      - name: 温度                        # 与 tab.name 匹配
        condition:
          entity: sensor.temperature
          operator: '>'
          value: '30'
        icon: mdi:thermometer-alert
        color: '#e74c3c'
```

#### 完整配置示例

**示例1：全屋安防监控**

一个按钮监控所有门窗传感器，任何门/窗打开时图标变色+动画，角标显示打开数量：

```yaml
  - type: dynamic_icon
    icon: mdi:shield-home
    color: '#95a5a6'
    on_color: '#2ecc71'
    primary: 安防
    loop_display: true
    display_time: 3
    show_badge: true
    rules:
      - condition:
          entity: binary_sensor.front_door
          operator: '=='
          value: 'on'
        icon: mdi:door-open
        color: '#e74c3c'
        animation: shake
      - condition:
          entity: binary_sensor.back_door
          operator: '=='
          value: 'on'
        icon: mdi:door-open
        color: '#e74c3c'
        animation: shake
      - condition:
          entity: binary_sensor.living_window
          operator: '=='
          value: 'on'
        icon: mdi:window-open-variant
        color: '#f39c12'
        animation: blink
      - condition:
          entity: binary_sensor.bedroom_window
          operator: '=='
          value: 'on'
        icon: mdi:window-open-variant
        color: '#f39c12'
        animation: blink
```

**示例2：环境告警**

监控温湿度异常，支持属性比较和复合条件：

```yaml
  - type: dynamic_icon
    icon: mdi:thermometer
    color: '#95a5a6'
    primary: 环境
    loop_display: true
    display_time: 4
    rules:
      - condition:
          entity: sensor.living_temperature
          operator: '>'
          value: '32'
        icon: mdi:thermometer-alert
        color: '#e74c3c'
        animation: blink
      - condition:
          entity: sensor.living_temperature
          operator: '<'
          value: '10'
        icon: mdi:snowflake-thermometer
        color: '#3498db'
        animation: breathe
      - condition:
          entity: sensor.living_humidity
          operator: '>'
          value: '80'
        icon: mdi:water-percent
        color: '#3498db'
        animation: breathe
      # 复合条件：高温+高湿
      - condition:
          logic: and
          conditions:
            - entity: sensor.living_temperature
              operator: '>'
              value: '30'
            - entity: sensor.living_humidity
              operator: '>'
              value: '70'
        icon: mdi:weather-sunny-alert
        color: '#e74c3c'
        animation: shake
```

**示例3：灯光亮度监控（使用 attribute）**

```yaml
  - type: dynamic_icon
    icon: mdi:lightbulb-outline
    color: '#95a5a6'
    primary: 灯光
    rules:
      - condition:
          entity: light.living_room
          attribute: brightness
          operator: '>'
          value: '200'
        icon: mdi:lightbulb-on
        color: '#f1c40f'
      - condition:
          entity: light.living_room
          operator: '=='
          value: 'on'
        icon: mdi:lightbulb
        color: '#f39c12'
        animation: breathe
```

**示例4：人员状态监控（value 数组 + badge_entity）**

```yaml
  - type: dynamic_icon
    icon: mdi:account-group
    color: '#95a5a6'
    primary: 人员
    badge_entity: sensor.people_home_count
    rules:
      - condition:
          entity: person.zhangsan
          operator: '=='
          value: ['home', 'company']      # 在家或在公司都算正常
        icon: mdi:account-check
        color: '#2ecc71'
      - condition:
          entity: person.zhangsan
          operator: '!='
          value: 'home'
        icon: mdi:account-alert
        color: '#f39c12'
        animation: breathe
```

**示例5：between 范围判断**

```yaml
  - type: dynamic_icon
    icon: mdi:battery
    color: '#95a5a6'
    primary: 电池
    rules:
      - condition:
          entity: sensor.phone_battery_level
          operator: between
          value: '20,80'                   # 电量在 20%~80% 之间
        icon: mdi:battery-70
        color: '#2ecc71'
      - condition:
          entity: sensor.phone_battery_level
          operator: '<'
          value: '20'
        icon: mdi:battery-alert
        color: '#e74c3c'
        animation: blink
```

### 6.11 时间轴 (type: timeline)

在按钮上直接显示当天设备状态变化的时间轴（例如人体传感器从"无人"到"有人"的变化记录）。点击时间轴段显示详细活动记录。

```yaml
  - type: timeline
    entity: binary_sensor.living_motion     # 要显示历史数据的实体
    map_table:                              # 状态值→显示文本/颜色的映射
      on:                                   # on状态下的子状态
        on:                                 # 状态值为"on"
          text: '有人'
          icon: 'mdi:account'
          color: '#2ecc71'
        active:                             # 状态值为"active"
          text: '活跃中'
          icon: 'mdi:run'
          color: '#3498db'
      off:                                  # off状态
        off:
          text: '无人'
          icon: 'mdi:account-off'
          color: '#95a5a6'
    api_base_url: http://192.168.1.100:8080  # 如果HA没有历史，可从外部API获取
```

### 6.12 内嵌卡片 (type: card)

在 head 模式中嵌入其他 HA 卡片（如天气预报、地图等）。

```yaml
  - type: card
    card_config:
      type: weather-forecast
      entity: weather.home
```

### 6.13 按钮 (type: button)

用于控制 `input_button`、`button` 等按压型实体，或 `switch` 等开关型实体。点击按钮触发操作，支持点击反馈动画和持续时长显示。

```yaml
  - type: button
    entity: input_button.ceshi           # 按钮实体ID（支持 input_button / button / switch 等）
    name: 打开监控                       # 显示名称
    icon: mdi:cctv                       # 图标
    icon_color: '#d0273e'                # 图标颜色（优先级高于 on_color/off_color）
    on_icon: mdi:cctv                    # 开启时图标
    off_icon: mdi:cctv-off               # 关闭时图标
    on_color: '#3498db'                  # 开启时图标颜色
    off_color: '#95a5a6'                 # 关闭时图标颜色
    icon_text: S                         # 右上角斜三角文字，支持 preset_xx 和 Jinja2 模板
    status_text: 点击                     # 自定义状态文本（替代默认的"开启/关闭"）
    status_text_completion: OK           # 点击后显示3秒的完成文本
    icon_click_color: '#006e54'          # 点击后图标变色3秒的颜色
    show_duration: true                  # 是否显示持续时长
    confirm: false                       # 点击是否需要确认
```

**各配置项说明：**

| 配置项 | 必填 | 类型 | 说明 |
|--------|:----:|------|------|
| `entity` | ✅ | `string` | 按钮实体ID，支持 `input_button`、`button`、`switch` 等域 |
| `name` | ❌ | `string` | 显示名称，默认 `按钮` |
| `icon` | ❌ | `string` | 默认图标 |
| `icon_color` | ❌ | `string` | 图标颜色，优先级高于 `on_color` / `off_color` |
| `on_icon` | ❌ | `string` | 开启时图标，默认 `mdi:toggle-switch` |
| `off_icon` | ❌ | `string` | 关闭时图标，默认 `mdi:toggle-switch-off` |
| `on_color` | ❌ | `string` | 开启时图标颜色，默认 `#3498db` |
| `off_color` | ❌ | `string` | 关闭时图标颜色，默认 `#95a5a6` |
| `icon_text` | ❌ | `string` | 右上角斜三角文字。支持 `preset_xx` 预设（`preset_state`/`preset_ac`/`preset_fan`/`preset_humidifier`/`preset_qweather`/`preset_media`）和 Jinja2 模板语法。不配置时不显示 |
| `status_text` | ❌ | `string` | 自定义状态文本，配置后替代默认的"开启/关闭" |
| `status_text_completion` | ❌ | `string` | 点击后按钮状态文本显示的完成文本，3秒后自动恢复为 `status_text`（或默认文本） |
| `icon_click_color` | ❌ | `string` | 点击后图标变色的颜色，3秒后自动恢复为原来的颜色 |
| `show_duration` | ❌ | `boolean` | 是否显示距上次状态变化的持续时长，默认 `false` |
| `confirm` | ❌ | `boolean` | 点击时是否弹出确认对话框，默认 `false` |
| `tap_action` | ❌ | `object` | 自定义点击动作，配置后替代默认的按钮按压行为 |

**点击交互流程：**

1. 点击按钮 → 图标变色（`icon_click_color`）+ 状态文本变为完成文本（`status_text_completion`）+ 时长从 `0秒` 重新计时
2. 3秒后 → 图标恢复原色 + 状态文本恢复为 `status_text`（或默认的"开启/关闭"）
3. 图标可单独点击查看历史记录

**实体类型与行为：**

- `input_button` / `button` 实体：调用 `press` 服务
- `switch` 等其他实体：调用 `toggle` 服务

### 6.14 独立按钮（无 type）

如果不写 type，就是一个独立的开关按钮，只控制一个实体。

```yaml
  - entity: switch.some_switch          # 实体ID
    icon: mdi:toggle-switch             # 图标
    on_icon: mdi:toggle-switch          # 开启时图标
    off_icon: mdi:toggle-switch-off     # 关闭时图标
    on_color: '#2ecc71'                 # 开启时颜色
    off_color: '#e74c3c'                # 关闭时颜色
    icon_text: 开                          # 右上角斜三角文字，支持 preset_xx 和 Jinja2 模板
    name: 开关                          # 名称
```

> 右上角斜三角背景色自动跟随 `on_color` / `off_color`（取半透明）。当 `icon_text` 未配置时三角不显示。

#### 独立按钮的角标（badge）

独立按钮支持 `badge` 数组或 `badge_entity` 配置，可以根据实体状态条件显示角标计数。**当配置了 `badge` 或 `badge_entity` 时，角标的值还决定了图标的显示状态**：

- **角标值 ≥ 1** → 显示 `on_icon` + `on_color`（视为"开启"状态）
- **角标值 < 1** → 显示 `off_icon` + `off_color`（视为"关闭"状态）

这意味着即使没有 `entity`，或 `entity` 状态与角标无关，只要配置了 `badge` / `badge_entity`，图标和颜色就会跟随角标值变化。

```yaml
  - name: 电脑
    badge:
      - entity: binary_sensor.192_168_1_34
        condition: "on"
    entity: binary_sensor.192_168_1_34
    on_icon: mdi:desktop-classic
    off_icon: mdi:desktop-classic
    on_color: "#f58220"
    off_color: "#74787c"
    tap_action:
      action: toggle
```

上例中：binary_sensor 为 on 时角标计数 = 1（≥1），图标显示橙色（on_color）；为 off 时角标计数 = 0（<1），图标显示灰色（off_color）。

多条件角标示例：
```yaml
  - name: 电脑
    entity: binary_sensor.192_168_1_34
    on_icon: mdi:desktop-classic
    off_icon: mdi:desktop-classic
    on_color: "#f58220"
    off_color: "#74787c"
    badge:
      - entity: binary_sensor.192_168_1_34
        condition: on
      - entity: sensor.zimi_cn_1137225298_zncz01_electric_power_p_10_1
        condition:
          - <10
```

如果 binary_sensor 为 on → 计数 +1；如果功率 < 10 → 计数 +1。两项都满足时角标显示 2，只满足一项显示 1，都不满足则角标不显示且图标为 off 状态。

badge_entity 示例：

```yaml
  - name: 未读消息
    badge_entity: sensor.unread_count      # 实体值作为角标，≥1 时显示 on 状态
    on_icon: mdi:bell-ring
    off_icon: mdi:bell-outline
    on_color: "#e74c3c"
    off_color: "#95a5a6"
```



**condition 支持的格式：**

| 格式 | 说明 | 示例 |
|------|------|------|
| 字符串状态 | 实体状态等于该值 | `condition: on` |
| 字符串表达式 | 数值比较 | `condition: <10`、`>=50`、`!=0` |
| 数组 | OR 语义，任一满足即可 | `condition: ['<10', '>100']` |
| 对象 | 透传给条件引擎（高级用法） | `condition: { operator: '>', value: 50, attribute: 'temperature' }` |
| 缺省 | 实体非 unknown/unavailable 即为真 | 不写 condition |

> 角标优先级： 配置了 badge 或 badge_entity 时，角标值决定图标/颜色，entity 的状态不再影响图标显示。badge 与 badge_entity 互斥，badge 优先级更高。

### 6.15 晾衣架 (type: clothes_dryer)

控制晾衣架的升降位置，提供可视化的机械仿真拖拽交互、收藏位置快捷按钮和灯光控制。点击按钮弹出晾衣架控制面板。

```yaml
  - type: clothes_dryer
    name: 晾衣架                              # 显示名称（显示在卡片顶部标题栏）
    entity: cover.clothes_dryer               # 晾衣架 cover 实体（用于升降控制）
    light_entity: input_boolean.ce_shi        # 灯光实体（自动插入灯光开关卡片，无需手动添加）
    on_icon: mdi:hanger                       # 开启时图标
    off_icon: mdi:tshirt-crew                 # 关闭时图标
    on_color: '#f58220'                        # 开启时颜色
    off_color: '#74787c'                       # 关闭时颜色
    width: 400px                               # 弹窗宽度
    locker: false                              # 关闭锁定模式，启用拖拽和收藏位置
    reverse: true                              # 位置方向反转（可选，不写=按实体属性自动识别）
    collect_position:                          # 收藏位置快捷按钮（最多3个）
      - name: 经常
        position: 70                           # 目标位置百分比（0=顶部, 100=底部）
      - name: 顶部
        position: 0
      - name: 底部
        position: 100
    card:                                      # 功能开关卡片（灯光开关已自动添加，此处只需配其他功能）
      - type: switch
        entity: switch.dryer_heat
        name: 恒温烘干
        icon: mdi:heart
```

**配置字段说明：**

| 配置项 | 必填 | 类型 | 说明 |
|--------|:----:|------|------|
| `entity` | ✅ | `string` | 晾衣架 cover 实体 ID，使用 `current_position` 属性获取/设置升降位置 |
| `name` | ❌ | `string` | 显示名称，显示在弹窗顶部标题栏，同时显示在线/离线状态标签 |
| `light_entity` | ❌ | `string` | 灯光实体 ID（如 `switch` / `input_boolean`），控制壳体灯光按钮和光晕效果；配置后会自动在功能卡片首位插入灯光开关，无需手动添加 |
| `on_icon` | ❌ | `string` | 开启时按钮图标，默认 `mdi:hanger` |
| `off_icon` | ❌ | `string` | 关闭时按钮图标，默认 `mdi:tshirt-crew` |
| `on_color` | ❌ | `string` | 开启时图标颜色，默认 `#2c7da0` |
| `off_color` | ❌ | `string` | 关闭时图标颜色，默认 `#95a5a6` |
| `width` | ❌ | `string` | 弹窗宽度，默认 `440px` |
| `locker` | ❌ | `boolean` | 锁定模式，默认 `true`。锁定时位置固定 75%，隐藏拖拽手柄和收藏位置按钮，仅通过上升/下降按钮控制电机方向；设为 `false` 时启用拖拽交互和收藏位置快捷按钮 |
| `collect_position` | ❌ | `array` | 收藏位置快捷按钮，最多 3 个，每个含 `name` 和 `position` 字段（仅在 `locker: false` 时显示） |
| `reverse` | ❌ | `boolean` | 位置方向反转，默认 `auto`（不写时自动读取实体 `position_reverse` 属性）。部分设备 `current_position` 与卡片视觉方向相反（HA `100` = 升起 / `0` = 放下）且没有该属性，可设 `reverse: true` 强制反转；也可显式写 `reverse: false` 关掉自动识别。别名 `position_reverse` 同义 |
| `card` | ❌ | `array` | 功能开关卡片列表，使用统一卡片系统渲染，2 列网格布局 |

**交互功能说明：**

1. **机械仿真拖拽**：弹窗中的晾衣架可视化区域支持触摸/鼠标拖拽，直接拖动晾杆到目标位置（`locker: false` 时可用）
2. **升降按钮（一条方向命令 + 位置同步）**：提供上升/停止/下降三个按钮。点「上升/下降」**只发一条**方向命令（`cover.open_cover` / `cover.close_cover`，方向随 `reverse` 翻转），之后每 300ms 读取实体 `current_position` 同步卡片百分比与晾杆位置，到 0/100 自动停止；再点同一方向等同停止。点「停止」立即发 `cover.stop_cover`（设备声明了 STOP 能力时只发这一条，不再补定位命令——旧位置会把它指回端点），并**立即刷新一次显示位置**（同时调 `homeassistant.update_entity` 让集成立刻上报真实位置）。全程不连发定位指令（此前每 18ms 一条、约 55 条/秒，设备会一直「滴滴滴」）
3. **收藏位置**：点一下与「上升/下降」同一套逻辑 —— 只发**一条**方向命令（朝目标方向），之后每 300ms 读实体 `current_position` 同步显示与晾杆动画，到达/越过目标自动 `stop_cover`；当前就在目标附近（±1.5%）时不动电机，位置匹配时按钮高亮（`locker: false` 时显示）
4. **灯光控制**：
   - 壳体右上角的灯光按钮可直接切换 `light_entity` 开关
   - 灯光开启时，壳体下方出现暖黄色倒置梯形光晕照射效果（上窄下宽）
   - 光晕效果实时响应灯光状态变化
5. **功能卡片**：底部 2 列网格展示功能开关卡片；配置了 `light_entity` 时，灯光开关会自动插入首位，无需在 `card` 中手动添加
6. **位置反转适配**：默认自动检测 cover 实体的 `position_reverse` 属性，适配不同品牌晾衣架的正反转逻辑；设备没有该属性时用 `reverse: true` 手动反向（影响位置显示、拖拽、收藏位置与上升/下降方向）
7. **外部状态实时同步**：面板（独立卡片 / 弹窗 / 功能网格）会跟随 `hass` 推送即时同步晾杆位置与标题栏在线圆点 —— 在 HA 前台、物理遥控器或其他卡片里升降后无需刷新页面；拖拽或电机运行中本地值优先，不会被回推覆盖

**`collect_position` 子项字段：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `name` | ✅ | `string` | 按钮显示名称 |
| `position` | ✅ | `number` | 目标位置百分比，0 = 顶部，100 = 底部 |

---
### 三种使用方式

#### 方式一：独立卡片（standalone_type）

直接作为独立设备控制卡片使用，无需按钮系统，完整控制面板直出：

```yaml
type: custom:room-elves-card
standalone_type: clothes_dryer
name: 晾衣架
entity: cover.clothes_dryer
light_entity: input_boolean.ce_shi
locker: false                                           # 关闭锁定启用拖拽
collect_position:
  - name: 经常
    position: 70
  - name: 顶部
    position: 0
  - name: 底部
    position: 100
card:                                                    # func grid 功能开关
  - type: switch
    entity: switch.dryer_heat
    name: 恒温烘干
    icon: mdi:heart
```

#### 方式二：单个按钮（buttons 中使用单设备）

在按钮系统中作为普通按钮使用，点击弹出控制面板，**不显示角标**（单设备）：

```yaml
buttons:
  - type: clothes_dryer
    name: 晾衣架
    entity: cover.clothes_dryer
    light_entity: input_boolean.ce_shi
    locker: false
    collect_position:
      - name: 经常
        position: 70
      - name: 顶部
        position: 0
      - name: 底部
        position: 100
    button:                                              # func grid 功能开关
      - type: switch
        entity: switch.dryer_heat
        name: 恒温烘干
        icon: mdi:heart
```

#### 方式三：聚合多设备（buttons 中使用 card 数组）

多台晾衣架时使用 `card` 数组配置，按钮上**显示角标**（已开启数量），点击弹出聚合列表：

```yaml
buttons:
  - type: clothes_dryer
    name: 晾衣架
    show_badge: true                                     # 显示角标（聚合模式默认开启）
    card:
      - entity: cover.dryer1
        name: 阳台晾衣架
        light_entity: input_boolean.ce_shi
        collect_position:
          - name: 经常
            position: 70
          - name: 顶部
            position: 0
          - name: 底部
            position: 100
        button:                                          # 每个子项独立的 func grid
          - type: switch
            entity: switch.dryer_heat
            name: 恒温烘干
            icon: mdi:heart
      - entity: cover.dryer2
        name: 次卧晾衣架
        light_entity: input_boolean.light2
        locker: true                                     # 锁定模式（仅按钮控制）
        button:
          - type: switch
            entity: switch.balcony_light
            name: 灯光
```

> **角标说明：** 单设备（使用 `entity` 字段）不显示角标；多设备（使用 `card` 数组）时按钮上显示已开启的晾衣架数量。
>
> **配置继承：** `locker`、`light_entity`、`collect_position` 等公共配置可以写在顶层，子项 `card` 内未配置时自动继承顶层值。`locker` 默认 `true`，配置了 `collect_position` 时自动解锁。

### 6.16 NAS 卡片 (type: nas)

NAS 卡片用于展示 HP iLO 服务器的硬盘状态、电源控制和运行状态监控。卡片分为三部分：上部分显示硬盘槽位（拟物 NAS 风格），中部分为电源开关操作区，下部分显示温度和风扇运行状态。

点击按钮弹出 NAS 控制面板，支持通过 `popup_card` 动作打开。

```yaml
  - entity: binary_sensor.192_168_1_223
    type: sensor
    name: Gen8
    on_card_color: true
    icon: mdi:nas
    tap_action:
      action: popup_card
      card:
        type: nas
        name: GEN8
        power_switch: switch.192_168_1_16_server_power_control
        storage_summary: sensor.192_168_1_16_storage_summary
        array_01: binary_sensor.192_168_1_16_array_01
        array_02: binary_sensor.192_168_1_16_array_02
        power_on_time: sensor.192_168_1_16_server_power_on_time
        cpu_temp: sensor.192_168_1_16_02_cpu
        chipset_temp: sensor.192_168_1_16_05_chipset
        sys_temp: sensor.192_168_1_16_12_sys_exhaust
        mem_temp: sensor.192_168_1_16_03_p1_dimm_1_2
        inlet_temp: sensor.192_168_1_16_01_inlet_ambient
        pcie_temp: sensor.192_168_1_16_11_pci_1_zone
        ilo_temp: sensor.192_168_1_16_09_ilo_zone
        fan_speed: sensor.192_168_1_16_fan_1
```

#### 配置字段

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `name` | 否 | `string` | 卡片标题（显示在顶部） |
| `power_switch` | 是 | `string` | 电源开关实体 ID（`switch.xxx`） |
| `storage_summary` | 是 | `string` | 存储汇总实体 ID（`sensor.xxx_storage_summary`） |
| `array_01` | 是 | `string` | 系统盘阵列状态实体 ID（`binary_sensor.xxx_array_01`） |
| `array_02` | 是 | `string` | 数据盘阵列状态实体 ID（`binary_sensor.xxx_array_02`） |
| `power_on_time` | 否 | `string` | 开机时长实体 ID（`sensor.xxx_server_power_on_time`） |
| `cpu_temp` | 否 | `string` | CPU 温度实体 ID |
| `chipset_temp` | 否 | `string` | 芯片温度实体 ID |
| `sys_temp` | 否 | `string` | 系统温度实体 ID |
| `mem_temp` | 否 | `string` | 内存温度实体 ID |
| `inlet_temp` | 否 | `string` | 进风温度实体 ID |
| `pcie_temp` | 否 | `string` | PCIe 温度实体 ID |
| `ilo_temp` | 否 | `string` | iLO 温度实体 ID |
| `fan_speed` | 否 | `string` | 风扇转速实体 ID |

#### 卡片布局

```
┌─────────────────────────────┐
│           GEN8              │  ← 标题（name 字段）
├─────────────────────────────┤
│ 数据盘阵列  RAID 1/1+0  ...  │  ← 阵列标签 + 状态
│ [Bay1] [Bay2] [Bay3] [Bay4] │  ← 硬盘槽位（拟物风格）
│ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │
│ 系统盘  RAID 0  232 GB      │  ← 系统盘阵列
│ [SSD 232GB  SYSTEM  🟢]     │  ← 系统盘横条
├─────────────────────────────┤
│ 电源控制                     │  ← 操作区标题
│ [🔌] ● 运行中               │  ← 电源开关按钮（点击弹确认对话框）
│       ⏱ 已运行: 66天 1小时   │  ← 开机时长
├─────────────────────────────┤
│ 运行状态                     │  ← 状态区标题
│ CPU 40°C  │ 芯片 60°C       │
│ 系统 49°C │ 内存 42°C       │
│ 进风 28°C │ PCIe 41°C       │
│ iLO 50°C  │ 风扇 19%        │
└─────────────────────────────┘
```

#### 交互说明

- **硬盘槽位**：显示容量和状态指示灯（绿色=正常，红色=异常），点击弹出气泡显示硬盘详细信息（型号、序列号、容量、固件、位置、所属阵列等）
- **电源开关**：点击弹出确认对话框，确认后执行开机/关机操作，状态实时更新
- **运行状态**：4×2 网格显示温度传感器和风扇转速，数据每 30 秒自动刷新
- **阵列标签**：显示 RAID 类型、容量（自动格式化如 `33527 GB → 32.7 TB`）和健康状态

> **依赖说明**：NAS 卡片的数据来源于 [HP iLO 集成](https://github.com/chjspp520/hp_ilo)。使用前需先配置 HP iLO 集成并生成对应实体。开机时长原始值单位为小时，卡片自动格式化为 `X天 X小时`。

### 6.17 情景模式 (type: scene_mode)

情景模式按钮用于一键执行一组预定义的操作（如"离家"关闭所有灯、"回家"打开指定灯），支持气泡选择、直接执行、执行进度展示和状态验证。

点击按钮后弹出气泡列表展示所有情景，点击情景执行对应的操作列表。执行过程中显示实时进度面板，验证每个操作是否成功。

```yaml
  - type: scene_mode
    primary: 情景模式                      # 按钮下方文字
    icon: mdi:tune                         # 按钮图标
    icon_color: "#9e579d"                  # 按钮图标颜色（可选）
    mode: bubble                            # 执行模式：bubble（气泡选择）| direct（直接执行）
    entity: input_text.scene_mode          # （可选）执行历史记录实体
    show_badge: false                       # 是否显示角标
    width: 400px                            # （可选）气泡/进度面板宽度
    fold: false                             # （可选）动作列表是否默认展开
    verify_timeout: 10                      # 验证超时秒数（默认10秒）
    scenes:                                 # 情景列表
      - name: 离家                          # 情景名称
        icon: mdi:home-export-outline       # 情景图标
        icon_color: "#e74c3c"              # 情景图标颜色（可选）
        confirm: true                       # 执行前是否弹出确认对话框
        actions:                            # 操作列表
          - entity: light.bed_light         # 目标实体
            value: "off"                    # 目标状态值
            name: 床头灯                    # 操作名称（显示在进度面板中）
            delay: 3                        # 延时执行秒数（可选）
            service_data:                   # 附加服务数据（可选）
              kelvin: 3000
          - entities:                       # 批量模式（对象格式）：键名为自定义名称，显示在进度面板中
              客厅灯: light.keting_dadeng
              客厅玄关灯: light.keting_xuanguan
              客厅灯带: light.keting_dengdai
            value: "off"
            name: 全屋灯光
      - name: 回家
        icon: mdi:home-import-outline
        icon_color: "#2ecc71"
        confirm: true
        actions:
          - entity: light.bed_light
            value: "on"
            name: 床头灯
            delay: 3
            service_data:
              kelvin: 3000
          - entities:                       # 批量模式（数组格式）：向后兼容
              - light.ciwo_xidingd
              - light.ertongfang_xidin
            value: "on"
            name: 其他灯光
```

#### 顶层配置项

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `type` | ✅ | `string` | — | 固定为 `scene_mode` |
| `primary` | ❌ | `string` | `情景模式` | 按钮下方文字 |
| `icon` | ❌ | `string` | `mdi:tune` | 按钮图标 |
| `icon_color` | ❌ | `string` | `#3498db` | 按钮图标颜色，设置后按钮背景和光晕也会跟随变化 |
| `mode` | ❌ | `string` | `bubble` | 执行模式：`bubble`（气泡选择）/ `direct`（直接执行第一个情景）|
| `entity` | ❌ | `string` | 无 | 执行历史记录实体（需为 `input_text` 类型，详见下方"执行历史"） |
| `show_badge` | ❌ | `boolean` | `true` | 是否显示角标（情景数量） |
| `verify_timeout` | ❌ | `number` | `10` | 执行后验证状态的超时秒数 |
| `width` | ❌ | `string` | `400px` | 气泡选择面板和执行进度面板的宽度（如 `400px`、`500px`），移动端高度不超过 60% |
| `fold` | ❌ | `boolean` | `false` | 动作列表是否默认展开。`true` 时展开所有情景的动作列表，`false` 或不配置时折叠 |
| `scenes` | ✅ | `array` | `[]` | 情景列表 |

#### 执行模式 (mode)

| 模式 | 说明 |
|------|------|
| `bubble` | 点击按钮弹出气泡列表，用户选择情景后执行。多个情景时默认使用此模式 |
| `direct` | 点击按钮直接执行第一个情景，不弹出气泡。适合只有一个情景的场景 |
| 不配置 | 自动判断：只有1个情景时为 `direct`，多个情景时为 `bubble` |

#### scenes 子项配置

每个情景 (scene) 支持以下字段：

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `name` | ✅ | `string` | `情景` | 情景名称（显示在气泡列表和进度面板中） |
| `icon` | ❌ | `string` | `mdi:palette-outline` | 情景图标（显示在气泡列表中） |
| `icon_color` | ❌ | `string` | 无 | 情景图标颜色，设置后图标背景和阴影也会跟随变化。未配置时使用默认蓝色 |
| `confirm` | ❌ | `boolean` | `false` | 执行前是否弹出确认对话框 |
| `fold` | ❌ | `boolean` | 顶层 `fold` 值 | 动作列表是否默认展开。`true` 时展开，`false` 时折叠；未配置时回退到顶层 `fold` 设置 |
| `actions` | ✅ | `array` | `[]` | 操作列表 |

#### actions 子项配置

每个操作 (action) 支持两种模式：

**单实体模式**：控制一个实体

```yaml
actions:
  - entity: light.bed_light         # 目标实体ID
    value: "off"                     # 目标状态值（如 "on"、"off"、"25" 等）
    name: 床头灯                     # 操作名称（显示在进度面板中）
    delay: 3                         # 延时执行秒数（可选，默认0=立即执行）
    service_data:                    # 附加服务数据（可选，传递给 HA 服务调用）
      kelvin: 3000
```

**批量模式**：将多个实体设为同一状态

`entities` 支持三种格式：

**格式一：对象格式（推荐）** — 键名为自定义名称，在进度面板中替代 entity ID 显示

```yaml
actions:
  - entities:                        # 键名=自定义名称，键值=实体ID
      客厅灯: light.keting_dadeng
      客厅玄关灯: light.keting_xuanguan
      客厅灯带: light.keting_dengdai
    value: "off"                     # 所有实体的目标状态值
    name: 全屋灯光                   # 操作分组名称
```

**格式二：列表式键值对格式** — YAML 语法糖，效果与对象格式相同

```yaml
actions:
  - entities:
      - 客厅灯: light.keting_dadeng
      - 客厅玄关灯: light.keting_xuanguan
      - 客厅灯带: light.keting_dengdai
    value: "off"
    name: 全屋灯光
```

**格式三：数组格式（向后兼容）** — 纯实体ID数组，进度面板中显示 entity ID 或 HA friendly_name

```yaml
actions:
  - entities:                        # 纯实体ID数组
      - light.ciwo_xidingd
      - light.ertongfang_xidin
    value: "off"
    name: 其他灯光                   # 操作名称
    delay: 0                         # 延时秒数（可选）
```

**进度面板显示效果**：

| entities 格式 | 进度面板中的名称显示 | 示例 |
|--------|------|------|
| 对象格式 / 列表式键值对 | 使用键名（自定义名称） | `客厅灯` `on→off` `成功` |
| 数组格式 | 使用 HA `friendly_name`，无则显示 entity ID | `light.keting_dadeng` `on→off` `成功` |
| 单实体模式（`entity`） | 使用 `name` > `friendly_name` > entity ID | `床头灯` `on→off` `成功` |

> 进度面板中每项显示格式为：**名称** + **当前状态→目标状态** + **执行结果**。例如 `客厅灯 on→off 成功`、`客厅灯 on→off 已是关闭，无需执行`。

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ❌* | `string` | 无 | 单实体模式的目标实体ID（与 `entities` 二选一） |
| `entities` | ❌* | `array` / `object` | 无 | 批量模式的实体列表，支持三种格式（见上方） |
| `value` | ✅ | `string` | 无 | 目标状态值（如 `"on"`、`"off"`、`"25"` 等） |
| `name` | ❌ | `string` | 无 | 操作名称（显示在进度面板中，批量模式下为分组名称） |
| `delay` | ❌ | `number` | `0` | 延时执行秒数，0 = 立即执行 |
| `service_data` | ❌ | `object` | 无 | 附加服务数据（传递给 HA 服务调用，如 `kelvin`、`brightness` 等） |
| `select` | ❌ | `boolean` | `true` | 动作复选框是否默认选中。`false` 时该动作默认不勾选（执行时跳过），不配置时默认选中 |
| `confirm_entity` | ❌ | `string` | 无 | 确认实体ID。用于设备本身无法通过自己的 state 确认执行结果的场景，卡片将轮询此实体的状态来判断执行是否成功 |
| `confirm_value` | ❌ | `string` | 同 `value` | 确认实体的期望状态值，支持比较运算符前缀（`>`, `<`, `>=`, `<=`, `!=`），如 `">10"` 表示功率大于 10 即视为成功 |
| `confirm_time` | ❌ | `number` | 无 | 执行后等待确认的秒数。服务调用成功后，等待指定秒数再开始验证 `confirm_entity` 的状态 |

> *`entity` 和 `entities` 至少配置一个。对象格式 `entities` 的键名优先级高于 `name`，会作为每个实体在进度面板中的独立显示名称。

**`select` 参数详解**：

每个 action 在气泡列表展开后会显示为复选框，用户可以取消勾选不想执行的动作。`select` 控制该复选框的默认状态：

- `select: true`（默认）— 复选框默认勾选，执行情景时会执行该动作
- `select: false` — 复选框默认不勾选，执行情景时跳过该动作（用户可手动勾选）

适用场景：某些动作是可选的（如"关闭空调"情景中，"关闭加湿器"是可选动作），设为 `select: false` 后默认不执行，但用户仍可在展开面板中勾选执行。

```yaml
scenes:
  - name: 离家
    actions:
      - entity: light.bed_light
        value: "off"
        name: 床头灯
        select: true               # 默认勾选（或不配置，效果相同）
      - entity: fan.bedroom
        value: "off"
        name: 卧室风扇
        select: false              # 默认不勾选，执行时跳过，用户可手动勾选
      - entity: vacuum.roborock
        value: "start"
        name: 扫地机
        select: false              # 默认不执行，离家时可选清扫
```

> `select` 仅控制复选框的**默认状态**，用户仍可在气泡展开面板中手动勾选/取消。如果情景配置了 `mode: direct`（直接执行，不弹出气泡），`select: false` 的动作将始终被跳过。

#### 确认实体配置（confirm_entity / confirm_value / confirm_time）

某些设备执行操作后无法通过自身的 state 来确认是否执行成功（例如使用 WOL 唤醒电脑的 `switch`，`switch` 本身变为 `on` 但电脑还在启动中），此时可以用另一个实体的状态作为判断依据。

**配置示例 — WOL 唤醒电脑**：

```yaml
actions:
  - entity: switch.chen_mo_fang_jian_dian_nao_wolkai_ji
    value: "on"
    name: WOL唤醒
    confirm_entity: sensor.iot_power             # 用功率传感器确认电脑是否已启动
    confirm_value: ">10"                         # 功率 > 10W 视为启动成功
    confirm_time: 5                              # 执行后等待 5 秒再开始验证
```

**执行与验证流程**：

1. 调用 `switch.turn_on` 发送唤醒包
2. 显示 `已发送`
3. 等待 `confirm_time: 5` 秒（进度面板显示 `等待5秒后确认`）
4. 进入验证阶段，轮询 `sensor.iot_power` 的状态值
5. 当功率 `> 10` 时验证通过（显示 `✅ 成功`）；超时未达到则标记失败

**`confirm_value` 支持的比较运算符**：

| 运算符 | 示例 | 说明 |
|--------|------|------|
| 无 | `"on"` | 精确字符串匹配（默认行为） |
| `>` | `">10"` | 数值大于 |
| `<` | `"<500"` | 数值小于 |
| `>=` | `">=0.5"` | 数值大于等于 |
| `<=` | `"<=100"` | 数值小于等于 |
| `!=` | `"!=unknown"` | 不等于 |

**`confirm_time` 不配置时**：依赖 scene 层 `verify_timeout` 进行验证。`confirm_time` 仅在需要"执行后等待设备启动/响应"时使用。

**`confirm_value` 不配置时**：默认使用 action 的 `value` 值作为期望值。

**进度面板显示效果**：当配置了 `confirm_entity` 时，状态转换文本改为显示确认实体信息：

| 场景 | 进度面板显示 |
|------|-------------|
| 无 confirm_entity | `床头灯` `on→off` `成功` |
| 有 confirm_entity | `WOL唤醒` `电功率: >10` `等待5秒后确认` → `WOL唤醒` `电功率: >10` `成功` |

#### 支持的实体类型与服务自动推断

卡片会根据实体 ID 的域前缀（如 `light.`、`climate.`）自动推断应调用的 HA 服务，无需手动指定服务名。以下是各实体类型支持的 `value` 值与对应服务：

| 实体域 | `value` 值 | 调用服务 | 说明 |
|--------|-----------|----------|------|
| `light` | `"on"` / `"true"` | `light.turn_on` | 开灯，`service_data` 可传 `brightness`、`kelvin`、`color_temp`、`effect` 等 |
| `light` | `"off"` / `"false"` | `light.turn_off` | 关灯，自动清理 `kelvin`/`brightness` 等参数 |
| `light` | 其他值 | `light.turn_on` | 作为亮度等参数 |
| `switch` / `input_boolean` | `"on"` / `"off"` | `turn_on` / `turn_off` | 开关切换 |
| `climate` | `"off"` | `climate.set_hvac_mode` | 关闭空调（`hvac_mode: "off"`），自动清理 `temperature`/`fan_mode` |
| `climate` | `"on"` / `"true"` | `climate.turn_on` | 开启空调 |
| `climate` | 数值（如 `"26"`） | `climate.set_temperature` | 设置温度，`temperature` 取数值 |
| `climate` | 模式字符串（如 `"cool"`、`"heat"`）+ `service_data` 含 `temperature` | `climate.set_temperature` | 同时设置 `hvac_mode` + `temperature` |
| `climate` | 模式字符串（无 `temperature`） | `climate.set_hvac_mode` | 仅设置模式 |
| `climate` | `service_data` 含 `fan_mode` | 额外调用 `climate.set_fan_mode` | `fan_mode` 自动拆分为独立服务调用；关闭模式（`value: "off"`）时跳过风速设置 |
| `cover` | `"open"` | `cover.open_cover` | 打开遮盖 |
| `cover` | `"closed"` / `"close"` | `cover.close_cover` | 关闭遮盖 |
| `cover` | 数值 | `cover.set_cover_position` | 设置位置百分比 |
| `fan` | `"on"` / `"off"` | `fan.turn_on` / `fan.turn_off` | 风扇开关 |
| `fan` | 数值 | `fan.set_percentage` | 设置风速百分比 |
| `media_player` | `"on"` / `"off"` | `media_player.turn_on` / `turn_off` | 媒体设备开关；toggle 时 `idle`/`paused`/`standby` 视为开启状态 |
| `media_player` | `"play"` / `"pause"` | `media_play` / `media_pause` | 播放/暂停 |
| `button` / `input_button` | 任意 | `press` | 按压按钮 |
| `input_select` | 任意 | `input_select.select_option` | `option = value` |
| `select` | 任意 | `select.select_option` | `option = value` |
| `input_number` | 数值 | `input_number.set_value` | 设置数值 |
| `automation` | `"on"` / `"off"` | `automation.turn_on` / `turn_off` | 自动化开关 |
| `automation` | 其他 | `automation.trigger` | 触发自动化 |
| `vacuum` | `"on"` / `"start"` / `"clean"` | `vacuum.start` | 开始清扫 |
| `vacuum` | `"off"` / `"return"` / `"home"` / `"dock"` | `vacuum.return_to_base` | 返回充电 |
| `vacuum` | `"stop"` | `vacuum.stop` | 停止清扫 |
| `vacuum` | `"pause"` | `vacuum.pause` | 暂停清扫 |
| `script` | 任意 | `script.{实体名}` | 执行脚本 |
| `lock` | `"locked"` / `"lock"` | `lock.lock` | 上锁 |
| `lock` | 其他 | `lock.unlock` | 解锁 |
| 其他域 | `"on"` / `"off"` | `turn_on` / `turn_off` | 通用开关 |
| 其他域 | 其他 | `homeassistant.turn_on` | 通用回退 |

**media_player 状态判定说明**：

`media_player` 实体有多种状态（`on`/`off`/`idle`/`paused`/`playing`/`standby` 等），卡片对其做了统一处理：

| 场景 | 判定逻辑 | 说明 |
|------|---------|------|
| toggle 切换 | `off`/`unavailable`/`unknown` 之外的状态均视为"开启" | `idle`（空闲）、`paused`（暂停）、`playing`（播放中）、`standby`（待机）都算开启，toggle 时会执行 `turn_off` |
| 验证 `value: "on"` | 状态为 `on`/`playing`/`idle`/`paused` 之一即视为成功 | `standby` 不视为开启 |
| 验证 `value: "off"` | 状态为 `off` 或 `standby` 均视为成功 | 部分设备（如 Sonos、Chromecast）`turn_off` 后状态变为 `standby` 而非 `off`，同样判定为关闭成功 |

**空调（climate）配置示例**：

```yaml
actions:
  # 制冷模式 + 温度 + 风速（自动拆分为3次服务调用）
  - entity: climate.xiaomi_air_conditioner
    value: cool
    service_data:
      temperature: "26"        # → climate.set_temperature { hvac_mode: "cool", temperature: 26 }
      fan_mode: level6          # → climate.set_fan_mode { fan_mode: "level6" }

  # 仅设置温度
  - entity: climate.xiaomi_air_conditioner
    value: "26"                 # → climate.set_temperature { temperature: 26 }

  # 仅设置模式
  - entity: climate.xiaomi_air_conditioner
    value: heat                 # → climate.set_hvac_mode { hvac_mode: "heat" }

  # 选择器实体
  - entity: select.ac_mode
    value: 制冷                 # → select.select_option { option: "制冷" }

  # 关闭空调（使用 set_hvac_mode 而非 turn_off，自动清理 temperature/fan_mode）
  - entity: climate.xiaomi_air_conditioner
    value: "off"                # → climate.set_hvac_mode { hvac_mode: "off" }
    # 即使 service_data 包含 temperature/fan_mode，关闭时也会自动清理，不会报错
```

**透传模式**：如果 `service_data` 中包含 `_service` 字段，则跳过自动推断，直接调用指定服务：

```yaml
actions:
  - entity: climate.xiaomi_air_conditioner
    value: cool
    service_data:
      _service: climate.set_hvac_mode    # 强制使用此服务
      # 其他字段原样传递
```

#### 执行流程

1. **用户点击按钮** → 根据模式弹出气泡列表或直接执行
2. **展开动作列表** → 点击情景右侧的展开按钮（▼），可查看该情景包含的所有动作（actions），以复选框形式展示
3. **取消勾选动作** → 取消勾选不想执行的动作，仅执行剩余勾选的动作
4. **选择情景** → 如果配置了 `confirm: true`，先弹出确认对话框
5. **逐个执行操作** → 仅执行勾选的 actions，按顺序执行，支持 `delay` 延时
6. **状态验证** → 所有服务调用完成后，轮询检查实体是否达到目标状态（超时由 `verify_timeout` 控制）
7. **显示结果** → 进度面板中每个操作显示：名称 + 状态转换 + 结果

**进度面板显示格式**：每项显示为 `名称 当前状态→目标状态 结果`

| 阶段 | 显示示例 |
|------|---------|
| 等待中 | `客厅灯` `on→off` `等待中` |
| 执行中 | `客厅灯` `on→off` `执行中` |
| 已发送 | `客厅灯` `on→off` `已发送` |
| 验证成功 | `客厅灯` `on→off` `成功` |
| 验证失败 | `客厅灯` `on→off` `未达到` |
| 调用失败 | `客厅灯` `on→off` `失败` |
| 已是目标状态 | `客厅灯` `off→off` `已是关闭，无需执行` |

> **动作选择**：气泡列表中每个情景右侧有一个展开按钮（▼），点击后展开该情景的动作列表。每个动作以复选框形式显示（默认全选），取消勾选后执行情景时会跳过该动作。批量模式（`entities`）的动作取消后，该批次所有实体都会被跳过。

> **设备展开**：包含多个设备的动作（`entities` 数组/对象）左侧会显示一个展开按钮（▸），点击后在该动作下方展开显示所有设备名称，再次点击折叠。这有助于查看批量操作中包含的具体设备。

> **按房间自动分组**：当 `entities` 的键名（自定义名称）中包含下划线 `_` 时，卡片会自动按下划线前的部分作为房间名进行分组显示。下划线前为房间名，下划线后为设备名。例如键名 `客厅_大灯` 会显示为房间标签"客厅"下的设备"大灯"。不含下划线的键名保持原始平铺显示（向后兼容）。

```yaml
# 使用下划线命名自动按房间分组
actions:
  - entities:
      客厅_大灯: light.keting_dadeng
      客厅_玄关灯: light.keting_xuanguan
      客厅_灯带: light.keting_dengdai
      厨房_大灯: light.chufang
      主卧_吸顶灯: light.zhuwo_xidingdeng
      主卧_床头南灯: light.zhuwo_chuangtounan
    value: "off"
    name: 全屋灯光
```

展开后效果示意：

```
客厅  大灯  玄关灯  灯带
厨房  大灯
主卧  吸顶灯  床头南灯
```

> 无下划线的键名（如 `大厅灯`、`走廊`）不会分组，保持原始平铺显示，与旧配置完全兼容。

#### 执行历史记录 (entity)

配置 `entity` 后（推荐使用 `input_text` 类型实体），每次执行完成会自动将执行模式、时间和结果写入该实体，并在气泡列表中显示上次执行信息。

**实体数据格式**（JSON 存储在 `input_text` 的 state 中）：

```json
{
  "离家": { "time": "2026-05-20T10:30:00.000Z", "result": "success", "detail": "全部执行成功" },
  "回家": { "time": "2026-05-20T08:00:00.000Z", "result": "partial", "detail": "成功2项,失败1项" }
}
```

**气泡列表中每个情景项额外显示**：

- 上次执行时间（如"今天 10:30"、"昨天 08:00"、"5/19 18:00"）
- 上次执行结果标签（绿色=全部成功，橙色=部分失败，红色=全部失败）

**Home Assistant 中创建记录实体的方法**：

在 `configuration.yaml` 中添加：

```yaml
input_text:
  scene_mode:
    name: 情景模式执行历史
    max: 255
```

> 不配置 `entity` 时，情景模式功能完全正常，只是不会记录和显示执行历史。

### 6.18 窗帘 (type: curtain)

控制电动窗帘的开合、层级切换和开合模式。支持单层/双层窗帘、百分比开合控制、同向/对开模式。

---
### 三种使用方式

#### 方式一：独立卡片（standalone_type）

直接作为独立设备控制卡片使用，完整控制面板直出：

```yaml
type: custom:room-elves-card
standalone_type: curtain
name: 客厅窗帘
fabric_entity: cover.living_room_fabric
sheer_entity: cover.living_room_sheer
layer_mode: double
open_mode: double
background_image: /local/window_bg_1.png
width: 460px
```

#### 方式二：单个按钮（buttons 中使用单设备）

在按钮系统中作为普通按钮使用，点击弹出控制面板，**不显示角标**（单设备）：

```yaml
buttons:
  - type: curtain
    name: 客厅窗帘
    entity: cover.living_curtain                # 窗帘 cover 实体
    fabric_entity: cover.living_curtain         # 布料帘实体（双层帘时指定）
    sheer_entity: cover.living_curtain_bc       # 纱帘实体（双层帘时指定）
    layer_mode: double                          # 层级模式：single | double
    open_mode: double                           # 开合方式：double（对开）| single（同向）
    on_icon: mdi:curtain-open
    off_icon: mdi:curtain
    on_color: '#3498db'
    off_color: '#95a5a6'
    width: 560px
    popup_position: center
    background_image: /local/window_bg_1.png
```

#### 方式三：聚合多设备（buttons 中使用 card 数组）

多台窗帘时使用 `card` 数组配置，按钮上**显示角标**（已开启数量），点击弹出聚合列表。**PC 端一行 2 个，移动端一行 1 个**：

```yaml
buttons:
  - type: curtain
    name: 全屋窗帘
    show_badge: true
    on_icon: mdi:curtain-open
    off_icon: mdi:curtain
    on_color: '#d4b896'
    off_color: '#7f8c8d'
    show_open: true                             # 可选，仅显示已打开的窗帘
    layer_mode: double                          # 全局默认层级模式（子项未配时使用）
    open_mode: double                           # 全局默认开合方式（子项未配时使用）
    background_image: /local/room.jpg           # 全局默认背景图
    width: 700px
    card:
      - name: 客厅窗帘
        height: 400px
        fabric_entity: cover.ke_ting_bu_lian
        sheer_entity: cover.ke_ting_sha_lian
        layer_mode: double
      - name: 卧室窗帘
        fabric_entity: cover.wo_shi_bu_lian
        layer_mode: single
        open_mode: single-left
      - name: 书房窗帘
        fabric_entity: cover.shu_fang_bu_lian
        background_image: /local/study_bg.png
```

> **角标说明：** 单设备（使用 `entity` / `fabric_entity` 字段）不显示角标；多设备（使用 `card` 数组）时按钮上显示已开启的窗帘数量（布帘位置 > 10% 视为开启）。
>
> **配置继承：** `layer_mode`、`open_mode`、`background_image` 等公共配置可以写在顶层，子项 `card` 内未配置时自动继承顶层值。

**配置字段说明：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `type` | ✅ | `string` | — | 固定为 `curtain` |
| `entity` | ❌ | `string` | 无 | 窗帘 cover 实体 ID，用于开合控制 |
| `name` | ❌ | `string` | `窗帘` | 显示名称 |
| `fabric_entity` | ❌ | `string` | 同 `entity` | 布料帘实体 ID（双层模式时指定不同的布料帘实体） |
| `sheer_entity` | ❌ | `string` | 无 | 纱帘实体 ID（双层模式时需要） |
| `layer_mode` | ❌ | `string` | `double` | 层级模式：`single`（单层）或 `double`（双层） |
| `open_mode` | ❌ | `string` | `double` | 开合方式：`double`（对开，左右分开）或 `single`（同向，单侧拉开） |
| `on_icon` | ❌ | `string` | `mdi:curtain-open` | 开启时图标 |
| `off_icon` | ❌ | `string` | `mdi:curtain` | 关闭时图标 |
| `on_color` | ❌ | `string` | `#d4b896` | 开启时图标颜色 |
| `off_color` | ❌ | `string` | `#7f8c8d` | 关闭时图标颜色 |
| `width` | ❌ | `string` | `560px` | 弹窗宽度 |
| `popup_position` | ❌ | `string` | `center` | 弹窗位置 |
| `background_image` | ❌ | `string` | 无 | 弹窗背景图片 URL |
| `show_open` | ❌ | `boolean` | `false` | 聚合模式：设为 `true` 时仅显示已打开的窗帘 |
| `card` | ❌ | `array` | `[]` | 聚合模式：窗帘列表，每个子项为一个窗帘配置 |

**card 子项配置字段：**

| 配置项 | 必填 | 类型 | 说明 |
|--------|:----:|------|------|
| `name` | ❌ | `string` | 窗帘名称，显示在控制面板顶部 |
| `fabric_entity` | ❌ | `string` | 布帘实体 ID，也可用 `entity` 字段 |
| `sheer_entity` | ❌ | `string` | 纱帘实体 ID（双层模式时需要） |
| `height` | ❌ | `string` | 自定义该窗帘舞台高度，如 `400px` |
| `layer_mode` | ❌ | `string` | 层级模式，覆盖全局默认 |
| `open_mode` | ❌ | `string` | 开合方式，覆盖全局默认 |
| `background_image` | ❌ | `string` | 背景图片，覆盖全局默认 |

**聚合弹窗响应式布局：**

| 设备 | 布局 | 说明 |
|------|------|------|
| PC / 平板 (≥768px) | 一行 2 个 | 弹窗自动扩展宽度，双列网格 |
| 移动端 (<768px) | 一行 1 个 | 单列布局，垂直滚动 |

**角标说明：** 单个窗帘不显示角标；多台窗帘（使用 `card` 数组）时按钮上显示已开启窗帘的数量（布帘位置 > `CURTAIN_OPEN_THRESHOLD`% 视为开启）。所有窗帘关闭时角标不显示。

### 6.19 风扇 (type: fan)

用于控制风扇设备，支持风速调节和摇头控制。

```yaml
  - type: fan
    entity: fan.living_room                  # 风扇实体 ID
    name: 风扇
    icon: mdi:fan
    on_color: '#3498db'
    off_color: '#95a5a6'
```

风扇按钮显示当前运行状态，点击切换开关。在弹窗中可调节风速百分比、切换摇头模式等。



### 6.20 快捷操作 (type: action)

快捷操作卡片将情景模式的功能集成到统一卡片系统中，可在自由布局弹窗、title_entities 等任意支持 `card_config` 的位置使用。点击卡片弹出与 `scene_mode` 相同的情景模式气泡，支持多步骤快捷操作、执行进度展示和状态验证。

**与 `scene_mode` 按钮的区别：** `scene_mode` 是头部模式下的专属按钮类型，`action` 是统一卡片系统的一种卡片类型，可在弹窗、title_entities 等任意位置使用，功能完全相同。

```yaml
  - type: action
    name: 情景模式                        # 显示名称
    icon: mdi:palette                     # 图标
    icon_color: "#3498db"                 # 图标颜色
    description: 3 个模式                  # 描述文本（不配则自动显示"N 个模式"）
    scene_mode: bubble                     # 执行模式：bubble（气泡选择）| direct（直接执行）
    scenes:                                # 情景列表（配置与 scene_mode 完全一致）
      - name: 回家模式
        confirm: true
        actions:
          - entity: light.living_room
            value: "on"
            delay: 2
          - entity: climate.ac
            service_data:
              temperature: 26
      - name: 离家模式
        actions:
          - entities:
              客厅灯: light.keting_dadeng
              卧室灯: light.bedroom
            value: "off"
```

**配置项说明：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `type` | ✅ | `string` | — | 固定为 `action` |
| `name` | ❌ | `string` | `快捷操作` | 显示名称 |
| `icon` | ❌ | `string` | `mdi:palette` | 图标 |
| `icon_color` | ❌ | `string` | `#3498db` | 图标颜色 |
| `description` | ❌ | `string` | 自动 | 描述文本，不配置时自动显示"N 个模式" |
| `scenes` | ✅ | `array` | `[]` | 情景列表，配置格式与 `scene_mode`（6.17 节）完全一致 |
| `scene_mode` | ❌ | `string` | 自动 | 执行模式：`bubble`（气泡选择）/ `direct`（直接执行），不配置时自动判断 |
| `fold` | ❌ | `boolean` | `false` | 动作列表是否默认展开 |
| `verify_timeout` | ❌ | `number` | `10` | 执行后验证状态的超时秒数 |

> `scenes` 的完整配置格式（actions 的 entity/entities/value/service_data/delay/confirm/select 等）与 6.17 节情景模式完全一致，此处不再重复。

**在自由布局弹窗中使用：**

```yaml
cards:
  - row: 1
    per_line: 1
    items:
      - type: action
        name: 快捷操作
        icon: mdi:palette
        scenes:
          - name: 回家模式
            actions:
              - entity: light.living_room
                value: "on"
```

**在 title_entities 中使用：**

```yaml
title_entities:
  - type: action
    name: 情景
    icon: mdi:palette
    scenes:
      - name: 回家
        actions:
          - entity: light.living_room
            value: "on"
```

---

无论哪种按钮类型，都可以配置以下通用字段：

| 配置项 | 说明 | 示例 |
|--------|------|------|
| `entity` | 绑定的实体ID | `light.living` |
| `name` | 显示名称 | `客厅灯` |
| `icon` | 默认图标 | `mdi:lightbulb` |
| `on_icon` | 开启时图标 | `mdi:lightbulb-on` |
| `off_icon` | 关闭时图标 | `mdi:lightbulb-off` |
| `on_color` | 开启时颜色 | `#2ecc71` |
| `off_color` | 关闭时颜色 | `#e74c3c` |
| `icon_animation` | **自定义图标动画**（不覆盖空调/动态图标）。优先级高于顶层 `icon_animation`。可选：`shake` / `rotate` / `blink` / `breathe` / `jump` / `random-move` / `none` | `breathe` |
| `show_badge` | 显示角标数字 | `true` |
| `badge_entity` | 指定实体值作为角标 | `sensor.count` |
| `badge` | 条件角标数组（独立按钮专用） | 见6.14节 |
| `confirm` | 点击是否需要确认 | `true` |
| `primary` | 按钮下方的文字，支持模板。需完整 Jinja2 时配合 `server_explain: true` | `已开启3个` |
| `server_explain` | `true` 时 primary 模板走 HA 后端渲染（仅限 expand 等 HA 独有函数） | `true` |
| `tap_action` | 点击动作（见下文） | 见下 |
| `width` | 弹窗宽度（像素） | `400` |
| `per_line` | 弹窗每行按钮数 | `3` |
| `row_column` | 网格位置（head按钮/弹窗item跨行跨列） | `'1,2-3'` |
| `close_time` | 弹窗自动关闭倒计时（秒），0=不自动关闭 | `300` |
| `show_duration` | 显示距上次变化的持续时长 | `true` |
| `popup_position` | 弹窗位置 | `top`, `bottom`, `left`, `right` |
| `tabs_by` | 聚合弹窗按字段分组（如 `room` / `group`） | `room` |
| `group_lights_by_room` | 灯光弹窗中按room字段分组显示设备 | `true` |

**点击动作（tap_action）详解：**

```yaml
tap_action:
  action: toggle                     # 切换开关
```

可用的 action 值：

- **`toggle`** — 切换设备开关（最常用），支持 `entities` 多实体批量切换
- **`set_value`** — 设置实体目标值，自动推断 HA 服务（最灵活）
  ```yaml
  # 单实体：设置空调温度
  tap_action:
    action: set_value
    value: "on"
    service_data:
      temperature: "26"
      fan_mode: level6

  # 多实体：一键关闭多个灯
  tap_action:
    action: set_value
    entities:
      - light.living_ceiling
      - light.living_led
    value: "off"
  ```
  > `set_value` 桥接情景模式的服务自动推断引擎（`_inferSceneService`），根据实体域自动调用对应服务（如 `light.turn_on`、`climate.set_temperature` 等），无需手动指定服务名。支持所有实体类型，详见 6.16 节"支持的实体类型与服务自动推断"表格。

- **`toggle-all`** — 切换分组中所有设备的开关
- **`more-info`** — 弹出 HA 自带的详细信息弹窗
  ```yaml
  tap_action:
    action: more-info
  ```
- **`navigate`** — 跳转到另一个页面
  ```yaml
  tap_action:
    action: navigate
    navigation_path: /lovelace/bedroom
  ```
- **`call-service`** — 调用 HA 的服务
  ```yaml
  tap_action:
    action: call-service
    service: light.turn_on
    service_data:
      entity_id: light.living
      brightness: 255
  ```
- **`popup_card`** — 弹出一个自定义内容弹窗（最强大）
  ```yaml
  tap_action:
    action: popup_card
    card:                                # 弹窗中的内容
      - type: sensor
        entity: sensor.temperature
        name: 温度
      - type: switch
        entity: switch.plug
    popup_position: top
    width: 350
  ```
- **`none`** — 不执行任何操作

**`toggle` 和 `set_value` 的多实体批量操作：**

`tap_action` 中支持 `entities` 数组字段，用于对多个实体执行相同操作。与 `entity`（单实体）二选一：

```yaml
# 多实体 toggle
tap_action:
  action: toggle
  entities:
    - light.keting_dadeng
    - light.keting_xuanguan

# 多实体 set_value
tap_action:
  action: set_value
  entities:
    - light.keting_dadeng
    - light.keting_xuanguan
  value: "off"
```

> 当同时配置了 `entity` 和 `entities` 时，`entities` 优先。

### 自动弹窗（auto_open_entity）

当 `tap_action` 配置了 `call-service` 且服务为 `show_free_layout_popup` 时，可以通过 `auto_open_entity` 参数实现**自动弹出弹窗**——当指定实体变为 on 时，自动打开该按钮的弹窗，无需用户手动点击。

```yaml
buttons:
  - name: 晾衣架
    entity: switch.giot_cn_1126348886_v64ksm_on_p_4_1
    on_icon: mdi:hanger
    off_icon: mdi:hanger
    on_color: "#f58220"
    off_color: "#74787c"
    tap_action:
      action: call-service
      service: modern_room_card.show_free_layout_popup
      popup_position: clone_button_top
      auto_open_entity: input_boolean.ce_shi    # 当此实体为 on 时自动弹出
      service_data:
        title: 晾衣架
        width: 360px
        cards:
          - row: 1
            per_line: 1
            items:
              - type: clothes_dryer
                entity: cover.clothes_dryer
                name: 晾衣架
```

**行为规则：**

| 场景 | 行为 |
|------|------|
| 页面加载时 `auto_open_entity` 已为 on | ✅ 自动弹出弹窗 |
| 运行中 `auto_open_entity` 从 off→on | ✅ 自动弹出弹窗 |
| 运行中 `auto_open_entity` 从 on→off | ❌ 不关闭弹窗（默认），配置 `auto_close: true` 可自动关闭 |
| 用户手动关闭弹窗后，`auto_open_entity` 仍为 on | ❌ 本轮 on 周期内不再自动弹出 |
| `auto_open_entity` 变为 off 后再次变为 on | ✅ 新一轮 on 周期，可再次自动弹出 |

**可选参数：**

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `auto_open_entity` | `string` | 无 | （必填）触发自动弹窗的实体 ID，状态为 on 时弹出 |
| `auto_open_delay` | `number` | `0` | 延迟弹出时间（毫秒）。entity 变为 on 后等待指定时间再弹出，避免短暂触发时立即弹出。延迟期间如果 entity 变回 off 则取消弹出 |
| `auto_close` | `boolean` | `false` | entity 变为 off 时是否自动关闭弹窗。默认 false（不关闭），设为 true 则 entity 变 off 时自动关闭 |

**`auto_open_delay` 延迟弹出示例：**

```yaml
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  auto_open_entity: binary_sensor.door_open
  auto_open_delay: 2000          # 门打开后等2秒再弹出（避免短暂开门误触发）
  popup_position: clone_button_top
  service_data:
    title: 门口监控
    cards: [...]
```

**`auto_close` 自动关闭示例：**

```yaml
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  auto_open_entity: input_boolean.show_panel
  auto_close: true               # 开关关闭时弹窗自动关闭
  popup_position: clone_button_top
  service_data:
    title: 控制面板
    cards: [...]
```

**使用场景举例：**

- 用 `input_boolean` 作为"展示模式"开关，开启后自动弹出设备详情
- 用某个传感器的自动化联动开关，当设备异常时自动弹出告警弹窗
- 用定时器实体，在特定时间段自动弹出控制面板
- 用 `auto_open_delay` 避免传感器短暂触发时误弹窗（如人体传感器经过而非停留）
- 用 `auto_close` 配合临时开关，实现"展示后自动收回"的效果

**注意事项：**

- `auto_open_entity` 仅在 `action: call-service` + `show_free_layout_popup` 服务下生效
- `auto_open_entity`、`auto_open_delay`、`auto_close` 均放在 `tap_action` 层级（与 `action`、`service_data` 同级），而非 `service_data` 内部
- 弹窗位置由 `popup_position` 控制，与手动点击时一致（如 `clone_button_top` 会定位在按钮上方）
- 多个按钮可以配置不同的 `auto_open_entity`，各自独立触发
- `auto_open_entity` 实体类型建议使用 `input_boolean`、`switch`、`binary_sensor` 等二态实体

### 6.21 按钮组 (type: button_group)

将多个小按钮组合在一起，以 Windows 选项卡样式排列在同一个容器中，适合将同一区域的设备（如同一个房间的灯、同一类设备）集中管理。

```yaml
buttons:
  - type: button_group
    direction: horizontal              # （可选）排列方向：horizontal / vertical，默认 horizontal
    name: 灯光控制                     # （可选）组标签
    on_color: '#3498db'                # （可选）子按钮开启状态默认颜色
    off_color: '#95a5a6'               # （可选）子按钮关闭状态默认颜色
    icon_size: 16                      # （可选）图标大小 px，默认 16
    show_name: true                    # （可选）是否显示按钮名称，默认 true
    buttons:                           # 子按钮列表（必填）
      - entity: light.living_room
        name: 客厅灯
        icon: mdi:ceiling-light
        on_icon: mdi:lightbulb-on      # 可选，开启时图标
        off_icon: mdi:lightbulb-off    # 可选，关闭时图标
        on_color: '#f1c40f'            # 可选，覆盖默认 on_color
        off_color: '#95a5a6'           # 可选，覆盖默认 off_color
        icon_size: 18                  # 可选，覆盖组的 icon_size
        show_name: true                # 可选，覆盖组的 show_name
        confirm: true                  # 可选，点击前弹出确认对话框
        tap_action:
          action: toggle               # 支持 toggle / set_value / more-info / navigate / call-service / popup_card / card / none
        badge:                         # 可选，条件角标数组
          - entity: binary_sensor.motion_living
            condition: 'on'
      - entity: light.bedroom
        name: 卧室灯
        icon: mdi:bed
      - entity: light.kitchen
        name: 厨房灯
        icon: mdi:lightbulb
```

#### 顶层配置项

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `type` | ✅ | `string` | — | 固定为 `button_group` |
| `direction` | ❌ | `string` | `horizontal` | 排列方向，`horizontal`（水平）/ `vertical`（垂直） |
| `name` | ❌ | `string` | 无 | 组标签，显示在按钮组上方（小字） |
| `on_color` | ❌ | `string` | `#3498db` | 子按钮开启状态的默认颜色 |
| `off_color` | ❌ | `string` | `#95a5a6` | 子按钮关闭状态的默认颜色 |
| `icon_size` | ❌ | `number` | `16` | 子按钮图标大小（px），子按钮可单独覆盖 |
| `show_name` | ❌ | `boolean` | `true` | 是否显示子按钮文字，子按钮可单独覆盖 |
| `gap` | ❌ | `string` | `4px` | 按钮间距，支持 CSS 间距值（如 `30px`、`8px`、`12px 8px`）|
| `buttons` | ✅ | `array` | `[]` | 子按钮列表 |

#### 子按钮（buttons 中的每项）配置

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ✅ | `string` | — | 实体 ID，用于读取状态和自动推断服务 |
| `name` | ❌ | `string` | 实体后缀 | 按钮显示名称 |
| `icon` | ❌ | `string` | 无 | 按钮图标（启用时也使用此图标） |
| `on_icon` | ❌ | `string` | `icon` | 开启时图标 |
| `off_icon` | ❌ | `string` | `icon` | 关闭时图标 |
| `on_color` | ❌ | `string` | 组 `on_color` | 开启时颜色，覆盖组默认 |
| `off_color` | ❌ | `string` | 组 `off_color` | 关闭时颜色，覆盖组默认 |
| `icon_size` | ❌ | `number` | 组 `icon_size` | 图标大小（px），覆盖组默认 |
| `show_name` | ❌ | `boolean` | 组 `show_name` | 是否显示按钮名称，覆盖组默认 |
| `confirm` | ❌ | `boolean` | `false` | 点击前是否弹出确认对话框 |
| `tap_action` | ❌ | `object` | `{ action: 'toggle' }` | 点击动作，支持所有标准动作类型 |
| `badge` | ❌ | `array` | 无 | 条件角标数组，满足条件的规则数量显示为红色角标 |

#### badge 子项配置

每个 badge 规则格式与主系统 badge 一致：

| 配置项 | 必填 | 类型 | 说明 |
|--------|:----:|------|------|
| `entity` | ✅ | `string` | 要判断状态的实体 ID |
| `condition` | ❌ | `string/array/object` | 条件判断，缺省时实体非 unknown/unavailable 即为真 |

condition 支持的格式：

| 格式 | 说明 | 示例 |
|------|------|------|
| 字符串状态 | 实体状态等于该值 | `condition: on` |
| 字符串表达式 | 数值比较 | `condition: '<10'`、`>=50`、`!=0` |
| 数组 | OR 语义，任一满足即可 | `condition: ['<10', '>100']` |
| 对象 | 透传给条件引擎 | `condition: { operator: '>', value: 50, attribute: 'temperature' }` |
| 缺省 | 实体非 unknown/unavailable 即为真 | 不写 condition |

#### 动作类型（tap_action）

按钮组内的子按钮支持以下 `tap_action` 类型：

| action | 说明 |
|--------|------|
| `toggle` | 切换实体状态（默认） |
| `set_value` | 设置实体目标值，需配置 `value` |
| `more-info` | 弹出 HA 实体详情弹窗 |
| `navigate` | 页面导航，需配置 `navigation_path` |
| `call-service` | 调用 HA 服务，需配置 `service` |
| `popup_card` | 弹出自定义卡片，需配置 `card` |
| `card` | 弹出设备内置控制弹窗，需配置 `card`（含 `type` 字段） |
| `none` | 不执行操作 |

#### 垂直布局（vertical）

设置 `direction: vertical` 可使按钮垂直排列，每个按钮占满整行宽度：

```yaml
buttons:
  - type: button_group
    direction: vertical
    name: 房间设备
    buttons:
      - entity: light.living_room
        name: 客厅灯
        icon: mdi:ceiling-light
      - entity: fan.living
        name: 客厅风扇
        icon: mdi:fan
      - entity: switch.living_tv
        name: 电视
        icon: mdi:television
```

垂直布局适合空间较窄的卡片（如手机竖屏），或按钮数量较多的场景。

#### 仅图标模式

设置 `show_name: false` 可隐藏按钮名称，只显示图标，适合按钮较多或空间有限的场景：

```yaml
buttons:
  - type: button_group
    show_name: false
    icon_size: 18
    buttons:
      - entity: light.living_room
        icon: mdi:ceiling-light
      - entity: light.bedroom
        icon: mdi:bed
```

#### 样式说明

按钮组以浅色圆角容器包裹，每个子按钮为紧凑小按钮，默认显示图标+名称：
- **水平布局**：按钮从左到右排列，自动换行
- **垂直布局**：按钮从上到下排列，每行占满
- **开启状态**：使用配置的 `on_color` 背景 + 白色文字
- **关闭状态**：使用浅灰背景 + 灰色文字
- **鼠标悬停**：轻微上浮，点击时微缩
- **角标**：配置了 `badge` 的子按钮在右上角显示红色计数角标
- **确认**：配置了 `confirm: true` 的子按钮点击后弹出确认对话框

#### 在自由布局弹窗中使用

`button_group` 不仅可以在主卡片的 `buttons` 中直接使用，也可以在自由布局弹窗（`show_free_layout_popup`）的 `items` 中嵌入，将弹窗中的多个按钮分组管理。

```yaml
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  popup_position: clone_button_left
  service_data:
    title: 冰箱
    width: 360px
    cards:
      - row: 1
        per_line: 1
        title: 灯光
        items:
          - type: button_group
            name: 灯光控制
            on_color: '#3498db'
            off_color: '#95a5a6'
            direction: horizontal
            buttons:
              - entity: light.living_room
                name: 客厅灯
                show_name: false
                icon: mdi:ceiling-light
                on_color: '#f1c40f'
                tap_action:
                  action: toggle
              - entity: light.bedroom
                name: 卧室灯
                icon: mdi:bed
                on_color: '#f1c40f'
                tap_action:
                  action: toggle
      - row: 2
        per_line: 1
        title: 风扇
        items:
          - type: button_group
            direction: vertical
            name: 风扇控制
            buttons:
              - entity: fan.living
                name: 客厅风扇
                icon: mdi:fan
              - entity: fan.bedroom
                name: 卧室风扇
                icon: mdi:fan
```

弹窗中每个 `row` 可独立配置 `button_group`，支持水平/垂直布局混用。

**注意事项：**

- 在自由布局弹窗中使用时，`button_group` 的配置格式与主卡片完全一致（`type: button_group` + `buttons` 子按钮列表）
- `update_interval` 控制弹窗中按钮组的刷新频率，设为 `0`（默认）由 hass 状态推送驱动实时更新
- 弹窗中的 `button_group` 自动绑定点击事件，支持 `confirm` 确认弹窗和 `badge` 条件角标

---

### 6.22 图表卡片概览

图表卡片用于在弹窗中可视化展示数据，支持 9 种图表类型，均基于 ECharts 渲染（`chart_gauge` 除外，使用纯 SVG）。图表卡片通常配置在弹窗的 `items` 中，也可直接用于主卡片 `buttons`。

**所有图表卡片共享的通用配置项：**

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `type` | `string` | — | 图表类型（见下表） |
| `name` | `string` | 实体名称 | 卡片标题 |
| `icon` | `string` | 各类型默认 | 标题图标 |
| `show_name` | `boolean` | `true` | 是否显示标题行 |
| `height` | `string/number` | 各类型默认 | 图表高度（如 `160px`、`200`） |
| `update_interval` | `number` | `0` | 自动刷新间隔（秒），`0` 为跟随 hass 实时推送 |
| `tap_action` | `object` | 无 | 点击动作，支持所有标准动作类型 |
| `layout` | `string` | `normal` | 布局模式：`normal`（标准）/ `mini` 或 `min`（紧凑），弹窗内小卡片推荐用 `mini` |

**图表类型一览：**

| type | 名称 | 渲染方式 | 数据源 | 典型用途 |
|------|------|----------|--------|----------|
| `chart_gauge` | 仪表图 | 纯 SVG | 单实体 | 温度、湿度、电量等数值仪表 |
| `chart_progress` | 进度条 | 纯 CSS | 多实体 | 多项指标进度对比 |
| `chart_bar` | 柱状图 | 纯 CSS | 单实体历史 | 24h/48h 历史数据柱状图 |
| `chart_line` / `chart` | 曲线图 | ECharts | 单实体历史 | 平滑趋势曲线 |
| `chart_pie` | 环形图 | ECharts | 多实体当前值 | 占比分析（环形+中心总计） |
| `chart_pie_full` | 完整饼图 | ECharts | 多实体当前值 | 占比分析（带图例+标签） |
| `chart_nightingale` | 南丁格尔玫瑰图 | ECharts | 多实体当前值 | 多维度数据对比 |
| `chart_heatmap` | 日历热力图 | ECharts | 实体属性/API | 年度数据热力图（类 GitHub） |
| `chart_calendar` | 日历图 | ECharts | 实体属性/API | 月历+年/月/日柱状图 |
| `chart_mixed` | 混合图表 | ECharts | 多实体属性/API | 柱+线+面积组合图 |

> ⚠️ **ECharts 依赖**：除 `chart_gauge`（纯 SVG）、`chart_progress`（纯 CSS）、`chart_bar`（纯 CSS）外，其余图表均依赖 ECharts。卡片优先加载本地文件 `www/pobaby_package/js/echarts.min.js`，不存在时自动从 CDN 回退（详见第二十节）。

---

### 6.23 仪表图 (type: chart_gauge)

显示数值型实体的半圆仪表盘，参照 HA 内置 gauge 卡片风格，使用纯 SVG 渲染，无需 ECharts。

```yaml
- type: chart_gauge
  entity: sensor.temperature          # 数值型实体
  name: 室内温度
  unit: °C                           # 单位（可选，默认取实体属性）
  min: 0                             # 最小值
  max: 40                            # 最大值
  severity:                          # 颜色分段（可选，不配置则绿→黄→红自动渐变）
    - value: 18
      color: '#3498db'               # 蓝（低温）
    - value: 26
      color: '#2ecc71'               # 绿（舒适）
    - value: 40
      color: '#e74c3c'               # 红（高温）
  tap_action:
    action: more-info
```

**配置项：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ✅ | `string` | — | 数值型传感器实体 ID |
| `unit` | ❌ | `string` | 实体属性 | 显示单位 |
| `min` | ❌ | `number` | `0` | 仪表最小值 |
| `max` | ❌ | `number` | `100` | 仪表最大值 |
| `severity` | ❌ | `array` | 自动渐变 | 颜色分段配置，每项含 `value` 和 `color` |

---

### 6.24 进度条 (type: chart_progress)

显示多条水平进度条，每条对应一个实体，支持自定义范围和颜色分级。

```yaml
- type: chart_progress
  name: 设备电量
  update_interval: 60
  cards:                                   # 进度条列表
    - entity: sensor.phone_battery
      name: 手机
      min: 0
      max: 100
      color: '#2ecc71'                     # 自定义颜色（可选）
      unit: '%'
      tap_action:
        action: more-info
    - entity: sensor.watch_battery
      name: 手表
      min: 0
      max: 100
    - entity: sensor.lock_battery
      name: 门锁
      min: 0
      max: 100
```

**进度条自动颜色分级**（未配置 `color` 时）：

| 范围 | 级别 | 颜色 |
|------|------|------|
| 0% ~ 30% | `low` | 绿色 |
| 30% ~ 70% | `medium` | 黄色 |
| 70% ~ 100% | `high` | 红色 |

**顶层配置项：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `cards` | ✅ | `array` | — | 进度条列表 |

**cards 子项配置：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ✅ | `string` | — | 实体 ID |
| `name` | ❌ | `string` | 实体ID | 进度条名称 |
| `icon` | ❌ | `string` | 无 | 进度条图标 |
| `show_name` | ❌ | `boolean` | `true` | 是否显示名称 |
| `min` | ❌ | `number` | `0` | 最小值 |
| `max` | ❌ | `number` | `100` | 最大值 |
| `unit` | ❌ | `string` | 实体属性 | 单位 |
| `color` | ❌ | `string` | 自动分级 | 自定义进度条颜色 |
| `tap_action` | ❌ | `object` | 无 | 单条进度条点击动作 |

---

### 6.25 柱状图 (type: chart_bar)

显示单实体的历史数据柱状图，支持按时间段聚合计算，纯 CSS 渲染无需 ECharts。

```yaml
- type: chart_bar
  entity: sensor.power_consumption
  name: 用电量
  unit: kWh
  height: 80px
  bar:                                  # 柱状图参数（也可写在顶层）
    min: 0                              # Y轴最小值
    max: 100                            # Y轴最大值（可选，默认自适应）
    hours_to_show: 48                   # 显示多少小时的历史数据
    bar_hours: 2                        # 每根柱子代表多少小时
    bar_hours_calc: average             # 聚合计算方式
```

**聚合计算方式（bar_hours_calc）：**

| 值 | 说明 |
|----|------|
| `average` | 平均值（默认） |
| `max` | 最大值 |
| `min` | 最小值 |
| `count` | 数据点数 |
| `max-min` | 极差（最大值-最小值） |
| `add` | 累加和 |

**配置项：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ✅ | `string` | — | 数值型实体 ID |
| `unit` | ❌ | `string` | 实体属性 | 单位 |
| `height` | ❌ | `string` | `60px` | 图表高度 |
| `bar.hours_to_show` | ❌ | `number` | `48` | 历史数据时长（小时） |
| `bar.bar_hours` | ❌ | `number` | `2` | 每根柱子的时间跨度（小时） |
| `bar.bar_hours_calc` | ❌ | `string` | `average` | 聚合计算方式 |
| `bar.min` | ❌ | `number` | `0` | Y轴最小值 |
| `bar.max` | ❌ | `number` | 自适应 | Y轴最大值 |

> 💡 `bar` 内的配置项也可直接写在顶层（如 `hours_to_show: 48`），`bar` 内优先级更高。

---

### 6.26 曲线图 (type: chart_line / chart)

使用 ECharts 渲染单实体的平滑历史数据曲线，支持自适应 Y 轴范围。

```yaml
- type: chart_line                       # 也可写成 type: chart
  entity: sensor.temperature
  name: 温度趋势
  unit: °C
  height: 120px
  line:                                  # 曲线参数（也可写在顶层）
    min: 10                              # Y轴最小值（可选，默认自适应）
    max: 35                              # Y轴最大值（可选，默认自适应）
    hours_to_show: 24                    # 显示多少小时历史数据
  tap_action:
    action: more-info
```

**配置项：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ✅ | `string` | — | 数值型实体 ID |
| `unit` | ❌ | `string` | 实体属性 | 单位 |
| `height` | ❌ | `string` | 自适应 | 图表高度 |
| `line.hours_to_show` | ❌ | `number` | `24` | 历史数据时长（小时），别名 `hours` |
| `line.min` | ❌ | `number` | 自适应 | Y轴最小值 |
| `line.max` | ❌ | `number` | 自适应 | Y轴最大值 |

> 💡 `line` 内的配置项也可直接写在顶层（如 `hours_to_show: 24`），`line` 内优先级更高。`type: chart` 是 `chart_line` 的别名，功能完全相同。

---

### 6.27 环形图 (type: chart_pie)

显示多实体的占比环形图（甜甜圈图），点击扇区可在中心显示该项详情，使用 ECharts 渲染。

```yaml
- type: chart_pie
  name: 用电分布
  icon: mdi:flash
  height: 160px
  unit: kWh                              # 中心总计单位
  update_interval: 30
  cards:                                 # 环形图数据项
    - entity: sensor.ac_power
      name: 空调
      color: '#5470c6'                   # 自定义颜色（可选，默认自动分配）
      unit: W                            # 单项单位（可选）
    - entity: sensor.fridge_power
      name: 冰箱
      color: '#91cc75'
    - entity: sensor.washer_power
      name: 洗衣机
```

**交互说明：**
- 中心默认显示**总计值**（所有项值之和）+ 单位
- 点击某个扇区 → 中心显示该项的名称、数值、单位
- 点击空白区域 → 恢复总计显示

**配置项：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `cards` | ✅ | `array` | — | 数据项列表 |
| `unit` | ❌ | `string` | 无 | 中心总计显示的单位 |

**cards 子项配置：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ✅ | `string` | — | 实体 ID（需为数值型） |
| `name` | ❌ | `string` | 实体ID | 扇区名称 |
| `color` | ❌ | `string` | 自动分配 | 扇区颜色 |
| `unit` | ❌ | `string` | 实体属性 | 该项单位 |

---

### 6.28 完整饼图 (type: chart_pie_full)

显示多实体的标准饼图，带图例和百分比标签，使用 ECharts 渲染。与环形图的区别：饼图展示完整扇形，底部有水平图例，鼠标悬停有 tooltip。

```yaml
- type: chart_pie_full
  name: 能耗占比
  icon: mdi:chart-pie
  height: 260px
  update_interval: 30
  chart:                                 # 饼图数据项
    - entity: sensor.ac_power
      name: 空调
      color: '#5470c6'
    - entity: sensor.fridge_power
      name: 冰箱
      color: '#91cc75'
    - entity: sensor.washer_power
      name: 洗衣机
      color: '#fac858'
```

**与环形图（chart_pie）的区别：**

| 特性 | chart_pie（环形图） | chart_pie_full（完整饼图） |
|------|---------------------|--------------------------|
| 图形 | 环形（中空） | 实心饼图 |
| 中心文本 | ✅ 总计/选中项详情 | ❌ 无 |
| 图例 | ❌ 无 | ✅ 底部水平图例 |
| 标签 | ❌ 无 | ✅ 名称+百分比（≤10项时） |
| Tooltip | ❌ 无 | ✅ 悬停显示详情 |
| 适合场景 | 紧凑空间、概览 | 数据分析、详细占比 |

**配置项：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `chart` | ✅ | `array` | — | 数据项列表 |

**chart 子项配置：** 与 `chart_pie` 的 `cards` 子项格式相同（`entity`、`name`、`color`、`unit`）。

---

### 6.29 南丁格尔玫瑰图 (type: chart_nightingale)

显示多实体状态值的南丁格尔玫瑰图，扇区半径按数值大小变化，使用 ECharts 渲染。适合多维度数据对比。

```yaml
- type: chart_nightingale
  name: 功率分布
  icon: mdi:air-conditioner
  height: 160px
  update_interval: 10
  chart:                                 # 玫瑰图数据项
    - entity: sensor.cabinet_power
      name: 机柜
      color: '#00a381'
    - entity: sensor.pc_power
      name: 电脑
      color: '#c85179'
    - entity: sensor.ac_power
      name: 空调
      color: '#5470c6'
```

> 💡 南丁格尔玫瑰图也支持非数值实体：`on`/`open`/`home` → 值为 1，`off`/`closed`/`away` → 值为 0。

**配置项：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `chart` | ✅ | `array` | — | 数据项列表 |

**chart 子项配置：** 与 `chart_pie` 的 `cards` 子项格式相同。

---

### 6.30 日历热力图 (type: chart_heatmap)

显示年度日历热力图（类 GitHub 贡献图），颜色深浅表示数值高低，使用 ECharts 渲染。支持两种数据源：实体属性和外部 API。

**方式一：实体属性数据源**

```yaml
- type: chart_heatmap
  entity: sensor.gas_meter
  name: 天然气用量
  height: 120px
  entity_array:                          # 从实体属性中提取数组
    attr: daylist                        # 属性名（可选，不配置时自动查找第一个数组）
    day: day                             # 日期字段
    value: f_gas                         # 值字段
```

**方式二：API 数据源**

```yaml
- type: chart_heatmap
  api_base_url: /api/gateway/xxx/api     # 外部 API 地址
  name: 日用电量
  height: 120px
  api_array:                             # 从 API 返回数据中提取数组
    attr: daily_data                     # 数组字段名（可选，不配置时自动查找第一个数组）
    day: date                            # 日期字段
    value: day_yong_dian_kwh             # 值字段
```

**配置项：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ❌¹ | `string` | — | 实体 ID（与 `api_base_url` 二选一） |
| `api_base_url` | ❌¹ | `string` | — | 外部 API 地址（与 `entity` 二选一） |
| `entity_array` | ❌ | `object` | `{}` | 实体属性数组提取配置 |
| `api_array` | ❌ | `object` | `{}` | API 返回数组提取配置 |

¹ `entity` 和 `api_base_url` 至少配置一项。

**entity_array / api_array 子配置：**

| 配置项 | 必填 | 类型 | 说明 |
|--------|:----:|------|------|
| `attr` | ❌ | `string` | 数组属性/字段名，不配置时自动查找第一个数组 |
| `day` | ✅ | `string` | 日期字段名 |
| `value` | ✅ | `string` | 值字段名 |

> 💡 字段名支持带双引号（如 `"day"`），卡片会自动处理。日期支持 `yyyy-mm-dd` 和 `yyyy-mm-dd hh:mm:ss` 格式。

---

### 6.31 日历图 (type: chart_calendar)

显示月历视图 + 年/月/日三级下钻柱状图，支持双数值系列对比，使用 ECharts 渲染。

```yaml
- type: chart_calendar
  entity: sensor.gas_meter
  name: 天然气
  height: 280px
  entity_array:
    attr: daylist
    day: day
    value_1: f_gas                        # 数值1字段
    value_1_name: 使用量                  # 数值1名称
    value_1_unit: m³                      # 数值1单位
    value_1_background: '#00a381'         # 数值1背景色
    value_2: e_gas                        # 数值2字段（可选，用于双系列对比）
    value_2_name: 金额
    value_2_unit: ￥
    value_2_background: '#c85179'
```

**与热力图（chart_heatmap）的区别：**

| 特性 | chart_heatmap | chart_calendar |
|------|---------------|----------------|
| 视图 | 年度方块热力图 | 月历 + 柱状图 |
| 数值系列 | 单系列 | 双系列（value_1 + value_2） |
| 下钻 | 无 | ✅ 年→月→日 三级 |
| 适合场景 | 年度总览 | 详细月度/日度分析 |

**配置项：** 与 `chart_heatmap` 相同的数据源配置（`entity`/`api_base_url` + `entity_array`/`api_array`）。

**entity_array / api_array 子配置（扩展）：**

| 配置项 | 必填 | 类型 | 说明 |
|--------|:----:|------|------|
| `day` | ✅ | `string` | 日期字段名 |
| `value_1` | ✅ | `string` | 数值1字段名 |
| `value_1_name` | ❌ | `string` | 数值1系列名称 |
| `value_1_unit` | ❌ | `string` | 数值1单位 |
| `value_1_background` | ❌ | `string` | 数值1柱状图颜色 |
| `value_2` | ❌ | `string` | 数值2字段名（双系列对比时配置） |
| `value_2_name` | ❌ | `string` | 数值2系列名称 |
| `value_2_unit` | ❌ | `string` | 数值2单位 |
| `value_2_background` | ❌ | `string` | 数值2柱状图颜色 |

---

### 6.32 混合图表 (type: chart_mixed)

使用 ECharts 渲染柱状图、折线图、面积图的组合图表，支持年/月/日三级下钻切换，多数据系列混搭。

```yaml
- type: chart_mixed
  name: 天然气分析
  icon: mdi:chart-bar
  chart:                                  # 数据系列列表
    - type: bar                           # 柱状图系列
      entity: sensor.gas_meter
      attr: daylist                       # 数组属性名（可选）
      day: day                            # 日期字段
      value: f_gas                        # 值字段
      value_name: 使用量                  # 系列名称
      value_unit: m³                      # 单位
      bar_color: '#00a381'                # 柱状图颜色
    - type: line                          # 折线图系列
      entity: sensor.gas_meter
      attr: daylist
      day: day
      value: e_gas
      value_name: 金额
      value_unit: ￥
      line_color: '#c85179'               # 折线图颜色
    - type: area                          # 面积图系列
      entity: sensor.gas_meter
      attr: daylist
      day: day
      value: e_gas
      value_name: 趋势
      value_unit: ￥
      area_color: '#c85179'               # 面积图颜色
```

**下钻导航：** 图表顶部自动生成年/月/日切换按钮 + 年月选择器，点击即可切换不同粒度视图。

**配置项：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `chart` | ✅ | `array` | — | 数据系列列表 |

**chart 子项配置：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `type` | ✅ | `string` | — | 图表类型：`bar`（柱状）/ `line`（折线）/ `area`（面积） |
| `entity` | ✅ | `string` | — | 实体 ID |
| `attr` | ❌ | `string` | 顶层 | 数组属性名（不配置时数据在实体顶层） |
| `day` | ✅ | `string` | — | 日期字段名 |
| `value` | ✅ | `string` | — | 值字段名 |
| `value_name` | ❌ | `string` | — | 系列显示名称 |
| `value_unit` | ❌ | `string` | — | 单位 |
| `bar_color` | ❌ | `string` | 自动 | 柱状图颜色（`type: bar` 时） |
| `line_color` | ❌ | `string` | 自动 | 折线图颜色（`type: line` 时） |
| `area_color` | ❌ | `string` | 自动 | 面积图颜色（`type: area` 时） |

---

### 6.33 插座桑基图（功率流向图）

插座按钮（`type: socket`）弹窗内置桑基图功能，可可视化展示各插座的功率/用电流向（三级结构：合计 → 房间 → 具体插座），使用 ECharts 渲染。

**启用方式：**

在插座按钮配置中设置 `shwo_sankey: true`：

```yaml
- type: socket
  icon: mdi:power-socket-au
  shwo_sankey: true                      # 启用桑基图
  card:
    - entity: switch.plug_living
      name: 客厅插座
      room: 客厅                         # room 用于桑基图按房间聚合
      entities:                          # 子实体列表（用于桑基图读取功率/用电量）
        - entity: sensor.plug_living_power
          name: 功率
        - entity: sensor.plug_living_daily
          name: 日用电
        - entity: sensor.plug_living_monthly
          name: 月用电
        - entity: sensor.plug_living_yearly
          name: 年用电
    - entity: switch.plug_bedroom
      name: 卧室插座
      room: 卧室
      entities:
        - entity: sensor.plug_bedroom_power
          name: 功率
        - entity: sensor.plug_bedroom_daily
          name: 日用电
```

**交互说明：**

- 弹窗顶部出现「桑基图」按钮，点击切换桑基图/列表视图
- 桑基图顶部有 4 个切换按钮：**功率**（实时，10 秒自动刷新）、**日用电**、**月用电**、**年用电**
- 功率类型启动后会每 10 秒自动更新数据

**桑基图数据结构：**

```
          ┌──── 客厅 ────┬─ 客厅插座(80W)
          │              └─ 客厅电视(120W)
总计(350W)┤
          └──── 卧室 ────┬─ 卧室插座(50W)
                         └─ 卧室灯(100W)
```

---

### 6.34 设备用电统计卡片 (type: device_usage)

设备用电统计卡片用于展示指定房间（或全屋）当日各设备的使用时长、用电量和事件分布。通过 `api_base_url` 对接 HA 数据统一存储系统（ha_data_store）的设备事件 API。

**两种显示模式：**

| 模式 | 说明 |
|------|------|
| `mini`（默认） | 紧凑卡片，显示摘要 + 设备列表，适合嵌入头部模式网格 |
| `full` | 完整弹窗，含 24h 甘特图 + 完整设备表 + 多种可视化视图 + 日期切换 |

**基础配置：**

```yaml
  - type: device_usage
    layout: mini                 # mini（默认）/ full
    top_count: 5                 # mini 模式下显示的设备数，0 或省略则自动填充全部
    date: "2026-06-21"           # 指定日期，默认今天
    show_timeline: true          # 是否显示 24h 甘特图，默认 true
    api_base_url: http://192.168.1.100:8080   # （可选）单独指定数据源，默认使用顶层配置
    key: your_api_key           # （可选）单独指定 API key
    room_name: 客厅              # （可选）单独指定房间名，默认使用 card room_name
```

#### mini 模式

mini 模式渲染一张紧凑统计卡片，显示当日总用电量/设备数/运行中设备数，以及 Top N 设备列表（每项含图标、名称、使用时长、用电量、运行状态指示灯）。

```yaml
buttons:
  - type: device_usage
    layout: mini
    top_count: 5
```

渲染效果（示例）：

```
┌─────────────────────────────┐
│ ⚡ 今日3.25度/8台设备(3运行)  │
├─────────────────────────────┤
│ 💡 客厅主灯          2.5h  0.8度 │
│ 🔌 电视插座          3.2h  1.2度 │
│ 🌀 循环扇           1.8h  0.3度 │
│ 📺 机顶盒           5.0h  0.6度 │
│ ❄️ 空调             1.0h  0.2度 │
└─────────────────────────────┘
```

#### 弹窗详情模式

mini 模式卡片点击后弹出完整详情弹窗，包含以下模块：

**1. 顶部栏**：房间名/全屋切换、日期前后切换

**2. 摘要统计**：
- 开机次数
- 总使用时长
- 总用电量（度）

**3. 24 小时事件分布甘特图**（ECharts）：
- 横轴为 24 小时时间线
- 每个设备一行，显示当日所有开机时段
- 运行中的设备以高亮色标记
- 鼠标悬停显示时段详情
- 全屋模式下左侧显示房间名分组，房间间有分隔线

**4. 设备明细表**：
- 支持 4 种视图切换：

| 视图 | 说明 |
|------|------|
| 表格 | 设备列表（房间/设备名/状态/时长/用电量/事件次数）+ 合计行 |
| 时长图 | 南丁格尔玫瑰图，按使用时长占比展示，只标注 Top 6 |
| 用电图 | 南丁格尔玫瑰图，按用电量占比展示，只标注 Top 6 |
| 复合图 | 柱状图（用电量）+ 平滑曲线（时长），双 Y 轴 |
| 房间利用率 | 全屋模式专属，各房间使用时长占比玫瑰图 |
| 3D | 全屋模式专属，3D 房间能耗地图（Three.js），可拖拽旋转/缩放/点击房间弹出能耗气泡 |

**房间/全屋切换**：

配置中 `person` 配置了多个 `rooms` 时，弹窗顶部出现"全屋"切换按钮：
- **单房间**：只加载该房间设备数据
- **全屋**：并行请求所有房间数据，整合后统一按设备去重，全屋模式设备表前缀增加房间名列

**日期切换**：

弹窗可通过 `◀ ▶` 按钮切换到任意历史日期查看数据。

**数据缓存**：

数据以 `device_usage_{房间名}` 为缓存键、以日期为子键缓存，同房间切回已加载日期时直接使用缓存。

**full 模式（较少使用）**：

直接在卡片区域渲染完整弹窗内容（不弹出），适合嵌入自由布局弹窗：

```yaml
  - type: device_usage
    layout: full
```

**完整配置示例：**

```yaml
buttons:
  - type: device_usage
    layout: mini
    top_count: 5
    room_name: 客厅
    date: "2026-06-21"
```

**全屋模式 3D 视图相关配置（嵌入 buttons_2+ 时使用）：**

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `energy_center_hide_room` | `string` | `""` | 3D 视图中隐藏指定房间，逗号分隔，如 `"儿童房外,次卧外,楼道"` |
| `energy_center_hide` | `string` | `""` | 隐藏 3D 视图中的指定元素，当前支持 `"3D"`（隐藏 3D 地图选项卡） |

#### 设备回放入口（show_device_replay）

设备用电详情弹窗支持在顶部「房间/全屋」切换胶囊内新增一个**「回放」按钮**，点击后弹出**设备回放卡片**（本卡片内置的子卡片，`standalone_type: replay`）。通过复用 Store 配置共享机制（`config_id` / `from_config_id`），**无需在弹窗内重复配置回放卡片**，只需指定一个已注册的回放配置 `config_id` 即可。

**配置方式：**

在 `device_usage` 卡片的 `card_config` 中配置 `show_device_replay`，值为**已注册到 Store 的回放配置 config_id**：

```yaml
buttons_2:
  - type: card
    row_column: 1,1-1
    card_config:
      type: device_usage
      show_device_replay: huifang     # 值为 Store 中已注册的回放配置 config_id
      layout: mini
      top_count: 4
```

**前提**：`huifang` 这个 `config_id` 必须在主卡配置中通过 `tap_action` 注册一份完整的**设备回放**配置节点 —— 注意 `type` 现在写**本卡片**（`custom:room-elves-card` + `standalone_type: replay`）：旧的 `custom:device-replay-card` 元素已随「并入内建」退役、不再注册，继续照旧写会拿不到卡片（见 6.40）。

```yaml
buttons:
  - name: 回放
    icon: mdi:video
    tap_action:
      action: popup_card
      config_id: huifang              # 注册到 Store
      card:
        type: custom:device-replay-card
        api_base_url: /api/ha_data_store/
        key: 你的密钥
        check_entity: light.keting_dadeng
        background_image: /local/house/3d_ui2/关灯.png
        entities:
          - entity: light.cuco_cn_696791082_v3_s_13
            name: 客厅-投影仪
            room: 客厅
            image_url: /local/house/3d_ui2/投影仪on.png
            x: 130
            y: 210
            on_state: 'on'
        # ... 其他回放配置
```

**说明：**

- `show_device_replay` 为**字符串**类型，值即为要引用的 Store `config_id`（不兼容 `true`/`false` 布尔值）
- 配置后，device-usage 弹窗标题栏的「房间/全屋」切换胶囊内会显示**「回放」文字按钮**（样式与 `du-scope-btn` 一致）
- 点击「回放」→ `RoomElvesStore.get(config_id)` 从 Store 取回放配置 → 弹出**设备回放卡片**（由本卡片内置渲染，`showDeviceReplayPopup`）
- 若指定的 `config_id` 未在 Store 中注册，控制台输出警告且不弹窗
- 回放配置复用 Store 机制，**改一处（注册节点）多处生效**，`modules/cards/device-replay.js` 无需改动

---

### 6.35 使用量日历卡片 (type: usage_calendar)

使用量日历卡片用于展示任意实体的用量/能耗/时长数据，支持日历视图和年/月/日 ECharts 图表视图。数据来源既可以是 [HA 数据统一存储系统](https://github.com/chjspp520/ha_data_store/releases)（ha_data_store）API，也可以是实体属性。

**六个选项卡视图：**

| 选项卡 | 说明 |
|------|------|
| 日历 | 月历网格，每个单元格显示当日用量和时长，点击有数据的日期弹出详情 |
| 历史 | 两张对比图：「历史本月」与「历史今日」 |
| 年 | 年度柱状图（ECharts），显示所有可用年份的用量/能耗对比 |
| 月 | 月度柱状图（ECharts），显示选定年份 12 个月的用量/能耗对比 |
| 日 | 日度柱状图（ECharts），显示选定月份每日的用量/能耗对比 |
| 洞察 | 跨年 / 全局视角（v5.7.3 新增），顶部筛选按钮切换四个子视图：**总计 / 热力图 / 动态排名 / 时段全景图**；其中时段全景图（v5.7.1 新增）支持点击柱体下钻到「该小时有使用的日期」 |

**数据源配置：**

支持三种数据源：API 单实体、API **多实体聚合**、实体属性。优先使用 API，未配置 API 时使用实体属性。

**方式一：API 数据源（推荐）**

通过 `api` 配置块对接 ha_data_store，`api_base_url` 和 `key` 可省略（自动从顶层配置继承）：

```yaml
  - type: usage_calendar
    api:
      entity: input_boolean.bing_xiang    # 设备实体 ID（必需）
      # api_base_url: /api/ha_data_store/ # 可选，省略时从顶层继承
      # key: your_api_key                 # 可选，省略时从顶层继承
```

**方式二：实体属性数据源**

通过 `entities` 配置块从实体属性读取数据：

```yaml
  - type: usage_calendar
    entities:
      data_entity: sensor.tianranqi        # 数据实体 ID
      consumption_attr: gas_consumption    # 用量属性名，默认 gas_consumption
      duration_attr: gas_duration_seconds  # 时长属性名（秒），默认 gas_duration_seconds
      date_attr: date                      # 日期属性名，默认 date
```

**方式三：多实体聚合（多个实体合计）**

配置 `api.entities`（实体数组）即进入**多实体聚合**模式：由后端把这一组实体合并成合计返回，卡片按**合计**展示全部选项卡。

```yaml
  - type: usage_calendar
    title: 全屋空调用电量日历
    api:
      entities:
        - climate.keting_ac_keting_ac          # 简写：只给实体 ID
        - entity: climate.zhuwo_xxx
          name: 主卧空调                        # 可选：图表/图例/日历角标显示的名字
          color: "#4C9AFF"                      # 可选：柱状图堆叠颜色（不写自动分配）
        - { entity: climate.ertongfang_xxx, name: 儿童房空调 }
```

多实体模式下的差异：

| 能力 | 说明 |
|------|------|
| 数据 | 走 `device_usage_multi` / `device_usage_detail` / `entities_hours_agg` 等**多实体接口**，各选项卡展示的都是这一组实体的**合计** |
| 标题 | 自动追加「（N 个设备合计）」后缀 |
| 柱状图 | **按设备堆叠**：每台设备一段，颜色取配置的 `color`（未配置时按 8 色调色板自动分配） |
| 日历角标 | 单元格左上角标注**当天有几台设备有数据**（形如 `2台`）。它与用量数值**互相独立** —— 某设备当天只瞬间开关过、用量四舍五入为 0 时数值不显示，但「当天有几台设备动过」仍然显示 |
| 时段全景图下钻 | 点击柱子所在的**那一段**即下钻到**该设备**：右侧列出「该设备在这一个小时有使用的日期」（标题带设备名），点日期看明细 |
| 每日明细 | 单日明细为**分设备甘特图**，逐台展开每段开关记录 |
| 图表图例 | 洞察/年/月/日等图表自动带**设备图例**，可点选隐藏某台设备 |

**基础配置：**

```yaml
  - type: usage_calendar
    title: 冰箱用电量日历                  # 卡片标题，默认"天然气使用量"
    show_title: false                     # 是否显示标题，默认 true
    width: 400px                          # 卡片宽度，默认 100%
    show_popup: true                      # 点击日期是否弹出详情，默认 true
    data_value_color: "#00a381"           # 用量数据颜色，默认 #F9D505
    calc_value_color: "#c85179"           # 时长/费用颜色，默认 #804AFF
    chart_line_color: "#FF6B6B"           # 图表曲线颜色，默认 #FF6B6B
    date_font_size: 11px                  # 日期字号，默认 11px
    value_font_size: 10px                 # 数值字号，默认 10px
```

**单位与精度配置：**

```yaml
    units: "°,h"        # 用量单位,时长/费用单位，默认 "m³,元"
    decimals: "2,2"     # 用量小数位,时长/费用小数位，默认 "2,2"
    series: "用量,时长"  # 柱状图系列名,曲线图系列名，默认 "用量,费用"
```

**calc_value_choose 计算值模式：**

控制日历和图表中"第二行数值"的显示方式：

| 值 | 说明 |
|------|------|
| `calculate` | 按计算系数换算费用（用量 × calculate 系数）|
| `value` | 直接显示时长（来自 duration_attr 属性）|

```yaml
    calc_value_choose: value              # 显示时长
    calculate: 1.0                        # calc_value_choose=calculate 时的换算系数，默认 1.0
```

> **智能默认**：使用实体数据源且配置了 `duration_attr` 时，`calc_value_choose` 默认为 `value`（显示时长）；否则默认 `calculate`（显示费用）。

**完整配置示例：**

```yaml
buttons:
  - type: usage_calendar
    title: 客厅空调用电量日历
    show_title: false
    width: 400px
    show_popup: true
    api:
      entity: climate.keting_ac_keting_ac
    calc_value_choose: value
    value_font_size: 10px
    date_font_size: 10px
    data_value_color: "#00a381"
    calc_value_color: "#c85179"
    units: "°,h"
    decimals: "2,2"
    series: "用量,时长"
```

**在 popup_card 中使用（vertical-stack 嵌套）：**

```yaml
  - name: 客厅空调
    entity: climate.keting_ac_keting_ac
    tap_action:
      action: popup_card
      popup_position: clone_button_down
      card:
        type: vertical-stack
        cards:
          - type: ac
            entity: climate.keting_ac_keting_ac
            name: 客厅空调
            width: 400px
          - type: usage_calendar
            title: 客厅空调用电量日历
            show_title: false
            width: 400px
            show_popup: true
            api:
              entity: climate.keting_ac_keting_ac
            calc_value_choose: value
            units: "°,h"
            series: "用量,时长"
```

**选项卡导航说明：**

- **日历选项卡**：底部显示 `◀ 年份 ▶` `◀ 月份 ▶ 本月` 导航条，支持快速切换年月；底部显示本月/本年用量和时长汇总
- **年选项卡**（v5.7.0 起为跨年对比分析）：顶部筛选按钮切换子视图，无年份导航栏
  - **总计**：全部年份合计指标卡（累计总用量 / 总时长 / 累计操作次数，三卡单行）+ 逐年对比表（年份 | 用电量 | 总时长，用电量带占比进度条，最新年份带「最新」徽标）
  - **年度**：年度柱状图，显示所有可用年份的用量对比（默认子视图）
  - **热力图**：日用电热力图，横向 12 个月、纵向日期，颜色深浅表示单日用量；标题右侧可切**用量 / 时长**两种口径（切时长后标题变「日时长热力图」，tooltip 单位变 h，零额外请求）
  - **动态排名**：各年累计**用量 / 时长**（按钮可切）bar-racing 动画，支持按日/按月累积、播放/暂停与调速、时间轴拖拽回放（切换主选项卡时自动停止播放）
  - **时段全景图**（v5.7.1 新增）：24 小时用电时段极坐标柱状图（ECharts），偶数小时显示刻度、柱高表示数值、透明度随数值渐变
    - 顶部可切换 **用电量 / 时长 / 次数** 指标，并实时显示峰值时段；hover 柱体查看该小时用电量/时长/次数
    - **点击柱体**：图表缩窄左移，右侧展开该小时「使用日期」面板（按月分组胶囊，点击日期胶囊可查看明细）
    - **点击日期胶囊**：弹出该日使用明细气泡（径向模糊遮罩、三角箭头指向点击处）——顶部显示该日总时长/总用电/时段数，逐条列出开始→结束、时长与用电量；正在运行段（`on_time` 非空且 `off_time` 为空）按「当前时间 − on_time」实时计算时长、按「now_kwh − on_power」计算用电，并以「● 运行中」高亮
    - 再次点击同一日期胶囊收起气泡；切换指标/小时/收起详情时气泡自动关闭
- **月选项卡**：显示年度按钮 + 月度柱状图，无导航栏
- **日选项卡**：显示 `◀ 年份 ▶` `◀ 月份 ▶ 本月` 导航条，支持快速切换年月
- **详情弹窗**：点击日历中有数据的日期，弹出该日的详细事件记录（设备开关机时段、时长、用量），弹窗宽度自动使用卡片配置的 `width`

**配置项汇总：**

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `api.entity` | string | — | API 数据源的设备实体 ID |
| `api.api_base_url` | string | 顶层继承 | ha_data_store API 地址 |
| `api.key` | string | 顶层继承 | API 密钥 |
| `entities.data_entity` | string | — | 实体属性数据源的实体 ID |
| `entities.consumption_attr` | string | `gas_consumption` | 用量属性名 |
| `entities.duration_attr` | string | `gas_duration_seconds` | 时长属性名（秒）|
| `entities.date_attr` | string | `date` | 日期属性名 |
| `title` | string | `天然气使用量` | 卡片标题 |
| `show_title` | boolean | `true` | 是否显示标题 |
| `width` | string | `100%` | 卡片宽度 |
| `show_popup` | boolean | `true` | 点击日期是否弹出详情 |
| `data_value_color` | color | `#F9D505` | 用量数据颜色 |
| `calc_value_color` | color | `#804AFF` | 时长/费用颜色 |
| `chart_line_color` | color | `#FF6B6B` | 图表曲线颜色 |
| `date_font_size` | size | `11px` | 日期字号 |
| `value_font_size` | size | `10px` | 数值字号 |
| `units` | string | `m³,元` | 用量单位,时长/费用单位 |
| `decimals` | string | `2,2` | 用量小数位,时长/费用小数位 |
| `series` | string | `用量,费用` | 柱状图系列名,曲线图系列名 |
| `calc_value_choose` | string | 智能推断 | `calculate`（费用）或 `value`（时长）|
| `calculate` | number | `1.0` | 换算系数（`calc_value_choose: calculate` 时生效；也可填实体 ID 实时取价）|

**多实体与其它可选配置项：**

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `api.entities` | array | — | **多实体聚合**：实体 ID 列表，元素可为字符串或 `{ entity, name, color }`（见「方式三」）|
| `card_width` | string | `100%` | 卡片宽度（与 `width` 同义，两者取先生效的一个）|
| `card_background_color` | color | 主题卡片底色 | 卡片背景色 |
| `calendarbox` | css | `1px solid var(--uc-grid-line, rgba(128,128,128,0.32))` | 日历格子边框（默认跟随 `--uc-grid-line` 变量，覆盖它即可统一改线色） |
| `daybackground` | color | `rgba(104,202,150,0.05)` | 日历格子底色 |
| `running_animation` | boolean | `true` | 「运行中」格子的流光动画；`false` 关闭以降低 CPU 占用 |
| `monthly_budget` | number | — | 月度预算（单位同 `units` 第一项），配置后在日历下方显示预算进度条 |

> **从空调组弹窗自动配置**：多空调组的合计日历**默认就是本卡片的多实体形态**，`api.entities` / `api_base_url` / `key` / 标题与展示项全部由卡片内部生成，无需手写 —— 见 [6.3 空调](#63-空调-type-ac) 的「合计日历」小节。

---

### 6.36 打印机统计卡片 (type: printer)

打印机统计卡片用于展示打印机的**状态、今日作业、日/月/年用量、累计统计、四色耗材、页数统计、事件日志**，分 4 个选项卡。

**只需要配一个实体** —— 集成生成的「全部实体」聚合传感器：

```yaml
  - entity: input_boolean.da_yin_ji
    type: sensor
    name: 打印机
    icon_text: preset_state
    on_icon: mdi:printer
    off_icon: mdi:printer-off
    on_color: "#f58220"
    off_color: "#74787c"
    tap_action:
      action: popup_card                    # 或 action: card（走独立弹窗）
      popup_position: clone_button_top
      width: 400px                          # 外层弹窗宽度（可选）
      card:
        type: printer
        name: HP OfficeJet Pro 7730         # 可选，标题；默认 'HP Printer'
        entity: sensor.hp_printer_quan_bu_shi_ti   # 聚合实体（默认就是它）
        # ── 以下都是可选项 ──────────────────────────────
        # colors:                           # 自定义类型颜色（图标/日历热力/累计卡/环形图全局同步）
        #   print: '#fb8c00'
        #   scan: '#8e24aa'
        #   copy: '#00897b'
        #   fax: '#78909c'
        #   jam_printer: '#e53935'
        #   all: '#fb8c00'
        # api_base_url: /api/ha_data_store/  # 历史逐日补数 / 明细接口（不配则只用实体本地数据）
        # key: 你的key
```

#### 数据来源

聚合实体的 `attributes.entities[]` 是 `{ entity_id, name, icon, state }` 清单；卡片拿清单去 `hass.states` 里逐个取**真实状态与属性**，再按**名称关键字**认出各类实体：

| 名称包含 | 用途 |
|---|---|
| `用量统计` | `daylist` / `monthlist` / `yearlist` / `total`（日-月-年用量、累计、近日记录） |
| `今日作业记录` | `print` / `scan` / `copy` / `fax` / `jam_printer` 明细数组（点今日指标弹气泡） |
| `事件日志` | `count` + 以 ISO 时间戳为键的 `{seq, code, description, occurrences, pages}` |
| `<颜色> 墨水剩余 / 墨盒状态 / 序列号 / 更换墨盒次数 / HP原装墨量` | 四色耗材（**累计用墨 = 更换次数 × 原装墨量**，不直接取集成值） |
| `<颜色> 累计用墨量` | 仅当原装墨量或更换次数取不到数时兜底 |
| `设备状态` / `打印机状态` / `错误状态` | 头部状态与状态区 |
| `…打印页数 / 复印页数 / 扫描页数 / 传真页数 / 卡纸次数` | 统计选项卡的页数分组 |
| `补齐历史用量` / `重新加载用量数据`（**button 域**） | 数据维护按钮（点击需二次确认，走统一动作系统 `button.press`） |

> 认实体用的是**名称关键字**而不是硬编码 entity_id —— 设备名或实体前缀不同也能用。
> 旧配置（`entity` 直接填 `sensor.hp_printer_yong_liang_tong_ji`）仍然可用：没有 `entities` 属性时自动走 legacy 路径。

**关于 `daylist` / `monthlist` 的重复条目**：集成实际输出里，**同一个日期（同一个月）会出现两条记录**。
卡片在数据层做合并（`_printerMergeByKey`）：按 `day` / `month` 归并，**逐字段取最大值**，不丢弃字段也不重复计数。
- 两条值相同 → 结果不变：10 月去重后 `print 47` 与 `monthlist` 的 `47` 完全对得上；
- 两条各只有部分字段 → 两个字段都会保留（不丢数据）；
- 不能累加（两条相同时会把 10 月算成 94）。
- 日历保留**所有日期**（0 值日期也在网格里，只是没有数量角标）；头部月合计优先取 `monthlist`
  （它有 `daylist` 未覆盖的更早月份，如 7/8 月），没有对应月份时才用逐日求和。

#### 配置字段

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `name` | 否 | `string` | 标题（默认 `HP Printer`） |
| `entity` | 否 | `string` | 「全部实体」聚合实体，默认 `sensor.hp_printer_quan_bu_shi_ti`；兼容填用量统计实体 |
| `width` | 否 | `string` | `card` 动作下弹窗宽度（默认 `560px`），`popup_card` 下用 `tap_action.width` |
| `popup_position` | 否 | `string` | 弹窗位置（默认 `center`），`popup_card` 下用 `tap_action.popup_position` |
| `today_print` | 否 | `string` | 今日作业记录实体；新版会自动认出，一般不用配 |
| `colors` | 否 | `object` | 各类型颜色（见下），**一处配置全局生效** |
| `api_base_url` | 否 | `string` | 历史明细 / 逐日补数接口前缀；不配则只能看实体本地保留期内的数据 |
| `key` | 否 | `string` | 上述接口的鉴权 key（与 `api_base_url` 成对出现） |

**`colors`（类型颜色，可选）**：图标色、日历热力图底色/角标/今日描边、头部合计胶囊、
累计总量小卡、月度折线图、墨盒环形图、明细气泡色点，**全部取自这一份配置**，改一处必然同步。

```yaml
card:
  type: printer
  colors:
    print: '#fb8c00'        # 打印（默认）
    scan: '#8e24aa'         # 扫描（默认）
    copy: '#00897b'         # 复印（默认）
    fax: '#78909c'          # 传真（默认）
    jam_printer: '#e53935'  # 卡纸（默认）
    all: '#fb8c00'          # 日历「全部」筛选的综合色
```

> 颜色可写 hex、`rgb()`、`hsl()` 或 `var(--xxx)`；热力图的浅色底由类型色自动混算。
> 取值优先级：按钮 `card` 配置 → 本次弹窗缓存 → 整卡配置。

#### 卡片布局

```
┌──────────────────────────────────────────┐
│ 🖨 HP 7730            [打印][耗材]…      │  ← 标题 + 状态副标题 + 4 个选项卡
│    在线 · 空闲                            │
├──────────────────────────────────────────┤
│ 设备状态                                  │
│ [● 设备 在线][● 打印机 空闲][● 错误 无]   │
│ 今日用量 · 2026-10-21                     │
│ [🖨 打印] [⇄ 扫描] [⧉ 复印] [🖯 传真] [⚠ 卡纸] │  ← 图标+名称一行，数值下一行
│    12        3        1        0        0 │
│ 月度统计（表格，点月份看折线图）           │
│ 累计总量                                  │
│ [累计打印 9970][累计扫描 1119]…           │  ← 每格用该类型自己的颜色
│ 近日记录                      [全部 ▾]    │  ← 下拉：全部/打印/扫描/复印/传真/卡纸
│ ‹ 2026年10月 ›                 打印 20    │  ← 合计胶囊同色跟随筛选类型
│ 一 二 三 四 五 六 日                      │
│ ▢ ▢ ① … ⑳ 8 ㉑ 12 …                      │  ← 日期=实心圆徽章；数量=彩色角标
│                          少 ▢▢▢▢▢ 多      │  ← 热力图图例
│ 数据维护                                  │
│ [补齐历史用量] [重新加载用量数据]          │  ← 点击弹确认框
├──────────────────────────────────────────┤
│ 耗材：墨量概览（4 色墨盒卡，点开墨量曲线） │
│       墨盒详情（每色两行卡 + 环形图）      │
├──────────────────────────────────────────┤
│ 统计：打印 / 复印 / 扫描 / 传真 / 异常 分组格子│
├──────────────────────────────────────────┤
│ 事件：事件日志（时间/描述/次数/页数）+ 今日卡纸│
└──────────────────────────────────────────┘
```

#### 交互说明

- **设备状态**：三块（设备 / 打印机 / 错误），带状态色点。**设备只显示「在线 / 离线」**（"运行中"→ 在线，`离线/offline/unavailable/unknown` → 离线）。
  **错误**：空错误码一律显示「无」（绿点）——`错误()`、`错误(0)`、`错误（）`、`错误( 0 )`、`错误(０)`、`Error()` 都算；
  `错误(12)`、`错误（缺纸）` 这类有内容的仍原样显示（红点）。
  每块还带 `data-raw-state` 属性，悬停 `title` 与属性里都是**集成原始值**，便于排查。
- **选项卡**：打印 / 耗材 / 统计 / 事件，页签在标题行右侧；支持左右滑动切换，颜色为**橙色**（可用 `accent` 覆盖）
- **高度**：以第一个选项卡「打印」为准锁定（`basis:'first', fit:'exact'`），切页不跳高度，超出内容页内滚动；头部吸顶 + 滚动羽化
- **今日用量**：5 张卡，「图标 + 名称」同一行、数值另起一行居中；图标色与日历热力色同源。
  配置了今日作业记录实体后，点击卡片弹该类别当日**逐条明细**（时间 / 张数 / 时长）
- **累计总量**：5 张卡（累计打印 / 扫描 / 复印 / 传真 / 卡纸），每张用该类型自己的颜色（淡底 + 同色字）
- **近日记录（日历）**：
  - 月视图，周一为第一天；**热力图**按当天数值分 5 档着色（当月该类型单日最大值为基准），今日加同色描边；
  - 日期是**实心圆徽章**、数量是**彩色角标**（带白描边），二者形状不同便于区分；
  - 标题行右端下拉可筛「全部 / 打印 / 扫描 / 复印 / 传真 / 卡纸」，日历头部**合计胶囊**的文字与底色跟随当前类型；
  - 日历下方有 `少 ▢▢▢▢▢ 多` 热力图图例；`‹ ›` 翻月，翻到缺数据的月份时按需向后端补数（见下）；
  - **点击有记录的日子**：优先直接用「用量统计」实体的 `daylist` 汇总（**不发请求**），
    今日且配了今日作业记录实体时改用逐条明细；只有 `daylist` 覆盖不到的日期才走 `printer_detail` 接口
- **月度统计**：表格点某个月份 → 该月每日各类型折线图（x 轴刻度自适应，不再重叠）
- **墨盒卡**：剩余 ≤20% 标红，点击弹该墨盒的历史墨量曲线（来自 `daylist` 的 `ink_*`；x 轴刻度自适应）
- **墨盒详情**：每色一张两行小卡 —— 第一行「色点 + 颜色名 + 状态徽章」，第二行「更换 / 原装墨量 / 累计用墨 / 序列号」
- **各色累计用墨占比（环形图）**：墨盒详情下方；右侧竖排图例（带数值）、环心显示合计、
  外部拉线标签显示占比；扇形颜色与墨盒色点一致
- **数据维护**：聚合清单里的两个 **`button` 域**实体 ——「补齐历史用量」「重新加载用量数据」，
  位于「打印」页日历下方。点击先弹**确认对话框**（补齐/重载各带一句说明），
  确认后通过**统一动作系统**执行（`call-service: button.press`），成功后右下角 toast 提示。
  按钮只认 `button.` 前缀，关键字误命中 sensor 时不会凭空生成按钮；legacy 模式（只配用量统计实体）没有这段。
- **事件日志**：最多渲染 120 条，最新在上

#### 数据与单位约定

- **累计用墨 = 更换次数 × 每盒原装墨量**（例：6 次 × 217ml = 1302ml）。
  集成自带的「累计用墨量」实体实测等于单盒容量（没乘次数），只在原装墨量 / 更换次数取不到数时兜底。
- **单位动态**：单位优先取实体自己的 `unit_of_measurement`（`ml` / `L` / 页…），缺失才回退 `ml`（更换次数回退 `次`）。
- **容量进位**：≥1000ml 自动显示为 L 并保留两位小数（`1302ml` → `1.30L`）；未到 1000 仍是整数（`217.0ml` → `217ml`）。
- **`daylist` / `monthlist` 去重**：集成每次写两条相同记录，卡片按 `day` / `month` 归并、**逐字段取最大值**（不累加、不丢字段）。
- **历史补数**：配了 `api_base_url` + `key` 时，日历翻到 `daylist` 未覆盖的月份会自动按天补齐（每月份只试一次）；
  没配接口时只显示 `monthlist` 的月汇总，并在日历下方给一行说明。

> **依赖说明**：需要生成「全部实体」聚合实体（`sensor.hp_printer_quan_bu_shi_ti`）的打印机集成。页面纯 DOM 构建（无 `innerHTML` 拼接），CSS 全部外置到 `room-elves-card-styles.css`。

---

### 6.37 飞牛 fnOS 全实体卡片 (type: fnos)

飞牛 fnOS 全实体卡片以**单个聚合实体**驱动整台飞牛的面板：只读 `sensor.fnos_all_entities` 的 `attributes.groups[]`（整机 + 全部 Docker 容器 + 全部虚拟机 + 文件 / 相册 / 影视的实体目录），**卡片不写死任何实体 id**，集成侧新增容器 / 虚拟机 / 应用时卡片无需改一行配置。

卡片最多只配置一个实体（`entity`）；不配置时自动使用内置的 `sensor.fnos_all_entities` 兜底（HA 里 id 被占号生成 `_2` 后缀也能识别）。

> 本卡（`fnos`）以聚合实体驱动：只依赖下面这套实体目录，不需要逐个填写 sensor / switch / button 的实体 id（旧的 `fnnas` 卡片已移除）。

#### 依赖集成

| 项 | 说明 |
|------|------|
| 集成 | **飞牛 fnOS 集成（fnos）** |
| 集成地址 | https://github.com/chjspp520/fnos |
| 必需实体 | `sensor.fnos_all_entities`（聚合实体，`attributes.groups[]` 即整机实体目录） |
| 其余实体 | 各组内的 `sensor` / `binary_sensor` / `switch` / `button`（由集成自动生成，卡片按分组与名称自动识别，无需配置） |

#### 配置示例

```yaml
# ① 常规：popup_card（点击按钮在房间卡片内弹出）
  - entity: input_boolean.fei_niu
    type: sensor
    name: 飞牛
    icon: mdi:nas
    tap_action:
      action: popup_card
      card:
        type: fnos
        # entity: sensor.fnos_all_entities   # 可选，不配就用它兜底
        name: 飞牛 fnOS                       # 可选，标题（默认「飞牛 fnOS」）
        icon: mdi:nas                         # 可选，标题图标
        accent: "#26a69a"                     # 可选，主色
        popup_width: 900px                    # 可选，弹窗宽度（兼容 width）
        popup_position: center                # 可选，弹窗位置
        confirm_power: true                   # 可选，重启/关机是否二次确认（默认 true）

# ② action: card（独立弹窗）
    tap_action:
      action: card
      card:
        type: fnos

# ③ 独立常显（standalone_type）
type: custom:room-elves-card
standalone_type: fnos
# entity: sensor.fnos_all_entities
```

#### 配置字段

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `entity` | 否 | `string` | 聚合实体 ID，默认 `sensor.fnos_all_entities`（被占号时自动识别 `_2` 后缀） |
| `name` | 否 | `string` | 卡片标题（默认 `飞牛 fnOS`） |
| `icon` | 否 | `string` | 标题图标（默认取聚合实体 icon，兜底 `mdi:nas`） |
| `accent` | 否 | `string` | 主色，写入本卡根元素的 `--re-accent*`，不影响全局。**默认琥珀橙 `#f59e0b`**（蓝 / 绿 / 紫 / 红已被其它卡片占用，飞牛用橙系区分） |
| `popup_width` / `width` | 否 | `string` | 弹窗宽度（默认 `900px`，最大 `94vw`） |
| `popup_position` | 否 | `string` | 弹窗位置（默认 `center`） |
| `confirm_power` | 否 | `boolean` | 重启 / 关机 / 强制关机等危险按钮是否二次确认（默认 `true`） |

#### 卡片结构

头部：图标 + 标题 + 副标题（**只显示 CPU 占用率**，如 `CPU 15%`）。选项卡按聚合实体里**真实存在的分组**动态生成 —— 没有 Docker 分组就不出现「Docker」页，没有虚拟机分组就不出现「虚拟机」页。

页内每个**区域（区块）都是常显的**：标题行没有折叠箭头、点击也不会折叠，所有内容一次性建好并参与 3 秒值级刷新（不会出现"折叠着就看不到实时值"的情况）。

| 选项卡 | 内容 |
|------|------|
| 主机 | **概览仪表**：CPU / 内存 / GPU 三个圆环（纯 SVG 百分比弧 + 中心大数字，≥80% 转深橙、≥90% 转红；**内存环下方另写「已用 / 总量」**，**点环弹出历史曲线气泡**：6 小时 / 24 小时 / 7 天三档切换 + 最低 / 平均 / 最高统计 + 首末时间轴，气泡内「查看全部属性」可跳到属性面板）；**网络与磁盘**：下载 · 上传、磁盘读 · 写各一张**双线迷你面积曲线**（卡片内每 2.5 秒采样、40 点滚动 ≈ 2 分钟，顶部留白自动缩放）；**系统信息**：版本 / 更新 / 网卡 / 硬盘 / 登录设备 / 未读通知 + Docker·虚拟机·证书·域名·FN Connect 胶囊（右上「硬件」按钮看硬件属性）；**存储概况**：使用率进度条 + 总 / 已用 / 可用 / 异常硬盘；**服务开关**：远程控制 / SSH / SMB / NFS / FTP / WebDAV / DLNA / 防火墙；**系统操作**：重启 / 关机 / 打开面板 |
| 存储 | **存储池**：名称 + 状态胶囊 + 使用率进度条 + 类型·磁盘数·挂载点 + 已用 / 可用 / 总容量；**硬盘**：设备 + 容量标签 + 系统盘徽标 + 型号·类型·温度·存储池 + 健康状态胶囊 |
| Docker | 顶部「运行中 / 总数」计数；每个容器一行：状态点 + 名称 + 状态徽标（运行中 / 已退出 / 异常…）+ CPU·内存 + 重启按钮 + 电源开关 |
| 虚拟机 | 每台一张卡：状态点 + 名称 + 电源状态 + 电源开关；资源胶囊（IP / vCPU / 内存 / 磁盘）；系统 / MAC 标签；重启 / 强制关机 / 打开远程 |
| 应用 | **文件**（最近 / 收藏 / 回收站 / 分享链接数 + 打开应用）、**相册**（可用状态 / 最近添加 / 打开）、**影视**（可用状态 / 打开） |

#### 交互说明

- **开关**：点击即启停（`switch.turn_on` / `switch.turn_off`）；实体为 `unknown` / `unavailable` 时开关置灰且不可点
- **按钮**：重启 / 关机 / 强制关机 / 容器重启等先二次确认（`confirm_power: false` 可关闭确认），执行后立即刷新并延时补刷两次
- **历史曲线气泡**：点击 CPU / 内存 / GPU 三个圆环，弹出该实体的历史曲线 —— 顶栏是实时值，下面是 `6 小时 / 24 小时 / 7 天` 三档范围胶囊（切换即重新取数）、最低 / 平均 / 最高统计、SVG 曲线（网格 + 面积 + 折线 + 末端圆点 + 首末时间轴），数据走宿主统一的 `getHistory`；没有历史数据时给明确提示。气泡内「查看全部属性」可跳到属性面板
- **属性气泡**：点击指标格、容器行、硬盘行、虚拟机卡，弹出该实体的实时值 + 全部属性（对象 / 数组自动分层，数组最多列 30 行）；气泡内的开关 / 按钮可直接操作
- **打开远程**：应用行与「打开面板」使用实体 `attributes.url` 的签名地址（24h 有效），取不到时给出提示
- **进度条 / 圆环配色**：常态跟随主色（琥珀橙），使用率 ≥80% 转深橙、≥90% 转红
- **迷你曲线**：网络 / 磁盘各一条双线面积图，数据是卡片自己按 2.5 秒节流采样（hass 推送再频繁也不会把时间轴压缩），最多 40 点、纯 SVG 绘制，不加载 ECharts

#### 数据口径与刷新

- 聚合实体只当**实体目录**用；实时值一律回 `hass.states` 现读，所以点开关后界面立即跟随，不用等聚合实体下一次合并刷新
- 结构签名（有哪些实体 / 属于哪一组 / 存储池与硬盘清单）变化才整卡重建；值变化走 **3 秒值级刷新**，只写发生变化的文本 / 宽度 / 类名（脏检查）
- 页面不可见时跳过刷新，卡片脱离 DOM 自动停表；独立模式下不依赖外部 1 秒轮询（`standalonePoll: false`），高度由内容决定（`height: auto`）

> **依赖说明**：数据来源于 [飞牛 fnOS 集成](https://github.com/chjspp520/fnos)，使用前需先安装并配置该集成，由它生成聚合实体 `sensor.fnos_all_entities` 及其分组实体。页面纯 DOM 构建（无 `innerHTML` 拼接），CSS 全部外置到 `room-elves-card-styles.css` 的 `.fnos-card-*` 段。

---

### 6.38 实体健康状态卡片 (type: entities_health)

实体健康状态卡片用于以房间/状态两个维度展示全屋实体的在线/离线情况。数据来源为实体健康监控实体（`sensor.hashu_ju_tong_yi_cun_chu_xi_tong_frontend_card_entities_health`）的 `attributes`（`total` / `online` / `offline` / `entities[]`）。

点击按钮弹出实体健康状态面板，支持通过 `popup_card` 或 `card` 动作打开。

```yaml
  - entity: input_boolean.she_shi_jian_kang
    type: sensor
    name: 实体健康
    icon_text: preset_state
    on_icon: mdi:monitor-cellphone
    off_icon: mdi:monitor-cellphone
    on_color: "#27ae60"
    off_color: "#e74c3c"
    tap_action:
      action: popup_card                 # 或 action: card（走独立弹窗）
      popup_position: center
      width: 400px                       # 外层弹窗宽度（可选）
      card:
        type: entities_health
        entity: sensor.hashu_ju_tong_yi_cun_chu_xi_tong_frontend_card_entities_health  # 可选，默认此实体
        hide_room: 次卧外,儿童房外,楼道,客厅外   # 可选，逗号分隔，户型图中不显示这些房间
```

#### 配置字段

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `entity` | 否 | `string` | 实体健康监控实体 ID，默认 `sensor.hashu_ju_tong_yi_cun_chu_xi_tong_frontend_card_entities_health` |
| `name` | 否 | `string` | 弹窗标题（显示在顶部，默认 `实体健康状态`） |
| `hide_room` | 否 | `string` | 逗号分隔的房间名，这些房间不在户型图中绘制（如 `次卧外,儿童房外`），默认不隐藏 |
| `width` | 否 | `string` | `card` 动作下弹窗宽度（默认 `600px`），`popup_card` 下用 `tap_action.width` |
| `popup_position` | 否 | `string` | 弹窗位置（默认 `center`），`popup_card` 下用 `tap_action.popup_position` |

#### 卡片布局

弹窗含两个选项卡（位于标题右侧）：**按房间** / **按状态**。

```
┌────────────────────────────────┐
│ 图标  实体健康状态  [按房间|按状态]│  ← 头部 + 选项卡（标题右侧）
├────────────────────────────────┤
│ 实体总数  在线    离线           │  ← 顶部整体统计（三卡）
│  [481]   [453]   [28]          │
├────────────────────────────────┤
│ 房间分布                        │  ← 户型图（红绿双色）
│  [户型图 SVG：房间多边形+角标]   │
│  在线数·离线数（离线>0 红/全在线绿）│
├────────────────────────────────┤
│ 房间实体状态                     │  ← ECharts 横向堆叠柱状图
│  [每房间 在线(绿)+离线(红)]      │
└────────────────────────────────┘
```

- 卡片高度以"按房间"面板为基准固定，切换选项卡时高度不变，"按状态"列表在相同高度内滚动
- 状态列表默认在卡片高度内滚动（`overflow-y: auto`），不撑高卡片

#### 按房间选项卡

从上到下分三部分：

1. **顶部整体统计**：实体总数 / 在线数 / 离线数三个统计卡，离线卡红色高亮，每个卡为"图标+名称一行、数值一行"（数值 18px）
2. **户型图**：读取卡片配置 `entities_tap_action.card.rooms` 的房间几何，每个房间按健康状态着色——**存在离线房间红色系，全部在线房间绿色系**；房间内叠加"在线 x · 离线 y"角标；`hide_room` 指定的房间不绘制且不参与画布尺寸计算
3. **ECharts 横向堆叠柱状图**：每个房间一个堆叠条 = 在线（绿）+ 离线（红），点击柱体显示数值

#### 房间气泡

点击户型图中的房间，以气泡形式（`_showBubble`，径向模糊遮罩、点击处清晰周围模糊）显示该房间的设备列表，气泡含两个选项卡：

- **在线 / 离线**（优先显示"离线"选项卡）
- 列表项：状态点 + 图标 + 设备名 + 当前状态值，点击设备行打开 HA 更多信息对话框
- 气泡高度固定，切换选项卡时三角指示器不错位

#### 按状态选项卡

- 全屋实体列表，**离线实体整体置顶**，各自内部按名称字符排序（`localeCompare('zh')`）
- 每行：状态点（绿/红）+ 图标 + 名称 + 房间名 + 当前状态值
- 点击行打开 HA 更多信息对话框
- 列表自适应卡片高度，内容超高时内部滚动

#### 交互说明

- **选项卡**：点击"按房间/按状态"切换，卡片高度固定不变
- **气泡**：房间点击弹出，默认显示离线设备，可切换在线
- **实体行**：点击打开 HA 实体更多信息面板

> **依赖说明**：实体健康卡片数据来源于实体健康监控实体（`sensor.hashu_ju_tong_yi_cun_chu_xi_tong_frontend_card_entities_health`），需由统一存储系统生成该实体（`attributes.total/online/offline/entities[]`）。页面纯 DOM 构建（无 `innerHTML` 拼接），CSS 全部外置到 `room-elves-card-styles.css`。

### 6.39 今日家庭日报卡片 (type: daily_report)

今日家庭日报卡片用于展示后端统一存储系统聚合的「今日家庭状态日报」。数据来源为 `sensor` 实体（默认 `sensor.hashu_ju_tong_yi_cun_chu_xi_tong_frontend_card`），读取 `state`/`summary`/`overall`/`alerts`/`sections`/`lights`/`offline`/`generated_at` 等属性。

点击按钮弹出日报弹窗，支持通过 `popup_card` 或 `card` 动作打开。

```yaml
  - entity: input_boolean.jin_ri_jia_ting
    type: sensor
    name: 今日日报
    icon_text: preset_state
    on_icon: mdi:clipboard-text-clock-outline
    off_icon: mdi:clipboard-text-clock-outline
    tap_action:
      action: popup_card                 # 或 action: card（走独立弹窗）
      popup_position: center
      card:
        type: daily_report
        entity: sensor.hashu_ju_tong_yi_cun_chu_xi_tong_today_family_status  # 可选，默认日报实体
        refresh: button.hashu_ju_tong_yi_cun_chu_xi_tong_generate_today_family_status  # 可选，刷新按钮实体
        hide_room: 次卧外,儿童房外,楼道,客厅外   # 可选，今日用电弹出的能耗中心使用
        env_from_config_id: env          # 可选，温度/湿度点击弹出的温湿度卡 config_id
        width: 400px
        name: 今日家庭日报
```

#### 配置字段

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `entity` | 否 | `string` | 日报数据实体 ID，默认 `sensor.hashu_ju_tong_yi_cun_chu_xi_tong_frontend_card` |
| `refresh` | 否 | `string` | 刷新按钮实体 ID（`button.*`）。配置后头部显示「刷新」按钮，点击按压该按钮触发后端重新生成，等待 5 秒后刷新弹窗数据；未配置时回退调用 `ha_data_store.generate_daily_summary` 服务 |
| `hide_room` | 否 | `string` | 逗号分隔的房间名，点击「今日用电」弹出的能耗中心（energy_center）使用 |
| `env_from_config_id` | 否 | `string` | 点击「温度/湿度」时，从全局配置存储器 `RoomElvesStore` 读取该 `config_id` 的温湿度卡片并弹出；宽度取被引用卡自身的 `card_width`/`width` |
| `width` | 否 | `string` | 日报弹窗宽度，默认 `400px` |
| `name` | 否 | `string` | 弹窗标题（默认 `今日家庭日报`） |
| `show_refresh` | 否 | `boolean` | 是否显示刷新按钮，默认 `true`；`false` 时 warning 状态仍显示原「提醒」徽章 |

#### 卡片布局

```
┌────────────────────────────────────┐
│ 图标  今日家庭日报  更新于16:00 [刷新]│  ← 头部（徽章，warning 时为刷新按钮）
├────────────────────────────────────┤
│ ⚪ 家中有人（大卫生间）、开着1盏灯…    │  ← 状态横幅（按 overall 着色）
├────────────────────────────────────┤
│ 今日概览                            │  ← summary 长文本（按语义分组换行）
│ 今日家庭状态：气温…湿度73.2%；       │
│ 家中有人…开着1盏灯…；               │
│ 今日共16台设备启用…；               │
│ 用电最多…；开关最频繁…；            │
│ 今日用电…；小爱对话…离线设备8台；    │
├────────────────────────────────────┤
│ 提醒                               │  ← 警告列表（有 alerts 才显示）
│ ⚠ 今日最高温 39.7°C 偏高           │
├────────────────────────────────────┤
│ 关键指标                            │  ← 6格指标网格
│ [◎温度] [◎湿度] [◎今日用电]       │
│ [◎设备] [◎灯光] [◎离线设备]       │
└────────────────────────────────────┘
```

#### 指标项点击行为

| 指标项 | 点击行为 |
|--------|----------|
| 温度 / 湿度 | 读取 `env_from_config_id` 对应的温湿度卡配置（`RoomElvesStore.get(id).card`）弹出；宽度取被引用卡自身的 `card_width`/`width` |
| 今日用电 | 弹出 `energy_center`（写死 `name: 全屋用电量`），`hide_room` 取日报顶层 `hide_room`，宽度复用日报 `width` |
| 灯光 | 弹出与概览条灯光段一致的 `light-control-popup theme-light`（聚合已打开灯光） |
| 离线设备 | 复用 notice 中已配置的 `entities_health` 卡片配置弹出（含 `entity`/`hide_room`/`unique_priority`） |

#### summary 语义分组

summary 长文本按全角分号 `；` 切成项，依据每项开头的语义锚点归入对应行（行内保留分号）：

| 行 | 锚点 |
|----|------|
| 0 | `今日家庭状态`（温度/湿度） |
| 1 | `家中有人`/`全屋无人`、`入户门`、`开着`/`关着` |
| 2 | `今日共`、`总运行`、`其中` |
| 3 | `用电最多` |
| 4 | `开关最频繁` |
| 5 | `今日用电` |
| 6 | `小爱对话`、`离线设备` |

锚点缺失时该项自动合并到前一行，保证 summary 顺序/措辞微调时不错行。

> **依赖说明**：日报卡片数据来源于后端统一存储系统生成的「今日家庭状态」实体（`state`/`attributes.summary` 等）。若配置了 `refresh` 按钮实体，后端需注册该 `button.*` 实体用于触发重新生成。页面纯 DOM 构建（无 `innerHTML` 拼接），CSS 全部外置到 `room-elves-card-styles.css`。

### 6.40 设备回放卡片 (type: replay)

把「户型图 + 设备事件时间轴」做成可播放的一天回放：上半部分是户型平面图，回放中的设备按配置坐标摆放、随时间点亮/熄灭，还可叠加传感器数值气泡；下半部分是每个设备一条轨道的时间轴，底部时间滑块可拖动、可变速播放，并可切换日期回看历史某一天。

数据来自 Home Assistant 的事件/历史接口与后端统一存储系统的历史查询接口（见本节末尾「后端接口」）。

#### 四种使用方式

**① 独立卡片（常显）**

```yaml
type: custom:room-elves-card
standalone_type: replay
card_width: 500                     # 设计基准宽度（实际随容器等比缩放）
floorplan_height: 400               # 户型图高度（同样按比例缩放）
background_image: /local/pobaby_package/floorplan/1f.png
entities:
  - entity: light.ke_ting
    name: 客厅-大灯
    x: 0
    y: 0
    image_url: /local/pobaby_package/device/ke_ting_on.png
    image_scale: 100
  - entity: climate.ke_ting
    name: 客厅-空调
    x: 300
    y: 100
    image_url: /local/pobaby_package/device/kong_tiao.png
    image_scale: 30
    rotation: 90
```

**② 设备按钮（`buttons:` 里直接弹窗）**

```yaml
buttons:
  - type: replay
    name: 设备回放
    icon: mdi:history
    entities: [ ...同上的回放设备列表... ]
```

按钮本身不渲染成设备卡片，点击弹出回放卡弹窗；**再点一次关闭**。

**③ `tap_action: card`**

```yaml
tap_action:
  action: card
  popup_position: center
  card:
    type: replay
    entities: [ ... ]
```

**④ `tap_action: popup_card`**

```yaml
tap_action:
  action: popup_card
  popup_position: center
  width: 760px
  card:
    type: replay
    entities: [ ... ]
```

#### 顶层配置字段

| 字段 | 必填 | 类型 | 默认 | 说明 |
|------|:----:|------|------|------|
| `entities` | **是** | `array` | — | 回放设备列表，每项见下一节。为空时卡片不渲染数据 |
| `card_width` | 否 | `number` | `400` | **设计基准宽度**。设备坐标、图标尺寸都按它书写；实际渲染尺寸 = 基准 ×（容器宽度 / 基准），即卡片会随容器等比缩放 |
| `floorplan_height` | 否 | `number` | `400` | 户型图高度（设计基准），同样参与等比缩放 |
| `background_image` | 否 | `string` | — | 户型图背景图 URL |
| `background_left` / `background_top` | 否 | `number` | `0` | 背景图偏移（设计基准像素）。设备坐标会叠加这个偏移 |
| `background_scale` | 否 | `number` | `100` | 背景图宽度 = `card_width × scale / 100` |
| `device_track_height` | 否 | `number` | `20` | 每条设备轨道的高度（px） |
| `device_track_font-size` | 否 | `number` | `12` | 轨道左侧设备标签的字号（px） |
| `device_label_align` | 否 | `string` | `left` | 轨道标签文字对齐：`left` / `center` / `right` |
| `min_duration_filter` | 否 | `number` | `0` | 过滤掉持续时长小于该值（秒）的事件，避免瞬时抖动刷屏 |
| `rooms` | 否 | `object` | 内置配色 | 轨道标签底色映射，`房间名: 颜色`，见下方 |
| `energy.entities` | 否 | `array` | — | 户型图上叠加的传感器数值气泡，见下方 |
| `api_base_url` | 否 | `string` | — | 后端统一存储系统地址（如 `http://192.168.1.10:8000/api/ha_data_store/`）。未配置时只回放 HA 当天状态变化 |
| `key` | 否 | `string` | — | 后端接口鉴权 key |
| `check_entity` | 否 | `string` | — | 后端可用性检查实体；配置后才启用历史日期与「有数据」标记 |
| `test_mode` | 否 | `boolean` | `false` | 编辑模式（保留给调试用） |
| `name` / `icon` | 否 | `string` | — | 作为按钮/卡片位时的显示名与图标（通用字段） |

> **透传继承**：这四种入口都支持直接复用外层卡片的 `api_base_url` / `key` —— 外层配置过就不必在回放卡里重复填写。

#### entities 配置字段（每个回放设备一项）

| 字段 | 必填 | 类型 | 默认 | 说明 |
|------|:----:|------|------|------|
| `entity` | **是** | `string` | — | 设备实体 ID（`light` / `switch` / `climate` / `media_player` 等）。它的状态变化构成回放事件 |
| `name` | 否 | `string` | 实体 ID | 设备名，同时用作轨道左侧标签文字；同名事件会归到同一条轨道 |
| `x` / `y` | 否 | `number` | `0` | 户型图坐标（按 `card_width` 设计基准书写，会随容器等比缩放） |
| `image_url` | 否 | `string` | — | 设备图标；不配置时退化为一个圆点 |
| `image_scale` | 否 | `number` | — | 图标宽度 = `card_width × scale / 100`（与下面两项**三选一**） |
| `image_width` / `image_height` | 否 | `number` | — | 图标固定像素宽/高（与 `image_scale` 三选一，同时配两者会报错并跳过） |
| `rotation` | 否 | `number` | `0` | 图标旋转角度（度），以元素左上角为原点 |
| `layer` | 否 | `number` | `1` | 层叠顺序，数值越大越靠上 |
| `color` | 否 | `string` | 按名称推断 | 无图标时的圆点颜色；同时作为该设备轨道填充色 |
| `on_state` / `on_states` | 否 | `string` / `array` | 内置常见开启态 | 自定义「开启」状态值（如 `open`、`playing`、`heat`、`on`），用于判定设备何时处于运行中 |
| `room` | 否 | `string` | 名称前缀 | 房间名，用于从 `rooms` 取轨道标签底色 |

#### energy.entities 配置字段（户型图数值气泡）

```yaml
energy:
  entities:
    - entity: sensor.ke_ting_gong_lv
      name: 功率
      unit: W
      x: 10
      y: 330
      color: "#ffffff"
      sensor_background_color: rgba(34, 197, 94, 0.8)
```

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `entity` | **是** | `string` | 传感器实体 ID |
| `name` | 否 | `string` | 气泡前缀文字（如 `功率`、`日用电`） |
| `unit` | 否 | `string` | 数值后缀单位 |
| `x` / `y` | 否 | `number` | 气泡位置（按 `card_width` 基准，随容器缩放） |
| `color` | 否 | `string` | 文字色 |
| `sensor_background_color` | 否 | `string` | 气泡底色 |

#### rooms 配置（轨道标签底色）

```yaml
rooms:
  客厅: "#ea5506"
  卧室: "#3498db"
  儿童房: "#9b59b6"
```

设备未显式配 `room` 时，按设备名里包含的房间关键字匹配；都匹配不到用内置默认色。

#### 卡片布局

```
┌──────────────────────────────────────────┐
│ 户型平面图                                │
│   背景图 + 设备图标（随回放时间点亮/熄灭）  │
│   + 传感器数值气泡                        │
├──────────────────────────────────────────┤
│ ◀  2026-09-27  ▶  此刻    1x ▾   [播放]   │  ← 控制条
├──────────────────────────────────────────┤
│ 客厅-大灯  ▓▓▓░░▓▓▓▓░░▓▓░░▓▓              │  ← 每个设备一条轨道
│ 客厅-空调  ░▓▓░░░░▓▓░░▓▓▓░                │     悬停显示当天明细
├──────────────────────────────────────────┤
│ ────────────●──────────────  15:55        │  ← 时间滑块（可拖拽）
│ 00:00   04:00   08:00   12:00   16:00 …   │
└──────────────────────────────────────────┘
```

#### 交互操作

| 操作 | 行为 |
|------|------|
| 拖动时间滑块 | 跳到该时刻（平面图与轨道同步刷新） |
| 播放 / 暂停 | 以所选速度自动推进时间 |
| 速度选择 `1x` / `5x` / `10x` / `30x` | 播放倍速 |
| `◀` / `▶` / `此刻` | 前一天 / 后一天 / 回到今天 |
| 点击日期框 | 弹出日期选择器（月历，带「有数据」标记：`H` = HA 有数据、`A` = 后端有数据） |
| 悬停设备轨道 | 气泡显示该设备当天的运行明细（时间段 + 时长） |

#### 后端接口与依赖

| 用途 | 接口 / 方法 |
|------|------|
| 实时事件 | HA WebSocket `subscribe_events(state_changed)`（订阅失败时自动降级为 2 秒轮询） |
| 状态历史 | HA WebSocket `history/history_during_period` |
| 环境数据（气泡数值） | `?type=env_history&key=...` |
| 房间日统计 | `?type=rooms_daily&key=...` |
| 日期选择器（年月 / 天标记） | `?type=device_data_periods&key=...`（`level=year` / `level=month&year=YYYY` / `level=day&month=YYYY-MM` 三档，**全局口径**不带 `entity_id`） |

> 未配置 `api_base_url` / `key` 时，只回放 HA 自身能查到的当天状态变化，日期选择器回到"年月都可选"的乐观渲染（不置灰、不标 A）。

#### 说明与已知边界

- **样式与主题**：全部样式在 `room-elves-card-styles.css`（作用域 `.device-replay-card-host`），配色跟随房间精灵主题（`--room-*`）。**例外**：按钮（蓝底白字）、时间轴与时间指示器（红色）、tooltip（蓝底白字）是回放卡自身的语义色，固定不跟随主题。
- **尺寸自适应**：`card_width` / `floorplan_height` 是设计基准，卡片随容器宽度等比缩放（独立卡片铺满容器、弹窗内随弹窗宽度），高分屏按 `devicePixelRatio` 渲染。
- **渲染方式**：纯 DOM API 构建（无 `innerHTML` 字符串拼接）；定时器注册在房间精灵的 `TimerManager` 上，后台标签页自动跳过重绘。
- **性能**：设备数量多、或外层卡片秒级刷新时，建议给 `min_duration_filter` 设置一个非零值（如 `30`）过滤瞬时事件。
- **原独立卡片已退役**：本卡片由独立卡片 `device-replay-card.js` 迁移而来，迁移后不再作为独立的 `custom:device-replay-card` 元素注册，配置需按上面的四种方式重写。

#### 扩展接口（供其它模块调用）

实现位于 `modules/cards/device-replay.js`，引擎封在模块内的 `DeviceReplayElement` 中，只对外暴露三个方法（注册在卡片原型上）：

| 方法 | 签名 | 说明 |
|------|------|------|
| `createDeviceReplayCard` | `(config, options) => HTMLElement` | 创建回放卡，返回卡片根元素。内部顺序：`setConfig`（此时无 hass，不渲染）→ `connectedCallback` → 注入 hass（触发 `render` 与取数）。元素上挂 `root.__replayEl` 指向引擎实例 |
| `updateDeviceReplayCard` | `(card, config) => void` | 宿主 hass 变化或配置变化时调用。用「配置引用 + 指纹」短路，配置没变时只注入 hass、不重建卡片 |
| `showDeviceReplayPopup` | `(config, triggerButton) => boolean` | 弹出回放卡弹窗（`showPopup`，`className: device-replay-popup-root`）。**已打开时再调用会关闭**（设备按钮的 toggle 语义），关闭/被替换时调 `el.destroy()` 收尾 |

分派链路：

| 入口 | 链路 |
|------|------|
| `standalone_type: replay` | `standalone.js` → `_resolveCardEntry` → `COMPOSITE_CARD_REGISTRY.replay` → `createDeviceReplayCard` |
| `cards:` 区 / `popup_card` | `card-factory.js` → 注册表统一分派 → `createDeviceReplayCard` |
| 设备按钮 `type: replay` | 按钮点击 → `showDevicePopup` → `popup-show.js` 的 `type === 'replay'` 委托 → `showDeviceReplayPopup` |
| `action: card` + `card.type: replay` | `actions.js` 的 `case 'replay'` → `showDeviceReplayPopup` |

> 引擎实例的 `destroy()`（内部即 `disconnectedCallback`）会清理：事件订阅、托管定时器与 `rAF`、`ResizeObserver`、日期选择器弹窗、文档级监听与各类缓存 —— 弹窗关闭或被替换时由 `onClose` / `onDestroy` 调用。

### 6.41 定时精灵卡片 (type: timer)

「延时 / 定时执行设备动作」的控制台：主界面显示倒计时时间框与进行中的任务，点击可打开**设置弹窗**新建设备定时器（选设备 → 选时长或时间点 → 选动作），也可以在**任务列表弹窗**里查看、取消已有任务与历史记录。

任务由后端 **HA 数据统一存储系统** 统一管理，分两类：**延时任务**（倒计时结束后执行，如「30 分钟后关灯」）与**定时任务**（指定时间点、可每天/每周/每月重复）。卡片通过 `sensor.ha_data_store_timer` 读取列表，通过 HA 事件与后端交互（见下方「后端依赖」）。

#### 四种使用方式

**① 独立卡片（常显）**

```yaml
type: custom:room-elves-card
standalone_type: timer
entity: light.ke_ting            # 默认选中的设备（可选）
default_duration: "00:30:00"     # 默认时长，默认 00:30:00
card_style: mini                 # mini / normal / icon
```

**② 设备按钮（`buttons:` 里直接弹窗）**

```yaml
buttons:
  - type: timer
    name: 定时精灵
    icon: mdi:timer-cog-outline
```

按钮本身不是设备卡片，点击弹出「任务中心」；再点一次关闭。图标模式（`card_style: icon`）下显示任务数徽章。

**③ `tap_action: card`**

```yaml
tap_action:
  action: card
  card:
    type: timer
    card_style: normal
```

**④ `tap_action: popup_card`**

```yaml
tap_action:
  action: popup_card
  popup_position: center
  card:
    type: timer
```

#### 三种卡片形态（`card_style`）

| 值 | 形态 | 说明 |
|----|------|------|
| `mini`（默认） | 小卡片：时间框 + 进度条 + 启动/取消按钮 | 适合塞进 `buttons:` 网格；`second_style: pull-down` 时点击时间框弹出时间选择器 |
| `normal` | 标准卡片：标题 + 时间框 + 任务滚动列表 | 高度由 `normal_height` 控制；点击标题打开任务列表弹窗 |
| `icon` | 图标模式：只显示一个图标（带任务数徽章） | 点击图标打开任务中心弹窗，适合只占用一个按钮位 |

#### 顶层配置字段

| 字段 | 必填 | 类型 | 默认 | 说明 |
|------|:----:|------|------|------|
| `entity` | 否 | `string` | — | 默认选中的设备；`mini`/`normal` 形态下显示为该设备的定时器（不配置则打开设置弹窗时自行选择） |
| `default_duration` | 否 | `string` | `00:30:00` | 默认时长（`时:分:秒`） |
| `card_style` | 否 | `string` | `mini` | 卡片形态：`mini` / `normal` / `icon` |
| `second_style` | 否 | `string` | `normal` | 为 `pull-down` 且 `card_style: mini` 时，点击时间框弹出时间选择器 |
| `icon` | 否 | `string` | `mdi:timer-cog-outline` | 图标模式的图标 |
| `show_buttons` | 否 | `boolean` | `true` | 是否显示启动 / 取消按钮 |
| `show_debug` | 否 | `boolean` | `false` | 显示调试信息 |
| `time_box_font_size` | 否 | `string` | `20px` | 时间框字号 |
| `time_box_width` / `time_box_height` | 否 | `string` | `auto` | 时间框尺寸 |
| `time_box_background` | 否 | `string` | `#f8f9fa` | 时间框背景色 |
| `time_box_progress_background` | 否 | `string` | `#1976d2` | 时间框内进度条颜色 |
| `timer_running_border` | 否 | `string` | `1px solid #1976d2` | 运行中卡片的边框 |
| `status_indicator_color` | 否 | `string` | `#28a745` | 状态指示点颜色（后端连接状态） |
| `status_indicator_width` / `status_indicator_height` | 否 | `string` | `6px` | 状态指示点尺寸 |
| `start_btn_color` | 否 | `string` | `#28a745` | 启动按钮颜色 |
| `start_btn_width` / `start_btn_height` | 否 | `string` | `auto` | 启动按钮尺寸 |
| `cancel_btn_color` | 否 | `string` | `#dc3545` | 取消按钮颜色 |
| `cancel_btn_width` / `cancel_btn_height` | 否 | `string` | `auto` | 取消按钮尺寸 |
| `normal_height` | 否 | `string` | `100px` | `normal` 形态的高度 |
| `normal_background` | 否 | `string` | 主题色 | `normal` 形态背景色（不配置则用 `--timer-card-bg`，即随主题） |
| `width` / `popup_position` | 否 | — | — | 弹窗宽度与位置（作为按钮/卡片位时的通用字段） |

> `theme` / `dark_light_theme` 配置项**保留但不再生效**（兼容旧配置）：配色统一由房间精灵主题提供。

#### 交互

| 操作 | 行为 |
|------|------|
| 点击时间框 | `second_style: pull-down` 时弹出时间选择器；否则进入设置 |
| 点击启动 | 按当前时长创建延时任务（`create_timer`） |
| 点击取消 | 取消该设备进行中的延时任务（`cancel_entity_timer`） |
| 点击标题 / 图标 | 打开任务列表弹窗或任务中心 |
| 任务项 | 显示进度条与剩余倒计时；定时任务显示距下次触发的时间 |
| 历史记录 | 任务列表弹窗内可筛选历史并清空（`clear_all_history`） |

#### 设置弹窗（添加定时器）

| 区块 | 内容 |
|------|------|
| 设备选择 | 按分类分组（灯光 / 气候 / cover / 风扇 / 媒体 / 开关 / 虚拟实体），支持搜索、可折叠 |
| 定时时长 | 时 / 分 / 秒输入 + 快捷时长按钮；可切换为**重复定时**：每天 / 每周几（`timer-day-btn`）/ 每月某日（`timer-monthly-day-btn`） |
| 定时动作 | `turn_off` 关闭 / `turn_on` 开启 / `toggle` 切换（`auto` 为按当前状态自动取反） |
| 任务概览 | 该设备当前已有的任务列表 |
| 底部按钮 | 取消 / 确定（确定时按类型发 `create_timer` 或 `create_schedule`） |

#### 后端依赖

| 用途 | 实体 / 事件 |
|------|------|
| 任务列表与进行中任务 | `sensor.ha_data_store_timer` 的 `all_task_list` 属性（含 `is_schedule`、`entity_id`、`remaining_seconds` / `schedule_countdown`、`status` 等） |
| 拉取全部任务 | 事件 `ha_data_store_timer_event`，`action: get_all_timers` |
| 新建延时任务 | `action: create_timer` |
| 新建定时任务 | `action: create_schedule` |
| 取消任务 | `action: cancel_entity_timer`（延时）/ `cancel_schedule`（定时） |
| 清空历史 | `action: clear_all_history` |
| 后端响应 | 订阅事件 `ha_data_store_timer_response` |

#### 扩展接口（供其它模块调用）

实现位于 `modules/cards/timer-control.js`，引擎封在模块内的 `TimerControlElement` 中，对外暴露：

| 方法 | 签名 | 说明 |
|------|------|------|
| `createTimerCard` | `(config, options) => HTMLElement` | 创建卡片并返回根元素；`options.lightweight = true` 时 root 不插入 DOM（仅承载数据与弹窗，供按钮路径复用） |
| `updateTimerCard` | `(card, config) => void` | 注入宿主与最新 hass、应用新配置 |
| `_showTimerTaskCenter` | `(group, button) => boolean` | 图标模式的任务中心弹窗；由 `popup-show.js` 的 `type === 'timer'` 分支委托调用 |

分派链路：

| 入口 | 链路 |
|------|------|
| `standalone_type: timer` | `standalone.js` → `COMPOSITE_CARD_REGISTRY.timer` → `createTimerCard` |
| `cards:` 区 / `popup_card` | `card-factory.js` → 注册表统一分派 → `createTimerCard` |
| 设备按钮 `type: timer` | 按钮点击 → `showDevicePopup` → `popup-show.js` 委托 → `_showTimerTaskCenter` |
| `action: card` + `card.type: timer` | `actions.js` → `createTimerCard` / 弹窗 |

#### 说明与已知边界

- **主题**：跟随房间精灵主题，`--timer-*` 变量在 `room-elves-card-styles.css` 里桥接到 `--room-*`（卡片与弹窗各写一份变量，因为弹窗内容不在卡片祖先链内）。
- **渲染方式**：纯 DOM API 构建（无 `innerHTML` 字符串拼接）；定时器统一走宿主的 `TimerManager`。
- **数据来源**：任务由后端统一存储系统管理，卡片本身不持久化任务；后端未就绪时卡片显示「等待 Hass 连接」状态，状态指示点用于提示连接情况。
- **原独立卡片已退役**：本卡片由独立卡片 `timer-control-card.js`（LitElement + Shadow DOM）迁移而来，配置需按上面的四种方式重写。

### 6.42 温湿度面板卡片 (type: wenshidu)

全屋温湿度面板：**时间轴控制区 + 温度户型图 + 湿度户型图**，支持拖时间轴回放历史时刻、点房间看历史曲线、切 3D 温度视图。房间多边形、房间实体、配色全部由配置给出。

面板由独立卡片 `wenshidu-card.js`（9,163 行 / 自带 Shadow DOM + ECharts + Three.js）迁移而来，引擎封在 `modules/cards/wenshidu.js` 的 `WenshiduElement` 内，样式统一在 `room-elves-card-styles.css` 的 `.wd-` 段。

#### 四种使用方式

**① 独立卡片（常显）**

```yaml
type: custom:room-elves-card
standalone_type: wenshidu
card_width: 440px
default_main_room: 客厅
main_entities:
  客厅: { temperature: sensor.keting_wendu }
rooms: [ ... ]
entities: { ... }
```

**② 内嵌到按钮区（`card` 数组）**

```yaml
buttons:
  - card:
      - type: wenshidu
        layout: mini          # mini：只显示户型图，点击卡片空白区弹出完整面板
        default_main_room: 客厅
        rooms: [ ... ]
        entities: { ... }
```

**③ `tap_action: card`**

```yaml
tap_action:
  action: card
  card:
    type: wenshidu
    default_main_room: 客厅
    rooms: [ ... ]
    entities: { ... }
```

**④ `tap_action: popup_card`**

```yaml
tap_action:
  action: popup_card
  popup_position: center
  card:
    type: wenshidu
    rooms: [ ... ]
    entities: { ... }
```

#### 面板结构

| 区块 | 内容 | 相关配置 |
|------|------|---------|
| 时间轴控制区 | 前一天 / 后一天 / 此刻 / 数据源切换按钮（HA ↔ API）、2D／3D 切换、演进 / 停止、时间显示、温度渐变条、刻度与时间标签 | `show_time_section`、`layout`、`show_3dtemperature_section` |
| 温度户型图 | 房间多边形按温度着色 + 房间名 + 房间温度值 | `rooms`、`entities`、`temp_colors`、`show_temperature_section` |
| 湿度户型图 | 同上，按湿度着色 | `humidity_colors`、`show_humidity_section` |
| 3D 温度视图 | Three.js 立体温度柱（可拖拽旋转、点柱看刻度） | `show_3dtemperature_section`（默认 **false**） |
| 房间历史曲线 | 点房间多边形 / 房间数值弹出单房间温湿度曲线；点「全屋温度 / 全屋湿度」标题（或标题按钮）弹出全屋曲线，区间可选 1/2/3/5/7 天 | `chart_period` |
| 日期选择器 | 点当前日期打开日历，可选任意日期回放；带 API 数据的日期显示角标 | `api_base_url` + `key` |

**常用交互**：拖动时间轴 → 回放到当天某一时刻；「演进」→ 自动播放一整天；「此刻」→ 回到实时；点击房间 → 该房间变为主房间（时间轴渐变改用它的温度着色）并弹出曲线。

#### 顶层配置字段

| 字段 | 必填 | 类型 | 默认 | 说明 |
|------|:----:|------|------|------|
| `card_width` | 否 | `string` | 自适应 | 面板宽度，如 `440px` |
| `layout` | 否 | `string` | `normal` | `normal` 显示全部区块；`mini` 隐藏时间轴区与标题（适合内嵌），并启用"点击空白区弹出完整面板" |
| `show_time_section` | 否 | `boolean` | `true` | 是否显示时间轴区（`layout: mini` 时强制隐藏） |
| `show_temperature_section` / `show_humidity_section` | 否 | `boolean` | `true` | 是否显示温度 / 湿度户型图 |
| `show_title` | 否 | `boolean` | `true` | 户型图上方是否显示「全屋温度 / 全屋湿度」标题（标题可点击弹全屋曲线） |
| `show_room_label` | 否 | `boolean` | `true` | 是否在房间内显示房间名 |
| `show_room_data` | 否 | `boolean` | `true` | 是否在房间内显示温湿度数值 |
| `show_3dtemperature_section` | 否 | `boolean` | `false` | 是否显示 2D／3D 切换按钮与 3D 视图（首次进入需加载 Three.js） |
| `default_main_room` | 否 | `string` | `main_entities` 的第一个房间 | 主房间：时间轴渐变按它的温度着色，对应房间会被高亮 |
| `viewBox` | 否 | `string` | `0 0 1100 1200` | 户型图坐标系（SVG viewBox），房间坐标按它等比缩放居中 |
| `corner_radius` | 否 | `number` | `15` | 房间多边形圆角半径（也可在单个房间上覆盖） |
| `temp_decimal_places` / `humidity_decimal_places` | 否 | `number` | `1` / `0` | 温度 / 湿度小数位 |
| `chart_period` | 否 | `string` | `hour` | 曲线图默认粒度 |
| `card_bg` | 否 | `string` | 不设置 = 跟随主题 | 面板底色。**不配则由房间精灵主题提供**；配了则以配置为准（内联样式覆盖主题） |
| `control_card_bg` / `floor_plan_panel_bg` | 否 | `string` | 不设置 = 跟随主题 | 时间轴控制区 / 户型图面板的背景色，规则同上 |
| `control_floor_boxshadow` | 否 | `string` | — | 控制区与户型图面板的阴影 |
| `popup_modal_width` | 否 | `string` | `card_width` | 弹窗形态的宽度 |
| `room_point_from` | 否 | `string` | `/local/pobaby_package/point/point.json` | 从 JSON/YAML 点位文件补充房间与实体（与户型图卡片共用缓存）；也可在 `rooms` 数组里用 `- room_point_from: xxx` 标记项指定 |
| `api_base_url` + `key` | 否 | `string` | — | 外部温湿度 API（HA 数据统一存储系统）。HA 无历史数据时可切到 API 数据源；日期选择器上的 API 日期角标也来自它 |
| `theme` | 否 | `string`/`object` | 不配置 = 跟随卡片主题 | 面板**单独**的主题：`light`/`dark`/`black`/`darkgray`/`transparent`/`on`/`off`/`time`/`phone`/`device`/实体ID/`{value\|entity}`。不配置则跟随卡片级 `theme:`，见下方「主题」说明 |
| `dark_light_theme` | 否 | `string` | `dark,light` | `on`/`off`/`time`/`phone` 用哪两套主题（`暗色名,亮色名`） |
| `title_button_*` | 否 | — | — | 标题按钮：`type`（`circle`/方形）、`size`、`color`、`hover_color`、`icon`、`label_position`、`show_label`、`position`（`top`/`left`/…）、`position_temperature`、`position_humidity`。配置了 `title_button_type` 即视为启用 |
| `enable_popup_card` | 否 | `boolean` | `true`（仅 mini 或隐藏时间轴时生效） | 点击卡片空白区是否弹出完整面板 |
| `popup_position` | 否 | `string` | `center` | 弹窗形态的位置 |

#### 房间与实体结构

```yaml
rooms:                      # 户型图几何（每个房间一块多边形）
  - id: 客厅                # 房间标识，与 entities 的键对应
    name: 客厅              # 显示名（可与 id 不同）
    points: "68,283 253,283 ..."   # SVG 多边形顶点（x,y 空格分隔）
    labelX: "206"           # 房间名坐标
    labelY: "311"
    dataX: "190"            # 温湿度数值坐标
    dataY: "330"
    room-data_font_size_round: 80,1   # 数值字号,小数位（可覆盖全局）
    room-label_font_size: 55          # 房间名字号
    room-unit_display:                # 是否显示单位
      temperature: true
      humidity: true

entities:                   # 每个房间的温湿度实体
  客厅:
    temperature: sensor.keting_wendu
    humidity: sensor.keting_shidu

main_entities:              # 仅主房间（用于时间轴渐变的温度着色），格式同 entities
  客厅:
    temperature: sensor.keting_wendu

temp_colors:                # 温度区间 → 颜色（区间左闭右开，最后一个区间含右端点）
  16-20: "#3498db"
  20-25: "#2ecc71"
  25-30: "#f39c12"
  30-32: "#e74c3c"
humidity_colors:            # 湿度区间 → 颜色
  0-30: "#e74c3c"
  30-50: "#f39c12"
  50-70: "#2ecc71"
  70-100: "#3498db"
```

#### 扩展接口（供其它模块调用）

实现位于 `modules/cards/wenshidu.js`，引擎封在 `WenshiduElement` 中，`WenshiduCardMixin` 对外暴露：

| 方法 | 签名 | 说明 |
|------|------|------|
| `createWenshiduCard` | `(config, options) => HTMLElement` | 创建面板并返回根元素 |
| `updateWenshiduCard` | `(card, config) => void` | 注入宿主与最新 hass、应用新配置 |
| `showWenshiduPopup` | `(config, triggerButton) => Function` | 弹窗形态（返回关闭函数） |
| `_collectWenshiduEntities` | `(cfg, out: Set) => void` | 把 `entities` / `main_entities` 里的实体登记进宿主订阅集（`subscriptions.js` 调用） |

分派链路：

| 入口 | 链路 |
|------|------|
| `standalone_type: wenshidu` | `standalone.js` → `COMPOSITE_CARD_REGISTRY.wenshidu` → `createWenshiduCard` |
| `buttons` 内嵌 / `popup_card` | `card-factory.js` → 注册表统一分派 → `createWenshiduCard` |
| `action: card` + `card.type: wenshidu` | `actions.js` → `showWenshiduPopup` |

#### 主题（默认跟随卡片，配了才单独一套）

**默认跟随房间精灵卡片的主题**——不配置 `theme` 时，面板与卡片用同一套配色（卡片切 dark，面板就是 dark）。若给面板单独配了 `theme`，则**只有面板**换成那一套，卡片与其它卡片不受影响。

```yaml
# ① 默认：跟随卡片主题
type: custom:room-elves-card
theme: dark                    # 卡片主题（面板跟着变深）
standalone_type: wenshidu

# ② 面板单独一套主题（卡片仍是亮的，只有面板变深）
type: custom:room-elves-card
theme: light
standalone_type: wenshidu
card:
  theme: dark                  # 面板自己的主题 → 只影响面板
```

| 面板 `theme:` 写法 | 效果 |
|---|---|
| 不配置（默认） | **跟随卡片主题**（卡片级 `theme:` 是什么，面板就是什么） |
| `light` / `dark` / `black` / `darkgray` / `transparent` | 面板单独用这一套（卡片不受影响） |
| `on` / `off` | 按 `dark_light_theme` 的亮色 / 暗色套（默认 `dark,light`） |
| `time` | 面板按时间自动切换（06:00-18:00 亮色，其余暗色） |
| `phone` / `device` | 面板跟随手机/系统的深浅色 |
| `<实体ID>` | 面板由实体状态决定（如 `input_select.panel_theme`，下拉状态直接写主题名即可） |
| `{ value: dark }` / `{ entity: input_select.xxx }` | 对象写法，同上 |

- 色值只有一处来源：面板复用宿主主题系统的配色表（`modules/core/theme.js` 的 `COLOR_SCHEMES`），**不再自带一套配色表**。
- 面板主题**只写自己的根元素**，不碰 `documentElement`，因此不会影响卡片与其它卡片；`time` / `phone` 模式下的 60s 定时器与系统主题监听只在该模式下建立，配置改动或卡片销毁时释放。
- 背景色优先级：`card_bg` / `control_card_bg` / `floor_plan_panel_bg`（配了就用，覆盖主题）> 生效中的主题 > 面板内置兜底色。
- 图表数据色（温度区间色 `temp_colors`、湿度区间色 `humidity_colors`、曲线系列色）与状态按钮色属于数据/状态语义，不随主题变化。

> 从原独立卡片迁移过来时：原先面板里的 `theme:` 现在含义不变（面板单独一套），若希望"跟卡片一致"直接删掉即可；`dark_light_theme` 用于 `on` / `off` / `time` / `phone` 的暗亮映射。

#### 说明与已知边界

- **渲染方式**：纯 DOM API 构建（面板、户型图 SVG、日期选择器、曲线弹窗均无 HTML 字符串拼接）；户型图用 `createElementNS`。
- **生命周期**：hass 变化按「关注实体指纹」去重（空闲时每秒仅一次对象身份比较），周期刷新（30s，外部 API 数据源 180s）统一走宿主 `TimerManager`；3D 的 rAF / 事件监听 / ResizeObserver 在切换回 2D 或关闭时全部释放。
- **曲线图**：走宿主 `showPopup` + 统一 ECharts 加载入口（本地 `www/pobaby_package/js/echarts.min.js` 优先、CDN 兜底），弹窗关闭时实例自动 dispose。
- **原独立卡片已退役**：本卡片由 `wenshidu-card.js` 迁移而来（源文件归档在 `src/wenshidu-card.js`），原有 `type: custom:wenshidu-card` 配置需按上面的四种方式重写，配置项名称不变。

---

### 6.43 通讯模块卡片 (type: comm)

读取运营商账户信息（话费 / 流量 / 通话 / 套餐权益）与通讯记录，**弹窗形态**，弹窗内两个面板：「账户」「通讯记录」。

> **底部圆点会跟着滑动高亮**：拖动中越过半屏就切到下一个圆点，松手那一刻即定在目标页（不会"滑完才闪过去"）。翻页机制见 `modules/infra/swipe-tabs.js`（通用模块，与 ESXi 卡片共用同一份实现）。
>
> **本卡没有选项卡栏**：在面板区域**左右拖动**即可切换（手机触摸、桌面鼠标拖动都支持），采用苹果式「跟手 + 吸附」——
> - **拖动中**两个面板实时跟随手指横向平移（不是切换时闪一下的淡入），拖多少走多少；
> - **松手**后按「位移超过面板宽度的 **28%**」或「甩动够快（> **0.35 px/ms**）」吸附到目标页，否则原路回弹；吸附曲线 `cubic-bezier(0.32, 0.72, 0, 1)` / 0.32s（近似 iOS 的减速感）；
> - **首 / 尾页**继续向外拖时位移打 **3.5 折**（阻尼：拖得动、拖不走，有手感反馈）；
> - **起手 6px 内先判主轴**：只有横向明显占优（> 1.2× 纵向位移）才进入翻页，否则整段手势交给浏览器纵向滚动 —— 明细列表上下滑不受影响。方向锁定后才 `setPointerCapture`（拖出容器也不丢事件，又不会破坏面板内的点击）。
>
> 底部一组小圆点指示当前面板，**圆点也可点击** —— 桌面端、键盘（Tab 聚焦 + 回车）与无障碍用户靠它切换，点击同样播放滑动动画。**卡片高度固定为「账户」面板的高度**：记录面板绝对定位、不参与高度计算，流水在面板内部滚动，因此翻页时卡片高度纹丝不动。

**数据来源**：`shaobo_pocket_carrier` 集成生成的**「数据总览」实体**（如 `sensor.zhong_guo_dian_xin_13363902961_shu_ju_zong_lan`）。该实体的每个属性节点对应一个子传感器（节点内为 `entity_id` / `state` / `icon` / `单位` + 子实体全部属性），卡片一次性读取全部节点，无需逐个配置子实体。

**推荐写法：只写电话号码**，卡片按「电话号码 + 后缀」自动拼接整套实体：

```yaml
tap_action:
  action: card
  card:
    type: comm
    tel_1: 13363902961
    name: 通讯
    width: 430px
```

> 一个 `tel_N` 展开出 **10 个实体**：`sensor.{tel}_overview`（数据总览）、`button.{tel}_button`（二次认证）、`text.{tel}_code`（验证码）、`date.{tel}_date`（查询起始日期）、`button.{tel}_update_region`（更新归属地库）、`switch.{tel}_daily_reset`、`switch.{tel}_auto_login`、`switch.{tel}_auto_region_update`、`switch.{tel}_auto_query`、`time.{tel}_auto_query_time`。号码会清洗为纯数字（`133-6390-2961` 也能识别），按**数字序**排列（`tel_2` 在 `tel_10` 之前）。多个号码写 `tel_1` / `tel_2` / …
>
> **旧配置仍可用**：`entity` / `entities`（含各自的 `button` / `code` / `date`）与 `tel_N` **可以并存** —— 指向同一实体时按实体 ID 去重，不会出现两个号码。
>
> 键名写法：`tel_1` / `tel_2`…（主推），只配一个号码时也可直接写 `tel`；**大小写不敏感**。若一个号码都没解析出来，卡片提示会把**实际收到的配置键**列出来，可直接分辨是"配置没传进来"还是"键名写成 `tel1` 了"。

```yaml
# 旧写法（等价，仍然支持）
tap_action:
  action: card
  card:
    type: comm
    entity: sensor.zhong_guo_dian_xin_13363902961_shu_ju_zong_lan
    name: 通讯
    width: 430px

# 或作为通用弹窗内容（popup_card）
tap_action:
  action: popup_card
  card:
    type: comm
    entity: sensor.zhong_guo_dian_xin_13363902961_shu_ju_zong_lan
```

| 参数 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `tel_N` | ❌ | `string` | **推荐**：电话号码（`tel_1: 13363902961`），自动拼接整套实体；多个号码写 `tel_1` / `tel_2`… |
| `tel_N_name` | ❌ | `string` | 该号码的**显示名**（`tel_1_name: 我的`），显示在头部号码块的下行；未配则回落运营商 |
| `entity` | ❌ | `string` | 单个「数据总览」实体 ID（旧写法，与 `tel_N` 可并存） |
| `entities` | ❌ | `array` | 多个数据总览实体（多号码 / 多运营商），元素为字符串或 `{ entity, name }`；配置 **2 个及以上**时头部出现号码切换行 |
| `name` | ❌ | `string` | 卡片标题。**不配则不显示标题行**（不再回落「通讯」—— 弹窗自身已有标题） |
| `icon` | ❌ | `string` | 标题图标，默认 `mdi:sim` |
| `width` | ❌ | `string` | 弹窗宽度，默认 `720px` |
| `popup_position` | ❌ | `string` | 弹窗位置，默认 `center` |
| `initial_tab` | ❌ | `string` | 初始选项卡：`account`（默认）/ `records` / `analysis`（需同时开 `analysis`） |
| `analysis` | ❌ | `bool` | **开启第三页「统计分析」**（默认 `false` 不显示这一页）。数据来自本地通讯库 API，与实体数据无关 |
| `key` | ❌ | `string` | 本地数据服务的 API Key。开了 `analysis` 就**必填** —— 但**不配时自动从顶层配置继承**（与空调日历 / 媒体卡同一套约定），所以通常只在根卡片上写一次。逐字段回落：本卡 > 顶层 > 无 |
| `api_base_url` | ❌ | `string` | 数据服务地址，**不配时同样从顶层配置继承**；顶层也没有则用默认 `/api/ha_data_store`（同源相对路径，通常不用填） |
| `fields` | ❌ | `object` | **节点名覆盖**，见下方说明 |
| `button` | ❌ | `string` | 通话详单二次认证 `button` 实体；配置后 hero 标签区出现可点击的**授权状态标签**（气泡入口） |
| `code` | ❌ | `string` | 通话详单验证码 `text` 实体；配置后气泡内出现验证码输入框 + 「写入」按钮 |
| `date` | ❌ | `string` | 通话详单查询起始日期 `date` 实体；配置后气泡内出现日期选择（改动即提交） |

多号码配置示例（`tel_N` 简写 —— 实体自动拼接，`tel_N_name` 是号码块的显示名）：

```yaml
tap_action:
  action: card
  card:
    type: comm
    tel_1: 13363902961
    tel_1_name: 我的
    tel_2: 17702925695
    tel_2_name: CM
    width: 430px
```

等价的完整写法（实体自己指定）：

```yaml
    entities:
      - entity: sensor.zhong_guo_dian_xin_13363902961_shu_ju_zong_lan
        name: 我的
      - entity: sensor.zhong_guo_lian_tong_xxxxxxxxxxx_shu_ju_zong_lan
        name: 联通
```

**卡片头部**（参照 `electricity-info-card` 的多户标题行 `multi-user-info`）：

- **标题行**：只在配置了 `name` 时出现，**居中显示且不带图标**；**不配就没有标题行**，头部只留号码行（弹窗自身已有标题，卡片里再来一行是重复信息）。`icon` 配置项仍然接受（不会报错），但头部不再绘制图标 —— 它与卡片 hero 的图标重复。
- **号码切换行**：等宽的若干块，每块**两行** —— 上行**话费余额**（`¥128.50`，与账户面板同源；拿不到数据显示 `—`，欠费转红）、下行**名称**（`tel_N_name`，未配则回落运营商 → 号码尾）。号码本身不在块里显示（卡片上方 hero 已有大号号码），收进**悬停提示**（同样走掩码出口）。未激活块半透明、激活块用主题色；块下方是一条**发光滑动指示条**，指示条之下还有一条横向贯穿的分隔线。点任意块即切换号码（面板与头部一起重建，指示条随之滑动）。
- **出现条件**：号码 ≥2 个时显示；单号码则只在配了 `tel_N_name` 时显示（否则单块没有额外信息可承载，纯占高度）。

**`fields` 节点名覆盖**：卡片按内置的中文别名表定位节点（余额 / 流量 / 通话 / 积分 / 通话记录 等）。若在 HA 里把子实体改了名，导致别名对不上（现象是该区块整块不显示），可用 `fields` 手动指定：

```yaml
fields:
  balance: 我的话费        # 覆盖「话费余额」节点
  call_record: 通话详单
```

#### 详单认证入口（hero 中的授权状态标签 + 气泡）

配置了 `button` / `code` / `date` 中任意一项后，hero 的标签区会多出一个**可点击的授权状态标签**。有效性判定以数据总览的「通话记录」节点为准：`授权剩余有效时长` 解析为 **0（或 ≤0）即判为失效**，其次看 `详单授权状态` 文案（过期 / 失效 / 未认证 / 无效）；两者都取不到时才退化到认证按钮实体上的同名属性。

| 情况 | 标签文案 | 颜色 |
|------|----------|------|
| 剩余时长 > 0 | `剩余 30 分钟` | 绿 |
| 剩余时长为 0，或状态文案含过期/失效 | `已过期` | 红 |
| 两项信息都取不到 | `详单认证` | 中性灰 |

点击该标签弹出气泡，**所有认证操作与设置都在气泡内完成**，不占用面板空间；九项全不配置则标签不出现。标签的 `title` 会带上原始「详单授权状态」文案（如「已过期 (需重新认证) · 展示本地缓存流水」）。

气泡从上到下分三段：

1. **主操作**：`button.{tel}_button` —— 文案随「验证码是否已填写」切换（未填 = 「获取验证码 / 刷新流水」，已填 = 「提交认证并拉取流水」）；
2. **认证字段**：验证码输入（`text.{tel}_code`，写入即提交）、查询起始日期（`date.{tel}_date`，改动即生效）；
3. **自动化设置**（分组标题 + 卡片式行列表）：默认 4 行开关 —— **自动获取通话记录**（`switch.{tel}_auto_query`）/ **自动短信登录**（`switch.{tel}_auto_login`）/ **自动更新号码归属地库**（`switch.{tel}_auto_region_update`）/ **每日重置查询起始日期**（`switch.{tel}_daily_reset`），加 1 行时间选择（**自动获取通话记录时间**，`time.{tel}_auto_query_time`）；底部一个动作按钮 **更新号码归属地库**（`button.{tel}_update_region`，一次性动作，与开关在语义上分开）。开关开 = 蓝、关 = 灰；实体不存在时置灰禁用（`title` 说明缺哪个实体）。行顺序按使用频率排：自动获取 → 时间 → 登录 → 归属地 → 重置。

> **每行用哪种控件，看实体的真实域**（`_commSettingControl` 分派），而不是一律画开关：

| 实体域 | 控件 | 点击动作 |
|---|---|---|
| `button.*` / `input_button.*` | **动作按钮**（行内小胶囊） | `button.press` / `input_button.press` |
| `time.*`（或域名缺省的 `type: time` 行） | 时间输入框 | `time.set_value` |
| `switch.*` / `input_boolean.*` / 域未知 | HA 风格滑动开关 | `<域>.turn_on` / `<域>.turn_off` |

> 为什么必须按域选型：`button.*` 没有 on/off 状态，画成开关会"永远显示已关闭"，点击又去调该域**不存在**的 `switch.turn_on` → 表现为"点了没反应"。开关的服务名同样按实体域拼（`switch` / `input_boolean` 都能用）。实体不存在时置灰禁用，不发起调用。

> 气泡里**所有点击动作都走宿主的统一动作系统**（`core/actions.js` → `handleCallServiceAction`），不是直接 `hass.callService` —— 这样操作记录埋点、本地服务分发与远程服务走的是同一条路径，埋点还能拿到"操作前"的状态快照。卡片内唯一的服务调用出口是 `_commCallService()`。⚠️ 埋点对象必须带**可记录的 `action`**（用 `core/action-log.js` 导出的 `actionLabelForService()` 映射：`button.press`→`press`、开关类→`toggle`、其余→`set_value`）—— 只写 `service` 会被埋点判成 `more-info` **静默丢弃**（既不记录、也不打印）。

```yaml
tap_action:
  action: card
  card:
    type: comm
    entity: sensor.zhong_guo_dian_xin_13363902961_shu_ju_zong_lan
    button: button.zhong_guo_dian_xin_13363902961_tong_hua_xiang_dan_er_ci_ren_zheng
    code: text.zhong_guo_dian_xin_13363902961_tong_hua_xiang_dan_yan_zheng_ma
    date: date.zhong_guo_dian_xin_13363902961_tong_hua_xiang_dan_cha_xun_qi_shi_ri_qi
    name: 通讯
    width: 430px
```

| 元素 | 交互 | 调用的服务 |
|------|------|------------|
| 验证码输入框 + 「写入」 | 填写后点「写入」，或直接回车 | `text.set_value`（参数 `value`） |
| 起始日期 | 选择日期即提交 | `date.set_value`（参数 `date`） |
| 二次认证按钮 | 点击 | `button.press`（语义见下表） |

**按钮语义**（由集成 `shaobo_pocket_carrier` 决定，卡片只负责触发并按状态显示文案）：

| 当前状态 | 按下后的行为 |
|----------|--------------|
| 验证码已填写 | 提交「姓名 + 身份证号 + 验证码」认证，成功后立即拉取流水；按钮文案显示为「提交认证并拉取流水」 |
| 验证码为空、授权仍有效 | 仅立即刷新一次流水 |
| 验证码为空、授权已失效 | 下发验证码短信，并在 180 秒内等待验证码写入后**自动提交**（无需再按） |

常规用法：点按钮下发短信 → 填验证码 → 点「写入」（授权失效时集成会自动提交）→ 若已错过等待窗口，再点一次按钮提交。

气泡内的布局自上而下三块：

1. **主操作按钮**（全宽）：未填验证码时是蓝色 `获取验证码 / 刷新流水`（按下即下发短信）；**验证码已填写后自动转绿色 `提交认证并拉取流水`** —— 让"获取"与"提交"两种语义一眼可分。按钮下方那行小字（180 秒内自动提交的说明）只在未填验证码时出现。
2. **字段区**（浅灰底圆角块）：`短信验证码`（输入框 + `写入` 按钮，回车等效）与 `查询起始日`（`date` 输入，改动即提交）。两行统一用「**定宽标签 + 控件**」两列，输入框左边界对齐。
   > 字段区下方紧跟一段**自动填写说明**（仅当配置了验证码实体时出现）：集成侧本就有「验证码写入即自动提交」机制（`telecom_auth.py` 的 `_async_after_set`），所以**若你在 HA 里另配了"短信转发 → 写入验证码实体"的自动化，这里完全不用手动输入** —— 按下「获取验证码」后短信一到就自动提交认证。卡片**无法探测该自动化是否存在**（集成未暴露对应属性），因此做成固定说明而不是条件提示，免得用户默认"必须手输"。
3. **状态提示**（逐条列出，前置小圆点）：以**「详单授权状态」原文**为主（如「已过期 (需重新认证) · 展示本地缓存流水」）；取不到原文时显示 `授权剩余 N 分钟` / `授权已过期`；等待验证码期间追加 `自动提交等待中`（剩余秒数）；仅当 `最近执行结果` 表示失败（含「失败 / 错误 / 未填写 / 缺少 / 无效 / 作废」）时才附上原因。**验证码下发时间、填写时间等纯历史信息不再显示** —— 它们不代表当前状态。

> 标题行 `详单认证` 保留：入口标签已经显示授权状态，气泡内不再重复显示徽标。

> 认证气泡**不随面板销毁**：数据刷新或认证操作后的定向刷新会同步重建气泡内容（按下按钮后能看到最新执行结果，输入框里未提交的内容也会保留）；关闭卡片弹窗时会一并收掉气泡。

> 按下按钮、写入验证码、修改日期后，卡片会在 **3 秒后主动刷新一次**（集成侧动作是异步的，要等运营商接口），常态另有 60 秒兜底刷新。
> 多号码时可在 `entities` 的每个条目里分别指定 `button` / `code` / `date`，切换号码即切换到该号码的认证实体。

#### 选项卡 1：账户

| 区域 | 内容 |
|------|------|
| 顶部概览（hero） | **纵向三段**：① 号码（**默认打星** `133****2961`，点击号码行展开完整号码，再点收起；切换号码时自动回到打星态），运营商以**右上角丝带**呈现（贴角 + 左下圆角，不占整行）；② **三指标行** —— **话费余额**（蓝，欠费时转红）、**剩余流量**（青）、**积分**（橙），只有数值 + 名称，某项无值显示 `—` 以保持三列对齐；③ 标签行 —— **四个可点击入口**（白底蓝边 + 右侧展开箭头，各带 `title` 提示）：**账户状态**（欠费红/正常绿，勾/叹号图标 → 点击弹话费明细气泡）、**主卡**（证件图标 → 主卡信息气泡）、**套餐名**（包裹图标 → 套餐与权益气泡）、**详单授权状态**（盾牌图标 → 详单认证气泡，仅配置了认证实体时出现）。标签一律用**短名**，细节交给 `title` 与气泡：「主卡」的 `title` 里带卡槽角色原文（`点击查看主卡信息（主号 (主卡)）`），套餐标签的 `title` 里带套餐全称。其中**套餐标签直接显示套餐名**（由 `套餐全称` 截掉「套餐 + 版本号」得到，如 `5G畅享199元套餐201910` → `5G畅享199元`，完整名在 `title` 中；取不到套餐名时退回「套餐与权益」）。**家庭融合、号码归属地两个标签已按需移除**（前者在套餐气泡的「融合类型」里、后者在主卡信息气泡里都有） |
| 流量 | ECharts **单层环**：本机 + 各副卡各占一段（段值取该成员已用量），**末尾再加一段灰色的「剩余」** —— 环整体即套餐总量，一眼看到还剩多少；**中心显示剩余量 + 剩余占比**（如 `226.36 GB` / `剩余 63%`），右列为 `已用 / 总量` 一行 + 同色图例（含「剩余」行；名称 / 用量 / 占比%，取整）+ 流量包明细。悬停任一段出 tooltip（名称 / 用量 / 占比，**百分比相对套餐总量**）；**触摸端改为点击某段弹小气泡**（触摸下 ECharts 内置 tooltip 定位不准、且触摸没有 mouseout 会一直挂着，故触摸端改用宿主 `_showBubble`，点外部即关）。拿不到总额度时不加「剩余」段（退化为已用量构成）；完全没有成员明细时退化为单值「剩余占比」进度环 |
| 通话 | 同上（单位分钟、共用同一套图例配色） |
| 页脚 | 数据最近更新、轮询间隔、凭证状态 |

**「话费明细」气泡**（点 hero 的账户状态标签）：当前可用话费、本月已消费、包含通用余额、包含专用余额、上月出账、欠费金额，以及近 6 个月出账条形图（**出账额固定 1 位小数**，`0.4 / 0.00001 / 0.5` 统一显示为 `0.4 / 0.0 / 0.5`，并用 `tabular-nums` 对齐小数点；其余金额仍保留最多 2 位）。

**「主卡信息」气泡**（点 hero 的主卡标签）：机主姓名、用户星级、网龄、信用额度、网络、归属地、卡槽角色、主套餐、名下宽带、名下副卡、名下固话、实名认证。

**「套餐与权益」气泡**（点 hero 的套餐与权益标签）：套餐全称、融合类型、网络制式、融合宽带、融合副卡、积分与积分体系、剩余短信，以及兑换特权提示。

#### 选项卡 2：通讯记录

**上部「本月通话」**（纯统计，全部由流水清单现算）：

- **标题栏右侧的「号码已隐藏 / 号码已显示」开关**：**默认隐藏中间几位**，一处控制**整卡所有号码** —— hero 的大号号码、顶部号码胶囊、Top3 排名里的号码、通话明细主号、主卡信息气泡里的名下固话。隐藏态下每个号码的 `title` 仍是完整号码（悬停可核对）
- **四宫格**：总次数（优先取节点「本月通话次数」，清单被 `overview_call_limit` 截断时也准）、**总时长**（明细求和）、总费用（明细求和）、**通话地点**（= 有归属地的记录里去重后的地点个数；运营商完全不给 `location` 时显示 `—` 而不是 0）
- **四宫格可点开看明细**（各区内容不同，气泡宽度固定 **320px**）：
  - **总次数** → 接听 / 呼叫次数（未接等其它类型归入「其它」，无则不显示该行）
  - **总时长** → 接听 / 呼叫累计时长
  - **总费用** → **0 元不给点击**（本月没花钱，弹出来是空信息）；非 0 → 费用最高的三通（时间 · 号码 · 金额）
  - **通话地点** → 每个地点的**时长 + 次数**
  - **流量**：总流量 → 本月流量概况（有上网的天数 / 日均 / 最大单日 / 单次最大 / 日均会话数）；上网时长 → **24 小时分布曲线**（见下）；上网次数 → 单次流量 Top5；总费用 → 计费会话（0 元同样不响应）
  - **短信：四格都不可点**（按需求不响应）
  - 接听 / 呼叫的判据与明细里的方向箭头**同源**（`_commCallDirArrow`），两处口径不会打架
  > 气泡里的键值表**单独一套样式**（作用域 `.comm-mini-tip`）：**单列**布局、标签用"主题深色 + 0.72 不透明度"。面板那套 `.comm-kv-*` 是两列 + 浅灰标签（为面板宽度与底色设计的），直接复用会在 320px 浮层里把长值折断、且整体显灰。
  > **24 小时分布曲线**（`_commHourChart`）：SVG 单位坐标 + `viewBox`，宽度交给 CSS —— 气泡在展开前宽度是 0，任何依赖 `offsetWidth` / canvas 尺寸的绘制（ECharts、canvas）都会画歪，而 SVG 靠浏览器缩放、不需要测量。24 个时段按真实小时铺满（缺的小时补 0），x 取**每格中心** `(h + 0.5) × 格宽`，HTML 横轴刻度按同一比例绝对定位 —— 用 flex 均分会与真实时段错位。曲线平滑（Catmull-Rom 转三次贝塞尔）+ 半透明面积，非零时段标小圆点、**峰值点换暖色**；每小时一个透明命中区（原生 `title` 悬停可看），触摸端不依赖悬停 —— 下方「峰值 XX 时 · 时长」与「N / 24 个时段有会话」已把关键信息给全。
  > 不画渐变的原因：气泡挂在 shadowRoot 下，`<defs>` 里的 id 在多卡片并存时会互相覆盖。
- **每日柱状图（每个分类各一张，只画本分类数据）**：通话 = `每日通话时长`、流量 = `每日上网流量`、短信 = `每日短信条数`。**纯 CSS** 柱子（不占第二个 ECharts 实例）：横轴 = 当月每一天（按真实天数铺满，没数据的日子补 0），纵轴按**当月单日最大值**归一，今天那根是暖色；悬停任一天弹出小浮层（日期 / 数值 / 次数）。横轴只标 `1 / 5 / 10 …` 与末日。
  > 早先设计过一张「每日趋势」三合一图（通话正柱 / 短信负柱 / 流量折线，双 Y 轴、0 刻度对齐、单位自适应）—— **已按用户要求下线**；三个方法 `_commTrendSection` / `_commTrendData` / `_commTrendOption` 保留但无调用点。
- **通话时长 Top3**（**按号码聚合**）：排名徽标（前三名**金 / 银灰 / 古铜**三色）+ 号码 + **累计时长** + **通话次数胶囊** + 最近一次通话时间（累计 0 秒的号码不入榜）

> Top3 是「**本月最费时间的三个号码**」，不是「单次最长的三通电话」—— 同一号码的多通会合并成一条，胶囊上的 `3 次` 即该号码本月通数；同分（累计时长相同）时按次数多的排前。悬停任一项的 `title` 会给出完整说明（`号码 · N 次 · 累计时长`）。点击仍按该号码筛选下方明细。
- **通话地点**（**两种口径，点小标题右侧按钮切换**）：`我的地点`（`location`，通话发生地，**默认**）↔ `对方地点`（`number_location`，号码归属地）。标签上显示该口径下的地点与通话次数（如 `西安 · 106 次`），按次数降序排列；该口径字段为空时回退到另一个字段。切换后**统计聚合、四宫格「通话地点」个数、配色基准、筛选字段**一起换（同时清掉旧口径的地点筛选 —— 旧筛选值在新口径下可能不存在，留着会变成"筛选中却看不到选中项"）。**配色与下方明细的地名共用同一套 8 色板**（同一地名在两处、两种口径下都同色），选中筛选时**不再覆盖成统一蓝**（那会丢掉"地点 → 颜色"的对应），改为加粗 + 用当前文字色内描边

> **点击排行项或地点标签 = 筛选**：下方明细只显示该号码 / 该地点的通话。筛选状态下**明细标题下方会多出一行筛选条**（`.comm-filter-bar`，淡蓝底）：`筛选口径 值 · 命中 / 共 N 条`，右端是「清除筛选」按钮 —— 例如 `对方地点 上海 · 12 / 共 118 条 [清除筛选]`。**筛选信息不挤进标题行**，标题始终是「通话明细」四个字；不筛选时标题直接带总数（`通话明细 · 118 条`），不多占一行。**再点一次同一项即取消**。不点击时始终显示全部（原行为不变）。统计区（四宫格 / 每日柱状图 / Top3 / 地点）**始终基于全部明细**，不会因为筛选而只剩一项；切换号码会清空筛选。筛选会重建明细面板，但**滚动位置会被保留** —— 刚滚到的位置不会被推回顶部（切排序、切视图、点地图圆点/省份同理）。

> 数据来源 / 详单授权状态 / 缓存说明等元信息**不再铺在这里** —— 授权状态在 hero 的认证标签上已有体现。

**第二页按分类分段显示**：页面顶部是**分类切换器**（**通话 / 流量 / 短信**，分段控件带图标），**一次只铺一类** —— 第二页原本把通话、短信、上网全列出来，太长了。

| 分类 | 内容 |
|---|---|
| **通话** | 本月通话概览（四宫格 / Top3 / 通话地点）+ 通话明细（列表 / 地图、筛选、排序） |
| **流量** | 本月上网（四宫格 + 上网明细 / **上网地点分布**） |
| **短信** | 本月短信（四宫格 + 短信明细 / **短信地图**） |

- **只列出有数据的分类**：没有短信节点就不会出现「短信」标签（点进去空的标签是误导）；**只剩一类有数据时不显示切换器**，与旧行为一致。
- **当前分类若已没数据**（如切号后新号码没有上网数据）→ 自动回落到通话，不会点出空白页。
- **切换器吸顶固定**（`position: sticky; top: 0`，配不透明底色 + 下分隔线）—— 面板内容再长，切换器也一直看得见；底色不能省，否则滚动内容会从它底下透出来。
- **切分类保持滚动位置**（与筛选 / 排序 / 切视图同一条路径）—— 切换器吸顶后不需要把页面拽回顶部，那样反而突兀。

**「本月短信」与「本月上网」**：同一份「数据总览」里另外两个明细节点 —— `短信记录` 与 `上网记录`。**节点不存在就整块不渲染**（集成未提供 / 运营商不支持），不留空区块。

- **本月短信** = 四宫格（总条数 / 发送 / 接收 / 总费用）+ **每日短信条数**柱状图 + 明细列表（时间 · 发送/接收徽标 · 号码 · 费用）。发送 / 接收按 `type` 关键词判（发送 / 发出 / 发信 ↔ 接收 / 收到 / 来信），**不假设固定取值**（运营商写法不统一）。数字走整卡掩码出口。
- **「地点」标题行还有方向筛选**：`全部 / 呼叫(发送) / 接听(接收)`（语音用"呼叫/接听"、短信与微信用"发送/接收"；**流量没有方向，不给这个键**）。它只作用于**地点胶囊的统计**（以及短信的明细与地图）—— 排行榜 / 四宫格 / 每日柱状图仍反映全量，否则"总次数"会跟着变、看着像丢了数据。与地点口径、地点筛选**正交**，可叠加；切方向**不清地点筛选**。
- **短信与上网也有「列表 / 地图」切换**（挂在小标题右端，与通话明细**共用同一个偏好** `card._commDetailView`，切一次三处都跟随）：走的还是通话那套地图件（`_commGeoGraph` + `_commMigrationChart`），底层一行没改。**短信**与通话同形态 —— 有我的地点也有对方归属地，画出**流向线**；**上网**那批数据**没有"对方归属地"**（不涉及联系人），所以图上只有地点、没有流向线（标题下明写「只标地点…」），标题也从「上网明细 · …（按日折叠）」换成「上网地点分布 · N 次上网 · M 天」。
- **这两张地图也支持地点筛选**（与通话明细同一套交互）：点地点 / 点省份即筛选，标题下方多一行 `我的地点 西安 · 2 / 共 3 条` + 「清除筛选」，再点同一项即取消。三个分类的筛选状态**各存一份**（`_commCallFilter` / `_commSmsFilter` / `_commTrafficFilter`），互不干扰；**切月份 / 换号会把三个一起清掉**（新月份未必有那个地点）。短信两种口径都能筛（我的地点 / 对方地点），上网只有我的地点。
- **「地点胶囊列表」三处都有**（小标题 + 口径切换 + 一排 `西安 · 62 次`，点一颗即筛选、再点取消）：抽成通用的 `_commPlaceBlock`，通话 / 短信 / 上网共用。**短信两种口径**（与通话共用同一个口径偏好，切一次两处一起变）；**上网只有我的地点**（那批数据不涉及联系人）→ 不给切换按钮、量词用「次」、标题写「上网地点」；短信量词是「条」。配色与地图、明细标签**共用同一张表**（都基于全部记录分配），所以统计里的胶囊、地图上的点、明细里的地名是同一个颜色。
- **短信 / 上网明细每行也带地点**：短信是 `时间 | 发送/接收 | 号码 | 西安 → 北京 | 费用`（两侧都有，箭头按发送 / 接收判）；上网是 `时间 | 流量 | 时长 | 西安 | 业务类型`（只有"我在哪儿上的网"，单段无箭头）。没地点的那条**不渲染空标签**。
- **本月上网** = 四宫格（总流量 / 上网时长 / 总费用 / 上网次数）+ **每日上网流量**柱状图 + 明细列表（时间 · 流量 · 时长 · 业务类型）。汇总优先读节点的 `合计`（集成已算好），**字段缺失时按会话清单回退求和**，老数据 / 字段改名后仍能出数。
- **流量单位自适应**：小于 1024MB 显示 `12.92 MB`，≥ 1024MB 转 `1 GB`（如 `20 GB`）。
- 明细里 **0 元不显示** —— 绝大多数短信 / 上网不计费，逐行标「0 元」只是噪音（与通话明细同一取舍）。

> **每日柱状图是同一套组件**（通话时长 / 上网流量 / 短信条数共用）：`_commDailySeries(monthKey, dayMap, opts)` 的 `value` 决定按哪个指标归一（**字段名不能叫 `valueOf`** —— 那是 `Object.prototype` 的内置方法，永远非 falsy，"不传就回落默认值"的分支会失效），`label` / `countLabel` / `format` 决定提示文案。所以「9月26日 · 2.76 MB · 2 次上网」与「9月1日 · 2 条」出自同一个浮层实现。

#### 选项卡 3：统计分析（需配置开启）

配置 `analysis: true` + `key: <API Key>` 后，底部圆点会多出第三页（**不配就没有这一页**，默认不显示）；可选 `api_base_url`（默认 `/api/ha_data_store`，同源相对路径，通常不用填）。

**它和第二页是什么关系**：第二页读「数据总览」**实体**（集成算好的当月数据），第三页读**本地通讯库 API**（原始记录，跨度可达十几年）。两者口径不同，所以**不强行对齐**：第三页有自己的范围条与渠道切换，**也不随顶部号码切换而变** —— 相当于一个独立的分析视图。

> **数据实况**（实测）：105,032 条 · 2006-10 ~ 今天 · 3 个我方号码 / 2074 个对方号码 · 微信 29448 / 流量 28415 / 短信 27385 / 语音 19783。

**默认视图「历史上的今天」**：按「月日相同」汇总历年同一天（`onthisday`），主图按年给柱；点某根柱子直接进入「全部数据」的该年。右上角胶囊按钮在「历史上的今天 ⇄ 全部数据」之间切换。

**「全部数据」视图**：

| 区块 | 内容 |
|---|---|
| 范围条 | 面包屑：`全部数据 › 2026 年 › 2026-09 › 09-30` —— **每一级都可点**，不用一级级退 |
| 通话时长榜 | 标题右端可选 **Top3 / Top5 / Top10 / 全部**（默认 Top3，状态存 `card._commRankN`，切换零额外请求）。标题带总数：`通话时长 Top3 / 共 24 个`。点某项 → 按该号码筛选下方明细（再点取消） |
| 指定日期 | 「历史今日」专属：`查某人` 旁边的胶囊按钮，默认写「日期」，点开项目通用的日历弹窗挑一天 —— **只取月日**（"历年同月同日"）。指定后按钮显示 `09-21`、面包屑第一层变 `历年 09-21`（点它回到今天）。基准日会下发给**全部六条 `onthisday` 请求**（主图正反向 / ranking / detail / 地图），所以图、KPI、排行、明细、地图一起变 |
| 查某人 | 头部「查某人」按钮：输入号码 / 姓名，或从 `parties` 前 8 的常用联系人里点一个（输入后会先用 `contact` 探一次，查不到当场提示）。选中后按钮变成「名字 ✕」，面包屑多一层。它是个**正交维度** —— 与「历史今日 / 全部数据」「全部 / 年 / 月 / 日」自由叠加（"历史今日 × 某人"、"某人 × 2025 年"都成立），所有查询（主图 / KPI / 明细 / 地图）都带上 `party_numbers`（有号码时）或 `party_names`（微信记录没有号码，只有姓名）。指定人时**那个位置整块不出现**（「联系排行」只会返回这一个人自己，没有信息量；曾经换成"该人的年度分布"，但列表区改成层级汇总后两者完全重叠 —— 同一份数据换个长相，所以去掉，只留下面那份汇总） |
| 渠道切换 | 语音 / 短信 / 微信 / 流量（分段控件，与第二页同一套样式） |
| 月份切换 | 顶部行右端 `◀ 2026-10 ▶` + 「本月」回位键。**本月走实体，历史月份走本地库 API**（`type=records&month=`）—— 数据先被"伪装"成第二页认识的实体节点（`通话流水清单` / `短信记录` / `上网会话清单`），所以柱状图 / 四宫格 / 明细**一行都没改**。首次进某月显示"正在读取…"，请求回来后面板自动重建。<br>**中间那个月份标签可点**（标题也提示"点击选择年月"）：弹出两列面板 —— 左边年份（可滚）、右边 12 个月（3×4），**年月分开选**。**选年只改选中**（右列重绘、当前月高亮仍在，不跳也不收面板），**选月才跳转并收起** —— 所以"某年某月"是两次点击，且不会在选年途中被弹走。<br>**范围来自后端 `type=months`**：先在乐观值（近 20 年 + 只禁未来）上把面板画出来（秒开），接口回来后收敛 —— **年份只留有数据的那几年**、**没数据的月份禁用**（打开 2024 年只会亮出 3 月 / 7 月），正在看的那个月永不禁用。接口拿不到就保持乐观渲染，功能照用。结果按卡片缓存（并发也只发一次），失败不缓存、下次可重试。 |
| 主图 | **双向柱**：上行 = 呼叫 / 发送，下行 = 接听 / 接收；**点柱子下钻一层**。纵轴**随渠道换指标**：语音 / 短信 / 微信 = **条数**（时长与金额在悬停提示里）；**流量 = 数据量（`traffic_usage`）** —— 一条流量记录是一次上网会话，"条数"只是会话次数，跟用了多少流量没关系。纵轴单位**按整根轴的量级自适应**：`max ≥ 1000 MB` 走 GB（图例「流量（GB）」，刻度 `332 GB`）、否则走 MB（`420 MB`），都不保留多余小数（GB 档刻度 < 10 时留一位，否则 0.5 GB 会变成 0）。后端未返回该字段时回落条数并在图下注明 |
| KPI | 条数 / **时长或流量** / 金额 / **联系人或地点**（四宫格，与第二页同款小格）。第二格**随渠道换指标**：语音 = 通话时长；**流量 = 数据量（`traffic_usage`，单位 MB）** —— 流量记录的 `duration` 是"上网时长"（会话持续多久），与"用了多少流量"是两个口径（实测 642 秒只跑 0.05 MB）；短信 / 微信显示 `—`。<br>**四格都可点**，弹「构成」气泡：语音 / 短信 / 微信按**方向**分（呼叫 vs 接听、发送 vs 接收），数据拆自已有的两个 total，零额外请求（短信 / 微信的时长格恒为 0，那一格不可点；金额 0 元同样不可点）。<br>**「联系人」格点开的是名单，不是两个数字**：`序号 · 姓名或掩码号码` → `条数 · 时长 · 金额`，标题带总人数。人数优先取后端总数（all 视图 `total.party_count`、历史今日视图排行的 `total_keys`）—— **但微信不走 `party_count`**（它按 `party_number` 去重，而微信那批记录的号码全是空串：实测给出 1、实际 2 人），改用排行行数。**流量没有方向**，四格改成「上网会话概览 / 各地点的流量 / （金额不可点）/ 地点活跃度」—— 数据来自 `crosstab&rows=location`（只在该渠道取），**第 4 格标签是「地点」而不是「联系人」** |
| 联系排行 | 主数据用 **`type=ranking&dimension=party_name`**（后端**按人聚合**，同一个人的多个号码算一个人），再配一份 **全量 `parties`** 建「姓名 → 号码」映射 + 补上**没有姓名**的那批独立联系人。行尾提示 `N 个号码`。<br>**为什么不能只用 `parties`**：它按号码聚合，而微信记录的 `party_number` 是**空串** —— 同一个「T」在档案里 8232 条、用 `parties` 只有 2815 条（差的 5417 正好是微信）。**为什么不能只用按姓名**：库里 2073 个号码中 1806 个没有姓名，纯按姓名会整段消失。两者都要。<br>显示时姓名三级回落：行内姓名 → 明细里的同号姓名 → **掩码号码**。**姓名本身也过掩码**（与号码同一个开关）：1 字 → `*`、2 字 → 留第 1 个、≥3 字 → 留前面的 n-2 个（`宋平` → `宋*`、`宋平平` → `宋**`、`欧阳娜娜` → `欧阳**`）。<br>**统一出口是 `_commPeerText(value, card)`**：`rank.key` / `party_name` / `peer.label` 里存的东西**不一定真是姓名**（实测有整段是号码的），所以它**按值的形态分流** —— 只有数字 / 空格 / `-` / `+` 走号码规则（`133****2861`），其余走姓名规则。直接把号码交给姓名规则会得到 `133639028**`（看着像号码、星号位置全错），这个坑踩过一次。**只有语音渠道**的标题右端有**榜长档位 `Top5 / Top10 / Top20 / 全部`（默认 Top5，无 Top3 —— 五个档位会把标题挤到换行）**（与第二页通话榜**共用** `card._commRankN`，设一次两边都变；标题带总数 `联系排行 Top3 · 共 2026 人`）。**「按条数 / 按时长」切换键**（短信 / 微信的 `duration` 恒为 0、流量压根没有排行榜，都不给这个键；流量那一块整块不渲染、请求也省掉）。切换键的排序依据交给后端 `by=count|duration`：排序交给后端 `by=count|duration`（`sort` / `order_by` 会被忽略），值里把**排序依据放最前**（`267 小时 19 分 · 2846 条`）。<br>**整行点击 = 筛选到这个人**（等价于「查某人」，时间范围回到全部）；档案气泡挪到**行尾小图标**（`mdi:information-outline`）上：总量 / 首末 / 距今 / 平均间隔 / 跨度 / 渠道分布 / 最常联系时段。号码位只接受**号码形态**的值 —— 微信那批 `party_number` 为空、`key` 就是姓名，当号码传会拿 `party_numbers=宋平平` 去查（必然 0 行）。全部数据视图用 `type=parties`（按号码聚合且带姓名），历史今日视图用 `onthisday&mode=ranking&dimension=party_number`（保住"月日相同"语义）。<br>**微信例外**：那批记录的 `party_number` 是空串（只有 `party_name`），按号码聚合得到 **0 行** —— 所以该渠道的对端维度改用 `party_name`（today 视图 `dimension=party_name`、all 视图 `type=ranking&dimension=party_name`），代价是**同名会被合并**（微信数据里没有更强的标识可用）。`type=parties` 写死按号码聚合、传 `dimension` 会被忽略，但它**带姓名**，所以号码维度仍优先用它 |
| 通话地图 | **右上角有「全屏」按钮**（第二页迁徙图同款：卡片内 `fixed` 铺满，不用原生 `requestFullscreen` —— Shadow DOM 里那个会被拒；Esc / 再点退出，全屏时图例一起进去）。复用第二页迁徙图的底层件（纯 option / 中国地图 / 省份判定），数据来自后端 **`type=geoflows`**（**聚合好的"地点 + 有向边"**，不再拉明细自己算 —— 明细有 `limit` 上限，记录一多地图就明显不全，这是数据不全的根因）。`geoflows` 吃全部通用过滤，所以"指定人 / 指定号码 / 指定时段 / 指定渠道"直接叠参数；「历史今日」用它的 `md`（`MM-DD`）取"历年同一天"。前端只做形状搬运（`_commGeoGraphFromApi`），**点城市 / 点省份即筛选明细**，口径自动选（只在对方归属地出现过就用 `party_places`） |
| 列表区 | **两种形态**。**「历史今日」= 逐条明细**；**「全部数据」= 跟随图表下钻层级的汇总** —— 每行一个时间桶，渲染成**表格**：表头随渠道与粒度变（`年份 / 呼叫 / 接听 / 合计`、`月份 / 发送 / 接收 / 合计`、`年份 / 合计 / 流量`…），**除第一列外一律右对齐 + 等宽数字**，一列数字上下对齐才能比大小。**语音的呼叫 / 接听 / 合计三格各带一行时长副行**（小字，主值是条数）：`2026 年 呼叫 461 / 9 小时 7 分`、`接听 548 / 7 小时 57 分`、`合计 1009 / 17 小时 5 分` —— 合计时长也是全量口径（比两方向之和大 1 分钟，差的就是「呼转」）。短信 / 微信 `duration` 恒为 0、流量的 `duration` 是"上网时长"另属一个口径 → 都不铺副行。表格**底部有一行「总计」**（逐行累加而非取 `list.total` —— 行的筛选口径与 `chart` / `down` 不一致，累加才能让三列说同一批数据；流量累加后再换算，不逐桶换算相加），一条贯通上边线 + 加粗与数据行区分，**不可点击**（不是桶）；只有 1 行时不显示。合计取**不带 `msg_types` 的全量**而非两方向相加 —— 库里还有「呼转」这类别的方向与没写 `msg_type` 的记录（实测 2008 年 `呼叫 930 + 接听 800 + 呼转 1 = 合计 1731`）；流量无方向，只给合计。列宽模板由 `--comm-sum-cols` 下发，行用 `display: contents` 让"整行可点"与"列对齐"并存。**点行即下钻一层**（与点柱子同一入口，下钻键与终点一致），空桶不显示、倒序、小时层为终点（不再给点击光标）。数据与 `years` **同参** → **零额外请求**（刻意不带 `limit`，否则查询串不一致、缓存失效）。右侧主指标同为渠道口径：流量给数据量、语音给时长、短信 / 微信恒无时长 → 只给条数。**年份 chips 在汇总模式下不出现**（这一层的行本身就是年份，点行即下钻）；切到该视图时会清掉残留的年份筛选（在汇总层没有落点）。地点筛选（地图点击）继续生效。<br>**下钻到「日」时，表格下面还会接一份该日的逐条记录**（不限是否指定人）：这一层的汇总粒度是"按小时"，看得出几点聊了几条、看不出聊了什么 —— 所以那一层多发一条 `type=records&date=<那天>`（带渠道，指定人时再带对端过滤），行复用明细区的渲染。其它层级不请求也不渲染。<br>**明细行尾的内容标签是「正文预览」而不是固定两字**：跟随**号码隐藏**开关 —— 隐藏态 `前2个字***`、显示态 `前10个字…`（`_commContentPreview`，与 `_commPhoneText` 同一个出口，`***` 固定三个不按长度铺）；换行 / 制表符先压成空格。点它仍是打开聊天窗口。<br>**明细形态**：当前范围的逐条记录（时间 · 类型徽标 · 对端 · 时长或金额），号码走整卡统一的掩码出口。**类型徽标按方向着色**：发送 / 呼叫（我打出去）蓝、接收 / 接听（别人打来）绿、流量等无方向的中性灰 —— 判据与第二页明细同源。**跨年时按年分段**（左色条 + `2025 年` + 右淡线），同年范围内不插（纯噪音）。**标题栏右侧是年份 chips，点一下只看那一年**（再点取消），筛选行显示 `2025 年 · 15 / 共 40 条` + 「清除筛选」。筛选**只作用于明细**（主图 / KPI / 排行 / 地图始终全量），且只有 `list` 的查询串变 → 其余请求全部命中缓存，切换实测只发一个请求。<br>**`content` 非空的行，行尾多一个「内容」小标签**（描边胶囊，与实心方向徽标区分），点开是**聊天窗口（仿微信）**：微信绿气泡靠右（我）、白底气泡靠左（对方），圆角方块头像，跨天插「今天 / 昨天 / 日期」分隔。数据走 `type=chat&mode=detail`（不跑汇总 SQL，`fields` 裁到 6 列），**渠道可在标题下的 chips 里换**（`全部` + 各渠道带条数，取自 `by_channel`；`channels` 必须显式传，不传就是"该对端的所有渠道"），**每条消息都带「渠道 · 时间」标记**（切「全部」时靠它分辨短信 / 微信 / 语音）。`empty_content` 按渠道定：微信 97.8% 有正文→滤空壳，语音 0%、短信 22.8%→不滤（滤了会整段空掉）。<br>**标题栏右侧有日期选择器**：走宿主的**通用日历**（`showCalendarPopup`，与时间线 / 设备用量 / 桑基图同一套，`--room-calendar-*` 主题配色），开启时会把**有记录的日期**打上点（通过它新开的 `apiOptions.fetchDates` 出口，调 `type=dates&month=YYYY-MM&party_names=…` 并按 `月|渠道` 缓存）。选某天是**跳过去**（不是筛选）—— 列表定位到那天，前后仍可自由滑动：**上滑看更早、下滑看更晚**。实现上日期只作"往更早方向翻"的右边界（`end=D 23:59:59`），"更晚"方向从**次日零点**起（`start` 是包含语义，用当天 `23:59:59` 会把锚点最后一条重复取回）。首屏定位：无锚点滚到底部（最新）、有锚点滚到顶部（第一条就是那天）。**渠道计数不受它影响**（恒为全量）。按钮可一键「回到最新」。<br>**从明细行的「内容」标签进来时，会定位并高亮那一条**：拿它的时间戳当首屏右边界（`end=<那条时间>`），于是它必然落在首屏，再滚到它并加 `.focus` 高亮（`outline` 画圈 —— 不占布局，气泡宽度不会因标记而跳动）；按「时间 + 正文」唯一匹配（同一秒可能有多条）。定位之后**仍可双向滑动**，不会被锁死。<br>**日历锚点优先于明细定位**：从明细进来后再用日期选择器，照样能跳（锚点是用户后来的动作，覆盖前者）；点「回到最新」会把两者一起清掉。<br>跳转时**用 `start`/`end` 圈定范围 + `limit=0` 取全量**（`chat` 原生支持，`limit=0` = 不限条数），范围取**目标日前后各一天**：只圈当天的话，那天若只有三五条，屏幕都填不满、滚动条不出现，上下滑动触发不了翻页，相邻日期就够不着了。若范围内容仍撑不满一屏（数据稀疏），**自动补一页更早的**兜底。首屏滚到**目标日期的日期头**上，补载完成后再定位一次（补载会往上方插内容）。**渠道计数也跟着日期收窄**（`by_channel` 吃 `date`，所以换日期时清单会重拉）；限了日期而那天没数据时页脚直说 `${date} 没有记录`。日期与渠道正交，可自由组合。窗口是 `showPopup` 的居中模态（不是锚定气泡），**滚到顶部自动加载更早 30 条**并保持视口位置；发送 / 呼叫靠右、接收 / 接听靠左，跨天插日期分隔。正文 `pre-wrap` 原样保留换行与制表符（最长的一条 1460 字 / 22 个换行）；附件路径（`./file/xxx.pdf`）渲染成"图标 + 文件名"；没有正文的记录用「类型 · 时长 / 金额」占位。**`content` 不是只有微信有** —— 实测微信 973/1000、短信 346/1000、语音 1/1000（一条备忘混进了语音）、流量 0。对端按 `party_number` → `party_name` 回落（微信记录的 `party_number` 是空的）。第二页短信明细共用同一套标签与窗口。

> **明细只覆盖到哪些年份，标题会写明**：明细是"最近 N 条"，流量这种密集渠道（库里 28415 条）的最近 60 条可能全在一年内 —— 于是标题写成 `显示最近 60 / 共 28415 条 · 仅 2026 年`，精确查看交给年份 chips。「历史今日」的数据量小，明细上限给到 **200**（该渠道当日全部），所以那里能看到真实的跨年分段。 |

**下钻粒度是自动的**：全部 →（按年）年 →（按月）月 →（按日）日 →（按小时）小时；到小时后不再下钻，再点即滚到下方明细。

> **为什么必须分渠道看**：`duration` 在不同渠道里含义不同 —— 语音是**通话秒数**、流量是**上网时长**、短信 / 微信恒为 0。把全表 `duration` 加起来会得到"9339 小时"这种没有意义的数字，所以渠道是第三页的第一层维度。

**几个实现取舍**（读代码时会用到）：

- **状态挂在卡片上**（`card._commAna`）：面板重建（换号 / 数据刷新）后原样恢复；查询结果**按查询串缓存**，所以重建不产生请求、视觉上完全静止。
- **并发保护**：连点柱子 / 连切渠道时，先到的旧响应会被丢弃（`reqId` 比对），不会覆盖新状态。
- **失败不等于空白**：错 key / 表不存在 / 网络异常都转成面板内一行提示，且**失败的查询不进缓存**（下次进入可重试）。
- **`fill=1` 只在有显式范围时生效**：传了 `year` / `month` / `date` 时后端补全空缺时间桶（横轴连续）；「全部数据」的年度视图没有边界可补，横轴只画**有数据的年份**。
- 图表实例在面板重建时显式 dispose（与环形图同一处理），不会泄漏。
- 「历史上的今日」排行走 `dimension=party_name`，返回的 `key` 是**姓名**而非号码 —— 查档案时按值的形态选 `party_name` / `party_number`。
- **明细标题写清范围与总数**（`明细 · 历年今日（10-01） · 共 40 条`），时间**始终显示完整年份**（`2026-10-01 12:04`）—— 第三页的范围可能横跨十几年，缩写或省掉年份都得靠猜。
- **主图的「正向 / 反向」是两个请求**：`stats` / `onthisday` 都只按时间分桶、给不出 `msg_type` 维度，所以「呼叫 / 接听」「发送 / 接收」各发一次（并发）；「流量」渠道只有一个方向，不发多余请求。**KPI 的合计要把两者相加**（联系人数取较大值，不能相加 —— 同一个人可能同时在两侧）。
- **第三页与「记录」面板共用「绝对定位、不参与容器高度」**（`.comm-panel[data-panel="records"], [data-panel="analysis"]`）：三个面板占同一个 grid 格子，容器高度取最大值，所以内容长的面板必须脱离高度计算，否则会把卡片撑高、切页时高度还会跳。**账户面板是唯一的定高基准**。

**下部「通话明细 · N 条」**：本月通话流水清单（取自「通话记录」节点的 `通话流水清单`，默认**按时间倒序**）。标题栏右侧是**视图切换**：**列表**（默认）/ **地图** —— 两者共用同一份（已筛选的）流水，切换只重建通讯记录面板。**列表视图**上方是**排序条**：左侧「排序」说明，右侧四个字段胶囊 —— **时间 / 时长 / 类型 / 地点**。每条记录两行：

- 主行：类型徽标（**呼叫 = 蓝、接听 = 绿**）+ 号码（与正文同字体，仅靠 `tabular-nums` 让数字等宽对齐）+ 时长
- 次行：**时间**（`09-28 10:39`，当年数据省略年份）+ **通话类型标签**（按类别分色）+ **地点标签**（定位图标 + 两个地名，格式见下）+ 费用（0 元保持次要色，真计费的记录标橙加粗）

> **地点标签的格式 = `我的地点 箭头 对方地点`**：**接听**（别人打给我）用 `←`，如 `西安←上海`（对方在上海、我在西安）；**呼叫**（我打出去）用 `→`，如 `西安→上海`。箭头判据与主行类型徽标同源（接听 / 被叫 / 呼入 / 来电 ↔ 呼叫 / 主叫 / 呼出 / 去电），其它取值（未接等）用中性 `·` 不编造方向。两个地名**各自按地名取色**（与统计区同色板），箭头为次要色；**两侧都有值时一律出两段**，哪怕两边同名 —— 本地通话就是 `西安→西安`（曾按"相同就合并成一个"处理，结果本地通话只剩一个地名，看起来像"这条没有对方归属地信息"，反而丢信息）；**只有一侧有值**时只显示该侧、不带箭头。
- **今日标记**：`call_time` 的日期等于今天的记录，在条目**右下角**显示绿色 `今日` 胶囊（次行已为其预留右侧空间，长文本不会压上去）

> **次行的标签配色**：通话类型按关键词分四档 —— **漫游通话**（橙，易产生额外费用）、**国际 / 境外 / 港澳台**（紫）、**视频通话**（青）、其余（如**国内通话**）为中性蓝灰兜底；**地点标签**带 `mdi:map-marker-outline` 图标，**两个地名各按地名从 8 色板里取文字色**（`_commPlaceToneMap`；标签底色保持中性，因为一行里要放两个地点）—— **同一地名恒同色、不同地名不同色**，颜色按「全部流水里 `location` 与 `number_location` 的**并集** + 拼音序」分配，因此切换筛选 / 排序 / 两种口径时同一地名都不会换色；费用为 `0元` 时保持次要色，只有真的计费（如 `0.2元`）才标橙加粗 —— 否则"全标红"反而看不出哪几通真的花了钱。通话类型的判据只看 `call_type` 文案关键词（各运营商取值不统一，关键词比对最稳）。次行现在是可换行的弹性行，窄屏下标签会自动折行。

> **排序交互**：点胶囊 = 按该字段排序（**时间 / 时长默认降序**，**类型 / 地点默认升序**）；**再点同一个胶囊 = 反转升降序**（激活项带 ↑ / ↓ 箭头）。未点过时把「时间 ↓」显示为激活态 —— 流水清单本身就是时间倒序，这样列表当前顺序一目了然。排序与筛选**可叠加**（先筛选、再排序），切换号码会把排序重置回时间降序。
>
> **排序口径**：时长解析不出的记录按 0 秒计（与「总时长」统计口径一致）；**时长 / 类型 / 地点相同的记录统一回落到时间倒序**做次序键，否则同值行会随刷新抖动、看起来像"排序乱跳"。**「地点」排序按统计区当前口径**（选「对方地点」时按 `number_location` 排）。

**地图视图（中国地图）**：把通话画成流向线 —— **点** = 通话地点（大小按通话次数、颜色与列表里的地点色板一致）、**线** = 通话方向（带流光动画，粗细按该流向的累计时长）。悬停某条线可看「从哪到哪 · 通话几次 · 累计多久」，悬停某点可看它作为"我的地点 / 对方地点"各几次。

**点击行为**：**点圆点** → 按该地点筛选明细（再点一次取消）；**点省份** → 一次筛出坐标落在该省内的所有地点；**点线** → 弹出**「流向详情」气泡**（**箭头指向点中的那一处**；触摸端**点地图本身不会关掉它** —— 关闭方式是点气泡外或点另一条线，这是为了避开"移动端浏览器在触摸后补发一次原生 click、把刚弹出的气泡关掉"的问题）—— 类型徽标（与线同色：呼叫橙 / 接听紫）+ `起点 → 终点`、通话次数 / 累计时长 / 平均时长、**这条线上的原始流水**（最近 12 条，号码跟随「号码已隐藏」开关），底部一个「筛选该流向」按钮。筛选从"点线的副作用"变成了气泡里的显式动作，避免线细误触一次就把列表筛没。

> **地图视图的四个要点**：
> 1. **方向 = 真实通话方向，且按类型分色**：**呼叫**（我打出去）为 `我的地点→对方地点`、**接听**（别人打来）为 `对方地点→我的地点`（判据与明细标签的箭头同源）。**呼叫画橙线（`#fb8c00`）、接听画紫线（`#7e57c2`）** —— 刻意**不沿用**列表徽标的蓝 / 绿：地图底图是淡蓝系（区域填充与省界都是蓝），蓝线会糊在图上；橙 / 紫这组互补色与底图对比最强、彼此也一眼可分。**线宽按该流向的累计通话时长**（`0.8 + 2.2 × √(时长 ÷ 最长时长)`，0.8~3.0px）而**不是次数** —— 打 5 通 30 秒与打 5 通 20 分钟在"通话量"上不是一回事。悬停可见该线的类型、次数与累计时长。同城通话不画线，只计入该地点的次数；方向判不出的类型（如未接）按"我的地点→对方地点"兜底。万一出现"方向相同、类型不同"的两条线（漫游时可能出现），两者曲率略有差异，不会完全糊在一起。
> 2. **地图数据运行时读取**，不进 bundle：首选 `/local/pobaby_package/js/china.json`（53KB，**省界简化、留岛少**），缺失时退化到同目录的 `china.geo.json`（590KB，省界精细），再退化到 CDN；加载一次后全局缓存，失败有提示且可切回列表查看。**用简化版不是因为体积** —— 精细数据的离岛与碎边界会把 geoJSON 包围盒撑大，ECharts 按包围盒适配容器，同样缩放级别下地图主体反而更小。**坐标**取自流水的 `location_coordinate` / `number_location_coordinate`（`经度,纬度`），解析不出或越界的记录跳过，图下方会注明"另有 N 条记录缺坐标"。
> 3. **筛选双向联动**：地图只用**筛选后**的流水作图。**点圆点**筛该地点、**点省份（面）**一次筛出坐标落在该省内的**所有地点**（按"点在多边形内"判定，不依赖"城市→省"的硬编码表；精细省界数据的顶点更密，判定也更准）；两者在该地点只作为"对方地点"出现时都会自动改用 `number_location` 口径，避免筛出空结果。同一圆点 / 同一省份**再点一次即取消**筛选。
> 4. **地图可拖动、可缩放，视野会被记住**：单指拖动平移、双指捏合或滚轮缩放（`roam`，限制在 0.9~8 倍）；**双击地图复位**到默认全景。拖动 / 缩放后的视野存在 `card._commMapView` —— **点圆点 / 点省份筛选、换号、定时刷新都不会把它推回全图**（这些操作都会重建地图，没有它每次都得重新放大）。地图区域**不参与左右滑动切选项卡**（手势起点落在地图上时翻页逻辑直接跳过），代价是地图内的纵向滚动也归地图，滚页面请在地图外的区域操作。**地图高度随容器宽度等比**（`aspect-ratio: 1.8 / 1`，下限 340px / 上限 480px，窄屏下限 300px）—— 宽屏弹窗下地图跟着长高、把宽度铺满，不会缩在中间留白；容器尺寸变化由 `ResizeObserver` 触发 `chart.resize()` 重绘。

> 流水清单目前直接读集成节点；**将来改由后端 API 拉取时只需替换 `_commCallView()` 的数据来源**，渲染层不用动。清单条数由集成的 `overview_call_limit` 选项控制（0 = 全部，实测 118 条）；面板本身是滚动容器，列表不再套内部滚动（避免双滚动条）。详单授权失效时集成只保留本地缓存，重新认证后可拉取最新明细。

#### 独立卡片模式（standalone_type）

不弹窗，直接把通讯模块当作**常显卡片**使用：

```yaml
type: custom:room-elves-card
standalone_type: comm
entity: sensor.zhong_guo_dian_xin_13363902961_shu_ju_zong_lan
name: 通讯
```

顶层写法与 `card:` 内的配置**完全一致**（`entity` / `entities` / `fields` / `name` / `icon` / `initial_tab` / `button` / `code` / `date` 等都会原样透传给 `createCommCard`）：

```yaml
type: custom:room-elves-card
standalone_type: comm
entities:
  - entity: sensor.zhong_guo_dian_xin_13363902961_shu_ju_zong_lan
  - entity: sensor.zhong_guo_lian_tong_xxxxxxxxxxx_shu_ju_zong_lan
    name: 联通
fields:
  balance: 我的话费
```

- **高度与外观**：不套用弹窗的 `88vh` 上限；背景用主题的**卡片底色** `--room-card-bg`（浅色半透白 / 深色深底，随主题变化，不是透明），圆角用 `--room-card-border-radius`。面板高度仍锁在「账户」选项卡高度上，流水在面板内部滚动。翻页手势、圆点切换、号码显示开关等交互与弹窗内完全一致。
- **刷新不依赖独立模式的 1 秒轮询**：注册表里该类型登记为 `standalonePoll: false`（数据本身是 30 分钟级），由卡片自身的 **60 秒低频任务**驱动。
- **卸载自清理**：独立模式没有弹窗的 `onClose` / `onDestroy` 回调，卡片从页面移除后由低频任务检测到 `isConnected` 为假、补跑一遍完整清理（关气泡 / 注销任务 / 解除视口观察 / 销毁环形 ECharts 实例）—— 低频调度器自己只会摘掉调度项，这些资源的解绑都在清理流程里。

#### 说明与已知边界

- **刷新机制（两级）**：数据总览实体本身为 30 分钟级轮询数据，卡片以 60 秒低频任务刷新（走宿主共享 tick，带视口门控），并按两个签名分别判断要做哪种刷新：
  | 签名 | 覆盖范围 | 命中时的动作 |
  |------|----------|--------------|
  | `dataSignature` | 「数据总览」的**内容指纹**（全部节点的属性值，但剔除认证易变字段） | **整体重建面板**（含环形图重挂） |
  | `signature` | 数据指纹 + 认证实体（详单按钮 / 验证码 / 日期）的时间戳 | 若非数据变化 → **只刷新"认证表面"**：hero 的授权标签文案与配色 + 四个气泡的内容，面板 DOM 一律不动 |

  > **为什么 `dataSignature` 取内容指纹而不是实体的 `last_updated`**：集成会把认证状态也镜像进总览的「通话记录」节点（`详单授权状态` / `授权剩余有效时长` 等），等待验证码窗口与倒计时期间这些字段**每秒被重写一次** → 实体时间戳每秒变。用时间戳做签名就会每秒整体重建面板：环形 ECharts 实例被反复 dispose、柱状图浮层被反复关闭 —— 用户看到的就是「图表标签/提示闪一下（约 1 秒）就消失」。
  >
  > 指纹里被剔除的字段（`COMM_AUTH_VOLATILE_KEYS`）：`详单授权状态` / `授权剩余有效时长` / `自动提交等待中` / `最近下发验证码时间` / `验证码填写时间` / `验证码状态` / `最近执行时间` / `最近执行结果` —— 它们只影响 hero 标签与认证气泡，走轻量刷新。而 `数据最近更新` / `数据来源` / `缓存说明` **不剔除**（集成本轮拉取数据时才写，变化即代表数据更新，理应重建）。流水清单只取"长度 + 首尾时间"参与指纹（整份 JSON 化在高频路径上代价过高）。
  >
  > **柱状图浮层还有一层兜底**：悬停的天号记在 `card._commDailyHover` 上，面板若仍被重建（数据刷新 / 换号等），新面板会在下一帧检测到指针仍停在图表上并把浮层恢复回来 —— 即使重建来源超出预期，用户也不会看到"闪一下就没"。
- **环形图**：走统一 ECharts 加载入口，中心数值由 DOM 渲染（ECharts 加载失败时数值仍可读）；切换号码或数据刷新时旧实例会被显式 dispose。
- **未配置 `entity` / `entities`**、或传入的实体不是「数据总览」实体时，弹窗内显示明确提示，不会静默空白。
- **区块小标题带虚线分割**：`.comm-sub-title`（每日通话时长 / 通话时长 Top3 / 通话地点）底部是一条横贯整宽的虚线，把标题栏与下方内容分开；「通话地点」那行的右侧额外的口径切换按钮也在这条线上。间距由 `.comm-section-body` 的 `gap` 提供。
- **卡片高度固定为「账户」选项卡的高度**：两个面板虽然共用同一个 grid 格子（用 `visibility` 切换，不是 `display: none`），但**「通讯记录」面板被设为 `position: absolute; inset: 0`**，从而不参与容器的高度计算 —— 否则容器高度会取两面板的较高者（= 长长的流水清单），卡片被撑高、切选项卡时高度还会跳。滚动因此下沉到各面板自身（`.comm-panel` 的 `overflow-y: auto`），流水再长也在面板内部滚；账户内容超过视口上限（88vh）时同样由面板自身滚动。
- **气泡一律向下展开**：hero 上的四个入口（话费明细 / 主卡信息 / 套餐与权益 / 详单认证）以及触摸端点击环形段弹出的小气泡，统一用 `placement: 'bottom'`。原先 `auto` 会按锚点上下空间自动翻向 —— 标签在卡片上部时反而容易翻到上方遮住 hero。向下的空间不够时由 `_showBubble` 自动收窄最大高度并内部滚动，不会跑出视口。
- **气泡/浮层在触摸端不因"抬手"关闭**：触摸端有两个陷阱会让"点出来"的气泡在同一个动作里被关掉 ——
  ① `pointerleave` 在**手指抬起时同样会被派发**（不是只有鼠标移出才触发）；
  ② `_showBubble` 的 `closeOnTargetClick`（默认 `true`）监听 target 的 `click`，而触摸端事件顺序是 `pointerdown`（打开）→ `pointerup` → **`click`（关掉）**。
  因此柱状图浮层在 `pointerleave` 里直接忽略 `pointerType === 'touch'`，环形段气泡把 `closeOnTargetClick` 设为 `false`；触摸端的关闭统一交给"点外部"（`closeOnClickAway`）或"再点同一项"（两处都实现了 toggle）。
- **气泡内的文字色**：hero 的三个气泡挂在 `shadowRoot` 下（**不在 `.room-card` 子树内**），而 `--room-*` 动态变量写在 `.room-card` 上，气泡里不一定取得到 → 气泡内所有文字色一律**显式声明**（`var(--room-xxx, 兜底色)`）而不依赖继承，否则深色主题下会继承宿主的白字、配上气泡的白底兜底变成"看不清"。

---

### 6.44 ESXi 虚拟化卡片 (type: esxi)

> **只配一个聚合实体，就能展示与控制 ESXi 主机 + 全部虚拟机 + 屏幕画面。**
>
> ⚠️ **前置条件：必须先安装自定义集成 [`esxi_control`](https://github.com/chjspp520/esxi_control)（必需）**
> —— 卡片自身不采集任何数据，全部内容都来自该集成生成的实体与聚合实体。
> **没装 / 没配置集成时，这张卡没有数据可显示**（只会给一句提示，不是卡片坏了）。

数据全部来自集成（`esxi_control`）的**聚合实体**（默认 `sensor.esxi_all_entities`，不存在时回退 `sensor.entities`）：`attributes.devices[]` 里主机与虚拟机各是一个设备节点，节点内是该对象的全部实体。卡片按「设备名 + 实体短名」自动识别角色（电源 / CPU / 内存 / 快照 / 画面 / 截图…），**不需要逐个配置实体**。

> ⚠️ **中文名虚拟机按「中文短名」匹配，不是 entity_id 后缀**：集成对中文名虚拟机生成的实体 ID 是**拼音化**的（如 `sensor.xu_ni_ji_windows10_down_cpushi_yong_lu`），靠后缀识别会落空。

#### 依赖集成：`esxi_control`（必需）

本卡片**不能独立工作**，它的全部数据都来自自定义集成 **`esxi_control`**：

- **仓库地址**：https://github.com/chjspp520/esxi_control （下载 / 更新都从这里取）
- **安装位置**：`<配置目录>/custom_components/esxi_control`（开发机映射盘 `Z:\custom_components\esxi_control`）
- **集成信息**：domain `esxi_control`，名称「ESXi Control」，当前 `version 0.12.0`，`iot_class: local_polling`，依赖 `pyvmomi==8.0.3.0.1` / `pycdlib==1.21.0` / `asyncssh>=2.14.0`（配置里 requirements 会自动安装）
- **安装步骤**：
  1. 从上面仓库下载，把整个 `esxi_control` 目录放进 HA 配置目录的 `custom_components/`；
  2. 重启 Home Assistant（首次启动会自动安装上面那几个 Python 包）；
  3. 「设置 → 设备与服务 → 添加集成」，搜索 **ESXi Control**，填 vCenter / ESXi 地址与账号密码。
  支持多个条目（多台主机 / 多个 vCenter）。
- **旧名迁移**：本集成原名 `esxi_stats`（目录 `custom_components/esxi_stats`），已整体改名为 `esxi_control`。**旧的 `esxi_stats.refresh` / `esxi_stats.sync` 服务已不存在**，外面若还写着旧域名，HA 会报「未找到 esxi_stats.refresh 动作」——自动化 / 脚本 / 前端里的旧域名都要一并改成 `esxi_control`。
- **它提供什么**：为每台主机 / 每台虚拟机 / 数据存储 / 许可证建实体（电源开关、CPU、内存、快照按钮、`image.*` 画面、以及可调的 `number` / `text` 参数），并生成**聚合实体 `sensor.esxi_all_entities`**（旧环境回退 `sensor.entities`）—— 卡片就是靠它"一次拿到全部设备与实体"，所以配置里只需写一个实体。
- **卡片会调用的服务**（都是集成注册的，不需要你手工调用）：

  | 服务 | 用途 | 卡片入口 |
  |------|------|----------|
  | `esxi_control.refresh` | 立即向 ESXi 拉一次最新数据。集成默认有节流（服务说明里写的是**约 45 秒**才真正拉一次），所以实时值想立刻更新就点它 | 头部「立即刷新数据」 |
  | `esxi_control.sync` | 重新扫描主机 / 虚拟机 / 数据存储 / 许可证，**对齐 HA 的实体清单**：为新增对象建实体、把已消失对象的实体移除（安全约束：只有本次刷新成功时才删，ESXi 不可达时只新增） | 「主机配置」里的「同步（重载集成）」 |

> ⚠️ **没有安装该集成时**，卡片不会报错崩掉，而是显示一句明确提示：`ESXi 聚合实体不存在或未加载：sensor.esxi_all_entities（或 sensor.entities）` —— 看到它就说明集成没装、没配置，或聚合实体还没生成。

#### 配置项

| 参数 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `entity` | ❌ | `string` | 聚合实体，默认 `sensor.esxi_all_entities`（不存在时回退 `sensor.entities`） |
| `name` | ❌ | `string` | 卡片标题，默认「ESXi 虚拟化」 |
| `icon` | ❌ | `string` | 头部图标，默认 `mdi:server` |
| `hosts` | ❌ | `string` / `array` | 只保留这些**主机**（按设备名；不配 = 全部） |
| `vms` | ❌ | `string` / `array` | 只保留这些**虚拟机**（不配 = 全部） |
| `exclude` | ❌ | `string` / `array` | 排除这些设备（与上面两项叠加；适合排掉集成的兜底设备，如「ESXi 统计」） |
| `default_vm` | ❌ | `string` | 「屏幕」页默认上墙的虚拟机（不配 = 自动优先挑一台**运行中**的） |
| `show_screen` | ❌ | `boolean` | `false` 时不生成「屏幕」选项卡（默认 `true`；且**必须有虚拟机**才生成） |
| `show_refresh` | ❌ | `boolean` | `false` 隐藏头部「立即刷新数据」按钮 |
| `show_sync` | ❌ | `boolean` | `false` 隐藏「主机配置」里的「同步（重载集成）」行 |
| `confirm_power_off` | ❌ | `boolean` | `false` 时**关机不再二次确认**（默认每次确认） |
| `width` / `popup_width` | ❌ | `string` | 卡片宽度 / 独立弹窗宽度（默认 `760px`；`popup_width` 优先） |
| `popup_position` | ❌ | `string` | 弹窗位置（默认 `center`） |

#### 三种入口

| 入口 | 配置方式 | 形态 |
|------|----------|------|
| 独立弹窗 | `tap_action: { action: card, card: { type: esxi } }` | 弹出的独立面板（默认为 `760px` 宽） |
| 内嵌弹窗 | `tap_action: { action: popup_card, card: { type: esxi } }` | 通用弹窗里嵌一张卡片 |
| 常显卡片 | `type: custom:room-elves-card` + `standalone_type: esxi` | 直接把面板当卡片用（高度由内容决定） |

```yaml
# 最省事：只给聚合实体
type: custom:room-elves-card
standalone_type: esxi
entity: sensor.esxi_all_entities
name: 虚拟化
```

```yaml
# 独立弹窗 + 只显示指定设备
tap_action:
  action: card
  card:
    type: esxi
    name: ESXi 主机
    hosts: 主机                # 只保留这台主机
    exclude: ESXi 统计         # 排掉集成的兜底设备
    show_screen: true
    confirm_power_off: false   # 关机不二次确认
```

#### 选项卡 1：主机

- **主机状态**：`CPU` / `内存` 两条进度条（数值 + 百分比条，**点它**可看这台主机近期的 CPU / 内存曲线气泡）；下方信息网格固定**两行两列** —— 运行时长 / 构建版本 / 维护模式 / 数据存储；许可证状态显示在区块右上角。
  > 信息网格**窄屏也不压成单列**（与桌面端保持同一套布局），长值由省略号收尾。
- **整机批量控制**：对全部虚拟机一键 **开机 / 关机 / 重启 / 强制重启 / 截图 / 快照**。
- **主机配置**：数据刷新间隔 / 聚合刷新间隔 / 截图间隔 / 批量分组四个参数，直接读写集成对应的 `number` / `text` 实体；末尾是「同步（重载集成）」。
  > 「同步」调集成服务 `esxi_control.sync`：重新扫描 ESXi，为新增对象建实体、把已消失对象的实体从注册表移除 —— **不重载集成、实体不中断、已存在虚拟机的 `entity_id` 保持不变**。它是低频操作（只在 ESXi 里新增 / 删除 / 改名虚拟机之后才需要），最长等 60 秒，超时只提示、不反复重试。
  > 另有头部「立即刷新数据」按钮：只把数据拉新（`esxi_control.refresh`），**不增删任何实体**，纯读、可随时点。

#### 选项卡 2：虚拟机

本选项卡内部再分**两个子选项卡**（位置在过滤胶囊那一行上面）：

| 子选项卡 | 内容 |
|----------|------|
| **管理主机** | 就是下面这套虚拟机列表（过滤胶囊 + 搜索 + 每台一张卡） |
| **新建虚拟机** | 嵌集成提供的**虚拟机管理页**：`sensor.<主机>_vm_manager`（显示名「虚拟机管理」）的地址，新建 / 克隆 / 改配置都在那个页面里做 |

> 这两个子选项卡**外观与头部主选项卡（`.esxi-tabs`）完全一致**（淡色圆角容器 + 激活项实心渐变），但类名不叫 `.esxi-tab` —— 翻页模块认的就是 `.esxi-tab` / `data-esxi-tab`，复用会把子选项卡当成主选项卡、打乱页序与高亮。
> 管理页地址取实体的 `attributes.url`（带 `authSig` 的完整地址；`state` 是不带签名的版本，因为带签名的约 400 字符、超过 HA 状态值 255 上限）。卡片**只保留 path + query、丢掉域名**再嵌 iframe：卡片可能经内网 IP / 域名 / 反代 / https 打开，照搬实体里的 host 会撞混合内容或跨域。
> 页面**懒加载**：只有切到「新建虚拟机」才创建 iframe，切走不销毁（回来还是原来那页、不丢表单）；地址没变就不会重设 `src`（否则 3 秒一次的值级刷新会把整页反复重载）。右上角有「重新加载」按钮，`authSig` 过期或页面卡住时用。
> 主机上的「远程桌面」总开关关掉时，集成不再签发地址（实体变成「已停用」），这一页会显示原因提示而不是空白页。

每台虚拟机一张卡：

- **标题行**：电源状态徽标 + IP；关机机器默认折叠成一行，点标题行展开（运行中的机器不折叠）。
- **指标**：`CPU`（名称里带 vCPU 核数）/ `内存`（优先用**活跃内存** —— ESXi 实际分配给它的物理内存；没有该实体时才回退「已用内存」）。点指标区看近期曲线气泡。
- **元信息（三列六项）**：系统 / 磁盘 / 快照 / 运行时长 / Tools / 状态。点它开**详细信息气泡**（配置 + 运行两组，列全 CPU 使用率、活跃内存、已用内存、所在主机、IP、快照数等）。
- **操作（三列）**：开机 / 关机 / 重启 / 强制重启 / 截图 / 快照 / 画面。
  - 「快照」弹菜单：**创建快照 / 删全部 / 删第一个（最早）/ 删最后一个（最新）**，每项都带二次确认（删除不可恢复）。
  - 「画面」弹**居中画面窗**：顶部是一条 teal 底色标题栏（虚拟机名 / 截图时刻 / 「全屏」按钮），画面在下方；标题栏是 sticky 的，画面比窗口高时也不跟着滚走。⚠️ 刻意不用气泡 —— 气泡锚在这台机器的那颗小按钮上，而每台虚拟机在列表里的位置都不同，定位（含箭头）会跟着飘。
- 顶部有**过滤胶囊**（全部 / 运行中 / 已停止）+ **名称搜索框**，两者叠加生效。

#### 选项卡 3：屏幕（屏幕墙）

- **墙面**：一行两列、最多 8 格；虚拟机超过 20 台时自动换「一行 4 个」。每格 = 画面（点开全屏）+ 状态条（状态点 / 名称 / 截图时刻 / 截图开关 / 全屏）。
- **工具栏**：「选择上墙的虚拟机」（气泡里多选，按钮上显示已选台数）+ 截图间隔 + 刷新。
- 画面不可用时给出明确原因：`虚拟机已关机` / `自动截图已关闭` / `暂无画面（等待截图）`。
- **取图走「实体聚合」给出的 `image.*` 实体**（HA 的 image 代理）：不自造缓存参数、不额外轮询 —— 只有换了新截图才重新指向一次（实现见 `modules/infra/image-entity.js`：画面地址算法 / 地址没变不发请求 / 加载三态类 / 画面时刻文案；屏幕墙、画面窗、全屏共用同一份）。

#### 刷新机制

- **自带 3 秒值级刷新**：只写文本 / 进度条宽度 / 类名，逐项脏检查（成本远低于整卡重建）；**只有结构签名变化才重建 DOM**（签名 = 聚合里的设备与实体清单）。
- **订阅刻意排除 `image.*`**：这类实体的 `state` 就是「最后截图时刻」，最短 2 秒一变 —— 订阅它等于每个 tick 重画一遍画面。
- 实时值一律从 `hass.states` 读，**不等聚合实体的刷新周期**（聚合实体的更新是分钟级的，集成侧对拉数据另有节流 —— 见上面「依赖集成」）⇒ 点了开关，界面立刻动，不用等下一次推送。

> **卡片里的实体操作都走宿主的统一动作系统**（`core/actions.js` → `handleCallServiceAction`），与通讯卡片同一套做法：操作记录埋点、本地服务分发与远程服务走同一条路径，埋点还能拿到"操作前"的状态快照（返回 `state` 值即 `state_log(from→to)` 的 from）。卡片内唯一的服务出口是 `_esxiCallService()`。⚠️ 埋点对象必须带**可记录的 `action`**（用 `core/action-log.js` 导出的 `actionLabelForService()` 映射：`button.press`→`press`、开关类→`toggle`、其余→`set_value`）—— 只写 `service` 会被埋点判成 `more-info` **静默丢弃**（既不记录、也不打印）。（`esxi_control.refresh / sync` 是卡片自身的服务调用、要拿返回的 Promise 做超时与结果反馈，故仍直连 —— 统一执行器不返回 Promise。）

#### 左右滑动切页 & 卡片高度

- 三个选项卡之间支持**鼠标拖动 / 触摸左右滑**切页：跟手拖动 + 松手吸附 + 首尾阻尼（与通讯卡片、以及其它所有分页处**同一套实现**，见 `modules/infra/swipe-tabs.js` 与「八-A、左右滑动」）；滑到两端就停，不循环。
- **选项卡高亮会跟着滑动走**：拖动中越过半屏就切到下一页的选项卡，松手那一刻即定在目标页（不会"滑完才闪过去"）。
- **卡片高度只由「主机」页决定**：另两页是绝对定位、不参与高度计算，内容超出时在**面板内部**滚动 —— 所以切到「虚拟机 / 屏幕」时卡片高度不会跳，屏幕墙也不会把卡片拉长。
- **弹窗高度上限 84vh**（带 `dvh` 兜底）：弹窗居中，上限有多高、可点的遮罩就只剩 `(100−上限)/2` —— 92vh 时手机上只剩上下各 4vh，**点不到遮罩（关不掉窗）**；现在上下各留 8vh。内容更高时在弹窗内滚动，底部的操作入口不会被挤掉（全屏查看那个弹窗与主弹窗同一上限，它没有关闭按钮、退出全靠点遮罩）。

#### 说明与已知边界

- 「虚拟机 / 屏幕」两页在**静止态不生成盒子**（`display: none`）：换来的是"翻页落地绝不会闪出旁边那一页"；代价是**切走再切回时，这两页的内部滚动位置会回到顶部**。
- 集成的兜底设备（如承载 vCenter 许可证的「ESXi 统计」）可能只有零散实体，用 `exclude` 排掉更清爽。
- 画面是否更新取决于集成侧是否产出了新截图（`image` 实体本身给出新地址）；这与 HA 内置 `picture` 卡片同源，也受同一限制。

### 6.45 个人账单卡片 (type: bill)

> **把 ha_data_store 里的个人账单画成一张卡：五个选项卡 + "一个窗口内一路下钻"的图表。**
>
> ⚠️ **前置条件：必须先安装自定义集成 [`ha_data_store`](https://github.com/chjspp520/ha_data_store)（v5.0.0+，必需）**
> 并配好 `api_base_url` + `key`；**没装 / key 不对时卡片没有数据**（会提示「接口不可用」）。
>
> 📌 **本节对应版本：v6.1.0**（2026-10-11）—— 个人账单卡片相关的内容都记在这一版下。
> 这张卡自 **v6.0.3**（2026-10-10，"五个页签 + 一路下钻"）起步，本节描述的是 **v6.1.0** 的形态：
> 五个页签 · 窗口内一路下钻 · 日历页「历年热力」· 查询页「结果热力」· 分析页「资金流向」（纯 SVG 桑基图）·
> 十余处本块来源筛选与四处口径切换。逐条改动见 `CHANGELOG.md` 的 **v6.1.0** 段（第 155~218 节）。

数据来自自定义集成 **[HA 数据统一存储系统](https://github.com/chjspp520/ha_data_store)** 的账单接口。卡片基本只读，只有「新增账单」与「写备注」两处会写入。**没有轮询**：只在「卡片打开」「切到还没取过数的页」「点头部刷新（↻）」「点查询 / 换条件」这四个时机请求。

#### 依赖集成：`ha_data_store`（必需）

- **仓库地址**：https://github.com/chjspp520/ha_data_store （需 **v5.0.0** 及以上：旧版账单接口字段不全）
- **安装位置**：`<配置目录>/custom_components/ha_data_store`（开发机映射盘 `Y:\custom_components\ha_data_store`）
- **安装步骤**：把整个 `ha_data_store` 目录放进 `custom_components/` → 重启 HA → 「添加集成」里添加它 → 开好账单接口并生成 **API Key**
- **必需配置**：`api_base_url` + `key`（见下方「配置项」；不配 `api_base_url` 时回退同源 `/api/ha_data_store/`）
- **它提供什么**：`personal_bill` 模块的账单表（交易时间 / 收支方向 / 金额 / 类型 / 对方 / 商品说明 / 支付方式 / 数据来源 / 交易状态 / 备注…），以及一组查询与聚合接口（卡片用到的见下方「接口一览」）
- 请求地址：`<api_base_url>/bill?type=…&key=…`（独立路径，不占 HA 的历史接口）

> ⚠️ 没装 / 没配 / key 不对时，卡片不会崩，而是显示「接口不可用（检查 api_base_url / key）」。

#### 五个选项卡

| 选项卡 | 内容 |
|--------|------|
| **概览** | 总计（环形图 + 环外拉线标注，右侧竖排 总收入 / 总支出 / 笔数 —— **每行"标签在左、数值在右"**，几行金额对得齐）· 各来源占比堆叠条（点某段 = 只看该来源，点条外 = 回到全部）· **年度收支** · **月度收支** · 最近 N 日收支（三块标题行右插槽各有一次**本块来源筛选** `来源 ▾`，互不影响；合计行**有哪个显示哪个**：收入 / 支出 / 净额 / 不计收支 / 笔数 —— 笔数是**服务端口径**，不随「加载更多」变；**收入 / 支出 / 不计收支 那三格可点 = 明细只看那一类**，再点一次或点提示条取消）+ 柱图 + 同窗口明细，**联动且可下钻到「时」**：点某天的柱子 → 柱图换成那天的 24 小时、明细列那天；点某个小时 → 明细再收窄到那一小时；面包屑 `全部 › 8/14 › 12时` 逐段可点返回。日层不取数，进「时」取一次并按天缓存；明细默认先列前 `10` 条，底部「加载更多」每次再放 `20` 条（数据已在手上，纯展开、不再请求；手上最多 `60` 条） |
| **分析** | 支出构成 / 收入构成（按类型）· 支出按支付方式 · 支出按来源（四张环形图，**每张卡标题行各有一次本卡来源筛选**）· 月度趋势柱图 · 支付时刻（24 小时柱图，次数 / 金额可切）· 对方排行 · **资金流向**（`bill_flow` → **纯 SVG 桑基图**：两维度之间的流量，起 / 终维度在标题行换；点节点 / 连线开范围窗口）—— **每块都能单独按来源筛**（标题行那颗 `来源 ▾`，互不影响）；**图例 / 柱子 / 排行的行 / 节点 / 连线点开都是「范围窗口」**（图上表下、一路下钻，见交互要点 ①） |
| **日历** | 账单日历（格子分两行写"收 / 支"，**底色按当天支出分 5 档 = 一张日热力图** —— GitHub 那种色阶，下面带 `少 → 多` 图例；**本月汇总的格子可点 = 本月明细只看那一类**）+ 本月明细分页 + **历年热力**（页面最下面，**默认收起、展开才取数**：ECharts 那种日历热力图 —— **一年一条、年与年竖着叠**（最近的年度在最上面），一条 = 7 行 × 53/54 列（周）、**连续铺满全年**，**整块只有一份月份标签**摆在最上面、**年份标签竖排**、左边标星期，底色按所选口径分 5 档但**全历史**分档；标题行 `来源 ▾` + 四个口径胶囊 `支出 / 收入 / 净额 / 笔数`（**底色跟着口径换色相**：支出红 / 收入绿 / 净额正绿负红 / 笔数主色；切口径**不重取数**）；点某天 = 范围窗口起手在那一天）；右插槽 `来源 ▾ ◀ [年月] ▶`（来源管整页，历年热力**跟着它**） |
| **查询** | 查询条件（**默认展开、可折叠**）+ 查询结果（**条件胶囊 + 时间路径条同一行**（`关键词 spp ✕ 全部 › 2020年 › 5月 › 26日`）/ 汇总（有哪个显示哪个、**可点筛方向**）/ **趋势柱图（点柱子往下一层钻）** / **结果热力**（日历热力图，**默认收起、展开才取数**；**不含时间路径** = 这批条件的全时间全景，点某天 = 把路径压到那天）/ 排序条 / 分页；标题行右插槽：**「来源 ▾」筛选**（只管这次查询）+ 「清除」） |
| **历史** | 历史今日（往年某个基准日的账 —— **基准日默认今天，可用标题行 `日期 ▾` 换**：`月日`（历年同月同日，点柱子就地钻到那天的小时）/ `几号`（历年每月那一天，点柱子开范围窗口）；上面一张**按年柱图** + 下面按年明细）· 历史本月（**同比块** —— 按年柱图 + 图下一排同比胶囊 `2019年 ↑12%`，今年还在过的月份标"进行中"；标题行 `◀ 9月 ▶` 可换月份）；两块标题行各有一次**本块来源筛选** |

明细行点开是「账单详情」气泡（全部字段 + 底部可写备注、可从"常用备注"点选）；「新增账单」是常驻右下角的**浮动小圆钮**，点开居中表单 → `POST bill/add`。

> 🏷 **来源标签**：每条明细的**时间下面**挂一枚小胶囊写 `source` —— 支付宝走**支付宝蓝**（`#1677ff`）、
> 微信走**微信绿**（`#07c160`），实底白字；其它来源（银行卡 / 云闪付 / 手动录入…）走中性灰，不抢眼。
> 颜色是**品牌色写死**的（不跟卡片主色 `--re-accent` 与明暗主题走 —— 它标的是"这条账从哪个渠道来"，
> 换个主题也不该变成别的颜色）。一列扫下来就能分出哪几条是微信、哪几条是支付宝。
> 没有 `source` 的行不出标签；超长由 CSS 省略（悬停有完整值的 tooltip）。

> 💡 **「不计收支」怎么显示（合计行"有哪个显示哪个"）**：微信 / 支付宝的原始账单里 `direction`
> 不只有 收入 / 支出 —— 还有**零钱充值 / 提现 / 转账**这类"钱在自己账户里倒"的账（原始值可能是
> `其他`）。后端口径下它们**既不算收入也不算支出**，但 `amount_sum` 是含它们的。所以卡片各处
> 的**合计**（概览总计、最近 N 日、年度 / 月度下钻窗口、日历本月、当日明细、范围明细弹窗、
> 查询结果、区间汇总行）统一改成 **"有哪个显示哪个"**：
> 有收入才摆「收入」、有支出才摆「支出」，两者全 0 时不摆「净额」（净额恒 0 没信息量）；
> 另有一段这类流水就补一格「**不计收支**」，金额 = `amount_sum − 收入 − 支出`。
> 格子名**跟着原始 `direction` 走**：`其他` → 显示成「不计收支」（表单 / 查询里那一项也叫这个），
> `转账` 等其他取值照原样写。于是"全是这类账"的一段（典型：对方是自己那张银行卡）
> 从「收入 ¥0.00 ｜ 支出 ¥0.00 ｜ 净额 ¥0.00」变成「**不计收支 ¥117,992.22 ｜ 笔数 65**」。
> 明细行里这类账的金额**不带正负号**、走灰色（`.bill-item-amount.is-mute`），合计格里也是灰的。

> 💡 **每一块图表都能各自按「来源」筛**（标题行右插槽那颗 `来源 ▾` 胶囊，`_billSrcPick`）
>
> - 落点：概览的**年度收支 / 月度收支 / 最近 N 日**三块，分析页的**四张环形图 / 月度趋势 /
>   支付时刻 / 对方排行 / 资金流向**（分析页环形图那颗在**卡片自己的标题行**），共 11 颗，**互不影响**。
> - 口径：**只影响这一块** —— 存 `state.blkSrc[<块>]`，只有那一块的取数参数带上 `source`
>   （概览的年度/月度从 `bill_trend` 对应粒度另取一次、最近 N 日再取一次 `bill_dashboard`；
>   分析页那几张各取自己那个接口）。没筛的块参数不变 → 命 URL 缓存，不会白跑。
> - 与**全局来源筛选**（点头部副标题 / 概览来源条那颗）的关系：块级筛选**压过**全局；
>   菜单第一项在设了全局时写「跟全局（<来源>）」= 撤掉本块筛选，没设则写「全部来源」。
> - 范围窗口（弹出窗口）里也有一颗（时间路径条那一行）：那是**窗口内临时**的，关窗即忘；
>   **入口自带来源时**（从来源条 / 来源环形图点进去）不摆 —— 那一颗就是它的身份，再筛没意义。
>
> 💡 **合计格可点 = 只看这一类**（**收入 / 支出 / 不计收支** 三格能点；「净额」「笔数」不是
> "某一类明细"，不可点）。几处的落法不同（因为数据来源不同）：
>
> · **概览「最近 N 日」**：数据本来就在手上 → **只筛明细列表**（客户端过滤，不发请求）。
>   点「合计支出」→ 明细只列支出，那一格高亮、明细上方出现 `只看支出 · 25 笔 ✕`；
>   **合计本身不跟着筛**（它仍是服务端口径的全量：笔数 / 收入 / 支出 / 净额都不变）——
>   合计是"这一段有多少"、明细是"给你看哪一类"。「加载更多」按**筛过之后**的条数算；
>   换层（钻到某天 / 某小时）或刷新 / 换筛选会复位成"全部"。
> · **日历页「本月汇总」**（`.bill-cal-summary`）：明细是**服务端分页**的 → 走接口 `direction`
>   （写进 `state.calDir`），只作用在**下面那块「本月明细」**上；**合计与日历格子都不跟着筛**
>   （它们是"这个月有多少 / 每天什么样"的全貌，与概览同一条口径）。高亮那一格 + 合计下面
>   一颗 `只看支出 ✕`（可点取消，也是"筛没了"时的退路）；「本月明细」的标题也跟着写
>   `本月明细 · 只看支出`（那颗是在上面那块点的，隔了区块要看得见）。换月**保留**筛选，
>   换来源 / 刷新则复位。
> · **范围窗口（弹出窗口）**：明细是**服务端分页**的，客户端筛只会筛到当前页（错的）→
>   走接口 `direction`，**图 / 明细 / 合计一起**按那一类重取（也正因为一起收窄，"图与明细笔数
>   必须相等"的口径自检才还成立）。提示那颗 `只看支出 ✕` 摆在**时间路径条那一行**，
>   点它或再点那一格取消；这一格筛没了（0 条）合计行会隐藏，那颗就是退路。
>   · 取值与查询页那颗「收支方向」下拉一致：`收入` / `支出` / `不计收支`（`BILL_DIR_PARAM`）
>   · ⚠️ 导入的微信 / 支付宝数据里这类账原始值是 `其他`，若后端不认「不计收支」这个值，
>     这一格会筛出 0 笔 —— 届时把 `BILL_DIR_PARAM.other` 换成后端认的值即可（一处）
> · `other` 那一类是**排除法**（概览那处客户端过滤时用）：`其他` / `转账` / `冻结` / 方向为空
>   都算（后端口径下都不计收支，见 `_billDirMatch`）—— 与「不计收支」那一格的金额同源。
>
> 📱 **窄屏（≤560px）「笔数」那一格不显示**（用户要求）：「笔数」多占一格，会把合计行挤成
> 两行（日历那处是 3 列：`收入 / 支出 / 净额 / 笔数` 正好第四格掉到第二行；其它几处是
> `auto-fit`，窄屏也常常差一格换行）。PC 端照常显示。实现：`_billStatCells` 给「笔数」那格带
> `kind: 'count'`，`_billFillStats` 据此挂 `.is-cell-count`，窄屏那条媒体查询按
> `.bill-recent-total .bill-stat.is-cell-count` / `.bill-cal-summary .bill-stat.is-cell-count`
> 藏掉（两套容器类名都要写：日历那处只有前者、概览 / 窗口 / 历史今日只有后者）。
> ⚠️ 兜底：整行只剩这一格时（这一段别的都凑不出来）用 `:only-child` 放回来，不然那一行成空虚线。

#### 交互要点

**① 范围窗口（图上表下 + 一路联动下钻）**

卡片里"点某根柱子 / 某一行 / 某个格子"打开的**都是同一个窗口**（`_showBillScopePopup`）——
不再各弹各的，全部在这一个窗口里就地换层：

```
星巴克 · 100 笔                            ← 抬头：入口范围 + 笔数（右侧搜索框）
全部 › 2025 › 02月 › 05日 › 10时  [来源 ▾] [只看支出 ✕]
                          ← 时间路径：每段可点，回到那一层。同一行还有两样东西：
                            本窗口的「来源 ▾」（点了换 / 取消；**入口自带来源时不摆**）、
                            方向筛选生效时的「只看支出 ✕」（点它或点合计那格取消）
[收入] [支出] [净额] [笔数]                 ← 当前范围的合计（**有哪个显示哪个**；
                                              全是"不计收支"的一段就摆 [不计收支] [笔数]）。
                                              **收入 / 支出 / 不计收支 可点** = 这一段只看那一类
                                              （图 / 明细 / 合计一起重取，再点一次取消）
 ▁▂ █▁ ▂▃ …（**当前范围的下一层**：全部时间→按年 / 某年→按月 / 某月→按天 / 某天→按小时）
 点柱子往下钻 …………………… 第 1 ~ 20 条，共 427 条   ← 提示 + 区间说明**同一行**
────────────────────────────────────────
时间 | 对方 / 类型 / 方式 / 来源 | 金额    ← 排序条（点列名排序）
 明细行…（点一行照旧开「账单详情」气泡）
[上一页] 第 [x ▾] / N 页 [下一页]           ← 页码是**下拉**（手机直接弹系统选择器）
```

- **哪些入口进来**：概览「年度收支 / 月度收支」的行 · 分析页四张环形图的图例 · 月度趋势的月柱 ·
  支付时刻的小时柱 · 对方排行的行 · 日历格子。**起手层不同**：年度行落在"某年"、月度行与月柱落在
  "某月"、日历格子落在"某天"（直接 24 小时柱）、其余落在"全部时间"（先看年）
- **图 = 当前范围的下一层**，点柱子把那一格并进范围 ⇒ 图与明细**一起**收窄，所以"从年一路钻到时刻"
  在每个入口都成立；**没有账单的时间桶不摆**（先按 年补齐首末年之间、月补齐 12 个月、日补齐当月天数、
  时补齐 0~23 算出边界，再把空桶滤掉，见 `_billChartCols`）—— 整月只 3 天有账单就只画 3 列，
  不再摆 31 列空档；刻度自带 `10月` / `12日` / `9时` 这类单位，跳过空档也读得出来是哪一格
- **明细每一层都在**（不像旧版只有钻到「日」才有）：抬头 + **搜索**（走接口 `keyword`，命中整段、
  不只是本页）+ **排序条** + **分页**（每页 `page_size`，默认 20，**页码是下拉选择**）——
  "点进来就是要找某一笔账"的用法完全不受影响。翻页 / 换排序只重取明细，图不重取
- **提示与区间说明同一行**：图下面那一行左边是"点柱子往下钻 / 再点收起 / 点柱子看那一格"这类短提示、
  右边是 `第 x ~ y 条，共 N 条`（两行在移动端挤不下）；挤的时候先省略**提示**，数字不截
- **收窄到某个小时**：图仍是那天的 24 小时柱、选中的那根标出来（`.is-picked`），再点同一根 = 收起
- **方向筛选**（点合计那一格的 收入 / 支出 / 不计收支）：`direction` 进请求（`scopeParams`），
  **图 / 明细 / 合计一起**按那一类重取 —— 只筛明细的话图上 30 笔、列表 8 笔，口径自检会当成
  "接口没按范围聚合"直接不画图。取消：再点那一格，或点路径条尾巴那颗 `只看支出 ✕`。
  翻页 / 换排序 / 上下钻都带着它（窗口内的临时状态，关窗即忘）
- **来源筛选**（路径条那行的 `来源 ▾`）：同款做法，`source` 进 `scopeParams`，整窗一起收窄；
  也是窗口内的临时状态。**入口自带来源时不摆**（从来源条 / 来源环形图点进来时，
  `params.source` 就是那次进入的身份，再叠一颗没意义）
- **"每天某小时"这类范围**（支付时刻的柱子）：最细到「天」，不再往下钻小时
- ⚠️ 图取 `bill_trend`、明细取 `bill_history`，两者是同一范围、笔数必须相等；对不上说明接口的趋势
  聚合没按这个范围过滤（例如不认 `counterparty`）→ **不画图**，只留明细并给一行说明（宁可不画，
  也不能拿全库的趋势配这个范围的明细）
- **没有账单的时间桶不摆（"不占位"）**：所有带时间轴的柱图都走 `_billChartCols` ——
  概览「最近 N 日」，分析页「月度趋势」/「支付时刻」，以及范围窗口的下钻图（年 / 月 / 日 / 时四层）。
  某月只 3 天有账单就 **3 列**（不再 31 列空档）、整天只 2 小时有就 2 列 —— 空列只会把有数据的列挤窄。
  列少时那几列**均匀撒开**（`.bill-cols` 的 `justify-content: space-evenly`）并给列宽上限
  （`.bill-col` 的 `max-width`，密排 / 极密档各收一档）—— 上限是前提：不封顶的话 `flex-grow`
  会把每列拉满、根本没有空余宽度可分；封了顶才不会出现"柱子缩在列中间、刻度钉在列右缘"的错位
- 柱上数值：`≥ 1 万` → `1.2万`（**一位小数**）；`1 万以下` → 取整、不带小数；`0` 不标。柱子够高时竖排画在柱内、柱矮则退到柱外按收支着色
- **每格两根柱（收入绿 / 支出红）+ 可能有的第三根（「不计收支」中性灰 `#8a94a6`）**：
  第三根**有才画、没有就不占位**（零钱充值 / 提现 / 内部划转那类账，大多数格子没有；
  格子里有就多一根、没有就还是两根）。金额 = `amount_sum − 收入 − 支出`，跟着 `_billOtherAmount`；
  与合计格里那格同源。tooltip 里会写 `不计收支 ¥…`。**所有双向柱图 / 条形图**都有：
  范围窗口的下钻图、概览「最近 N 日」、分析页「月度趋势」，以及**年度收支 / 月度收支
  那两处"收 / 支"进度行**（有这类流水就多一条灰色「不计收支」，同样是 `amount_sum` 推的；
  历史本月已不用进度行，见 ③b 那条）；支付时刻是单值柱图，不涉及
  ⚠️ 前提是**那一层的分桶带 `amount_sum`**（`bill_trend` 的分桶带，所以月度趋势 / 范围窗口 /
  下钻都画得出来）；`bill_dashboard` 的 `days` / `years` / `months` 若没带，那几处就画不出来
  —— 届时可改从 `bill_trend` 取那几天/那几年的序列（前端可做，不用动后端）
- **X 轴刻度写明是什么、且斜排 45°**：`2015年` / `10月` / `12日` / `9时`（原来年是两位 `25`、月是 `02`，
  列一多还会被列宽截成 `20…`，既看不出单位也读不出数）。斜排后文字沿对角线走，
  水平足迹 ≈ (字宽+行高)×0.707，只要小于列距就不撞 —— 极密档（整月 31 天 / 整天 24 小时）
  列距 ~18px，两三个字刚好放得下。日 / 时**不补零**（`9日` / `9时`，刻度这里宽度紧），
  路径条与面包屑不受宽度约束，仍是补零的 `09日` / `09时`。
  这一套是**所有柱图共用**的（范围窗口 / 概览「最近 N 日」/ 月度趋势 / 支付时刻）。
  **锚点**（斜排的旋转中心）= 刻度盒的**右端·垂直居中**，再用负 margin 抵消 `.bill-col` 的列间距
  ⇒ 锚点正好落在**柱底（X 轴）**上 —— 也就是"末字以中心压在轴线上"（`.bill-col-label`）

**①b 分析页 · 资金流向**（`_buildBillFlow`，纯 SVG 桑基图 —— 本卡不引第三方图表库）

- 取数：`bill_flow`（后端第 40 个接口：`from_dim` → `to_dim`，返回 `nodes` + `links`
  `{source, target, count, income, expense, amount_sum}`，按 `amount_sum` 倒序、默认 `limit=500`）
  · 起 / 终维度**在标题行换**（两颗胶囊 `从 来源 ▾ → 到 类型 ▾`，气泡里列
  **来源 / 类型 / 方式 / 对方 / 收支方向 / 状态** —— 与后端 `BILL_DIMENSIONS` 同一套白名单，
  **不含时间维度**：那是交叉汇总 `bill_crosstab` 的活儿，画成桑基图读不出"流向"）；
  换一个 = `_billReload` + 重绘（只这一份 URL 变了，别的块命缓存）
  · 默认 **来源 → 类型**（用户定的；⚠️ **不是**接口那个默认 `counterparty` ——
    本卡的口径是"钱从哪个渠道走、花在哪类"，来源是一眼能对上明细行的维度）；
    副标题写 `来源 → 类型　·　12 条流`，一眼看出在看哪两维；
    ⚠️ 两颗维度胶囊带 `从 / 到` 前缀：起点默认就是「来源」，而这一块还有一颗**来源筛选**
    （`来源 ▾`），不加前缀会出现两颗都写「来源」的胶囊、分不清哪颗是筛选
  · 这一块也有**本块来源筛选**（`来源 ▾`，`_billSrcPick('flow')`）
- 画法（`<path>` 三次贝塞尔 + `stroke-width` 当带宽）：
  · **两侧各留金额最大的 7 个节点**，其余并成「其他 N 项」（聚合节点**不可点**，
    与概览来源占比条「其他 N 项」同一套路）；节点上下顺序 = 金额从大到小
  · **两侧共用一个比例尺**（桑基图的规矩：宽度可比）+ 节点间留缝；节点高 = 该侧总流量 × 比例尺
  · **连线颜色跟起点节点**（与节点色块同色，顺着一条流读下去）；带宽 = 该条流的金额
  · 文字：名称一行 + 金额一行（`_billCompact`），**贴着节点块的垂直中线**；行太矮（< 12）就只写名称，
    免得压到下一行 —— SVG 没有省略号，按留出的宽度**截字**（完整值在 tooltip 里）
  · 整块**等比缩放**（viewBox 宽 360 用户单位 + `height: auto`，与环形图 `.bill-donut-svg` 同一套）：
    字号也是用户单位（8.4 / 7.2），桌面卡片渲染约 11px / 9.7px，窄卡片一起缩小
- 交互：**点节点** → 这一维度值的账单；**点连线** → **两个维度都筛上**（`对方` 走精确匹配
  `counterparty_exact=1`，与对方排行同一个口径）—— 都落在范围窗口（与环图 / 排行同一落点）；
  tooltip 给全（`A → B`、金额、笔数、收 / 支 —— `bill_flow` 是按两个值分组、不区分方向）
- ⚠️ 这一块也**不能让卡片被撑宽**：副标题 + 那排胶囊都会在 max-content 里出价 →
  `.bill-analysis-flow-section { contain: inline-size }`（与热力图那条同一个道理）

**② 日历页**

- 格子分两行：上一行**收入**（绿、`+` 号）、下一行**支出**（红、`-` 号）；金额单位同上（不保留小数 / `x.xx万` / `x.x百万`）
- **日格子是一张「热力图」**（GitHub 那种色阶，纯 CSS 底色、不引图表库）：底色越红 = 那天花得越多。
  档位**按这个月"有支出的那些天"的 20/40/60/80 分位分 5 档**（`_billHeatThresholds` /
  `_billHeatLevel`）—— 原来只有 3 档、按**最大值等比**，一个月里只要有一笔大额，其余格子全会掉到
  最浅、整月看着一片淡。有支出的天**少于 5 天**时退回按最大值等比（否则阈值全挤在一个值上）。
  **没花钱 / 没数据的那天不给档位类**（保持最浅底色）。最深的第 5 档只到 0.38 的 alpha：
  格子里还有收 / 支两行金额（绿 / 红），做成实心红会盖没；深档同时把**日期数字**压深。
  日历下面跟着一条**图例** `少 ▢▢▢▢▢ 多` + 一句口径说明（`_billHeatLegend` 建的 `.bill-cal-legend`，
  色块与格子**共用同一组色值**；下面「历年热力」那张图例也是同一个函数，只是口径说明换成"全历史分档"）
- 点格子 → **范围窗口起手在那一天**（时间路径 `全部 › 2026 › 10月 › 09日`）：图直接是那天的 **24 小时柱**，下面列当天的账（合计 / 搜索 / 排序 / 分页都在，见 ①）
- 右插槽 `[来源 ▾] ◀ [年月] ▶`：**本块来源筛选**（这颗管**整页** —— 日历格子 / 合计 / 本月明细是同一次取数）；
  中间那颗点开是通用「选择年月」面板（左年右月，没有数据的月份置灰），也可以直接左右切月
- **本月汇总的格子可点 = 「本月明细」只看那一类**（走接口 `direction`；合计与格子不跟着筛，
  见上面那条 💡）+ 合计下面一颗可点取消的 `只看支出 ✕`
- **页面最下面还有一张「历年热力」**（`_buildBillYearHeat` —— ECharts 那种日历热力图）：
  · **默认收起**（`state.yheatOpen`），副标题写「点标题展开（展开才取数）」；
    **展开才建内容、才发那一次取数**（框架的惰性建体 + `_billYheatFill`）——
    16 年 ≈ 5600 行，不该跟着每次进这一页 / 点合计格一起拉。展开状态在同一次会话里保留
    （重绘 / 换来源后仍是展开的，数据缓存作废会重取一次）
  · **一年一条、年与年竖着叠**（**最近的年度在最上面**，与「年度收支」的阅读顺序一致）；
    一条 = 7 行（日 → 六）× N 列（周，**全块统一的列数**：53 / 54，取各年最大）——
    一列是一周、**连续铺满全年**（**不按月重置**，所以横着读就是"时间往前走"；
    起点是 1 月 1 日所在那一周的**周日**）
  · **「月」整块只有一份，摆在所有年带上面**（`.bill-yheat-top`，用户要求）：
    左边是与年带**等宽的空壳**（同一个 `.bill-yheat-year-label` 类 + 同样的间距），
    所以标签与下面的格子自动对齐（实测：左边界差 0、宽度差 0）；
    label 落在"这个月第一天"所在那一列、前面一条浅竖线（ECharts 的 `monthLabel` + `splitLine`）。
    ⚠️ 各年 1 月 1 日落在不同星期 → 月份列位置最多差 1 列，所以**精确的月边界**靠
    **每条年带里"每月第一天那条浅竖线"**，顶上这份是刻度
  · **年份标签竖排**（`writing-mode: vertical-rl` = 整体转 90°，用户要求）：宽度收成 14px、
    垂直居中贴着年带（实测盒子 14 × 24.7）
  · 左边只标星期 `一 / 三 / 五`（ECharts 的 `dayLabel`）
  · **标题行右插槽** = **本块来源筛选**（`来源 ▾`，`_billSrcPick('yheat')`）**+ 四个口径胶囊**
    `支出 / 收入 / 净额 / 笔数`（选中的走**实底**，与「支付时刻」的次数 / 金额同一套视觉）。
    · 数据源**压过日历页那颗**（`records`）：设了就只看这个来源，两颗都没设 = 全局口径；
    · 切口径**不发请求** —— 四个值都在同一次 `level=day` 里（`count` / `income` / `expense`），
      只重画这一段（`state.yheatMetric` 记着，重绘 / 换页后仍是它；收起状态下切也行，展开时按新口径画）；
    · 胶囊都带 `re-nostart`（点口径不会把这一块折叠起来）；窄到放不下时**右插槽折行**
      （`.re-section-head .re-section-right` 默认 `flex: none`，这里放开收缩 + `flex-wrap`），
      不把标题挤成省略号（实测 342px 宿主：不放开时标题只剩 43px 可用宽会截断，放开后 83.6px ✓）
  · 底色 = **当天支出 / 收入 / 净额 / 笔数**的 5 档（跟着上面那颗口径走），档位是**全历史**
    一次分数分出来的（`_billHeatThresholds`）—— 按月各分各的，各年深浅就不可比；
    **没有账单的天完全不上色**（格子透明，实测 `rgba(0, 0, 0, 0)`）**没有账单的年份不占位**；
    **有账单、但当前口径下是 0** 的那天（如"支出"口径里只进不出）给一层中性灰（`.is-zero`，
    与档位类互斥）；
    **色相跟着口径换**（色值抽成了 `--heat-rgb`，5 档只用写一遍）：支出 = 红（默认，与月历格子
    共用同一组色值）、收入 = 绿、笔数 = 主色（teal）；**净额逐格按当天正负给色**（正绿 · 负红，
    同一张图上红绿都有），值为 0 的那天不给档位、也不给色相。图例那 5 个色块跟着换口径换色
  · 有账单的那天可点 = **范围窗口起手在那一天**（与上面月历的格子同一落点），有账单的天才有 tooltip
  · 数据 = `bill_periods level=day&mode=normal`（**全历史逐日、后端不截断**），与格子 / 合计 / 明细
    **同一份筛选口径** → 所以它**跟着页面那颗来源**（`来源 ▾` 管整页），自己不另摆一颗
  · ⚠️ 量级：16 年 ≈ 6000 个格子 —— 每条年带都挂了 `content-visibility: auto`（只渲染看得见的），
    点击是 `.bill-yheat` 上的**一个事件委托**（不给每格挂监听）；格子尺寸**随容器自适应**
    （列宽 `1fr` + `aspect-ratio: 1`：实测桌面 722px 宿主 → 每格 **10.11px**、年带高 82.9；
    342px 宿主 → 每格 2.94px；**不横向滚**，月份标签零重叠）
  · ⚠️ **宽度完全由父级给**（`.bill-heat-section { contain: inline-size }` ——
    两处落点共用这一个类，见下面 ③ 查询页那条）—— 与上面历史页那条同一个坑
    （见 ③b 前的说明）：`repeat(N, minmax(0,1fr))` 的 **max 是内容**，而 12 个月份标签是
    `nowrap` 文字；**标题行也会出价**（副标题 `nowrap` + 一排胶囊）——
    所以守卫挂**整块**而不是只挂 body。宿主里有"按内容定宽"的一类（未配 `width` 的
    `popup_card` 是 shrink-to-fit）→ 窄宿主会被**顶宽**。
    实测（headless Chrome，本该 342px）：只挂 body → 格子那部分被顶到 **483px**、
    加了胶囊与长副标题后整块 **491.94px**；挂整块 → **342px** ✓（两处落点都对）
    固定 360px 宽时**横向溢出 0** ✓（"不要改变宽度"指的就是这个）

**③ 查询页**

- 条件七个字段（关键词 / 对方 / 开始日期 / 结束日期 / 最小金额 / 最大金额 / 收支方向），**默认展开**；点标题行可折叠（折叠状态在这一会话里保留），**点「查询」后自动折叠**把高度让给结果，**点「清除」自动展开**
- 结果区从上到下：**条件胶囊 + 时间路径条（同一行）** → **汇总**（收入 / 支出 / 净额 / 不计收支 / 笔数 —— **有哪个显示哪个**；口径是**整段条件的全量**，不只是本页；**收入 / 支出 / 不计收支 三格可点 = 结果只看那一类**，写进 `direction`、再点一次取消）→ **趋势柱图** → **排序条**（时间 / 对方 / 类型 / 方式 / 来源 / 金额：点列名排序、再点同一列反向）→ 结果列表 + 分页。
  标题行右插槽是 **「来源 ▾」筛选**（只作用于这次查询：写进 `state.query.source`，与条件胶囊同一套，
  所以它会以 `来源 xxx` 一颗出现在那排胶囊里、点一下去掉）+ 「清除」
- **趋势柱图**（与范围窗口同一张图：两根柱 + 可能有的「不计收支」灰柱、**没账单的时间桶不占位**）：
  取 `bill_trend`、**与明细同一套条件**（两者笔数必须相等，对不上就**不画**并给一行说明 ——
  接口的趋势聚合可能不认 `keyword` 这类条件）：图看的是**时间路径的下一层**
  （0 段 → 按年；1 段"某年" → 按月；2 段"某月" → 按天；3 段"某天" → 按小时）。
- **结果热力**（`_buildBillQueryHeat` —— 与日历页「历年热力」**同一套渲染**，见 ② 那句：
  两处共用 `_buildBillHeatSection` / `_billYheatDraw` / `_billYheatYear` / 四口径与色相 / 图例）：
  · 位置：**趋势柱图下面、排序条上面**（独立一块，默认收起 + **展开才取数**）；
  · ⚠️ **不吃时间路径**（用户定的）：只吃**条件**（`state.query` + 全局维度）——
    于是无论钻到哪一层，它都是"**这批条件的全时间全景**"；副标题写明
    「全部时间（不含时间路径）· N 个年份 · M 天有账单」（这条口径**也是它的缓存键**：
    只钻时间路径不重取，条件一变自动重取）；
  · **点某天 = 把时间路径压到那一天**（`_billQueryGotoDay`：三段 `2026年 › 10月 › 9日`）——
    明细 / 柱图随即收窄到那天（与"点柱子"同一手势，热力图是一步到位）；
    顺手把表单里手填的 `start` / `end` 让位（两套时间条件并存会打架，与 `_billQueryDrill` 同一条规则）；
  · 右插槽：**四个口径胶囊**（支出 / 收入 / 净额 / 笔数，切口径不重取数）——
    **不摆来源筛选**（结果区那颗 `来源 ▾` 本身就是条件，这一块跟着它）；
  · 边界：一条都没命中 → 「没有符合条件的账单」；**这个口径下一个正数都没有**
    （条件筛"支出"、口径却停在"收入"）→ 补一行"换上面一个口径看看"，图照画不空白；
  · 视觉：这块**套在「查询结果」那个大框里**，所以自己不再套框
    （`.bill-query-heat-section` 去背景 / 边框 / 内边距，与 `.bill-hero-section` 同一套）
- **时间下钻 = 一条路径**（与范围窗口同一条 `.bill-crumb`、同一套手势）：点年 / 月 / 天的柱子
  往路径里压一段，攒出来的是 `state.queryPath`，**塞在条件胶囊那一行里**，读起来就是
  **`关键词 spp ✕ 全部 › 2020年 › 5月 › 26日`**（根段「全部」点它 = 清掉时间、只留条件；
  每段可点返回那一层）。已经在"某天"这一层（按小时）→ 点柱子打开**范围窗口**看那一小时
  （查询条件的粒度到"天"为止，再往下交给它自带的搜索 / 排序 / 分页）。
  · **不再往查询条件里写日期**（早期版本写 `start` / `end`，结果摊成
    `开始 …` + `结束 …` 两颗胶囊，很难读 —— 用户提的）
  · **不再有「涉及年」那排**：时间下钻已经有路径条 + 柱图，那排年份胶囊是重复的第二套入口
    （连带 `bill_periods` 那一次请求也省了）
  ⚠️ **日期字段的键名是 `start` / `end`**（查询表单那套，`BILL_QUERY_LABELS` 里就是
  `start: '开始'`）—— 写成 `date_from` / `date_to` 后端**不认**，条件形同没填
  （明细里会混着别的年份）；页面 `load` 会顺手自愈掉早期版本留下的错键。
  ⚠️ **趋势接口另有一套时间口径** `year` / `month` / `date`（下钻窗口就是这么传的），
  所以拼 `bill_trend` 参数时按路径补这套；手填区间（表单那两个日期框）则从区间反推
  "最窄且完整"的那一级（同月 → 按天；同天 → 按小时）。
- 当前生效的每一条条件都会在结果区顶部显示成**可点的胶囊**（点一下去掉这一条）—— 从详情气泡钻进来的条件也在这儿管理；**起止日期合成一颗**（`日期 2020-06-01 ~ 2020-06-30`，点它两个字段一起去掉）

**③b 历史页**（两块都是"按年"柱图，`_billYearBars`）

- **历史今日**：**默认**柱图按年（那几年这几天的收支）+ **一行合计**（`.bill-recent-total`，
  与「最近 N 日」同一版式：`往年收入 / 往年支出 / 净额 / 不计收支 / 笔数`，"有哪个显示哪个"；
  钻进某一年时换成**那一年的**合计）+ 下面按年列明细（**各年一律收起、不默认展开**）；
  这一行**纯展示**（不接"点格子筛明细" —— 下面那排是**按年份**分的块，方向筛要另起一套）；
  ⚠️ 它下面紧接的年份块**同色底**（都是 `--bill-surface`），基类没有下外边距 ⇒
  这一处单独补 `margin-bottom: 9px`（`.bill-otd-section .bill-recent-total`），
  与日历页 `.bill-cal-summary` 同因同法，否则两块灰底会连成一片；
  **基准日默认「今天」，也可以指定** —— 标题行那颗 `日期 ▾`（`_billOtdPick`）：
  · **月日口径**（`month_day=03-24`）：历年**同月同日** —— `otdYear` 一钻就出「那一天的小时」；
  · **几号口径**（`day_of_month=24`）：历年**每月 24 号**（跨所有月）—— 一个年份 = 12 个日期，
    所以点柱子**不开就地钻**，改成开**范围窗口**（参数钉住 `day_of_month`，在里面 年 → 月 → 日 → 时）
  · 两个口径**互斥**（`state.otdMd` / `state.otdDom`），气泡里一排 `月日 / 几号` 切换，
    下面分别是通用两列面板（`.rm-pick`）与 1~31 格子（`.rm-pick-right.cols-7`），
    底部一颗 `回到今天` 清空；选定 → `_billOtdSet` 重取 + 重绘
  · **标题跟着基准日变**（`_billOtdTitle`）：没指定 = `历史今日`（月日由副标题交代）；
    月日口径 = `历史 03-24`；几号口径 = `历史 · 每月 24 日`。标题带了基准日，副标题就不再重复它
  · **选「月日」会联动下面那块「历史本月」**：`state.tmMonth` 跟着变成同一个月 ——
    两块说的就是同一个时点（`历史 03-24` + `历史 3 月`）。**选「几号」不联动**
    （没有月份可言），`回到今天` 则是两块一起复位（历史本月回「当月」）
  上面两种口径下：柱图都是**按年** + 下面按年列明细（**各年一律收起** —— 进来先看
  "一张按年图 + 一排年份标题"，想看哪一年的明细点它自己展开；点柱子钻进去时那一块才展开）
- **月日口径下点某年的柱子 = 就地钻到"这一年的这一天"** —— 月日相同 ⇒ **年 → 时一步到位**
  （中间不摆"月 / 日"两层，在这里它们是同一个值）：柱图换成**那天的小时**
  （`bill_trend granularity=hour` + `date`，**按日期缓存**、空小时不占位），
  下面 `bill-otd-list` 只列**那一年**的明细，副标题也换成「2019 年 · 这一天按小时」；
  上面多一条面包屑 `全部年份 › 2019 年`（点根段回各年概览）。标题行那颗「往年合计」照旧。
  （年份条那个折叠入口还在 —— 各年概览时点年份条仍是展开 / 收起那一年。）
- **历史本月 = 一块讲「同比」的地方**（`bill_yoy` + `month_of_year`）：
  · 柱图**按年**（这个月历年的收支），**年份由早到晚**（趋势的正序 —— 同比"从去年指向今年"才对得上）；
    **点柱子 = 开该年该月的范围窗口**（与「年度收支」的行同一落点）
  · 图下一排**同比胶囊**（`2019年 ↑12%`）：**只跟"去年同月"比**（`year-1` 真在数据里才算），
    缺去年（或去年是 0）→ `—` 灰 —— 原来那个"较相邻那一年"的算法在缺年时会跨年比、语义飘。
    **↑ 红 = 比去年同月花得多** / ↓ 绿 = 少 / 0% 无箭头；今年这个月还在过 → 描一下边 + tooltip 写"进行中"；
    tooltip 给全（两个绝对值 + 笔数 / 净额）。「收入同比」没做（`bill_yoy` 只给支出同比，口径以接口为准）
  · **月份可换**：标题行 `◀ 9月 ▶`（按 1~12 环绕），换月重取一次 `bill_yoy(month_of_year=X)`；
    看的是当月时副标题补一句「（当月）」；不在当月时**月份标签自己可点 = 回本月**（省一颗按钮）
  · **标题跟着月份变**：当月（默认）= `历史本月`、副标题 `9 月 · 5 个年份（当月）`；
    指定了月份 = `历史 3 月`、副标题只报 `5 个年份`（换月、或被「历史今日」的月日联动都走这里）
  · ⚠️ 原来"柱图 + 同一份数据的进度行"是**同一份数字看两遍**（柱子只当"点开窗口"的入口）——
    这块的进度行已撤掉，换成同比那一排：重复没了，块真正想说的那件事上了台面
- 两张图与其它柱图同一套：两根柱 + 可能有的「不计收支」灰柱、**没账单的年份不占位**、
  带 X 轴与柱顶数值；标题行各有一颗**本块来源筛选**（`bill_onthisday` / `bill_yoy` 各取各的 `source`）。
- ⚠️ **历史页的区块 body 声明了 `contain: inline-size`**（`[data-bill-page="history"]`）——
  这一页的内容**不能反过来把卡片撑宽**。原因与 `.bill-cols` 那条同一个：宿主里有"按内容定宽"
  的（未配 `width` 的 `popup_card`），而**五档面板是同格叠放的**（`visibility` 藏），
  任何一档有多宽、卡片就多宽；历史页最容易出事的是「历史本月」那排同比胶囊
  （`flex-wrap` 在 max-content 计算里不换行）。只加这一页：别的页的宽度就是卡片本该有的宽度。
- ⚠️ 历史今日那块：接口**若只回净额**（不回收 / 支），柱图自动退成**单值柱**
  （`|净额|`，按正负着色），提示行也写明"按年看净额" —— 不会因为缺字段就没图。

**④ 明细行 → 详情气泡 → 一键去查询**

「账单详情」气泡里的 **数据来源 / 交易类型 / 收·支方式 / 对方 / 对方单号 / 商品说明 / 交易状态 / 交易单号** 这些字段**可以点**：点一下直接切到「查询」页、按这一个字段重查（**所有选项卡**的明细行都生效，因为它们开的是同一颗气泡）。`对方账号 / 导入备注 / 记录 ID` 在后端没有对应过滤口径，保持"只能看"。

#### 三种入口

| 入口 | 配置方式 | 形态 |
|------|----------|------|
| 独立弹窗 | `tap_action: { action: card, card: { type: bill } }` | 弹出的独立面板（默认 `720px` 宽，见配置项 `popup_width`） |
| 内嵌弹窗 | `tap_action: { action: popup_card, card: { type: bill } }` | 通用弹窗里嵌一张账单卡（宽度用 `tap_action.width`） |
| 常显卡片 | `type: custom:room-elves-card` + `standalone_type: bill` | 直接把整卡当一张卡片用 |

```yaml
# 最常见：挂在某颗按钮上，点开是独立弹窗
type: custom:room-elves-card
room_name: 客厅
buttons:
  - entity: sensor.wen_du          # 挂哪颗按钮上就点哪颗
    name: 账单
    icon: mdi:receipt-text-outline
    tap_action:
      action: card
      card:
        type: bill
        name: 个人账单
        api_base_url: http://192.168.1.100:8123/api/ha_data_store/
        key: 你的KEY
        popup_width: 760px
        popup_position: center
```

```yaml
# 常显：直接作为一张卡片
type: custom:room-elves-card
standalone_type: bill
name: 个人账单
api_base_url: http://192.168.1.100:8123/api/ha_data_store/
key: 你的KEY
page_size: 20
recent_days: 7
```

#### 配置项

| 参数 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `api_base_url` | ❌ | `string` | ha_data_store 地址（不配时回退同源 `/api/ha_data_store/`；作为弹窗子卡时会**继承宿主卡**的同名值） |
| `key` | ❌ | `string` | API Key（同上，可继承） |
| `name` | ❌ | `string` | 标题，默认「个人账单」 |
| `icon` | ❌ | `string` | 标题图标，默认 `mdi:receipt-text-outline` |
| `subtitle` | ❌ | `string` | **未选数据来源时**的副标题文案（选了来源就显示来源名） |
| `accent` | ❌ | `string` | 外壳主色，默认 teal `#26a69a` |
| `page_size` | ❌ | `number` | 明细分页每页条数，默认 `20`（最小 5） |
| `recent_days` | ❌ | `number` | 概览「最近 N 日」天数，默认 `7`（明细默认先列前 `10` 条、可「加载更多」每次 +`20`；手上最多该窗口接口能给的最近 `60` 条。两者都不可配） |
| `source` / `direction` | ❌ | `string` | 初始维度筛选（数据来源 / 收支方向） |
| `width` / `popup_width` | ❌ | `string` | 卡片宽度 / 独立弹窗宽度（默认 `720px`；两者都给时 `width` 优先） |
| `popup_position` | ❌ | `string` | 弹窗位置，默认 `center` |

#### 接口一览（卡片实际调用的）

| 接口 | 用途 | 用在哪 |
|------|------|--------|
| `bill_dashboard` | 概览一次取全（总计 + 来源 + 年度 + 最近 N 日） | 概览 |
| `bill_trend` | 趋势序列（`granularity=year/month/day/hour`） | 分析「月度趋势」、概览「月度收支」「年度收支（带本块来源筛选时）」、下钻窗口、**查询结果区那张柱图** |
| `bill_group` | 分组汇总（`category` / `source` / `pay_method`） | 分析四张环形图 |
| `bill_ranking` | 排行榜（`dimension=counterparty`） | 分析「对方排行」 |
| `bill_hour_dist` | 按小时分布 | 分析「支付时刻」 |
| `bill_flow` | 资金流向（`from_dim` → `to_dim`，`nodes` + `links`） | 分析「资金流向」（纯 SVG 桑基图；起 / 终维度在标题行换，**默认 `source → category`**、`limit=500`） |
| `bill_calendar` | 活跃日历（`month=YYYY-MM&fill=1`） | 日历页格子 |
| `bill_history` | 明细（分页 + 子串过滤 + `order_by`） | 日历页本月明细、查询页结果、**范围窗口的明细 + 合计**（`summary` 是整段全量算的） |
| `bill_periods` | 有数据的年月 / 年份（`level=year|month&mode=minimal`）/ **全历史逐日**（`level=day&mode=normal`，后端不截断） | 日历页年月面板、**日历页「历年热力」**、**查询页「结果热力」**（后两处都是 `level=day` 那一次：16 年 ≈ 6000 行，`mode=normal` 已含收 / 支；**展开那一块时才发**，都不进页面的 `load`；查询页那份**只带条件、不带时间路径**） |
| `bill_yoy` | 逐年同月（`month_of_year`） | 历史页「历史本月」 |
| `bill_onthisday` | 历史今日（`month_day=MM-DD` 历年同月同日 / `day_of_month=DD` 历年每月那一天；都不传 = 今天） | 历史页「历史今日」 |
| `bill_notes` | 备注候选（去重 + 次数） | 详情气泡的"常用备注" |
| `bill/add` · `bill/remark` | 新增一条账单 / 单写备注（**仅这两处写入**） | 浮动「新增」按钮、详情气泡 |

#### 说明与已知边界

- **无轮询**：数据只在四个时机取（打开卡片 / 切到没取过数的页 / 点头部刷新 / 查询与换条件）；`hass` 推送只重算外壳（页签、副标题、高度），**不会重新取数**。
- **月度序列后端是 `ORDER BY bucket ASC LIMIT n`**（截的是"最早的那一批"）：卡片为此留够条数（240）再取尾部 12 个月 —— 自己写调用时别直接 `limit: 12`，否则会拿到十几年前的那 12 个月。
- 「月度收支」默认只显示最近一个月（与「年度收支」同款折叠），点右上角「更多月份」展开其余。
- 卡片与它所有弹窗**不引第三方图表库**：环形图是 SVG（`stroke-dasharray`）、柱图是 flex 高度百分比。
- 明细行的「数据来源 / 类型 / 方式…」点击查询、以及查询页的「来源 ▾」筛选 / 「排序条」，口径都以**后端接口的过滤字段名**为准（`source` / `category` / `pay_method` / `status` / `bill_no` / `keyword` / `start` / `end` / `direction` …）。

### 6.46 iKuai 全实体卡片 (type: ikuai_card)

> **一张卡看全一台爱快：只配一个聚合实体，卡片自己认设备、认角色。**
>
> ⚠️ **前置条件：必须先安装自定义集成 [`ikuai`](https://github.com/chjspp520/ikuai)（必需）**
> —— 卡片自身不采集数据，全部内容都来自该集成的聚合实体 `sensor.ikuai_all_entities`。
> **没装 / 没配置集成时，这张卡没有数据可显示**（只会给一句提示，不是卡片坏了）。
>
> 📌 **本节对应版本：v6.3.0（2026-10-14，后续小版本微调）** —— 这张卡在 **v6.2.0**（2026-10-12）入库
> （四个页签进头部 + "数据驱动、不写死实体 id"这两条口径）。**v6.3.0** 定下的形态：
> 虚拟机画面「叫醒」时序修正 · IM 聊天记录只留重要信息 · 「路由」页新增 **DHCP 子页签** ·
> 硬件信息的「复制」按钮与查询时间并成页脚一行。**v6.3.4** 又加了一条：查询 API 开着时，
> 头部那条分割线变成「API 密钥剩余时长」进度条（见本节末段）。**v6.3.5** 再加两条：
> ① 头部副标题只在前三个页签及以内显示（页签数 >3 就隐藏）；② 副标题里那对总上传/总下载
> 挪进「网络」左栏 —— 紧跟实时速率行下面当第二行（第一行速度、第二行流量，↑ 绿 / ↓ 蓝）。
> 逐条改动见 `CHANGELOG.md` 的 **v6.3.5** 段（第 232 节）、**v6.3.4** 段（第 231 节）与
> **v6.3.0** 段（第 226~229 节），布局由来见 **v6.2.0** 段（第 219~225 节）。
>
> ⚠️ 旧的 `type: ikuai`（依赖旧集成 `ikuai_router`）**已在 v6.4.x 整卡移除**（`CHANGELOG.md` 第 242 节），
> 现在爱快只有这一张卡 —— 根类名 `.ikuai-card-root`（类型名本身已含 card，按规则会得到 `ikuai-card-card`，故单独定名）。

#### 依赖集成：`ikuai`（必需）

本卡片**不能独立工作**，数据全部来自自定义集成 **`ikuai`**：

- **仓库地址**：https://github.com/chjspp520/ikuai （下载 / 更新都从这里取）
- **安装位置**：`<配置目录>/custom_components/ikuai`（开发机映射盘 `Y:\custom_components\ikuai`）
- **安装步骤**：
  1. 从上面仓库下载，把整个 `ikuai` 目录放进 HA 配置目录的 `custom_components/`；
  2. 重启 Home Assistant；
  3. 「设置 → 设备与服务 → 添加集成」，搜索 **iKuai**，填爱快路由地址与账号密码。
- **它提供什么**：为整台爱快建实体（系统 / 接口 / 线路 / DHCP / 客户端 / 本地认证 / Docker / 虚拟机 / 日志 / 查询 API…），并生成**聚合实体 `sensor.ikuai_all_entities`** —— 卡片就是靠它"一次拿到全部设备与实体"，所以配置里**只要一个实体**，不必逐个写。
- ⚠️ **别装错集成**：旧集成 `ikuai_router` 是已删除的 `type: ikuai` 旧卡用的，**不适用这张卡**。

聚合实体的 `attributes.groups[]` 就是一份**实体目录**（集成按设备标识自动归类：`router` / `docker` / `auth` / `vm_<id>`，
每项 `{entity_id, name, state, icon}`）。

- **卡片不写死任何实体 id**：角色与归类全认**短名**（显示名去掉设备名前缀：`iKuai CPU占用` → `CPU占用`，
  `虚拟机 win7 远程控制台` → `远程控制台`），id 后缀只作兜底 —— HA 占号（实测 `sensor.ikuai_cpu_2`、
  `switch.ikuai_docker_nps_2`）很常见，按 id 锚定必然错；新增容器 / 账号 / 虚拟机不用改一行代码。
- 目录里的 `state` 是集成侧的合并快照，**实时值一律回 `hass.states` 读**（否则点了开关界面最长好几秒不动）。

#### 三种入口（与其它卡片一致）

| 入口 | 写法 |
|------|------|
| 独立卡片 | `standalone_type: ikuai_card`（高度 `auto`，卡片自带 3 秒值级刷新，故不参与独立模式的 1 秒轮询） |
| 点按钮弹出 | `tap_action: { action: card, card: ikuai_card }`（走 `showIkuaiAllPopup`） |
| 弹窗内嵌 | `tap_action: { action: popup_card, card: { type: ikuai_card } }` |

#### 配置项

| 键 | 必填 | 类型 | 说明 |
|----|:----:|------|------|
| `entity` | ❌ | string | 聚合实体（默认 `sensor.ikuai_all_entities`） |
| `name` / `icon` | ❌ | string | 头部标题 / 图标（默认「爱快」/ `mdi:router-network`） |
| `accent` | ❌ | string / object | 主色调（走框架 `applyAccent`：命名色 / hex+rgb / auto / 实体驱动） |
| `width` / `popup_width` / `popup_position` | ❌ | number / string | 卡片宽度、弹窗宽度与弹出方位 |
| `confirm_power_off` | ❌ | bool | 关机类操作是否二次确认（默认开） |

#### 四个页签（后三个按"内容存在与否"自动出现）

| 页签 | 内容 |
|------|------|
| **路由** | 页内再分六个子页签，见下一节 |
| **Docker** | 容器一行一个（状态 / 镜像 / 内存占用；点开看该容器信息）+ 启停 / 重启 / 删除；容器区不折叠 |
| **虚拟机** | 每台一张卡：电源开关 + 远程控制台（集成签好的 noVNC 地址，iframe 内嵌）+ **画面预览** + 属性与操作；屏幕墙是页内折叠区块（最多 8 格，点某格才进控制台 —— 格子本身不嵌 iframe） |
| **日志** | ① 告警与消息（未读数 + 全部已读 / 清空）；② 每个分类一个折叠区块（标题 = 短名去掉「日志-」前缀 + 实时条数，展开列出最近记录，点单条看完整字段，右上「清空」二次确认） |

#### 「路由」页的六个子页签（`ikuai-card-mini-tabs`）

顺序按"一台路由器实际长什么样"排 —— 先总览 → WAN 侧 → **LAN 侧地址分配** → 拿到地址的终端 → 认证 → 设置：

| # | 子页签 | 内容 |
|---|--------|------|
| ① | **网络** | 网络总体状态 + 上下行当前速率（两栏大字，带色点）+ **近 30 分钟双线 SVG 曲线**（历史一次 + 之后每 5 秒采一点）+ 网络关键格 + 流量分布环形图（近30分钟 / 近1小时 / 近1日 三档胶囊）+ 网络接口（外网口 / 内网口）+ ARP 表（条目数 + 已绑定筛选） |
| ② | **线路** | 拨号 / VPN：四个页签（在线线路 / PPPoE / PPTP / L2TP，数写在页签里）+ 选中那一类一行一条（连上没连上、连的谁、拨在哪个口、上线多久） |
| ③ | **DHCP** | DHCP 服务（`sensor.ikuai_dhcp`）：四档页签（服务端 / 静态分配 / 动态租约 / MAC 名单）+ 选中那一档。**条件页签：没有这个实体就不出现**（其余五档常驻，各有空态文案） |
| ④ | **客户端** | 在线终端一行一台 + 右侧「**允许上网**」开关（直接控制 `switch.ikuai_mac_*`，不是"写 MAC + 按按钮"）；缺 MAC 管控 / 终端跟踪实体时给一句说明，不空屏 |
| ⑤ | **本地认证** | 本地认证 / VPN 服务端（PPPoE・PPTP・L2TP・OpenVPN）的启停与参数 + 认证用户 |
| ⑥ | **设置** | 系统操作（只露常用：重启 / 重连 WAN / 同步时间 / 清空流量 / 拉黑放行；低频项在「更多操作」气泡里）+ 服务开关（按功能分组）+ 网络唤醒 + 固件（只报版本，升级在爱快后台）+ 规则统计 + 兜底的其他实体。**整页不折叠** |

#### DHCP 子页签（v6.3.0 新增）

数据源就是 `sensor.ikuai_dhcp` 的四组属性：`servers`（服务端配置）/ `statics`（静态绑定）/ `leases`（动态租约）/
`blocked`（MAC 名单），条数差异极大（实测 1 / 76 / 78 / 1）—— 所以和「线路」页同一套打法：**页签分四档 + 按需建体**，
只把选中那一档的行建进 DOM；页签里带着条数（优先用集成的 `static_total` / `lease_total` / `blocked_total`），空的档淡一档。

- **服务端**：一台一张小卡 —— 启用旗标 + 物理口 + 只露**非 0** 的选项旗标（地址有效性检测 / 仅中继 / 延迟）
  + 参数两列（地址池 / 排除地址 / 掩码 / 网关 / DNS 并排 / WINS / 域名 / 可用地址 / 租期），**集成没给的字段不列**；
  点了这张卡看完整配置。
- **静态分配 / 动态租约**：共用一个「筛选框 + 可排序表格」（列只差最后一格 —— 接口 / 剩余租期）。
  - 排序：点表头换列、再点反向（↑ ↓）；**IP 按 `ip_addr_int` 数值排**（不是字符串）；
  - 筛选：可搜 IP / MAC / 名称 / 主机名 / 接口，**多个词是「且」**；底部 `显示 x / y 条`（集成截断过会说明一句）；
  - 租约行的色点按 `status === 1` 分「在线 / 其它」两档（集成没给这个字段的映射，所以不猜语义，
    原始值放在行 `title` 里：`status=0 · 到期 … · 起租 …`）；
  - 点一行 → **详情气泡**：hero = 记录名 + `IP · 所属接口` + 状态徽标（静态绑定的「已启用/已停用」、租约的「租期中/已到期」）、
    关键格全是**中文标签**（IP 地址 / MAC 地址 / 备注 / 主机名 / 所属接口 / 剩余租期 / 到期时刻…）、
    「复制 IP / 复制 MAC」动作，摆不下的生僻键收进**折叠的「原始字段」**（默认收起，排查时才展开）；
    每个值**现读**当前那一行，属性一刷新（3 秒 tick）就跟着变。
- **MAC 名单**：`acl_mode_text` 说明这是黑名单还是白名单 + 一行一条（MAC / 备注 / 启用状态），
  IPv6 侧（`dhcp6_blocked`）有内容才画一段。

#### 头部那条分割线：API 密钥剩余时长进度条

`switch.ikuai_api`（查询 API）**开着**时，头部下面那条分隔线本身就是**进度条**（`.ikuai-card-api-bar`）：
填充比例 = `sensor.ikuai_api_key` 的 `remaining_seconds` / 3600（集成整点换新，一把 key 的周期就是 1 小时），
从右往左退。**一枚小标签骑在进度条上**，跟着填充端点一起滑动，写剩余时长 ——
**<1 分钟 `x秒` ｜ <60 分钟 `x分` ｜ 否则 `x.x时`**（向下取整）；**轨道与标签同色三档**：
**<1 分钟红 ｜ 1~10 分钟黄 ｜ >10 分钟绿**（两端各收 6%，标签不会滑出卡片）。
**点标签**弹出「API 密钥」详情气泡（中文标签 + 简约骨架：密钥 / 条目 / 有效至 / 剩余时长 /
调用次数 / CPU 指纹 / 算法 / 用法 + 复制密钥）。`off` 时整条进度条不出现，头部保持原样。
剩余时长的取值顺序：`remaining_seconds` → 实体 state（分钟）→ `valid_until` 推算；三者都没有就不画，不编数。

#### 刷新与开销

- **3 秒值级刷新**（只做文本 / 宽度 / 类名的脏检查写入）：页面不可见跳过、卡片脱离 DOM 自动停表；
- `image.` 实体**不订阅**（每 5 秒一跳纯噪音）；画面只在「虚拟机 / 屏幕墙」页才 render；
- 虚拟机那格画面预览是**懒加载实体**的特例：实体 state 为空时卡片会**主动叫醒**一次
  （给 `<img>` 指一次 `/api/image_proxy/…?state=kick…`；叫醒期间 20 秒内不再调 render 把它撤掉），
  抓帧成功后实体 state 有值，常规路径自然接管 —— 缘由与坑见 `CHANGELOG.md` 第 226 节；
- 大分组（>12 项）区块默认收起，框架的 section **展开时才建 body** —— 173 个实体的环境首屏也不会把 DOM 撑起来。

---

### 6.47 叮咚门铃卡片 (type: dingdong)

> **只配一个「实体清单」实体，就能把一台叮咚（移康 eques）门铃装进一张卡：抓拍 / 实时画面 + 按天回看的事件时间轴 + 设置 + 诊断。**
>
> 清单实体由 `eques_dingdong` 集成提供（默认 `sensor.eques_bell_entities`），它的属性
> `entities = [{ entity_id, name, icon, state }, …]` 列出该设备名下**全部**实体；
> 卡片按「**域 + entity_id 后缀**」自己反查角色（22 条角色表见下）——
> **换设备、多台门铃、实体被集成改名，都不必改配置**。
>
> 📌 卡片本体就是一张**卡内选项卡**（不再自动开弹窗）；`action: card` 弹出的是同一套内容的独立弹窗。

#### 依赖

| 依赖 | 必需性 | 说明 |
|------|:------:|------|
| `eques_dingdong` 集成（`Y:\custom_components\eques_dingdong`） | ✅ | 卡片**只读**它产生的实体，不调用集成内部代码 |
| **「实体清单」实体**（默认 `sensor.eques_bell_entities`） | ✅ | 卡片唯一的入口实体；取不到 → **整卡空态**（只留一句"实体清单不可用" + 实体 id），不留半截空壳 |
| 「录像抓拍接口密钥」实体（`sensor.*_api_key` 的 `key` 属性）+ 集成路由 `/api/eques_dingdong/day` · `/events` · `/media` | ➖ | 按天明细、多天事件、媒体直链走接口。集成那几条路由是自鉴权的，直链必须显式带 `?key=`；**接口关着/取不到 → 退化为实体属性里残留的那部分**，并在块下给一句原因 |
| 画面实体：`image.*_last_capture`（抓拍）/ `camera.*_live`（实时）/ `camera.*_live_sub`（反转）/ `camera.*_last_clip`（最近录像） | ➖ | 缺哪个就不摆哪个画面源按钮；一个都没有 → 画面区只有 HUD 空态 |
| `switch.*` / `number.*` / `select.*_sensitivity`（设置项）、`button.*_refresh_info` · `_switch_camera` · `_restart` | ➖ | 卡片按域全收开关/数字；缺了对应区块不出现 |

> 卡片**不引第三方库、不连 CDN**（图表与装饰全是 SVG / CSS）；不用自带轮询定时器，
> 5 秒值级刷新挂在宿主卡片的共享 tick 上，页面不可见/脱离 DOM 自动停表。

#### 适用范围

**适用：**

- ✅ **叮咚 / 移康（eques）门铃**由 `eques_dingdong` 集成接管的设备。一张卡一台设备，多台就配多张卡（各自写自己的清单实体）。
- ✅ 以**按天回看**为主的场景：日期条选天 → 当天的事件 / 抓拍 / 录像**混在一条时间轴**上；另有跨天的双向时间轴（竖向日期 × 横向时刻，10 分钟一格）。
- ✅ **电池供电设备**：默认只显示「最后一条」抓拍（不唤醒设备），要看实时得手动切到「实时」，切走/关闭即释放会话。

**不适用 / 需注意：**

- ❌ **非 `eques_dingdong` 接管的摄像头**：卡片只认这一个清单实体（角色靠集成固定命名反查），其它品牌请用 HA 原生 picture / camera 卡片。
- ⚠️ **`standalone_type: dingdong` 未适配**：卡片能被常显渲染，但独立模式的高度分支（`modules/core/standalone.js` 里那份"高度由内容决定"的名单）**还没有这一项**，常显时会走 `height: 100%` 可能把内容裁掉。**要常显请用 `popup_card` 内嵌**（或在自由布局弹窗里用 `type: card` 内嵌）。
- ⚠️ **实时画面会唤醒电池设备**：集成侧是私有 P2P 协议转 MJPEG，拉流即唤醒机器。不希望被唤醒就把 `show_live: false`（画面源只剩「最后一条」），或干脆切到「最后一条」。
- ⚠️ **日期条能不能选，取决于「每日汇总」实体**：可用标记与置灰都以它的 `每日` 属性为准（媒体被淘汰后不回退，是"哪些日子有数据"的权威口径）；没有这个实体时日期条退化为只读当天。

#### 三种用法

```yaml
# ① 卡片自带弹窗（action: card）
tap_action:
  action: card
  card:
    type: dingdong
    width: 520px

# ② 内嵌进 HA 原生弹窗（popup_card）
tap_action:
  action: popup_card
  card:
    type: dingdong
    name: 入户门铃

# ③ 内嵌进自由布局弹窗（rows[].items 里用 type: card + card_config）
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  service_data:
    title: 门铃
    width: 440px
    tabs:
      - name: 门铃
        icon: mdi:door
        rows:
          - row: 1
            per_line: 1
            items:
              - type: card
                name: 画面
                card_config:
                  type: dingdong
                  width: 430px
```

#### 配置项

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` / `entity_list` | ❌ | `string` | `sensor.eques_bell_entities` | 「实体清单」实体；**必配的只有它一个**（两个键名等价） |
| `name` | ❌ | `string` | 清单实体的设备名（去掉尾巴"实体清单"） | 卡片标题 |
| `accent` | ❌ | `string` | 主题主色 | 外壳主色（走框架 `applyAccent`） |
| `date` | ❌ | `string` | 最近有数据的那天，没有就今天 | 初始选中日期 `YYYY-MM-DD` |
| `events_limit` | ❌ | `number` | `5` | 该日时间轴最多几条**事件**（1~20） |
| `shots_limit` | ❌ | `number` | `4` | 该日时间轴最多几张**抓拍**（0~12，`0` = 轴上不放抓拍） |
| `videos_limit` | ❌ | `number` | `5` | 该日时间轴最多几段**录像**（0~12，`0` = 轴上不放录像） |
| `show_live` | ❌ | `bool` | `true` | 是否给「实时 / 反转」画面源（关掉 = 只留「最后一条」，**电池设备的省电开关**） |
| `hero_ratio` | ❌ | `string` | 空 = 实测实时视频比例，量不到按 `16:9` | 锁死画面区比例，写 `16:9` / `4/3` / `1.78` 都认；**切换画面源不会改变高度** |
| `hero_max_height` | ❌ | `string` / `number` | 空 = 不限 | 画面区最高多少，`320`（自动补 `px`）或 `40vh` |
| `width` | ❌ | `string` | `520px` | 弹窗宽度（`action: card` 时生效） |
| `popup_position` | ❌ | `string` | `center` | 弹窗位置（`action: card` 时生效） |

> 「重启设备」的二次确认是**内置行为**（没有开关可配）：确认框文案固定为"确定要**重启门铃**吗？重启期间设备会短暂离线。"

#### 界面

**画面区（hero）**

| 位置 | 内容 |
|------|------|
| 右上 | 画面源切换：**最后一条 · 实时 · 反转**（按角色出现；`show_live: false` 时只剩「最后一条」） |
| 左上 | 在线点（绿/红/灰）+ 设备名 + 在线文案 |
| 左下 | 最近事件（类型图标 + 相对时间） |
| 右下 | 今日报警大号数字（0 时弱化） |
| 整帧 | HUD 四角 + 缓慢下扫的光带（装饰，`prefers-reduced-motion` 下关掉）；响铃时红边脉冲 + 「响铃中」徽标 |

- **画面区高度固定**：口径优先 `hero_ratio` → 实测的**实时**视频比例 → `16:9` 兜底；**切换信号源不会改变高度**（抓拍与实时的原始比例不同，卡片刻意只认实时那一份）。
- **图片只自适应**：`object-fit: contain` —— 既不裁切也不拉伸，比例与画面区不一致时留**黑边**（画面区底色是纯黑）。
- **点画面**＝在**卡内窗口**看这一帧大图；录像则在卡内播放（不再跳新标签页）。

**选项卡（按实体可用性裁剪）**

| 选项卡 | 内容 |
|--------|------|
| **门铃事件** | 日期条 `◀ [2026-10-15 ▾] ▶ [今天]` + 该日三计数；下面是**事件 · 抓拍 · 录像混在一条轴**上的时间轴：日期组头（`10-15 周三 ──── 12`）、每条一个带图标的彩圈 + 标题/副标题/标签、右侧时刻（合并过的给范围）与抓拍缩略图 / 录像播放键。**点抓拍条目＝卡内看大图，点录像条目＝卡内播放**，同类事件 2 分钟内合并成「N 条 xx」，点它弹气泡看逐条 |
| **事件时间轴** | 跨天的双向时间轴（竖向日期轴 × 横向时刻轴，10 分钟一格一个点）；点小点弹气泡列出那一格的逐条明细，点日期行 = 选定那天并切回上一页（最多摆 12 天） |
| **设置** | 操作（刷新 / 换镜头 / 重启，重启二次确认）+ 开关（按域全收，中文短名取清单里的 `name`）+ 侦测灵敏度 + 数字参数 |
| **诊断** | 状态概览网格 + 设备诊断信息 + 录像抓拍接口 + 实体清单 |

#### 实体角色反查表（22 条）

卡片**不写死任何完整实体 id**：按「域 + entity_id 后缀」从清单实体的 `entities` 里反查，后缀**按长度降序**匹配（否则 `live` 会抢走 `live_sub`、`events` 与 `entities` 相互误吞）。

| 域 | entity_id 后缀 | 用途 |
|----|----------------|------|
| `binary_sensor` | `online` | 在线状态 |
| `binary_sensor` | `ringing` | 响铃中 |
| `sensor` | `alarm_today` | 今日报警数 |
| `sensor` | `last_event` | 最近事件 |
| `sensor` | `events` | 事件记录（条数 + 明细属性） |
| `sensor` | `daily` | 每日汇总（**日期条的可用性口径**） |
| `sensor` | `archive` | 最近录像与抓拍 |
| `sensor` | `battery` | 电池电量 |
| `sensor` | `storage_used` | 存储已用百分比 |
| `sensor` | `wifi_level` | WiFi 信号等级 |
| `sensor` | `device_info` | 设备诊断信息 |
| `sensor` | `api_key` | 录像抓拍接口密钥 |
| `sensor` | `entities` | 实体清单（自身） |
| `image` | `last_capture` | 最近抓拍（默认画面源） |
| `camera` | `live_sub` | 反转监控 |
| `camera` | `live` | 实时监控 |
| `camera` | `last_clip` | 最近录像 |
| `event` | `event` | 事件实体 |
| `button` | `refresh_info` | 立即刷新设备信息 |
| `button` | `switch_camera` | 切换摄像头 |
| `button` | `restart` | 重启设备 |
| `select` | `sensitivity` | 侦测灵敏度 |

> `switch.*` / `number.*` 两类**按域全收**（都是设备设置项，数量固定），中文短名直接取清单里的 `name`，不维护映射表。

#### 刷新与开销

- **5 秒值级刷新**（只做文本 / 类名 / 宽度的脏检查写入，`_registerLowFreqTask` 挂在宿主共享 tick 上）；结构（实体成员）变了才重建 DOM，重建时保留当前选项卡与选中日期。
- 抓拍画面走通用件 `infra/image-entity.js`（`/api/image_proxy/…?token=…&state=…`）；**存档里的媒体直链**（集成自己的 `/api/eques_dingdong/media/…`）直接给 `<img>` / `<video>` 并显式带 `?key=` —— 两者不是一回事，混用会让存档图被 image 实体的 token 算法重指。
- 实时画面走 HA 的 MJPEG 代理，**切走或关闭即释放会话**（电池设备不能 7×24 拉流）。

---

## 七、通用动作系统（tap_action）

所有支持 `tap_action` 的位置（按钮、title_entities、entities 区域、传感器卡片等）共享同一套动作执行引擎。动作类型统一，配置方式一致，`set_value` 和 `toggle` 还支持 `entities` 多实体批量操作。

### 统一动作清单

| action | 说明 | 支持多实体 | 必需参数 |
|--------|------|:----------:|----------|
| `toggle` | 切换开关状态（on↔off），自动推断服务 | ✅ | `entity` 或 `entities` |
| `set_value` | 设置实体目标值，自动推断服务（最灵活） | ✅ | `entity` 或 `entities` + `value` |
| `loop_assign` | 循环赋值：每次点击把实体推进到 `values` 序列下一个值，到末尾回绕 | ✅ | `entity`/`loop` + `values` |
| `process_execute` | 流程执行：按 `steps` 序列依次执行多实体操作，每步独立延时，复用情景推断引擎 | ❌ | `steps` |
| `quick-action` | 快捷操作，弹出情景模式气泡执行多步骤操作 | — | `scenes` 或 `actions` |
| `more-info` | 弹出 HA 标准详细信息弹窗 | ❌ | `entity` |
| `navigate` | 页面导航 | ❌ | `navigation_path` |
| `call-service` | 调用 HA 服务 | ❌ | `service` |
| `popup_card` | 弹出自定义卡片弹窗 | ❌ | `card` |
| `card` | 弹出设备内置控制弹窗 | ❌ | `card`（含 `type` 字段） |
| `toggle-all` | 切换分组中所有设备（仅聚合按钮） | — | — |
| `none` | 不执行任何操作 | — | — |

### toggle — 切换开关

自动根据实体域推断调用 `turn_on` / `turn_off` / `press` 等服务，无需手动指定。

```yaml
# 单实体 toggle
tap_action:
  action: toggle

# 多实体批量 toggle
tap_action:
  action: toggle
  entities:
    - light.keting_dadeng
    - light.keting_xuanguan
    - light.keting_xuanguan2
```

**自动推断逻辑：**

| 实体域 | on → 调用 | off → 调用 |
|--------|----------|-----------|
| `light` | `light.turn_on` | `light.turn_off` |
| `switch` / `input_boolean` | `turn_on` | `turn_off` |
| `button` / `input_button` | `press` | `press` |
| `cover` | `cover.open_cover` | `cover.close_cover` |
| `fan` | `fan.turn_on` | `fan.turn_off` |
| `media_player` | `media_player.turn_on` | `media_player.turn_off` | `idle`/`paused`/`standby` 视为开启 |
| `vacuum` | `vacuum.start` | `vacuum.return_to_base` |
| 其他域 | `turn_on` | `turn_off` |

### set_value — 设置目标值（最灵活）

根据实体域和 `value` 值自动推断应调用的 HA 服务，与情景模式（6.17 节）共享同一套服务推断引擎。无需手动指定服务名，只需提供目标值即可控制灯光、空调、遮盖、风扇等任意设备。

```yaml
# ---- 灯光 ----
# 开灯
tap_action:
  action: set_value
  value: "on"

# 关灯
tap_action:
  action: set_value
  value: "off"

# 开灯 + 亮度/色温
tap_action:
  action: set_value
  value: "on"
  service_data:
    brightness: 200
    kelvin: 4000

# 多实体一键关灯
tap_action:
  action: set_value
  entities:
    - light.keting_dadeng
    - light.keting_xuanguan
  value: "off"

# ---- 空调 ----
# 设置温度（数值 → climate.set_temperature）
tap_action:
  action: set_value
  entity: climate.xiaomi_air_conditioner
  value: "26"

# 设置模式（模式字符串 → climate.set_hvac_mode）
tap_action:
  action: set_value
  entity: climate.xiaomi_air_conditioner
  value: cool

# 制冷 + 温度 + 风速（自动拆分为 3 次服务调用）
tap_action:
  action: set_value
  entity: climate.xiaomi_air_conditioner
  value: cool
  service_data:
    temperature: "26"       # → climate.set_temperature
    fan_mode: level6         # → climate.set_fan_mode（自动拆分）

# 关闭空调
tap_action:
  action: set_value
  entity: climate.xiaomi_air_conditioner
  value: "off"

# ---- 遮盖 ----
# 打开
tap_action:
  action: set_value
  value: "open"

# 关闭
tap_action:
  action: set_value
  value: "close"

# 设置位置百分比
tap_action:
  action: set_value
  value: "50"

# ---- 风扇 ----
# 开关
tap_action:
  action: set_value
  value: "on"          # 或 "off"

# 设置风速百分比
tap_action:
  action: set_value
  value: "60"

# ---- 选择器 ----
# select / input_select
tap_action:
  action: set_value
  value: "制冷"

# ---- 数值输入 ----
# input_number
tap_action:
  action: set_value
  value: "25"

# ---- 按钮 ----
# input_button / button（任意 value 均调用 press）
tap_action:
  action: set_value
  value: "press"

# ---- 自动化 ----
# 开关
tap_action:
  action: set_value
  value: "on"          # → automation.turn_on

# 触发
tap_action:
  action: set_value
  value: "trigger"     # → automation.trigger

# ---- 脚本 ----
tap_action:
  action: set_value
  entity: script.morning_routine
  value: "run"         # → script.morning_routine

# ---- 门锁 ----
tap_action:
  action: set_value
  value: "locked"      # → lock.lock

tap_action:
  action: set_value
  value: "unlocked"    # → lock.unlock

# ---- 扫地机 ----
# 开始清扫
tap_action:
  action: set_value
  entity: vacuum.roborock
  value: "on"          # → vacuum.start（"start" / "clean" 同理）

# 返回充电
tap_action:
  action: set_value
  entity: vacuum.roborock
  value: "off"          # → vacuum.return_to_base（"return" / "home" / "dock" 同理）

# 停止清扫
tap_action:
  action: set_value
  entity: vacuum.roborock
  value: "stop"         # → vacuum.stop

# 暂停清扫
tap_action:
  action: set_value
  entity: vacuum.roborock
  value: "pause"        # → vacuum.pause

# ---- 透传模式（强制指定服务）----
tap_action:
  action: set_value
  entity: climate.xiaomi_air_conditioner
  value: cool
  service_data:
    _service: climate.set_hvac_mode    # 强制使用此服务，跳过自动推断
    # 其他字段原样传递
```

**`set_value` 支持的实体类型与服务自动推断对照表：**

| 实体域 | `value` 值 | 调用服务 | 说明 |
|--------|-----------|----------|------|
| `light` | `"on"` / `"true"` | `light.turn_on` | 开灯，`service_data` 可传 `brightness`、`kelvin`、`color_temp`、`effect` 等 |
| `light` | `"off"` / `"false"` | `light.turn_off` | 关灯，自动清理 `kelvin`/`brightness` 等参数 |
| `light` | 其他值 | `light.turn_on` | 作为亮度等参数 |
| `switch` / `input_boolean` | `"on"` / `"off"` | `turn_on` / `turn_off` | 开关切换 |
| `climate` | `"off"` | `climate.set_hvac_mode` | 关闭空调（`hvac_mode: "off"`），自动清理 `temperature`/`fan_mode` |
| `climate` | `"on"` / `"true"` | `climate.turn_on` | 开启空调 |
| `climate` | 数值（如 `"26"`） | `climate.set_temperature` | 设置温度，`temperature` 取数值 |
| `climate` | 模式字符串 + `service_data` 含 `temperature` | `climate.set_temperature` | 同时设置 `hvac_mode` + `temperature` |
| `climate` | 模式字符串（无 `temperature`） | `climate.set_hvac_mode` | 仅设置模式 |
| `climate` | `service_data` 含 `fan_mode` | 额外调用 `climate.set_fan_mode` | `fan_mode` 自动拆分为独立服务调用；关闭模式（`value: "off"`）时跳过风速设置 |
| `cover` | `"open"` | `cover.open_cover` | 打开遮盖 |
| `cover` | `"closed"` / `"close"` | `cover.close_cover` | 关闭遮盖 |
| `cover` | 数值 | `cover.set_cover_position` | 设置位置百分比 |
| `fan` | `"on"` / `"off"` | `fan.turn_on` / `fan.turn_off` | 风扇开关 |
| `fan` | 数值 | `fan.set_percentage` | 设置风速百分比 |
| `media_player` | `"on"` / `"off"` | `media_player.turn_on` / `turn_off` | 媒体设备开关；验证时 `standby` 也视为关闭成功 |
| `media_player` | `"play"` / `"pause"` | `media_play` / `media_pause` | 播放/暂停 |
| `button` / `input_button` | 任意 | `press` | 按压按钮 |
| `input_select` | 任意 | `input_select.select_option` | `option = value` |
| `select` | 任意 | `select.select_option` | `option = value` |
| `input_number` | 数值 | `input_number.set_value` | 设置数值 |
| `automation` | `"on"` / `"off"` | `automation.turn_on` / `turn_off` | 自动化开关 |
| `automation` | 其他 | `automation.trigger` | 触发自动化 |
| `vacuum` | `"on"` / `"start"` / `"clean"` | `vacuum.start` | 开始清扫 |
| `vacuum` | `"off"` / `"return"` / `"home"` / `"dock"` | `vacuum.return_to_base` | 返回充电 |
| `vacuum` | `"stop"` | `vacuum.stop` | 停止清扫 |
| `vacuum` | `"pause"` | `vacuum.pause` | 暂停清扫 |
| `script` | 任意 | `script.{实体名}` | 执行脚本 |
| `lock` | `"locked"` / `"lock"` | `lock.lock` | 上锁 |
| `lock` | 其他 | `lock.unlock` | 解锁 |
| 其他域 | `"on"` / `"off"` | `turn_on` / `turn_off` | 通用开关 |
| 其他域 | 其他 | `homeassistant.turn_on` | 通用回退 |

> 此对照表与 6.17 节情景模式的推断逻辑完全一致，因为底层共享同一个 `_inferSceneService` 引擎。

### loop_assign — 循环赋值（每次点击轮换到下一个值）

每次点击把实体推进到 `values` 序列中的**下一个值**，到达末尾后回绕到第一个。典型场景是下拉型实体（`input_select` / `select`）逐级循环切换，一个按钮即可按预设顺序轮换选项。

**定位方式**：读取实体当前状态，在 `values` 中找索引并赋下一个值；若当前值不在序列中，则从序列第一个开始。赋值底层复用情景模式的服务推断引擎（支持 `select_option` / `set_value` 等，详见上方 `set_value` 对照表）。

**防抖**：卡片会过滤连续点击，两次点击间隔小于 `interval`（默认 `500` ms）的点击被忽略，确保每次点击都能读到 HA 更新后的最新状态，避免快速连点跳值/漏值。

```yaml
# 单实体：每次点击依次切换 input_select.模式 为 自动 → 睡眠 → 强风 → 自动…
tap_action:
  action: loop_assign
  entity: input_select.模式
  values: ['自动', '睡眠', '强风']
  interval: 800            # 可选，连续点击最小间隔(ms)，默认 500

# 多实体：各自独立轮换（loop 数组）
tap_action:
  action: loop_assign
  loop:
    - entity: input_select.模式
      values: ['自动', '睡眠', '强风']
    - entity: input_select.风速
      values: ['低', '中', '高']
      interval: 1000
```

| 参数 | 必填 | 类型 | 说明 |
|------|------|------|------|
| `entity` | 单实体时必填 | `string` | 要轮换的实体 ID（与 `loop` 二选一） |
| `values` | ✅ | `string[]` | 轮换的目标值序列，按点击顺序依次赋值，末尾回绕 |
| `loop` | 多实体时必填 | `array` | 多实体数组，每项含 `entity` / `values` / 可选 `interval` / `service_data`（与 `entity`+`values` 二选一） |
| `interval` | ❌ | `number` | 连续点击最小间隔（ms），默认 `500` |
| `service_data` | ❌ | `object` | 透传给服务调用的附加参数（如 `_service` 强制指定服务） |

> `loop_assign` 的 `entity` / `values` 可直接改用 `service_data` 透传 `_service` 强制指定赋值服务；单实体简写 `entity`+`values` 与多实体 `loop` 数组均可。

### process_execute — 流程执行（按步骤序列依次执行）

按 `steps` 配置的步骤序列**依次**执行多个实体操作，每个步骤可独立设置 `delay` 延时。多实体类型通过情景模式的**推断引擎**（`_inferSceneService`）自动识别服务（`light`/`switch`/`climate`/`cover`/`fan`/`media_player`/`button`/`input_select`/`select`/`input_number`/`automation`/`vacuum`/`script`/`lock` 等 15+ 类型），适合"离家模式""回家模式"等按顺序开关多设备的场景。

**执行反馈**：执行时弹出进度气泡面板，逐步骤显示 等待 → 延时倒计时 → 执行中 → 已发送 → 状态验证成功/失败，复用情景模式的进度面板机制。

```yaml
tap_action:
  action: process_execute
  name: 离家模式
  width: 400px                  # 可选，进度气泡宽度
  verify_timeout: 10            # 可选，状态验证超时（秒），默认 10
  steps:
    - entity: light.kegting
      value: off
    - entity: switch.suoyou
      value: on
      delay: 3                  # 可选，本步骤执行前延时 N 秒
    - entity: cover.chuanglian
      value: closed
```

| 参数 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `steps` | ✅ | `array` | 步骤数组，每项为一步操作，结构与情景 action 一致 |
| `name` | ❌ | `string` | 流程名称，默认「流程执行」，显示在进度面板标题 |
| `width` | ❌ | `string` | 进度气泡宽度，默认 `400` |
| `verify_timeout` | ❌ | `number` | 状态验证超时（秒），默认 `10` |

**每个 step 支持的字段**（与情景模式 `actions[]` 一致）：

| 参数 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `entity` | 单实体时必填 | `string` | 目标实体 ID |
| `entities` | 批量时可选 | `object/array` | 多实体对象（`{ 别名: entity_id }`）或数组，自动展开为多步 |
| `value` | ❌ | `string` | 目标值，由推断引擎按实体域映射到对应服务（`off`→`turn_off`、`closed`→`close_cover`、数值→温度/位置等） |
| `delay` | ❌ | `number` | 本步骤执行前的延时（秒），进度面板显示「延时 Ns」 |
| `service_data` | ❌ | `object` | 透传给服务调用的附加参数（如空调温度/风扇挡位）；含 `_service` 时强制指定服务 |
| `confirm_entity` | ❌ | `string` | 确认实体 ID，执行后轮询此实体验证 |
| `confirm_value` | ❌ | `string` | 确认实体期望值，支持比较运算符前缀 |
| `confirm_time` | ❌ | `number` | 执行后等待 N 秒再开始验证 |

> `process_execute` 复用情景模式的 `_expandSceneActions` / `_buildSceneProgressPanel` / `_executeSceneActions` 执行链，与 `scene_mode` 的 `actions` 在实体类型、推断服务、状态验证、延时上行为完全一致；区别是 `process_execute` 为**独立入口**（跳过按钮旋转动画、不写入执行历史）。

### more-info — 详细信息弹窗

弹出 HA 标准的实体详细信息弹窗。

```yaml
tap_action:
  action: more-info
```

### navigate — 页面导航

跳转到 HA 的另一个页面。

```yaml
tap_action:
  action: navigate
  navigation_path: /lovelace/bedroom     # 目标页面路径
```

### call-service — 调用 HA 服务

调用任意 HA 服务，支持卡片本地服务路由。

```yaml
# 标准 HA 服务
tap_action:
  action: call-service
  service: light.turn_on
  service_data:
    entity_id: light.living
    brightness: 255

# 卡片本地服务（自由布局弹窗等）
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  service_data:
    title: 控制面板
    cards: [...]
```

### popup_card — 弹出自定义卡片

弹出一个包含自定义内容的弹窗。

```yaml
tap_action:
  action: popup_card
  card:
    - type: sensor
      entity: sensor.temperature
      name: 温度
    - type: switch
      entity: switch.plug
  popup_position: top         # 可选：top / bottom / left / right / center
  width: 350                  # 可选：弹窗宽度（像素）
```

### card — 弹出设备内置控制弹窗

弹出卡片内置的设备控制弹窗（如窗帘面板、灯光面板、空调面板等），配置方式与 `buttons` 数组中的按钮配置一致。与 `popup_card` 的区别：`popup_card` 弹出的是 HA 原生卡片（如 `weather-forecast`、`entities` 等），`card` 弹出的是卡片自身内置的设备专属控制面板（带拖拽滑块、动画等交互）。

**支持的设备类型：**

| type | 说明 | 弹窗效果 |
|------|------|----------|
| `lights` | 灯光组控制面板 | 亮度/色温调节、按房间分组、批量开关 |
| `light` | 单灯控制面板 | 精简灯光弹窗 |
| `socket` | 插座控制面板 | 批量开关、功率桑基图 |
| `ac` | 空调控制面板 | 温度/模式/风速调节 |
| `curtain` | 窗帘控制面板 | 百分比滑块、单双层切换、拖拽控制 |
| `clothes_dryer` | 晾衣架控制面板 | 机械仿真拖拽、收藏位置 |
| `consumables` | 耗材管理面板 | 电池/滤芯剩余量 |
| `device` | 通用设备状态面板 | 设备开关状态 |
| `media` | 媒体控制面板 | 播放/暂停/音量 |
| `health` | 健康数据面板 | 步数/心率等 |
| `scene_mode` | 情景模式气泡 | 气泡选择/执行进度 |
| `esxi` | ESXi 虚拟化面板 | 主机状态 / 虚拟机批量操作 / 屏幕墙三选项卡（见 6.44） |
| `bill` | 个人账单面板 | 概览 / 分析 / 日历 / 查询 / 历史五选项卡 + 窗口内下钻图表（见 6.45） |
| `dingdong` | 叮咚门铃面板 | 抓拍 / 实时画面 + 按天回看的时间轴（事件·抓拍·录像混轴）+ 设置 + 诊断四选项卡（见 6.47） |

**配置示例：**

```yaml
# 弹出全屋窗帘聚合弹窗
tap_action:
  action: card
  card:
    type: curtain
    name: 全屋窗帘
    show_open: false
    on_icon: mdi:curtain-open
    off_icon: mdi:curtain
    card:
      - name: 客厅窗帘
        height: 400px
        fabric_entity: cover.ke_ting_bu_lian
        sheer_entity: cover.ke_ting_sha_lian
        layer_mode: double
      - name: 卧室窗帘
        height: 400px
        fabric_entity: cover.wo_shi_bu_lian
        layer_mode: single

# 弹出灯光控制面板
tap_action:
  action: card
  card:
    type: lights
    name: 客厅灯光
    per_line: 2
    card:
      - entity: light.living_ceiling
        name: 天花灯
      - entity: light.living_floor
        name: 落地灯

# 弹出空调控制面板
tap_action:
  action: card
  card:
    type: ac
    card:
      - entity: climate.living
        name: 客厅空调
      - entity: climate.bedroom
        name: 卧室空调

# 弹出情景模式气泡
tap_action:
  action: card
  card:
    type: scene_mode
    scenes:
      - name: 回家
        actions:
          - entity: light.living
            value: "on"
      - name: 离家
        actions:
          - entity: light.living
            value: "off"
```

**弹窗参数：**

`popup_position` 和 `width` 可配置在 `tap_action` 层级，对所有设备类型生效（`card` 层级未配置时降级使用）：

```yaml
tap_action:
  action: card
  popup_position: center        # 可选：弹窗位置
  width: 600px                  # 可选：弹窗宽度
  card:
    type: lights
    card:
      - entity: light.living_room
        name: 客厅灯
```

**`card` 与 `popup_card` 的区别：**

| 对比 | `popup_card` | `card` |
|------|-------------|--------|
| 弹窗内容 | HA 原生卡片（第三方/内置卡片） | 卡片内置的设备专属控制面板 |
| card 字段含义 | HA 卡片配置（`{ type: entities, ... }`） | 设备类型配置（`{ type: curtain, ... }`） |
| 交互能力 | 取决于嵌入的卡片 | 带拖拽滑块、动画等丰富交互 |
| 适用场景 | 嵌入任意 HA 卡片（天气、地图等） | 弹出灯光/空调/窗帘等设备控制面板 |

### quick-action — 快捷操作

在任意支持 `tap_action` 的位置触发情景模式快捷操作，弹出气泡选择器并执行多步骤操作。桥接情景模式执行引擎（6.17 节），支持执行进度展示、状态验证、延时执行等全部功能。

**完整模式（scenes 数组）：** 配置多个情景，点击弹出气泡选择器

```yaml
tap_action:
  action: quick-action
  name: 情景模式                    # 气泡标题
  scenes:                            # 情景列表（格式与 scene_mode 一致）
    - name: 回家模式
      confirm: true
      actions:
        - entity: light.living_room
          value: "on"
        - entity: climate.ac
          service_data:
            temperature: 26
    - name: 离家模式
      actions:
        - entities:
            客厅灯: light.keting_dadeng
            卧室灯: light.bedroom
          value: "off"
  scene_mode: bubble                 # 可选：bubble | direct
```

**简写模式（actions 数组）：** 直接配置操作列表，自动包装为单情景直接执行

```yaml
tap_action:
  action: quick-action
  name: 一键回家
  actions:                           # 简写模式，自动包装为 [{ name: "一键回家", actions }]
    - entity: light.living_room
      value: "on"
    - entity: climate.ac
      service_data:
        temperature: 26
  confirm: true                       # 可选：执行前确认
```

**配置项说明：**

| 配置项 | 必填 | 类型 | 说明 |
|--------|:----:|------|------|
| `action` | ✅ | `string` | 固定为 `quick-action` |
| `scenes` | ❌* | `array` | 情景列表，格式与 `scene_mode`（6.17 节）完全一致 |
| `actions` | ❌* | `array` | 操作列表（简写模式，与 `scenes` 二选一） |
| `name` | ❌ | `string` | 操作名称，用于气泡标题，默认 `快捷操作` |
| `scene_mode` | ❌ | `string` | `bubble`（气泡选择）/ `direct`（直接执行），不配置时自动判断 |
| `confirm` | ❌ | `boolean` | 简写模式下执行前是否确认，默认 `false` |
| `icon` | ❌ | `string` | 图标，默认 `mdi:palette` |
| `fold` | ❌ | `boolean` | 动作列表是否默认展开，默认 `false` |
| `verify_timeout` | ❌ | `number` | 验证超时秒数，默认 `10` |

> *`scenes` 和 `actions` 至少配置一个。`scenes` 优先级更高，同时配置时使用 `scenes`。

### none — 无操作

不执行任何操作，用于禁用点击。

```yaml
tap_action:
  action: none
```

### entities 多实体批量操作

`toggle` 和 `set_value` 支持 `entities` 数组，一次性对多个实体执行相同操作：

```yaml
# 多实体 toggle：一键切换所有灯
tap_action:
  action: toggle
  entities:
    - light.living_ceiling
    - light.living_led
    - light.living_spot

# 多实体 set_value：一键关闭所有灯
tap_action:
  action: set_value
  entities:
    - light.living_ceiling
    - light.living_led
    - light.living_spot
  value: "off"
```

> `entity`（单实体）和 `entities`（多实体）二选一，同时配置时 `entities` 优先。

### 适用位置

通用动作系统在以下位置均可用：

| 位置 | 配置字段 | 说明 |
|------|---------|------|
| 按钮的 `tap_action` | `buttons[].tap_action` | 概览按钮点击 |
| 独立按钮 | `buttons[].tap_action` | 无 type 的独立按钮 |
| 弹窗内设备卡片 | `card[].tap_action` | 灯光/插座/耗材弹窗内的设备 |
| title_entities | `title_entities[].tap_action` | 弹窗标题右侧的实体/按钮 |
| entities 区域 | `entities[].tap_action` | 卡片左侧传感器区域 |
| 传感器卡片 | `tap_action` | 自由布局弹窗内的 sensor 类型卡片 |
| 设备状态卡片 | `tap_action` | 设备状态弹窗内的卡片 |

---

## 八、弹窗中的选项卡（Tabs）

灯光、插座、耗材等弹窗以及自由布局弹窗（`show_free_layout_popup` / `popup_card`）都支持使用选项卡来分类显示设备。选项卡功能非常丰富，支持图标、高亮、自动跳转、条件过滤、禁用、角标等。**选项卡之间可以直接左右滑动切换**（跟手 + 吸附 + 高亮跟手，规则见「八-A、左右滑动」）。

---

### 8.1 基础用法

在按钮配置中添加 `tabs` 数组即可启用选项卡模式，每个选项卡通过 `name` 命名，通过 `rows` 定义内容：

```yaml
  - type: lights
    tabs:                                 # 启用选项卡模式
      - name: 客厅                        # 选项卡名称
        rows:                             # 此选项卡中的行
          - row: 1
            title: 主照明
            items:
              - entity: light.living_ceiling
                name: 吸顶灯
          - row: 2
            title: 氛围灯
            items:
              - entity: light.living_led_strip
                name: LED灯带
      - name: 卧室
        rows:
          - row: 1
            items:
              - entity: light.bedroom_light
                name: 卧室灯
```

### 8.2 选项卡完整配置项

每个选项卡支持以下配置字段：

| 字段 | 必填 | 类型 | 默认值 | 说明 |
|------|:----:|------|--------|------|
| `name` | ❌ | `string` | `Tab N` | 选项卡显示名称 |
| `icon` | ❌ | `string` | 无 | 选项卡图标（如 `mdi:sofa`），显示在名称左侧 |
| `belong` | ❌ | `string` | 无 | 所属分组（如 `1楼`、`2楼`），用于将选项卡按归属分组显示（见 8.10） |
| `entity` | ❌ | `string` | 无 | 绑定的实体 ID，用于高亮判断、自动跳转、display_only 过滤 |
| `entity_value` | ❌ | `string` / `array` | 无 | 实体匹配值，当 `entity` 的状态等于此值时视为"匹配"（支持数组，任一匹配即算） |
| `rows` | ❌ | `array` | `[]` | 选项卡内容行（自由布局弹窗格式） |
| `disabled` | ❌ | `boolean` | `false` | 是否禁用此选项卡（禁用后不可点击、灰色显示、不参与自动跳转） |
| `badge` | ❌ | `string` / `number` | 无 | 选项卡角标固定值（显示在名称右上角的小数字） |
| `badge_entity` | ❌ | `string` | 无 | 选项卡角标实体（动态取值，条件选项卡专用） |
| `config_id` | ❌ | `string` | 无 | 注册 ID，将该选项卡配置注册到全局 Store，供 `tabs_config` 引用（见第十八节） |

### 8.3 选项卡图标（icon）

为选项卡添加图标，显示在名称左侧。激活时图标不透明度提高，非激活时略淡。

```yaml
tabs:
  - name: 客厅
    icon: mdi:sofa                        # 选项卡图标
    rows: [...]
  - name: 卧室
    icon: mdi:bed
    rows: [...]
  - name: 书房
    icon: mdi:desk
    rows: [...]
```

### 8.4 实体高亮（entity + entity_value）

为选项卡绑定一个实体和匹配值，当实体状态匹配时，该选项卡会以橙色渐变背景高亮显示，便于快速识别哪些设备正在运行。

**高亮逻辑**：
- 实体状态等于 `entity_value`（或数组中任一项）时，选项卡显示橙色渐变背景 + 橙色文字
- `entity_value` 为数组时，任一值匹配即算高亮
- 实体状态为 `unavailable` / `unknown` 时不高亮

```yaml
tabs:
  - name: 冰箱
    entity: switch.bingxiang              # 绑定实体
    entity_value: 'on'                    # 匹配值（on 状态时高亮）
    rows: [...]
  - name: 电饭锅
    entity: sensor.chunmi_status
    entity_value:                         # 数组形式，任一匹配即高亮
      - Delay
      - Keep Warm
      - Busy
    rows: [...]
```

> **优先级**：选项卡自身的 `entity` + `entity_value` 优先级最高。如果未配置，还会查找 `dynamic_icon` 按钮的 `rules` 中 `name` 与选项卡 `name` 相同的规则。

### 8.5 自动跳转（auto_redirect）

当多个选项卡都有设备在运行时，可以自动跳转到最近状态变化的选项卡。

```yaml
tabs:
  - name: 冰箱
    entity: switch.bingxiang
    entity_value: 'on'
    rows: [...]
  - name: 微波炉
    entity: switch.weibolu
    entity_value: 'on'
    rows: [...]
  - name: 空气炸锅
    entity: switch.kongqizhaguo
    entity_value: 'on'
    rows: [...]
auto_redirect: true                       # 自动跳转到最近状态变化的选项卡
```

**跳转规则**：
- `auto_redirect: false`（默认）：始终激活第一个非禁用且可见的选项卡
- `auto_redirect: true`：在所有 `entity` 匹配的选项卡中，选择 `last_changed` 时间最新的那个跳转
- 无匹配时降级为第一个非禁用且可见的选项卡
- 禁用的选项卡不参与自动跳转

### 8.6 条件过滤（display_only）

通过 `display_only` 配置仅显示实体状态匹配的选项卡，隐藏不匹配的选项卡。这在设备较多时非常实用——只显示正在运行的设备。

```yaml
tabs:
  - name: 冰箱
    entity: switch.bingxiang
    entity_value: 'on'
    rows: [...]
  - name: 微波炉
    entity: switch.weibolu
    entity_value: 'on'
    rows: [...]
  - name: 空气炸锅
    entity: switch.kongqizhaguo
    entity_value: 'on'
    rows: [...]
display_only:                             # 仅显示实体状态匹配这些值的选项卡
  - 'on'                                  # 匹配 "on"
  - Delay                                 # 也匹配 "Delay"（支持多值）
  - Keep Warm                             # 也匹配 "Keep Warm"
  - Busy                                  # 也匹配 "Busy"
```

**过滤规则**：
- `display_only` 为空或未配置：所有选项卡可见
- 选项卡未配置 `entity`：始终可见
- 实体不存在或状态为 `unavailable` / `unknown`：始终可见
- 实体状态匹配 `display_only` 中任一项：可见
- 否则：隐藏

**实时更新**：当实体状态变化时，选项卡的可见性会实时更新。如果当前激活的选项卡被隐藏，会自动切换到第一个可见的选项卡。

**所有选项卡均不可见时**：导航栏和内容区会隐藏，并显示空状态提示（如"3个设备中没有现在处于开启的设备"）。

### 8.7 禁用选项卡（disabled）

设置 `disabled: true` 可以禁用某个选项卡，禁用后选项卡变灰、不可点击、不参与自动跳转。

```yaml
tabs:
  - name: 客厅
    rows: [...]
  - name: 卧室
    disabled: true                       # 禁用此选项卡（灰色显示，不可点击）
    rows: [...]
```

### 8.8 选项卡角标（badge / badge_entity）

为选项卡添加角标，显示在名称右上角的小数字，用于提示数量或状态。

```yaml
tabs:
  - name: 客厅
    badge: 3                             # 固定角标值
    rows: [...]
  - name: 卧室
    badge_entity: sensor.bedroom_active_count  # 动态角标（从实体取值）
    rows: [...]
```

> 对于灯光/插座/等聚合弹窗，角标会自动统计每个选项卡中处于 `on` 状态的设备数量，无需手动配置。

### 8.9 选项卡布局控制

#### 每行固定数量（table_per_line）

控制导航栏中每行显示的选项卡数量，适用于选项卡较多时保持整齐排列。

```yaml
service_data:
  title: 全部厨具
  table_per_line: 2                       # 每行显示2个选项卡
  tabs: [...]
```

| 配置值 | 效果 |
|--------|------|
| 不配置 / `0` | 自适应宽度，一行尽可能多 |
| `2` | 每行2个选项卡，各占50%宽度 |
| `3` | 每行3个选项卡，各占33%宽度 |
| `4` | 每行4个选项卡，各占25%宽度 |

#### 固定宽度（table_one_width）

控制每个选项卡的最小宽度，适用于选项卡名称较长时避免压缩。

```yaml
service_data:
  title: 全部厨具
  table_one_width: 80px                   # 每个选项卡最小宽度80px
  tabs: [...]
```

| 配置值 | 效果 |
|--------|------|
| 不配置 | 自适应宽度 |
| `60px` | 选项卡最小宽度60px |
| `80` | 等同于 `80px`（纯数字自动加px） |

> `table_per_line` 和 `table_one_width` 可以同时使用：`table_per_line` 控制每行数量，`table_one_width` 保证最小宽度。

### 8.10 选项卡分组（belong）

通过为选项卡添加 `belong` 字段，可以将选项卡按归属分组显示。这在设备较多、且分布在不同楼层/区域时非常实用——导航栏会以分组形式展示，左侧显示分组标签（如"1楼"、"2楼"），右侧以芯片按钮形式显示该分组下的选项卡。

#### 适用范围

`belong` 字段在以下场景中均可用：

| 弹窗类型 | 配置位置 | 说明 |
|----------|----------|------|
| 自由布局弹窗 | `tabs` 数组中每个选项卡 | 在 `show_free_layout_popup` / `popup_card` 的 `tabs` 配置中使用 |
| 灯光聚合弹窗 | `card` 数组中每个设备 | 在 `type: lights` 的 `card` 子项中使用 |
| 插座聚合弹窗 | `card` 数组中每个设备 | 在 `type: socket` 的 `card` 子项中使用 |
| 耗材聚合弹窗 | `card` 数组中每个设备 | 在 `type: consumables` 的 `card` 子项中使用 |

#### 基础用法（自由布局弹窗）

在 `tabs` 数组中为每个选项卡添加 `belong` 字段即可：

```yaml
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  service_data:
    title: 厨具
    width: 430px
    tabs:
      - name: 电饭锅
        belong: 1楼              # ← 归属1楼
        entity: sensor.chunmi_status
        entity_value: ['Delay', 'Keep Warm', 'Busy']
        rows: [...]

      - name: 热水器
        belong: 1楼              # ← 同属1楼，与电饭锅并排显示
        entity: switch.reshuiqi
        entity_value: 'on'
        rows: [...]

      - name: 烧水壶
        belong: 2楼              # ← 归属2楼，另起一行显示
        entity: input_boolean.shao_shui_hu
        entity_value: 'on'
        rows: [...]
```

**渲染效果：**

```
┌────────────────────────────────────────────────┐
│ 1楼 │ [电饭锅] [热水器]                         │
│ 2楼 │ [烧水壶]                                  │
└────────────────────────────────────────────────┘
```

#### 灯光/插座/耗材聚合弹窗用法

在灯光、插座、耗材等聚合弹窗中，`belong` 字段配置在每个设备项上（而非选项卡上），与 `tabs_by` 配合使用：

**灯光聚合示例：**

```yaml
buttons:
  - type: lights
    tabs: input_boolean.tabs           # 启用选项卡模式
    tabs_by: room                      # 按 room 字段分组
    table_per_line: 9                  # 每行9个按钮
    card:
      - name: 大灯
        room: 客厅
        belong: 1楼                    # ← 归属1楼
        entity: light.keting_dadeng
        on_icon: mdi:lightbulb
        off_icon: mdi:lightbulb-off
        tap_action:
          action: toggle

      - name: 玄关灯
        room: 客厅
        belong: 2楼                    # ← 归属2楼（虽然同属"客厅"，但在2楼）
        entity: light.keting_xuanguan
        on_icon: mdi:alarm-light
        off_icon: mdi:alarm-light-off
        tap_action:
          action: toggle
```

**插座聚合示例：**

```yaml
buttons:
  - type: socket
    tabs: true
    tabs_by: room
    table_per_line: 7
    card:
      - entity: switch.monitor
        name: 监控插座
        room: 客厅
        belong: 2楼                    # ← 归属2楼
        icon: mdi:video
        tap_action:
          action: toggle

      - entity: switch.projector
        name: 投影
        room: 客厅
        belong: 1楼                    # ← 归属1楼
        icon: mdi:projector
        tap_action:
          action: toggle

      - entity: switch.desk
        name: 学习桌
        room: 客厅
        belong: 1楼                    # ← 同属1楼，与"投影"并排
        icon: mdi:power-socket-au
        tap_action:
          action: toggle
```

**耗材聚合示例：**

```yaml
buttons:
  - type: consumables
    tabs: true
    tabs_by: group                     # 按 group 字段分组
    card:
      - entity: sensor.bedroom_battery
        name: 主卧
        group: 温度计电量
        belong: 1楼                    # ← 归属1楼

      - entity: sensor.living_battery
        name: 客厅
        group: 温度计电量
        belong: 1楼                    # ← 同属1楼

      - entity: sensor.dining_battery
        name: 餐厅
        group: 温度计电量
        belong: 2楼                    # ← 归属2楼
```

#### 分组规则

| 规则 | 说明 |
|------|------|
| **分组触发** | 至少有一个选项卡/设备配置了 `belong` 字段时，自动启用分组模式 |
| **分组顺序** | 按 `belong` 值首次出现的顺序排列 |
| **无 belong 的项** | 放在导航栏最前面（不分组，传统平铺） |
| **相同 belong** | 合并到同一分组行 |
| **不配置 belong** | 所有项均不配置时，使用传统选项卡平铺模式（完全不变） |

#### 聚合弹窗中的分组逻辑

灯光/插座/耗材聚合弹窗使用 `tabs_by` 字段分组（如按 `room` 分为"客厅"、"卧室"）。当设备项同时配置了 `belong` 时：

- 按 `(belong, tabsBy值)` 组合分组，确保不同 belong 但同 tabsBy 的项目分到不同选项卡
- 例如：`belong: 1楼, room: 客厅` 和 `belong: 2楼, room: 客厅` 会成为两个独立的选项卡
- 选项卡显示名仍为 `tabsBy` 的值（如"客厅"），`belong` 仅用于导航分组

**渲染效果（插座示例）：**

```
┌─────────────────────────────────────────────────────┐
│ 1楼 │ [客厅]                                            │
│ 2楼 │ [客厅]                                            │
└─────────────────────────────────────────────────────┘
```

点击"1楼"下的"客厅"显示投影、学习桌；点击"2楼"下的"客厅"显示监控插座。

#### 分组导航样式

分组模式下的选项卡使用**芯片风格**（Chip），与传统选项卡的**下划线风格**完全区分：

| 状态 | 外观 |
|------|------|
| **默认** | 浅灰色圆角芯片（`border-radius: 14px`）、1px 浅色边框、微阴影 |
| **悬停** | 边框加深、阴影提升、微微上浮（`translateY(-0.5px)`） |
| **激活** | 蓝色边框 + 蓝色半透明背景 + 蓝色文字 + 加粗 |
| **高亮** | 橙色边框 + 橙色 135° 渐变背景 + 橙色文字（entity 匹配时） |
| **禁用** | 40% 透明度 + 禁止点击 |

**分组标签样式：**

- 右对齐文字、10px 小字号、较浅颜色
- 右侧有**蓝色渐变竖线装饰**，从上到下渐隐
- 竖线长度随按钮行数自动变化（单行短、多行长）
- 标签文字竖向居中对齐

#### 分组模式下的布局控制

`table_per_line` 和 `table_one_width` 在分组模式下继续生效，作用于每个分组内的按钮容器：

```yaml
table_per_line: 3                    # 分组模式下，每个分组内每行3个按钮
table_one_width: 60px                # 每个按钮最小宽度60px
```

**多行换行对齐：** 当某分组下按钮较多一行放不下时，自动换行显示，第二行及之后的按钮与第一行竖向对齐：

```
1楼 │ [电饭锅] [热水器] [设备3] [设备4]
    │ [设备5] [设备6]                ← 第二行与第一行竖向对齐
2楼 │ [烧水壶]
```

#### 完整配置示例（自由布局弹窗 + belong）

```yaml
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  service_data:
    title: 厨具
    width: 430px
    popup_position: center
    display_only:
      - 'on'
      - Delay
      - Keep Warm
      - Busy
      - 'off'
      - Idle
    auto_redirect: true
    table_per_line: 4                     # 每行4个按钮
    tabs:
      - name: 电饭锅
        belong: 1楼
        config_id: dian_fan_guo
        entity: sensor.chunmi_cn_404489380_eh1_status_p_2_1
        entity_value:
          - Delay
          - Keep Warm
          - Busy
        rows:
          - row: 1
            per_line: 1
            title: 电饭锅
            show_title: false
            items:
              - type: picture
                show_button_background: false
                halo_entity: input_boolean.chu_fang_dian_fan_guo
                bg_image: /local/house/电饭锅.png

      - name: 热水器
        belong: 1楼
        config_id: re_shui_qi
        entity: switch.reshuiqi
        entity_value: 'on'
        rows:
          - row: 1
            per_line: 1
            title: 热水器
            show_title: false
            items:
              - type: picture
                show_button_background: false
                bg_image: /local/house/热水器.png
                halo_entity: switch.reshuiqi

      - name: 烧水壶
        belong: 2楼
        config_id: shao_shui_hu
        entity: input_boolean.shao_shui_hu
        entity_value: 'on'
        rows:
          - row: 1
            per_line: 1
            title: 烧水壶
            show_title: false
            items:
              - type: picture
                show_button_background: false
                bg_image: /local/house/小米恒温电水壶2pro.png
                halo_entity: input_boolean.shao_shui_hu
```

**渲染效果：**

```
┌─────────────────────────────────────────────────────────────┐
│ 厨具                                                        │
├─────────────────────────────────────────────────────────────┤
│ 1楼 │ [电饭锅] [热水器]                                      │
│ 2楼 │ [烧水壶]                                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   （选项卡面板内容区域）                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 8.11 选项卡导航栏样式

选项卡导航栏默认为**下划线风格**：非激活选项卡显示淡灰色背景，激活选项卡显示蓝色半透明背景 + 底部蓝色下划线。支持以下视觉状态：

| 状态 | 外观 |
|------|------|
| **默认** | 淡灰色背景（`rgba(0,0,0,0.04)`），深灰文字 |
| **悬停** | 稍深灰色背景（`rgba(0,0,0,0.08)`） |
| **激活** | 蓝色半透明背景（`rgba(52,152,219,0.1)`）+ 蓝色文字 + 底部蓝色下划线 |
| **高亮** | 橙色渐变背景 + 橙色文字（entity 匹配时） |
| **禁用** | 40%透明度 + 禁止点击 |

所有背景色均可通过 CSS 变量自定义覆盖：

| CSS 变量 | 默认值 | 说明 |
|----------|--------|------|
| `--room-tab-inactive-bg` | `rgba(0,0,0,0.04)` | 非激活选项卡背景 |
| `--room-tab-hover-bg` | `rgba(0,0,0,0.08)` | 悬停选项卡背景 |
| `--room-tab-active-bg` | `rgba(52,152,219,0.1)` | 激活选项卡背景 |

### 8.12 聚合弹窗按字段分组（tabs_by）

在灯光（`type: lights`）、插座（`type: socket`）和耗材（`type: consumables`）等聚合按钮弹窗中，可以通过 `tabs_by` 配置将设备按某个字段值自动分组为选项卡。

**基础用法：**

```yaml
  - type: socket
    tabs: true                            # 启用选项卡模式
    tabs_by: room                         # 按 card 中每个设备的 room 字段自动分组
    card:
      - entity: switch.plug1
        name: 客厅插座
        room: 客厅                        # 选项卡按此值分组
      - entity: switch.plug2
        name: 卧室插座
        room: 卧室
      - entity: switch.plug3
        name: 厨房插座
        room: 厨房
```

| 配置项 | 说明 | 示例值 |
|--------|------|--------|
| `tabs` | 启用选项卡模式。可为 `true`（自动）或实体 ID（通过实体 on/off 控制是否启用） | `true` / `input_boolean.xxx` |
| `tabs_by` | 指定按哪个字段分组，字段在 card 数组的每个设备中定义 | `room` / `group` |

**灯光示例：**

```yaml
  - type: lights
    tabs: true                            # 启用选项卡
    tabs_by: room                         # 按 room 分组
    card:
      - entity: light.living_ceiling
        name: 吸顶灯
        room: 客厅
      - entity: light.bedroom_light
        name: 卧室灯
        room: 卧室
```

**耗材示例：**

```yaml
  - type: consumables
    tabs: true
    tabs_by: group                        # 按 group 字段分组
    card:
      - entity: sensor.lock_battery
        name: 门锁
        group: 电池
      - entity: sensor.temp_battery
        name: 温度计
        group: 电池
      - entity: sensor.water_filter
        name: 净水器
        group: 滤芯
```

> `tabs_by` 与 `belong` 可同时使用：`tabs_by` 决定选项卡的内容分组，`belong` 决定选项卡在导航栏中的显示分组。

### 8.13 完整配置示例

```yaml
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  service_data:
    title: 厨具
    width: 430px
    display_only:                         # 仅显示正在运行的设备
      - 'on'
      - Delay
      - Keep Warm
      - Busy
    auto_redirect: true                   # 自动跳转到最近变化的选项卡
    table_per_line: 2                     # 每行2个选项卡
    tabs:
      - name: 冰箱
        icon: mdi:fridge
        entity: switch.bingxiang
        entity_value: 'on'
        rows:
          - row: 1
            items:
              - type: picture
                bg_image: /local/house/冰箱.png
              - type: sensor
                entity: sensor.bingxiang_power
                name: 功率

      - name: 电饭锅
        icon: mdi:pot-steam
        entity: sensor.chunmi_status
        entity_value:
          - Delay
          - Keep Warm
          - Busy
        rows:
          - row: 1
            items:
              - type: picture
                bg_image: /local/house/电饭锅.png

      - name: 微波炉
        icon: mdi:microwave
        entity: switch.weibolu
        entity_value: 'on'
        badge: 1
        rows:
          - row: 1
            items:
              - type: picture
                bg_image: /local/house/微波炉.png

      - name: 空气炸锅
        icon: mdi:toaster-oven
        entity: switch.kongqizhaguo
        entity_value: 'on'
        disabled: true                    # 暂时禁用此选项卡
        rows:
          - row: 1
            items:
              - type: picture
                bg_image: /local/house/空气炸锅.png
```

---

### 8.14 标题栏「使用量」入口（calendar_card）

自由布局弹窗（`show_free_layout_popup`）在**选项卡模式**下，标题栏右侧会多一个「使用量」按钮 —— 点它直接用**本布局各选项卡的 `entity`** 打开一张「使用量日历」（多实体形态）：

```
┌───────────────────────────────────────────┐
│ 厨具                          [使用量]     │  ← 点这个按钮
├───────────────────────────────────────────┤
│ [电饭锅] [空气炸锅] [微波炉] …             │
```

- **实体从哪来**：`tabs[].entity` 自动汇总（同一实体在多个选项卡里重复时只取第一个，名称取该选项卡的 `name`）；没有 `entity` 的选项卡不参与；
- **什么时候出现**：选项卡模式 + 至少一个 tab 配了 `entity` + 未显式关闭入口（未配置 `api_base_url` / `key` 时按钮仍在，点开会在弹窗里说明原因）；
- **点开得到什么**：完整的使用量日历卡片（日历 / 历史 / 年 / 月 / 日 / 洞察 六个选项卡），与手动配一张 `api.entities` 多实体卡片等价 —— 内部自动带上 `api.entities` / `api_base_url` / `key`（后者取卡片顶层配置），无需手写；
- **内置口径**：用电量单位 **`°`**，第二个系列取**时长（`h`）**（即 `units: '°,h'`、`series: '用量,时长'`、`calc_value_choose: value`，与空调组合计日历一致），配色 `#00a381` / `#c85179`、小数 `1,2`；
- **弹窗宽度**：`calendar_card.width` > **外层弹窗的 `width`（即 `tap_action.service_data.width`）** > `min(560px, 92vw)`；
- **生命周期**：点开时创建一个「孪生实例」（不影响页面上已有的使用量日历卡片），**关闭弹窗即销毁**（停轮询、断观察器、释放图表）。

想微调卡片参数（配色 / 单位 / 标题 / 弹窗宽度等），在 `service_data` 里加 `calendar_card`：

```yaml
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  service_data:
    title: 厨具
    width: 430px
    display_only: ['on', 'Delay', 'Keep Warm', 'Busy', 'off', 'Idle']
    auto_redirect: true
    calendar_card:                       # ← 不写就用内置默认（单位 ° + 时长 h）
      title: 厨房设备用电量日历
      width: 620px                       # 弹窗宽度；不写则沿用上面的 width: 430px
      # 想换成"用电量 + 费用"口径（需要电价）：
      calc_value_choose: calculate
      calculate: 0.55                    # 元 / kWh
      units: '°,元'
      series: '用量,费用'
    tabs:
      - name: 电饭锅
        entity: sensor.chunmi_cn_404489380_eh1_status_p_2_1
        rows: [...]
      - name: 空气炸锅
        entity: switch.kongqizhaguo
        rows: [...]
```

| `calendar_card` 取值 | 效果 |
|---|---|
| 不配置 | 显示入口；卡片用内置默认（标题 = `${title}用电量日历`，单位与配色跟随 `usage_calendar` 默认） |
| 对象 `{…}` | 显示入口；对象里的字段**最后合并**进卡片配置（优先级最高，可覆盖任意 `usage_calendar` 配置项；其中 `width` 只用于弹窗宽度，不会传给卡片） |
| `false` | **不显示**该入口 |

> 与空调组合计日历（`ac_calendar_card: usage`）是同一套机制：实体列表由调用方自动汇总、卡片内部自动补 `api` 配置 —— 区别只是这里的实体来自 `tabs[].entity`。

---

## 八-A、左右滑动（切换选项卡 / 翻页）

**卡片里所有分页的地方都支持左右滑动**：弹窗内的选项卡、头部模式的多页按钮，以及各卡片自己的分页（多房间 / 多用户 / 多档位 / 多数据集）。它们由同一个通用机制驱动（`modules/infra/swipe-tabs.js`），所以手感完全一致：

- **跟手拖动**：内容跟着手指走；已经在第一页还往右拖、或最后一页还往左拖时会更"黏"（拖得动、但拖不走，一松手就弹回）。
- **松手吸附**：按位移与甩动速度决定翻到上一页 / 下一页，不过阈值就弹回原位。
- **页签高亮跟手**：拖动过程中越过半屏，目标页的选项卡 / 底部圆点就先亮起来，不会出现"滑完了高亮才闪过去"。
- **纵向滚动不受影响**：先动的方向决定归属 —— 横向归翻页、纵向交回浏览器滚动。起点落在**按钮 / 输入框 / 日期导航**上时不算翻页（那是交互）；页面里**横向可滚动的区域**（如横向卡片列表）会主动让路。
- **只有一页时不启用**：没有可翻的页就不绑手势，也不会影响页面滚动。
- **无需任何配置**：配了多页 / 多个选项卡就自动生效；桌面端在**头部多页**上还可以直接用**滚轮**翻页。

**支持左右滑动的位置一览**

| 位置 | 翻动的是什么 |
|---|---|
| 卡片头部多页（`head: true` + `buttons_2` / `buttons_3` …） | 按钮页（底部圆点指示当前页） |
| 灯光 / 插座 / 耗材弹窗 | 房间 / 楼层选项卡 |
| 自动化管理卡片 | 「信息 / 编辑」 |
| 媒体播放器卡片 | 底部页面页签（播放列表 / 自由布局页等） |
| 用户卡片 | 多个用户之间（每人一页） |
| 用户详情弹窗 | 上一个人 / 下一个人 |
| 健康数据弹窗 | 「查询 / 新增」 |
| 空调弹窗 | 两页（控制 / 曲线） |
| 使用量日历卡片 | 六个选项卡（日历 / 历史 / 年 / 月 / 日 / 洞察） |
| 设备用电详情弹窗 | 房间 / 全屋 / 桑基图 |
| 调试信息卡片 | 调试 / 性能 / 版本 / 数据库 |
| 最近使用气泡（概览行） | 数据集（卡片 / 全部） |
| 自由布局弹窗（选项卡模式） | 分组选项卡 |
| ESXi 卡片 | 主机 / 虚拟机 / 屏幕墙 |
| iKuai 全实体卡片 | 路由（六个子页签）/ Docker / 虚拟机 / 日志 |
| 通讯模块（`comm`） | 账户 / 通讯记录 / 统计分析 |

> **滑不动怎么办**：先确认该处确实有多于一页；再确认起手位置不是在按钮 / 输入框 / 日期导航上（这些位置是交互，不翻页）。纵向拖动是故意交给页面滚动的，不会翻页。

---

## 九、人员/人在传感器（Person）

在卡片左下角显示一个人体感应小按钮，点击弹出完整的人员活动弹窗，包含：

> 实体状态 → 时间轴 → 活动统计 → 平面户型图

```yaml
person:
  - main_entity: binary_sensor.living_motion  # 主传感器
    icon: mdi:motion-sensor
    rooms:                                      # 各房间传感器映射
      客厅: binary_sensor.living_motion
      卧室: binary_sensor.bedroom_motion
      书房: binary_sensor.study_motion
    entities:                                   # 其他相关实体
      - entity: sensor.illuminance
        name: 光照
      - entity: sensor.volume
        name: 音量
    show_timeline: true                         # 显示活动时间轴（默认显示）
    room_point_from: /local/point.json          # 平面图坐标数据文件
    room_name_font_size: 16                     # 平面图房间名字体大小
    corner_radius: 8                            # 平面图房间圆角大小
    width: 600px                                # 弹窗宽度
    api_base_url: http://192.168.1.100:8080     # 外部历史数据API地址
    device_type: 人在                           # 设备类型
    person_icon:                                # 有人图标自定义（可选，不配置则使用默认样式）
      size: 30px                                # 图标大小（默认：当前房间28px / 普通房间22px）
      top: 20px                                 # 图标相对房间中心的向下偏移（默认：20px）
      left: 10px                                # 图标相对房间中心的向右偏移（默认：0px，负值向左）
      color: rgb(39, 174, 96)                   # 图标颜色（默认：当前房间#27ae60 / 普通房间#2ecc71）
```

每个人物实体图标旁有个小历史图标，点击可查看该实体的历史记录时间轴。

### person_icon 配置详解

`person_icon` 用于自定义平面户型图中"有人"状态图标的样式。不配置时使用默认值，配置后覆盖默认样式。

**配置格式**（支持两种写法）：

```yaml
# 写法1：对象格式（推荐）
person_icon:
  size: 30px
  top: 20px
  left: 10px
  color: rgb(39, 174, 96)

# 写法2：数组格式（也可用）
person_icon:
  - size: 30px
  - top: 20px
  - left: 10px
  - color: rgb(39, 174, 96)
```

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `size` | `string` | 当前房间 `28px` / 普通房间 `22px` | 图标尺寸，如 `"30px"` |
| `top` | `string` | `20px` | 图标相对房间几何中心的向下偏移量，如 `"20px"` |
| `left` | `string` | `0px` | 图标相对房间几何中心的向右偏移量，如 `"10px"`（负值向左偏移） |
| `color` | `string` | 当前房间 `#27ae60` / 普通房间 `#2ecc71` | 图标颜色，支持所有 CSS 颜色值（如 `#2ecc71`、`rgb(39,174,96)`、`rgba(46,204,113,0.8)` 等） |

> **注意：** `person_icon.color` 仅控制实时模式下的图标颜色。历史模式（拖动时间轴时）始终使用橙色 `#f39c12` 以区分实时状态。

---

## 十、自动化开关

在卡片底部右侧显示，列出所有自动化开关，点击弹出控制面板统一管理。

```yaml
automation:
  - entity: automation.good_morning     # 自动化实体ID
    name: 早安模式                       # 显示名称
  - entity: automation.away_mode
    name: 离家模式
  - entity: automation.good_night
    name: 晚安模式
```

---

## 十一、概览栏（Overview Bar）

当 `head: true` 时，可以在卡片顶部显示一条全屋设备态势概览栏。它会自动统计各设备类型的运行状态数量，点击可弹出对应的控制面板。

### 11.1 灯光概览
自动从 `type: lights` 按钮中统计已开启的灯数量，无需额外配置。

### 11.2 空调概览
自动从 `type: ac` 按钮中统计已开启的空调数量。

### 11.3 插座概览
自动从 `type: socket` 按钮中统计已开启的插座数量。

### 11.4 耗材概览
自动从 `type: consumables` 按钮中统计已低于阈值的耗材数量。

### 11.5 环境概览（需配置）
显示温湿度数据。

```yaml
overview:
  - type: environment
    rooms:
      户外:
        temperature: sensor.outdoor_temp
        humidity: sensor.outdoor_hum
      客厅:
        temperature: sensor.living_temp
        humidity: sensor.living_hum
```

### 11.6 人员概览（需配置）
显示在家人员、各房间占用状态。

```yaml
overview:
  - type: person
    rooms:
      客厅: binary_sensor.living_motion
      卧室: binary_sensor.bedroom_motion
    person:
      - entity: person.zhangsan
        name: 张三
      - entity: person.lisi
        name: 李四
```

### 11.7 能耗概览（需配置）
显示用电量、功率、余额等信息。

```yaml
overview:
  - type: energy
    utilities:
      电力:
        entity: sensor.electricity_meter          # 主实体（使用量）
        power: sensor.electricity_power           # 功率
        power_onsumption: sensor.daily_consumption # 今日用电量
        cost_entity: sensor.balance               # 余额
        icon: mdi:transmission-tower
        tap_action:                                # 余额点击动作
          action: call-service
          service: room_card.show_free_layout_popup
          card:
            - type: sensor
              entity: sensor.electricity_detail
      天然气:
        entity: sensor.gas_meter
        cost_entity: sensor.gas_balance
```

除了固定 entity+power 模式，每个 utility 也支持 **`content` 自由配置模式**——使用 [Jinja2 模板语法](#1111-公告栏notice-bar) 完全自定义显示内容，并支持 `tap_action` 动作系统：

```yaml
overview:
  - type: energy
    name: 能耗
    utilities:
      电力:                                   # ← 保持现有格式不变
        entity: sensor.electricity_meter
        power: sensor.electricity_power
        power_onsumption: sensor.daily_consumption
        cost_entity: sensor.balance
        icon: mdi:transmission-tower
      空调:                                   # ← 自由配置，无需 entity
        icon: mdi:air-conditioner
        content: |-                           # Jinja2 模板，渲染到右侧
          {% set balance_raw = states('sensor.ele_6103231959710') %}
          {% set balance = balance_raw | float(0) %}
          {% set text_color = '#d9383a' if balance < 20 else '#006e54' %}
          ❶电费余额：<span style="color: {{ text_color }}; font-weight: bold;">{{ balance_raw }} 元</span>，
          可用{{ states('sensor.dian_fei_zhang_hu_6103231959710_yu_ji_ke_yong') }}天
        tap_action:                           # 支持完整动作系统
          card_config:
            from_config_id: ele
            get_type: all
          card_params:
            initial_tab: "1"
```

**`content` 模式字段说明：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `content` | ✅ | `string` | Jinja2 模板字符串，渲染后的 HTML 显示在行右侧；左侧固定显示 `icon` + `name` |
| `icon` | ❌ | `string` | 左侧图标，如 `mdi:air-conditioner` |
| `tap_action` | ❌ | `object` | 行点击动作，支持 `card_config.from_config_id` 引用等完整动作系统 |

> **提示**：`content` 模式下无需配置 `entity`/`power`/`cost_entity` 等字段，所有动态数据通过 Jinja2 模板中的 `states()` / `state_attr()` 函数读取。模板引擎与公告栏共享同一套内置函数和过滤器。

#### 11.7.1 层级树状结构（`level`）

从 v5.1.11 起，`utilities` 中每个自定义类型支持 `level` 字段，用于建立层级归属关系。子项会自动锚定到"最近的上一个 level 比自己小的"作为父级，UI 中以树状连接线（`├─` / `└─` / `│`）直观展示。

| 字段 | 必填 | 类型 | 默认值 | 说明 |
|------|:----:|------|--------|------|
| `level` | ❌ | `number` | `1` | 层级深度，`1` 为顶层（加粗），`2` 为二级子集，`3` 为三级子集 |

**层级规则：**
- 不配置 `level` 时默认为顶层（level=1），**顶层名称自动加粗显示**
- 配置顺序决定层级关系：子项必须紧跟父项，不可写在父项前面
- 跳级自动容错（如 1→3 直接跳到三级，锚定到最近的有效父级并 console.warn）
- 首个 item `level > 1` 自动降级为 1

**配置示例：**

```yaml
overview:
  - type: energy
    utilities:
      电力:
        entity: sensor.ele_xxx
        # 不写 level = 顶层（默认1），名称加粗
      空调:
        level: 2                              # 电力下的二级子集
        icon: mdi:air-conditioner
        content: >-
          今日：{{ states('sensor.ac_daily') | float(0) | round(1) }}kWh
          | 总功率：{{ (states('sensor.ac_power') | float(0) / 1000) | round(1) }}kw
      新风:
        level: 2                              # 也是电力下的二级子集
        icon: mdi:air-filter
        content: >-
          今日：{{ states('sensor.fan_daily') | float(0) | round(1) }}kWh
      热水器:
        level: 3                              # 新风下的三级子集
        icon: mdi:water-boiler
        content: >-
          今日：{{ states('sensor.heater_daily') | float(0) | round(1) }}kWh
      自来水:
        entity: sensor.water
        # 不写 level，回到顶层
```

**UI 效果：**

```
⚡ 电力          用电量：15.2kWh | 功率：2.1kW    ← 顶层加粗
│  ├─ 🌀 空调     今日：5.1kWh | 总功率：1.8kw    ← 二级，连续竖线连接
│  │  └─ 🔥 热水器 今日：2.1kWh | 总功率：1.5kw   ← 三级，多级竖线连接
│  └─ 🍃 新风     今日：0.8kWh | 总功率：0.3kw    ← 二级最后子项，└─ 拐角收尾
💧 自来水         12.5 m³                         ← 顶层加粗
```

> **提示**：`level` 适用于 `entity` 模式和 `content` 自由配置模式，两种模式均可建立层级关系。实体模式和自由配置模式可以混合在同一层级树中。

#### 11.7.2 能耗折叠（`fold`）

从 **v5.3.1** 起，概览弹窗「全屋能耗」卡片标题栏右端新增**折叠/展开按钮**，通过 `energy` 配置项的 `fold` 字段控制是否显示。用于收起能耗明细（燃气灶、热水器、空调、服务器等二级子项），仅保留顶层大标题。

```yaml
overview:
  - type: energy
    name: 能耗
    fold: true                      # true=显示折叠按钮并初始折叠 level>1 子项；false/不配置=全部展开
    icon: mdi:gas-burner
    utilities:
      天然气:
        entity: sensor.gas_xxx
      燃气灶:
        icon: mdi:water-boiler
        level: 2
        content: >-
          今日：{{ states('sensor.xxx') | float(0) | round(2) }}m³
      电力:
        entity: sensor.ele_xxx
      # ... 其他子项
```

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `fold` | ❌ | `boolean` | `true` 显示折叠按钮并初始折叠所有 `level > 1` 的子项（仅显示顶层大标题）；`false`/不配置 全部展开 |

**规则说明：**
- 配置了 `fold`（无论 `true`/`false`）→ 显示折叠按钮；未配置 → 不显示按钮（现行模式）
- 折叠规则按**层级**：`fold: true` 折叠所有 `level > 1` 的行，保留 level 1 顶层（天然气、电力等）
- **交互**：点击标题栏**任意位置**（标题文字/图标）或右侧折叠按钮均可折叠/展开；图标在 `mdi:chevron-down`（折叠）与 `mdi:chevron-up`（展开）间切换
- 初始状态按配置：`fold: true` 打开弹窗即默认折叠；关闭弹窗后重置，重开时按配置重新初始化
- 余额行（`balance-row`）不参与折叠，始终显示

### 11.8 天气概览（需配置）

在概览弹窗的微气候卡片中显示天气预报项，点击可展开完整的天气气泡（含今日详情、7日预报等）。

支持**多城市天气**和**API 数据源**（无 HA 实体时也能用）。

---

#### 基础配置（单城市）

```yaml
overview:
  - type: weather
    entity: sensor.he_feng_tian_qi          # 和风天气 HA 实体（推荐）
```

#### 多城市配置（推荐）

```yaml
overview:
  - type: weather
    weather:                                  # 多地区数组（与用户卡片天气配置格式一致）
      - name: 未央区                           # 地区名称（显示在 Tab 上）
        entity: sensor.he_feng_xi_an           # 和风天气 HA 实体（优先）
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx  # API 地址（降级）
      - name: 西乡县
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110807&key=xxx  # 仅 API，无实体
```

也支持 `regions` 字段名（等同 `weather`）：

```yaml
overview:
  - type: weather
    regions:
      - name: 西安市
        entity: sensor.he_feng_xi_an
      - name: 汉中市
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx
```

#### 天气配置字段说明

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `name` | ❌ | `string` | 地区名称，显示在多城市 Tab 切换按钮上 |
| `entity` | ❌ | `string` | 和风天气 HA 实体 ID（优先使用，需含 `daily` 属性） |
| `api_base_url` | ❌ | `string` | 和风天气 API 地址（实体无数据时降级使用） |
| `living_index` | ❌ | `string` | 自定义首页生活指数，多个用逗号隔开，如 `穿衣指数,洗车指数`。不配置时默认显示穿衣指数。支持：`运动指数`、`洗车指数`、`穿衣指数`、`钓鱼指数`、`紫外线指数`、`旅游指数`、`过敏指数`、`舒适度指数`、`感冒指数`、`空气污染扩散条件指数`、`空调开启指数`、`太阳镜指数`、`化妆指数`、`晾晒指数`、`交通指数`、`防晒指数` |

**数据源优先级：** `entity` > `api_base_url`。同时配置时优先用实体数据，实体无数据则降级到 API。

**API 数据缓存：** 从 API 获取的数据会缓存 30 分钟，避免频繁请求。打开气泡时如果缓存过期会自动刷新。

**无实体纯 API 模式：** 当没有 `entity` 只有 `api_base_url` 时，首次加载会显示"加载中"占位，API 数据获取后自动刷新为真实天气数据。

#### 天气配置格式支持三种写法

```yaml
# 写法1：标准数组格式（推荐）
overview:
  - type: weather
    weather:
      - name: 西安市
        entity: sensor.he_feng_xi_an
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx
      - name: 汉中市
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx

# 写法2：对象键名作为地区名
overview:
  - type: weather
    weather:
      - 西安市:
          entity: sensor.he_feng_xi_an
          api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx
      - 汉中市:
          api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=xxx

# 写法3：旧格式（单地区，向后兼容）
overview:
  - type: weather
    entity: sensor.he_feng_xi_an
```

#### 天气气泡展示内容

点击概览弹窗微气候区的"天气预报"项，会弹出天气气泡，包含：
- **今日概览**：天气图标、温度范围、天气描述、风力、日出日落
- **详情指标**：紫外线、湿度、气压、能见度、云量
- **7日预报**：每日天气图标、温度范围、天气文字
- **更新时间**：根据日期颜色编码（今日=绿、昨日=黄、更早=红）

#### 完整配置示例

```yaml
overview:
  - type: environment
    name: 环境
    icon: mdi:thermometer-water
    rooms:
      户外:
        temperature: sensor.outdoor_temp
        humidity: sensor.outdoor_hum
      客厅:
        temperature: sensor.living_temp
        humidity: sensor.living_hum

  - type: weather
    weather:
      - name: 未央区
        entity: sensor.wang_luo_api_he_feng_tian_qi_api
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110101&key=你的KEY
      - name: 西乡县
        api_base_url: https://devapi.qweather.com/v7/weather/7d?location=101110807&key=你的KEY
```

> **注意：** 天气预报项需要和 `type: environment` 配合使用——它显示在微气候卡片的 env-grid 中。如果未配置 `environment`，天气项不会显示。

### 11.9 自定义设备概览（需配置）
可以创建自己的设备统计类别。

```yaml
overview:
  - type: overview_device
    name: 窗户                         # 显示名称
    icon: mdi:window-open               # 图标
    entities:                           # 要统计的设备列表
      - entity: binary_sensor.window1
        name: 客厅窗户
      - entity: binary_sensor.window2
        name: 卧室窗户
    condition: ['on']                   # 匹配条件（匹配"on"状态）
    show_badge: true                    # 显示匹配数量
    show_card: true                     # 概览弹窗中显示
    tap_action:                         # 点击动作
      action: toggle
      entity: switch.all_windows
```

条件支持数值比较（如 `'<10'`、`'>=20'`），也支持字符串匹配（如 `'on'`、`'home'`）。多个条件为"或"关系。

### 11.9.1 实体健康概览（可选配置）

从 **v5.3.1** 起，概览弹窗（`overview-control-popup`）的**设备概览**区域新增一张**实体健康状态**小卡片，展示全屋实体在线/离线/未知概况，点击弹出 `entities_health` 实体健康状态弹窗（按房间 / 按状态两个选项卡）。

**数据来源**：后端 `ha_data_store` 实体上报传感器（默认 `sensor.hashu_ju_tong_yi_cun_chu_xi_tong_frontend_card_entities_health`），读取 `total`/`online`/`unknown`/`offline` 属性。

**小卡片展示**：主值显示离线数、`/总数`，详情 `在线 x · 未知 y · 离线 z`，图标 `mdi:heart-pulse`，存在离线时高亮。

可选配置（在 `overview` 数组中增加 `type: entities_health` 配置项，用于自定义数据源、外观、过滤房间及显示开关）：

```yaml
overview:
  - type: entities_health
    entity: sensor.hashu_ju_tong_yi_cun_chu_xi_tong_frontend_card_entities_health  # 数据源（可选，默认上述实体）
    hide_room: 次卧外,儿童房外,楼道,客厅外    # 弹窗户型图过滤的房间（逗号分隔）
    name: 实体健康                           # 小卡片标题（默认「实体健康」）
    icon: mdi:heart-pulse                    # 小卡片图标
    width: 600px                             # 弹窗宽度
    show_card: true                          # false 时隐藏该小卡片
```

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `type` | ✅ | `string` | 固定为 `entities_health` |
| `entity` | ❌ | `string` | 数据源传感器，覆盖默认实体 |
| `hide_room` | ❌ | `string` | 逗号分隔房间名，弹窗户型图过滤掉这些房间（传给 `showEntitiesHealthPopup`） |
| `name` | ❌ | `string` | 小卡片标题，默认「实体健康」 |
| `icon` | ❌ | `string` | 小卡片图标，默认 `mdi:heart-pulse` |
| `width` | ❌ | `string` | 弹窗宽度 |
| `show_card` | ❌ | `boolean` | `false` 时隐藏该小卡片 |

**行为**：
- 配置了 `type: entities_health` → 用配置的 `entity` 读取数据渲染小卡片，可用 `name`/`icon` 自定义外观，`show_card: false` 隐藏；点击弹窗时把完整配置（含 `entity`/`hide_room`/`width`）传给 `showEntitiesHealthPopup`
- 未配置 → 保持默认（用默认 sensor，`total > 0` 时显示）

### 11.9.2 概览顶部信息条（overview_info）

从 **v5.3.1** 起，概览弹窗（`overview-control-popup`）**顶部**（"全屋态势"标题行横线 `.section-title::after` 下方）可显示一条**信息条**，居中展示指定实体的状态值；点击弹出气泡显示该实体的 `summary` 属性（如家庭日报全文）。

```yaml
overview:
  - overview_info: sensor.hashu_ju_tong_yi_cun_chu_xi_tong_today_family_status   # 实体 ID
    name: 今日家庭状态          # 可选，气泡标题（默认「今日家庭状态」）
```

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `overview_info` | ✅ | `string` | 实体 ID，读取其 `state` 显示在信息条，`attributes.summary` 显示在气泡 |
| `name` | ❌ | `string` | 气泡标题，默认「今日家庭状态」 |

**行为**：
- 信息条显示实体 `state`（如 `家中有人（客厅），开着 1 盏灯，入户门关闭`），居中、单行省略
- 点击弹出气泡，展示气泡标题 + 状态值 + `summary` 长文本（`white-space: pre-wrap`，可滚动）
- 仅配置 `overview_info` 时也会显示"全屋态势"标题行（作为信息条定位基准）
- 未配置 `overview_info` 或无实体数据 → 不显示信息条

### 11.10 其他概览配置项

```yaml
overview:
  - type: consumables                   # 耗材概览配置
    condition: ['<10']                  # 告警阈值
    show_card: true                     # 概览弹窗是否显示
    show_badge: true                    # 概览栏是否显示角标
  - type: environment
    show_card: true
  - type: energy
    show_card: true
  - type: person
    show_card: true
    room_point_from: /local/point.json   # 平面图文件
    automatic_folding_ha_info: true      # HA系统信息卡片默认折叠
  - recently-used: sensor.hashu_ju_tong_yi_cun_chu_xi_tong_jin_qi_shi_yong_she_bei  # 最近使用设备（见 11.10.1）
```

#### 11.10.1 最近使用设备（recently-used）

在概览栏**最左侧的固定入口列**（`.ov-entry-col`，约 70px，与"自动化管理"横向并排两格，独立成列、带右分隔线）显示"常用"入口，点击弹出**最近使用设备气泡卡片**（复用统一气泡弹窗 `_showBubble`）。

**依赖**：需配合 **HA 统一数据存储系统 2.13.0 及以上版本**（提供"近期使用设备"实体及 `config_id` / `device_type` 字段）；「全部」选项卡还依赖后端提供实体 **`all` 节点**与查询类型 **`timeline`** / **`all_rooms_data_dates`**，后端未提供这些节点/接口时「全部」列表为空、时间线与日历标记不显示（前端不报错）。

```yaml
overview:
  - recently-used: sensor.hashu_ju_tong_yi_cun_chu_xi_tong_jin_qi_shi_yong_she_bei  # 近期使用设备实体ID（必需）
    width: 430px        # 可选，气泡宽度，默认 440px（为"时空"表盘留空间；空数据时 300px）
    maxItems: 20        # 可选，气泡中最多显示的设备数，默认 50
```

> 兼容写法：`- type: recently-used` + `entity: sensor.xxx` + `width: 430px` + `maxItems: 20`

**功能**：

- **入口**：概览栏**最左侧固定入口列**（`.ov-entry-col`，约 70px）中与"自动化管理"横向并排一格，显示"常用"文本 + 去重后的设备个数；固定入口列自带右分隔线，与中间动态指标列（`.ov-left-col`）隔开，点击入口列间隙/边距不会误开"全量概览"弹窗。
- **气泡宽度**：可通过 `width` 参数自定义（如 `430px`），未配置时默认 440px。
- **数据集选项卡「卡片 / 全部」**（`recently-used-header` **右端**，胶囊样式 `.recently-used-view-tabs`；默认「卡片」，无 `devices` 数据时自动落到「全部」）：
  - **卡片**（默认）：数据源为实体 `attributes.devices[]`（用户操作过的设备卡片，含 `user_name` / `config_id`），即原有内容；标题「卡片内最近使用（N）」。
  - **全部**：数据源为实体 `attributes.all[]`（全部受监控设备，**无用户维度**：`room` → 房间名，无 `user_name` / `config_id`，点击按实体反查配置树）；**列表行布局、图标/状态标签、房间标签、右侧控件、点击弹窗、实时状态同步与「卡片」完全一致**，只是数据不同；标题「全部最近使用（N）」。
  - 切换选项卡时重建下方子选项卡行（用户筛选 + 时间线 + 时空），两个选项卡各自的「时空 / 时间线」惰性渲染状态互相独立；标题括号内数量为**该数据集**去重后的设备总数，不随用户筛选变化。
- **气泡列表**：按 `entity_id` 去重、按最近使用时间倒序；设备项之间显示分割线；`header` 固定不滚动、列表独立滚动；图标按实体/名称推断（实体域 `climate` → `mdi:air-conditioner`，名称含"灯"或"照片" → `mdi:lightbulb`，名称含"插座/插排" → `mdi:power-socket-au`）。
- **用户筛选**：子选项卡行按 `user_name` 筛选（"全部" + 各用户选项卡，复用 `eh-tabs` 样式），默认选中当前登录用户；「全部」数据集无用户维度 → 不显示用户选项卡。
- **"时间线"选项卡**（子选项卡行内固定项）：按时间倒序展示当日事件（日期导航 `◀ 日期 ▶` + 可滚动列表），条目 = 左侧节点（有用户 → 用户头像；无用户 → **事件来源图标**，底色按 `source` 区分）+ 设备名 + 状态徽章 + 房间/状态/用户 + 右下角操作控件。
  **数据源按数据集区分**：

  | 数据集 | 接口 | 字段映射 |
  |---|---|---|
  | 卡片 | `query?type=user_actions_daily&key=xxx&date=YYYY-MM-DD` | 原 `actions` 结构：`ts` / `ts_text` / `user_name` / `room_name` / `state_log` / `config_id` |
  | 全部 | `query?type=timeline&key=xxx&date=YYYY-MM-DD`（后端多来源事件流：device / user_action / automation / vacuum / xiaoai / health / printer） | `ts_ms` → `ts`、`ts` → `ts_text`、`room` → `room_name`、`user` → `user_name`、`detail` → `state_log`、`name` 缺失时回退 `title`、`config_id` 置空 |

  来源底色 `_timelineSourceColor()`：device 橙 / user_action 蓝 / automation 紫 / vacuum 绿 / xiaoai 青 / health 红 / printer 深灰；`event: on/off` 追加「开启 / 关闭」徽章；无用户事件不显示用户名标签。
  **点击日期文本**打开日历弹窗（`calendar-popup-container`），日期 "A" 标记的数据源同样按数据集区分：卡片 → `user_actions_month_dates`；全部 → `all_rooms_data_dates&category=device`（复用 `_fetchCachedMonthDates` 的 10 分钟共享缓存）。
- **"时空"表盘选项卡**：用户筛选选项卡栏**最右侧**新增固定选项卡 **"时空"**，点击切换到 **24 小时同心环表盘**视图（表盘**自适应气泡宽度**保持正方形，气泡默认宽 440px）：
  - **空间 = 圈层**：每个房间一圈同心环（`room_name`，空房间归为 **"头部"**），环半径**基于表盘半径自动均匀分配**，最外圈半径**随房间个数动态求解**且**贴近刻度内侧**（最外房间区域延伸到表盘外环、外部不留大段空白），从中央保留区到外圈等距铺满，环内即该房间区域；按房间操作总次数降序由内到外。房间名**沿环带中心半径按弧度错落分布**在 **02:00→06:00 方向**弧段（不同房间不同半径+角度），不再固定于左右两端。图标**落在环带内部中心**（非边界线上），避免与环线/标签重叠。
  - **时间 = 角度**：设备最后使用时间（`last_used`）映射角度，0 点在正上方、顺时针，精确到分钟。
  - **设备 = 图标**：每个设备一个图标点（复用列表图标推断逻辑），**用户色圆形背景圆圈 + 白色图标**，尺寸随使用频率变化。
  - **用户 = 图标背景色**：背景圆圈按用户名分配用户色（当前登录用户蓝色 `#0072ff`，其他用户 hash 取色），图标白色。
  - **频率 = 图标大小**：先求出所有设备 `count` 的**最小值/最大值**，线性插值把图标尺寸映射到 **9–28px**（最小 count → 最小图标，最大 count → 最大图标），次数越多图标越大、差异更明显、图标更紧凑减少重叠。
  - **外圈刻度**：0/6/12/18 粗刻度并标注数字（0 显示为 24）；中央显示"时空"标题 + 当前时间（已去掉当前时刻指针）。
  - **点击图标点** → 弹出该设备**本次操作详情**（谁 / 何时 / 何房间 / 何设备 / 何操作，含状态与参数摘要），详情弹窗**底部右端显示可操作控件**（切换开关 / 按下按钮，与 recently-used 列表一致）。
  - **点击房间环带（任意位置）** → 弹出该房间**数据汇总**：房间名、总操作次数、各用户操作统计（用户色标签）、设备列表（图标 + 名称 + 次数 + 最近时间 + **用户名称标签**（涉及多个用户时在 meta 左侧显示，样式同 recently-used-user-tag）+ 右端**操作控件**，与 recently-used 列表一致：打开按钮 / 切换开关 / 按下按钮）。
  - **逐层关闭**：点击内部详情弹窗并关闭它时，不会连带关闭气泡本身；需先关内层弹窗，再点击遮罩关闭气泡。
- **点击设备项弹窗**（`recently-used-info`，按优先级依次尝试，命中即返回）：

  | 优先级 | 条件 | 行为 |
  |---|---|---|
  | 0 | `cover` 域且窗帘**三级定位**命中（`_resolveCurtainGroup`：all_curtain 总表 / 配置树 curtain 分组 / 自动构建） | 直接弹出该窗帘的帘布控制窗（忽略记录 `config_id`） |
  | 1 | 设备有 `config_id`，且 `RoomElvesStore.get(config_id)` 取到**弹窗内容**（`service_data.cards/tabs` 或 `tabs/rows/card`） | 打开该 `config_id` 引用弹窗（free-layout / 选项卡） |
  | 2 | 分组配置匹配且设备 `type === 'ac'`（空调） | 通过分组级 `config_id`（如 `all_ac`）按主实体 `entity` 筛选，直接渲染单个空调卡片 |
  | 3 | 反查配置树设备节点有 `entities` | `showEntityDetailsPopup` 打开设备详情弹窗 |
  | 4 | 设备节点 `tap_action` 是弹窗类（`card`/`popup_card`/`popup` 或 `call-service` + 弹窗） | 执行该 `tap_action` |
  | 5 | 以上全部未命中 | 打开 more-info 弹窗 |

- **右侧控件**（按实体类型）：
  - **可开关设备**（名称含"插座"，或 `switch` / `light` / `input_boolean` 域）→ 右侧同时显示 **"打开"按钮（左）+ 切换开关（右）**：点击"打开"弹出 config_id 弹窗，点击开关直接开/关并记录操作日志；点击设备项主体则打开 config_id 弹窗；
  - **按钮实体**（`input_button` / `button`）→ 右侧显示橙色"按下"按钮，点击执行 `press` 并记录操作日志；
  - **点击会打开弹窗的不可切换设备**（空调分组 / 窗帘总表命中 / 设备弹窗 / tap_action 弹窗类）→ 右侧显示**淡蓝色"打开"按钮**，点击打开对应弹窗。
- **点击左侧图标弹出历史记录**：列表项**左侧图标**点击后弹出该实体的**历史操作记录**（复用 `showEntityHistoryTimeline` / `timeline-history-bubble`，访问 HA 历史数据 API，含时间轴图表 + 时间段记录 + 日期切换）。

**空调分组级 config_id（可选）**：若想点击最近使用空调时直接渲染单个空调卡片，需给 `buttons` 分组的空调分组配置 `config_id`（如 `all_ac`），程序会按实体 `entity` 匹配并直接渲染对应空调。

```yaml
buttons:
  - type: ac
    name: 全屋空调
    config_id: all_ac          # ← 分组级 config_id
    card:
      - type: ac
        entity: climate.xxx
        ...
```

**窗帘实体（cover 域）自动弹出（增强）**：点击最近使用中的**窗帘**会直接弹出该窗帘的**帘布控制窗**（`showCurtainControlPopup`），不再落入 more-info。窗帘无论从哪个入口（头部全屋 / 房间 / 引用弹窗）操作过，记录里的 `config_id` 可能不同或为空，程序**忽略记录 config_id**，统一按以下**三级定位**找到窗帘并弹出：

| 级 | 定位来源 | 说明 |
|---|---|---|
| 1 | 全屋窗帘总表 `all_curtain` | 头部"全屋窗帘"按钮带 `config_id: all_curtain`（`buttons` 分组，`card[]` 收录所有房间窗帘）。按 `fabric_entity` / `sheer_entity` / `entity` 匹配；命中时窗帘窗**强制使用本地窗景背景** `/local/window_bg_1.png` |
| 2 | 当前配置树 `type: curtain` 分组 | 遍历 `buttons` / `buttons_N`，即使分组**未带 `config_id`**（未注册 Store）也能按实体命中，继承分组/子卡的开合模式与背景 |
| 3 | 自动构建（无任何配置锚点） | 仅当可确认是窗帘：`cover` 实体 `attributes.device_class === 'curtain'` 或名称含"窗帘"→ 自动组装**单层布帘**（`layer_mode: single`）窗帘窗；其他 cover（车库门/卷帘门等）不受影响 |

```yaml
# 三级定位第 1 级依赖的分组（可选配置——未配置该组时自动退到第 2/3 级）
buttons:
  - type: curtain
    name: 全屋窗帘
    config_id: all_curtain
    card:
      - name: 客厅窗帘
        fabric_entity: cover.xxx
```

- **弹窗名称**：与最近使用列表项名称一致（点击时透传列表显示名，非 HA `friendly_name`）。
- **只布帘**：无纱帘实体（`sheer_entity`）时 `layer_mode` 自动降为 `single`，只渲染布帘层，不出现空纱帘/同步开关；有纱帘实体才保留 `double` 双层。
- **列表入口**：命中窗帘后列表项**右端出现"打开"按钮**；图标名称含"窗帘" → `mdi:curtains`。
- **防克隆按钮残留**：该窗帘窗不向 `showPopup` 传触发元素，避免触发元素被克隆成高亮按钮残留在原位置。
- **操作记录 icon 兜底**：常用气泡内操作实体上报 `icon` 不再为空——名称含"窗帘/灯/插座"或按实体域名推断默认图标（`action-log.js _inferActionLogIcon`）。

**未配置** `recently-used` 时，概览栏保持原有模式，不显示"常用"入口。

#### 11.10.2 自动化管理卡片（automations）

在概览栏**最左侧固定入口列**（`.ov-entry-col`，约 70px，与"最近使用设备"横向并排两格、独立成列、带右分隔线）增加"自动化管理"入口（`ov-seg ov-automations`），点击弹出**自动化管理弹窗卡片**，含两个选项卡：

- **信息**：自动化整体统计 + 明细列表
  - 数据源 `sensor.ha_data_store_automation` 实体：`state` = 启用自动化个数
  - `attributes`：`total/enabled/disabled` = 总数/启用/停用；`success/failed/skipped/never` = 最近一次执行结果统计（成功/失败/条件跳过/从未执行）；`total_runs/updated_at` = 总执行次数/数据更新时间；`automations[]` = 明细项 `{ id, name, enabled, trigger_type, trigger_desc, stop_on_error, next_run, last_run, last_result, last_duration_ms, run_count, success_count, failed_count, skipped_count }`
- **编辑**：自动化完整管理（后端 REST API，`api_base_url` + `key` 鉴权）
  - `GET /api/ha_data_store/automations` 列表
  - `POST /api/ha_data_store/automations` 新建
  - `PUT /api/ha_data_store/automations/{id}` 更新（启停/编辑）
  - `DELETE /api/ha_data_store/automations/{id}` 删除
  - `POST /api/ha_data_store/automations/{id}/run` 手动运行（`?force=1` 跳过条件）

```yaml
# 写法1：overview 键名 automations（值为实体 ID 字符串，或 { entity } 对象）
overview:
  - automations: sensor.ha_data_store_automation
    width: 400px        # 可选，弹窗宽度，默认 640px
    name: 自动化管理      # 可选，分段标题，默认「自动化管理」

# 写法2：overview type 字段 + entity
overview:
  - type: automations
    entity: sensor.ha.data.store.automation   # 兼容点号写法，自动归一化为下划线
    width: 400px
    name: 自动化管理
```

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `automations` | ✅ | `string`/`object` | 数据源实体 ID 字符串，或 `{ entity }` 对象（写法1） |
| `type` | ✅ | `string` | 固定为 `automations`（写法2） |
| `entity` | ❌ | `string` | 数据源传感器，覆盖默认实体 `sensor.ha_data_store_automation`；兼容点号写法自动归一化为下划线 |
| `name` | ❌ | `string` | 分段/弹窗标题，默认「自动化管理」 |
| `width` | ❌ | `string` | 弹窗宽度，默认 `640px` |

**独立弹出窗口（按钮 + popup_card）**：也可用 `buttons` 按钮配置 `tap_action.action: popup_card` + `card.type: automation`，点击按钮直接弹出自动化管理卡片（通用弹窗包裹，`createAutomationCard`），不依赖概览分段：

```yaml
buttons:
  - name: 自动化管理
    icon: mdi:robot
    tap_action:
      action: popup_card
      card:
        type: automation
        entity: sensor.ha.data.store.automation
        name: 自动化管理
        width: 400px
```

**行为**：
- 写法1/2 配置后概览栏出现"自动化管理"分段（`ov-seg ov-automations`），点击弹出自动化管理卡片
- 独立弹窗写法不依赖概览分段，任意 `tap_action` 位置（按钮/设备）均可配置 `popup_card` + `card.type: automation` 触发
- `entity` 未配置时默认 `sensor.ha_data_store_automation`（兼容点号写法，自动归一化为下划线）

---

### 11.11 自定义右列（type: right-col）

概览栏**右列**（`.ov-right-col`，带左侧分隔线的窄列）默认显示「户外温湿度 + 用电量」两行。配置 `type: right-col` 后改为**自定义来源**：**一行一个 `content`**，支持 **Jinja2 模板**与 **HTML**（解析规则与公告栏一致）。

```yaml
overview:
  - type: right-col
    items:
      - icon: mdi:thermometer          # 可选：行首图标
        name: 客厅                      # 可选：行首标签（浅色）
        content: >-                     # 一行一个 content
          {{ states('sensor.keting_wendu') }}℃/{{ states('sensor.keting_shidu') }}%
      - icon: mdi:flash
        name: 今日
        content: >-
          {{ states('sensor.today_energy') | float(0) | round(1) }}<span style="color:#e67e22">kWh</span>
    tap_action:                         # 整列共用一个点击动作
      action: navigate
      navigation_path: /lovelace/energy
```

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `type` | ✅ | `string` | 固定为 `right-col` |
| `items` | ✅ | `array` | 行列表，**一行一个 content**；为空数组时视为未配置 |
| `items[].icon` | ❌ | `string` | 行首图标（如 `mdi:thermometer`） |
| `items[].name` | ❌ | `string` | 行首标签，浅色显示；支持模板 |
| `items[].content` | ❌ | `string` | 行内容，支持 Jinja2 模板 + HTML |
| `tap_action` | ❌ | `object` | 整列点击动作，**不分行** —— 配置几个 item 都只有一个动作 |

**行为**

| 事项 | 说明 |
|------|------|
| 兼容性 | **未配置 `type: right-col`（或 `items` 为空数组）时，右列完全走原有逻辑**，本配置是纯增量 |
| 模板 | `content` / `name` 走与公告栏相同的前端 Jinja2 引擎（`_TemplateEngine`），可用 `states()` / `state_attr()` / `is_state()` / `iif()` / `now()` 等 |
| HTML | 与公告栏同口径：**仅保留 `<span style="...">`**，其他标签剥离、文本转义，`onclick` 等事件属性与 `url()` / `expression()` 被过滤 |
| 实时刷新 | 模板中引用的实体会被**自动加入订阅集**（支持 `states('x.y')` / `is_state(...)` / `state_attr(...)` / `has_value(...)` / `expand(...)` 以及旧式 `states.sensor.x`），实体一变即刷新 |
| 首屏 | hass 就绪前，纯静态文本立即显示、模板部分先显示 `--`，随后无缝替换为真实值 |
| 点击 | 整列共用一个 `tap_action`，支持 `toggle` / `more-info` / `navigate` / `call-service` / `popup_card` / `none`；**未配置 `tap_action` 时**仍弹出原来的「室外温湿度 + 用电趋势」气泡 |
| 宽度 | 自定义列不再固定 85px，按内容自适应（最窄 72px、最宽 55%），超出显示省略号；概览栏固定 38px 高，**建议 2 行**，3 行会偏挤 |

> 与 `type: environment` / `type: energy` 同时配置时，**右列以 `right-col` 为准**；后两者仍照常写入概览弹窗（`overview-control-popup`），只是不再占用右列位置。

---

### 11.12 公告栏（Notice Bar）

公告栏显示在概览栏上方，用于展示通知、状态提示等信息。支持两种内容类型：
- **content**：使用 Jinja2 模板语法（内置 `_TemplateEngine`），支持 `states()`、`state_attr()`、`is_state()`、`iif()`、`now()` 等函数
- **entity**：直接读取实体状态值 + 单位

两种类型可以混排在 `items` 数组中。

#### 基本配置

```yaml
notice:
  style:                                # 可选，自定义样式
    - width: 100%
    - height: 30px
  stay_time: 3000                       # 可选，每条公告停留时间（毫秒），默认 3000
  scroll_duration: 800                  # 可选，滚动到下一条的耗时（毫秒），默认 800
  scroll: false                         # 是否自动滚动（仅多条时有效）
  items:
    - content: "{{iif(is_state('device_tracker.spp_39', 'not_home'), '不在家', '在家')}}"
    - entity: sensor.keting_wendu        # 显示：状态值 + unit_of_measurement
    - content: "{{now().hour}}时{{now().minute}}分"
```

#### 自动滚动模式

当 `scroll: true` 时，多条内容会自动逐条向上滚动，每条停顿后继续无缝循环。可通过 `stay_time` 和 `scroll_duration` 精细控制停留和滚动速度。

```yaml
notice:
  style:
    - width: 100%
    - height: 30px                      # 滚动模式下建议设固定高度
  stay_time: 5000                       # 每条停留 5 秒（默认 3000ms）
  scroll_duration: 1200                 # 滚动到下一条耗时 1.2 秒（默认 800ms）
  scroll: true
  items:
    - content: "{{iif(is_state('device_tracker.spp_39', 'not_home'), '不在家', '在家')}}"
    - content: "{{iif(is_state('device_tracker.15pro', 'not_home'), '不在家', '在家')}}"
    - entity: sensor.keting_wendu
```

> **注意**：`scroll: true` 时需要设置 `style.height`（默认 35px），否则内容不会溢出也就不会滚动。

#### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `style` | `array` | 无 | 自定义样式，格式同卡片 `style`，支持 `width`、`height`、`background` 等 CSS 属性 |
| `stay_time` | `number` | 3000 | 每条公告停留时间，单位**毫秒**。仅 `scroll: true` 时生效 |
| `scroll_duration` | `number` | 800 | 从当前条滚动到下一条的耗时，单位**毫秒**。仅 `scroll: true` 时生效 |
| `scroll` | `boolean` | `false` | 是否自动滚动。`true` 时多条内容逐条向上滚动，无缝循环 |
| `items` | `array` | `[]` | **必填**，公告内容数组，每项为 `content` 或 `entity` |
| `tap_action` | `object` | 无 | 统一点击动作。该动作对所有未设置逐条 `tap_action` 的 item 生效。优先级低于 `items[].tap_action`（详见下方"点击动作"） |

#### items 配置

| 类型 | 参数 | 说明 |
|---|---|---|
| 模板文本 | `content: "模板字符串"` | 使用 Jinja2 模板语法，支持所有 `_TemplateEngine` 内置函数 |
| 实体状态 | `entity: entity_id` | 读取实体当前状态值，自动拼接 `unit_of_measurement` |
| 后端渲染 | `server_explain: true` | 搭配 `content` 使用，将模板发送到 HA 后端渲染（仅限 `expand()` 等 HA 独有函数，详见第十七节） |
| 点击动作 | `tap_action` | `object` | 可选，点击该条公告时触发的动作。未设置时点击无反应。详见下方"点击动作" |

#### 点击动作（tap_action）

公告栏支持点击动作，点击每条公告时触发指定的操作（如弹窗、跳转、调用服务等）。支持**两个层级**的配置：

- **逐条定义**：在 `items[].tap_action` 中单独设置，只对该条生效
- **统一定义**：在 `notice.tap_action` 中统一设置，对所有未设置逐条动作的 item 生效

**优先级**：`items[].tap_action` > `notice.tap_action` > 无动作（点击无效）

动作配置格式同卡片其他元素的 `tap_action`，支持以下类型：

| 动作 | 说明 |
|------|------|
| `more-info` | 弹出实体更多信息弹窗 |
| `navigate` | 页面导航跳转 |
| `call-service` | 调用 HA 服务 |
| `toggle` | 切换实体状态 |
| `none` | 无操作 |

> **提示**：最常用的场景是通过 `call-service` 调用 `modern_room_card.show_free_layout_popup` 实现点击公告弹出自定义卡片。

##### 逐条定义

每条公告独立配置点击动作：

```yaml
notice:
  style:
    - width: 100%
    - height: 25px
  scroll: true
  items:
    - content: "电费余额：…"
      server_explain: true
      tap_action:
        action: call-service
        service: modern_room_card.show_free_layout_popup
        service_data:
          title: 机柜
          width: 400px
          popup_position: clone_button_down
          cards: …
    - content: "天然气余额：…"
      server_explain: true
      # 该条未设置 tap_action，点击无反应
```

##### 统一定义

所有公告共享同一个点击动作：

```yaml
notice:
  style:
    - width: 100%
    - height: 25px
  scroll: true
  tap_action:
    action: call-service
    service: modern_room_card.show_free_layout_popup
    service_data:
      title: 机柜
      width: 400px
      popup_position: clone_button_down
      cards: …
  items:
    - content: "电费余额：…"
      server_explain: true
    - content: "天然气余额：…"
      server_explain: true
```

##### 混用

部分条目用自己的动作，其余使用统一动作：

```yaml
notice:
  tap_action:                              # 统一动作（fallback）
    action: navigate
    navigation_path: /lovelace/dashboard
  items:
    - content: "电费余额：…"
      tap_action:                          # 该条用自己的动作
        action: call-service
        service: modern_room_card.show_free_layout_popup
        service_data:
          title: 电费详情
          cards: …
    - content: "天然气余额：…"
      # 该条使用统一的 navigate 动作
```

#### 内联样式支持（HTML）

`content` 内容支持标准的 `<span style="...">` 标签实现内联样式渲染，适用于需要高亮显示部分信息的场景（如余额数字标色）。

- 只放行 `<span style="...">` 标签，其他 HTML 标签自动剥离
- 支持**嵌套** `<span>`
- 支持**所有 CSS 属性**：`color`、`background`、`font-weight`、`font-size`、`border` 等
- 事件属性（`onclick`、`onerror` 等）自动过滤，安全无 XSS 风险
- `server_explain: true` 模式下也同样支持

```yaml
notice:
  style:
    - width: 100%
    - height: 25px
  scroll: true
  items:
    - content: >-
        {% set sensor = 'sensor.tian_ran_qi_2_new_2' %}
        {% set balance = states(sensor) | float(0) %}
        {% set daylist = state_attr(sensor, 'daylist') %}
        天然气余额：<span style="background: #006e54; color:#fdeff2">{{ balance }} 元</span>，
        {%- if daylist and daylist | length > 0 %}
          {%- set e_gas_list = daylist | map(attribute='e_gas') | map('float') | list %}
          {%- set avg_e_gas = e_gas_list | sum / e_gas_list | length %}
          {%- set days_left = (balance / avg_e_gas) | round(0) if avg_e_gas > 0 else 0 %}
          可用 {{ days_left }} 天，每天用气 {{ avg_e_gas | round(2) }} 方
        {%- else %}
          暂无历史数据无法预测
        {%- endif %}
      server_explain: true
```

嵌套示例：

```yaml
- content: >-
    <span style="color: red">警告：<span style="font-weight: bold; font-size: 14px">温度过高</span></span>，
    当前 {{ states('sensor.temp') }}℃
```

> **注意**：标签内必须使用标准 CSS 语法，属性间用 `;` 分隔。支持的颜色格式：`red`/`#rrggbb`/`rgb(r,g,b)` 等 CSS 标准格式。

#### 模板函数参考

公告栏 `content` 中可使用以下模板函数（由 `_TemplateEngine` 提供）：

| 函数 | 用法 | 说明 |
|---|---|---|
| `states()` | `{{states('sensor.temp')}}` | 读取实体状态值 |
| `state_attr()` | `{{state_attr('weather.x', 'forecast.0.temperature')}}` | 读取实体属性，支持点号路径导航和数组索引 |
| `is_state()` | `{{is_state('light.x', 'on')}}` | 判断实体状态是否为指定值，返回 `true`/`false` |
| `state_default()` | `{{state_default('sensor.x', '离线')}}` | 读取实体状态，`unavailable`/`unknown` 时返回默认值 |
| `float()` | `{{float(states('sensor.x'), 0)}}` | 转换为浮点数，可指定默认值 |
| `int()` | `{{int(states('sensor.x'), 0)}}` | 转换为整数，可指定默认值 |
| `iif()` | `{{iif(is_state('light.x', 'on'), '开启', '关闭')}}` | 内联条件表达式 |
| `now()` | `{{now().hour}}:{{now().minute}}` | 当前时间属性：`year`/`month`/`day`/`hour`/`minute`/`second`/`weekday` |

也支持 `{% set %}`、`{% if %}/{% else %}/{% endif %}` 等控制语法。

#### 嵌套属性读取

`state_attr()` 支持点号路径导航和数组索引，例如：

```yaml
# 读取天气实体的预报数组第一项的温度
- content: "{{state_attr('weather.sha_yu_lei_de_jia', 'forecast.0.temperature')}}℃"

# 读取嵌套属性
- content: "{{state_attr('sensor.x', 'data.0.name')}}"
```

---

## 十二、主题设置

内置 5 种预设主题，也可以根据时间或实体状态自动切换。

### 固定主题

```yaml
theme: light           # 亮色（白色背景，深色文字）
theme: dark            # 暗色（深灰背景，白色文字）
theme: black           # 纯黑（纯黑背景，白色文字）
theme: darkgray        # 深灰（深灰背景，白色文字）
theme: transparent     # 半透明（适合放在背景图片上）
```

### 自动切换主题

```yaml
theme: time            # 根据时间自动切换（6-18点亮色，其余暗色）
theme: phone           # 跟随手机系统主题
theme: device          # 同 phone
theme: off             # 始终为暗色
theme: on              # 始终为亮色
```

### 通过实体控制主题

```yaml
theme: input_boolean.night_mode    # on=亮色，off=暗色
theme: select.theme_switch         # 下拉选择实体，选项可以是主题名称
```

### 自定义暗/亮主题对

```yaml
dark_light_theme: 'black,light'    # 格式：暗色主题,亮色主题
```

## 十三、其他配置

### 心跳包（检测app/网页是否在前台运行）

心跳包功能主要用于检测app/网页是否在前台运行，也可配合自动化实现外网 API 网关的安全管理。

**基本配置：**

```yaml
heartbeat_packet:
  entity: input_number.api_gateway_heartbeat_counter  # 心跳计数器（数字型实体）
  interval: 10                                        # 多少秒写入一次（建议10-60秒）
  whether_send: input_boolean.api_gateway_man_close   # 手动开关控制是否发送（on=发送）
  show_breathe: true                                  # 在房间名称旁边显示一个呼吸点
```

> 心跳值为递增整数（1, 2, 3...），可以在 HA 中创建一个 `input_number` 或 `sensor` 实体来接收。
> 当配置了 `heartbeat_packet` 时，在 room-name 后面显示一个小绿色呼吸点。写入失败时显示红色呼吸，成功时绿色呼吸。

#### 外网 API 网关安全推荐

外网环境使用 `api_base_url` 调用 API 接口时，**强烈建议**搭配心跳包实现自动网关控制：

- **APP 打开时**：心跳持续发送 → API 接口自动开放
- **APP 关闭/后台**：心跳停止超过 20s → API 接口自动关闭
- **手动优先**：`input_boolean.api_gateway_man_close` 开关拥有最高权限，可手动强制关闭 API 接口

以下是一个完整的自动化示例，实现了瞬时联动、心跳维持和异常兜底的闭环控制：

```yaml
alias: 0-安全网关：综合逻辑闭环控制 (V8-瞬时同步)
description: >
  【逻辑摘要】 1. 瞬时联动：手动开关拨到 ON 立即开网关，拨到 OFF 立即关网关并清零。
  2. 心跳维持：在 ON 状态下，持续的心跳包会重置 20s 关闭倒计时。
  3. 异常兜底：若手动为 ON 但长久无心跳，则自动关闭网关并清零。
triggers:
  - entity_id: input_number.api_gateway_heartbeat_counter
    trigger: state
  - entity_id: input_boolean.api_gateway_man_close
    trigger: state
actions:
  - choose:
      - alias: 手动关闭逻辑
        conditions:
          - condition: state
            entity_id: input_boolean.api_gateway_man_close
            state: "off"
        sequence:
          - target:
              entity_id: switch.ha_data_store_api_access
            action: switch.turn_off
          - if:
              - condition: template
                value_template: >-
                  {{ states('input_number.api_gateway_heartbeat_counter') |
                  float > 0 }}
            then:
              - target:
                  entity_id: input_number.api_gateway_heartbeat_counter
                data:
                  value: 0
                action: input_number.set_value
      - alias: 手动开启与心跳监控逻辑
        conditions:
          - condition: state
            entity_id: input_boolean.api_gateway_man_close
            state: "on"
        sequence:
          - target:
              entity_id: switch.ha_data_store_api_access
            action: switch.turn_on
          - wait_for_trigger:
              - entity_id: input_number.api_gateway_heartbeat_counter
                trigger: state
            timeout: "00:00:20"
            continue_on_timeout: true
          - if:
              - condition: template
                value_template: "{{ wait.trigger == none }}"
            then:
              - target:
                  entity_id: switch.ha_data_store_api_access
                action: switch.turn_off
              - wait_for_trigger:
                  - entity_id: switch.ha_data_store_api_access
                    to: "off"
                    trigger: state
                timeout: "00:00:05"
              - if:
                  - condition: state
                    entity_id: switch.ha_data_store_api_access
                    state: "off"
                then:
                  - target:
                      entity_id: input_number.api_gateway_heartbeat_counter
                    data:
                      value: 0
                    action: input_number.set_value
mode: restart
```

### 性能模式（performance_mode）

控制卡片的渲染性能策略，适用于不同性能的设备。

```yaml
performance_mode: auto              # 自动检测（默认）
performance_mode: desktop           # 强制桌面模式（全性能）
performance_mode: mobile            # 强制移动模式（低性能优化）
```

| 模式 | 说明 |
|------|------|
| `auto` | 自动检测设备类型。桌面设备全性能渲染，移动设备自动启用低性能优化 |
| `desktop` | 强制桌面模式，所有动画和渲染效果全部启用 |
| `mobile` | 强制移动模式，减少动画帧数、禁用部分重渲染、优化滚动性能 |

### 禁止首页滚动

有时候卡片弹窗关闭后，页面仍然不能滚动——用这个配置可以强制锁定：

```yaml
prohibit_homepage_scroll: true                              # 始终锁定页面滚动
prohibit_homepage_scroll: input_boolean.lock_scroll         # 用实体控制（on=锁定）
```

---

## 十四、Head 模式网格布局

在 `head: true` 模式下，按钮按网格排列。可以用 `row_column` 控制每个按钮占多大地方。

```yaml
head: true
head_columns: 6                       # 网格列数，默认6列

buttons:
  - type: lights
    card:
      - entity: light.living_ceiling
    row_column: '1,2-3'               # 序号1，占2行3列
  - type: ac
    card:
      - entity: climate.living
    row_column: '2,1-2'               # 序号2，占1行2列
  - type: media
    entity: media_player.tv
    row_column: '3,1-4'               # 序号3，占1行4列
  - entity: switch.plug               # 没有 row_column 会自动排列
```

> 序号只决定排列顺序，不决定最终位置。系统会自动检测碰撞，优化布局。

---

## 十四-A、弹窗内卡片跨行跨列布局（row_column）

自由布局弹窗（`show_free_layout_popup` / `popup_card`）的 row 分组中，items 默认用 `per_line` 控制每行显示几个卡片。现在可以通过 `row_column` 让单个 item 跨行跨列，实现更灵活的布局。

### row_column 格式

和 head 模式一致：`'序号,行数-列数'`

| 示例 | 含义 |
|------|------|
| `'1,2-2'` | 序号1，占2行2列 |
| `'2,1-1'` | 序号2，占1行1列 |
| `'3,1-2'` | 序号3，占1行2列（跨2列） |

### 基础示例

```yaml
cards:
  - row: 1
    per_line: 4                        # 该组共4列
    title: 用电量
    items:
      - entity: sensor.bingxiang_day
        type: sensor
        layout: mini
        name: 日用电
        row_column: '1,2-2'           # 序号1，占2行2列
      - type: sensor
        entity: sensor.bingxiang_month
        layout: mini
        name: 月用电
        row_column: '2,1-1'           # 序号2，占1行1列
      - type: sensor
        entity: sensor.bingxiang_year
        layout: mini
        name: 年用电
        row_column: '3,1-1'           # 序号3，占1行1列
```

渲染效果（4列网格）：

```
┌──────────────┬──────────────┬──────┬──────┐
│              │              │ 月用电│ 年用电│ ← 第1行
│   日用电      │   日用电     ├──────┼──────┤
│  (2行2列)     │  (2行2列)    │      │      │ ← 第2行
│              │              │ 空   │ 空   │
└──────────────┴──────────────┴──────┴──────┘
```

#### 头部多屏模式（多页滑动）

当 `head: true` 且按钮数量超过一页时，可以通过 `buttons_2`、`buttons_3`…… 等配置将按钮分到多个页面，**左右滑动即可切换页面**（跟手拖动 + 松手吸附；底部圆点指示当前页，拖动越过半屏时高亮就跟手过去）。桌面端也可以直接把**纵向滚轮**转成翻页。机制与其它选项卡完全一致，见「八-A、左右滑动」。

```yaml
head: true
head_columns: 6               # 第1页列数
head_columns_2: 4             # 第2页列数（可选，默认继承 head_columns）

buttons:                      # 第1页按钮
  - type: lights
    card:
      - entity: light.living_ceiling
  - type: ac
    card:
      - entity: climate.living

buttons_2:                    # 第2页按钮
  - type: curtain
    entity: cover.living_curtain
  - type: media
    entity: media_player.tv
    row_column: '1,1-3'       # 第2页也支持 row_column
```

**配置说明：**

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `buttons` | `array` | 必填 | 第1页按钮列表 |
| `buttons_2` | `array` | 无 | 第2页按钮列表 |
| `buttons_3` | `array` | 无 | 第3页按钮列表（支持无限多页） |
| `head_columns` | `number` | `6` | 第1页网格列数 |
| `head_columns_2` | `number` | 同 `head_columns` | 第2页独立列数 |

**多屏模式特性：**

| 特性 | 说明 |
|------|------|
| **滑动切换** | 横向整屏滑动，滚动捕捉（scroll-snap），支持触屏拖拽和鼠标滚轮 |
| **底部指示器** | 圆点显示当前页位置，点击圆点可直接跳转到对应页 |
| **每页独立列数** | 通过 `head_columns_N` 为每页设置不同网格列数 |
| **按钮排列** | 每页按钮独立排列，`row_column` 分别生效 |
| **概览栏/公告栏** | 仅在首页（Page 0）显示，切换页面时随首页一起滑动消失 |
| **页内按钮更新** | 实时状态更新覆盖所有页面，翻页后按钮状态已是最新 |

**完整示例：两页布局**

```yaml
head: true
head_columns: 6
head_columns_2: 3              # 第二页用大按钮，3列布局

buttons:
  - type: lights
    card:
      - entity: light.living_room
        name: 客厅灯
    row_column: '1,2-3'
  - type: ac
    entity: climate.living
    row_column: '2,2-3'
  - type: curtain
    entity: cover.bedroom_curtain
    row_column: '3,2-3'
  - type: media
    entity: media_player.tv
    row_column: '4,1-3'
  - type: scene_mode
    name: 全关
    scenes:
      - name: 全关
        actions:
          - entities:
              全屋灯: light.living_room
            value: "off"
    row_column: '5,1-3'

buttons_2:                     # 第二页：设备详情
  - type: sensor
    name: 温湿度
    entity: sensor.temperature
    row_column: '1,2-2'
  - type: sensor
    name: 湿度
    entity: sensor.humidity
    row_column: '1,3-3'
  - type: dynamic_icon
    name: 空气质量
    entity: sensor.air_quality
    icon: mdi:air-filter
    row_column: '2,1-3'
```

### 完整配置示例（冰箱弹窗）

```yaml
tap_action:
  action: call-service
  service: modern_room_card.show_free_layout_popup
  service_data:
    title: 冰箱
    width: 360px
    cards:
      - row: 1
        per_line: 2                    # 2列网格
        title: 综合面板
        items:
          - type: picture
            row_column: '1,2-1'       # 序号1，占2行1列（左边大图）
            show_button_background: false
            bg_image: /local/house/冰箱.png

          - type: timeline
            row_column: '2,1-1'       # 序号2，占1行1列（右上）
            entity: switch.giot_cn_1124641761_v6shsm_on_p_2_1
            name: 冰箱运行情况

          - type: sensor
            row_column: '3,1-1'       # 序号3，占1行1列（右下）
            entity: sensor.bingxiang_day
            layout: mini
            name: 日用电

      - row: 2
        per_line: 3                    # 不用 row_column，走原有 per_line 模式
        title: 用电统计
        items:
          - entity: sensor.bingxiang_day
            type: sensor
            layout: mini
            name: 日用电
          - type: sensor
            entity: sensor.bingxiang_month
            layout: mini
            name: 月用电
          - type: sensor
            entity: sensor.bingxiang_year
            layout: mini
            name: 年用电
```

渲染效果：

```
┌──────────────┬──────────────┐
│              │ 冰箱运行情况   │ ← 第1行
│   冰箱图片    ├──────────────┤
│  (2行1列)     │  日用电       │ ← 第2行
├──────┬───────┴──────────────┤
│ 日用电 │ 月用电  │ 年用电     │ ← 第3行 (per_line:3)
└──────┴──────────────────────┘
```

### 兼容规则

| 情况 | 行为 |
|------|------|
| 所有 item 都没有 `row_column` | 原有 `per_line` 模式，完全不变 |
| 有任意 item 配了 `row_column` | 该 row 组切换为 CSS Grid 跨行跨列模式 |
| 部分 item 有 `row_column`，部分没有 | 没有 `row_column` 的 item 按1×1自动排列 |

> `row_column` 只影响同一个 row 组内的布局。不同 row 组之间仍然是上下堆叠关系。

### 标题实体值（title_entities）

在弹窗 row 分组的标题右侧，可以显示一组实体状态值或控制按钮，支持 Way 计算引擎和点击动作。

`title_entities` 支持三种模式：

1. **传感器模式**（`entity` + `way`）— 显示实体状态值，适合展示传感器数据
2. **控制按钮模式**（`entities` + `tap_action`）— 显示为可点击按钮，适合快捷控制
3. **快捷操作模式**（`type: action`）— 显示为可点击按钮，点击弹出情景模式气泡

#### 传感器模式示例

```yaml
cards:
  - row: 1
    per_line: 1
    title: 电饭锅运行时刻
    title_entities:
      - entity: switch.dian_fan_guo
        icon: mdi:stove
        name: 今日使用次数
        show_name: false
        way: today_usage_count
        format: '今天用了{_default}次'
      - entity: switch.dian_fan_guo
        icon: mdi:clock-outline
        name: 使用时长
        way: today_usage_time
        tap_action:
          action: more-info
```

#### 控制按钮模式示例

```yaml
cards:
  - row: 2
    per_line: 1
    title: 热水器运行时刻
    title_entities:
      # 多实体 toggle：一键切换多个灯
      - entities:
          - light.keting_dadeng
          - light.keting_xuanguan
        name: 灯光
        icon: mdi:lightbulb-group
        tap_action:
          action: toggle

      # 多实体 set_value：一键关闭多个灯
      - entities:
          - light.keting_dadeng
          - light.keting_xuanguan
        name: 关灯
        tap_action:
          action: set_value
          value: "off"

      # 单实体 set_value + service_data：设置空调温度
      - entity: climate.xiaomi_m6_00c5_air_conditioner
        name: 空调26°C
        tap_action:
          action: set_value
          value: "on"
          service_data:
            temperature: "26"
            fan_mode: level6

      # 传感器 + way：显示统计数据（原有模式）
      - entity: switch.reshuiqi
        icon: mdi:water-boiler
        way: today_usage_count
        format: '今天用了{_default}次'
```

#### 快捷操作模式示例

```yaml
cards:
  - row: 1
    per_line: 1
    title: 客厅控制
    title_entities:
      # 快捷操作：点击弹出情景模式气泡
      - type: action
        name: 情景
        icon: mdi:palette
        scenes:
          - name: 回家模式
            actions:
              - entity: light.living_room
                value: "on"
          - name: 离家模式
            actions:
              - entities:
                  客厅灯: light.keting_dadeng
                  卧室灯: light.bedroom
                value: "off"
```

#### title_entities 每项字段说明

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `type` | ❌ | `string` | 模式类型：`action` 表示快捷操作模式（需配合 `scenes`） |
| `entity` | ❌* | `string` | 单实体 ID（传感器模式必填，与 `entities` 二选一） |
| `entities` | ❌* | `array` | 多实体 ID 数组（控制按钮模式，与 `entity` 二选一） |
| `scenes` | ❌* | `array` | 情景列表（快捷操作模式必填，格式与 6.17 节一致） |
| `icon` | ❌ | `string` | 图标（如 `mdi:stove`） |
| `name` | ❌ | `string` | 显示名称（控制按钮模式下建议必填，否则只显示图标） |
| `show_name` | ❌ | `boolean` | 是否显示名称，默认 `true` |
| `way` | ❌ | `string` | Way 计算方式（见第十六节），仅传感器模式有效，不配则直接显示实体状态值 |
| `format` | ❌ | `string` | Way 格式化模板（仅 `way` 存在时有效） |
| `unit` | ❌ | `string` | 自定义单位（仅 `way` 存在时有效，覆盖实体自带单位） |
| `tap_action` | ❌ | `object` | 点击动作（见下方说明） |

> **统计明细气泡**：传感器模式（`entity` + `way`）下，点击标题右侧的**值文本**会自动弹出"统计明细"气泡（统一气泡 + 径向模糊遮罩）。气泡顶部按该实体配置的每个 `way` 显示统计块；下方明细按配置自动展示：「今日使用记录」（含 `today_*`、`on_duration` 等）、「昨日使用记录」（含 `yesterday_*`）为逐段文本（起止时间 + 时长，进行中标注"运行中"）；「近期使用记录·近30天」（含 `last_usage_time`）为 **ECharts 柱状图**——柱高 = 每日累计使用时长（小时），工具提示显示当日次数与时长，图上方汇总 30 天总次数与总时长。柱状图数据来自**卡片顶层** `api_base_url`/`key` 配置（接口 `query?type=device_history&start=..&end=..`）；未配置 API 或请求失败时该区块仅显示空态提示，不回退文本列表。无需额外开关配置。

> *`entity` 和 `entities` 至少配置一个。控制按钮模式（`entities` + `set_value`）下，`name` 或 `icon` 至少配置一个，否则按钮无法显示。

#### title_entities 的 tap_action

`tap_action` 支持以下 action 类型：

| action | 说明 | 示例 |
|--------|------|------|
| `toggle` | 切换开关状态，支持 `entities` 多实体批量 | `action: toggle` |
| `set_value` | 设置目标值，自动推断服务（桥接情景模式引擎），支持 `entities` 多实体 | `action: set_value` + `value: "off"` |
| `quick-action` | 快捷操作，弹出情景模式气泡执行多步骤操作 | `action: quick-action` + `scenes: [...]` 或 `actions: [...]` |
| `more-info` | 弹出 HA 详细信息弹窗 | `action: more-info` |
| `navigate` | 页面导航 | `action: navigate` + `navigation_path: /xxx` |
| `call-service` | 调用 HA 服务 | `action: call-service` + `service: xxx` |
| `popup_card` | 弹出自定义卡片 | `action: popup_card` + `card: [...]` |
| `card` | 弹出设备内置控制弹窗 | `action: card` + `card: { type: curtain, ... }` |
| `none` | 不执行任何操作 | `action: none` |

**`set_value` 详细说明：**

`set_value` 动作会根据实体域（`light.`、`climate.` 等）自动推断应调用的 HA 服务，与情景模式（6.17 节）共享同一套服务推断引擎。无需手动指定服务名，只需提供目标 `value` 即可：

```yaml
# 灯光：value "on" → light.turn_on，value "off" → light.turn_off
tap_action:
  action: set_value
  value: "on"
  service_data:            # 可选附加参数
    brightness: 200
    kelvin: 4000

# 空调：数值 → climate.set_temperature
tap_action:
  action: set_value
  value: "26"
  service_data:
    fan_mode: level6

# 空调：模式 → climate.set_hvac_mode
tap_action:
  action: set_value
  value: cool

# 选择器：任意值 → select.select_option
tap_action:
  action: set_value
  value: "制冷"
```

> 完整的"实体类型与服务自动推断"对照表见 6.16 节。

> **弹窗顶层标题**也支持 `title_entities`（配置在 `service_data.title_entities` 中），功能与 row 级别一致。

### 弹窗内支持的卡片类型

在自由布局弹窗（`show_free_layout_popup` / `popup_card`）的 `rows[].items` 中，支持以下卡片类型。每个 item 通过 `type` 字段指定类型。

| 类型 | 说明 | 主要配置项 |
|------|------|-----------|
| `sensor` | 显示传感器数值 | `entity`、`name`、`layout: mini/full`、`unit`、`icon` |
| `switch` | 开关控制 | `entity`、`name`、`icon` |
| `toggle` | 开关切换按钮 | `entity`、`on_icon`、`off_icon`、`on_color`、`off_color` |
| `button` | 按压按钮 | `entity`、`name`、`icon`、`show_duration`、`confirm` |
| `light` | 单灯控制（亮度/色温） | `entity`、`name` |
| `cover` | 窗帘/遮盖控制 | `entity`、`name` |
| `curtain` | 窗帘详细控制面板 | `entity`、`fabric_entity`、`sheer_entity` |
| `select` | 下拉选择器 | `entity`、`name` |
| `number` | 数值输入 | `entity`、`min`、`max`、`step` |
| `text` | 文本显示 | `entity`、`name` |
| `slider` | 滑块控制 | `entity`、`min`、`max`、`step` |
| `radio` | 单选按钮组 | `entity`、`options` |
| `timeline` | 时间轴（当天状态变化） | `entity`、`map_table`、`api_base_url` |
| `picture` | 图片展示（详见下方） | `bg_image`、`halo_entity`、`bg_image_position` |
| `html` | 自定义 HTML | `content` |
| `ac` | 空调控制面板 | `entity` |
| `clothes_dryer` | 晾衣架控制面板 | `entity`、`light_entity` |
| `nas` | NAS 服务器状态卡片 | `power_switch`、`storage_summary`、`array_01`、`array_02` |
| `user` | 用户信息卡片 | `persons` |
| `button_group` | 按钮组（选项卡样式聚合小按钮） | `buttons`、`direction`、`on_color`、`off_color`、`show_name` |
| `action` | 快捷操作（点击弹出情景模式气泡） | `name`、`icon`、`scenes`、`scene_mode` |
| `water_temp` | 水温可视化卡片 | `entity`、`min_temp`、`max_temp`、`width`、`height` |
| `printer` | 打印机用量统计卡片（日历热力图 / 墨盒详情 / 用墨占比环形图） | `entity`、`name`、`colors`、`api_base_url`、`key`、`today_print` |
| `fnos` | 飞牛 fnOS 全实体卡片（主机 / 存储 / Docker / 虚拟机 / 应用） | `entity`、`name`、`icon`、`accent`、`popup_width`、`popup_position`、`confirm_power` |
| `daily_report` | 今日家庭日报卡片 | `entity`、`refresh`、`hide_room`、`env_from_config_id`、`width` |
| `esxi` | ESXi 虚拟化卡片（主机状态 / 虚拟机批量操作 / 屏幕墙三选项卡） | `entity`、`hosts`、`vms`、`exclude`、`default_vm`、`show_screen`、`show_refresh`、`show_sync`、`confirm_power_off`、`width` |
| `bill` | 个人账单卡片（概览 / 分析 / 日历 / 查询 / 历史五选项卡） | `api_base_url`、`key`、`name`、`icon`、`subtitle`、`accent`、`page_size`、`recent_days`、`source`、`direction` |
| `dingdong` | 叮咚门铃卡片（抓拍 / 实时画面 + 按天回看时间轴 + 设置 + 诊断四选项卡） | `entity`、`name`、`date`、`show_live`、`events_limit`、`shots_limit`、`videos_limit`、`hero_ratio`、`hero_max_height`（见 6.47） |

#### radio 卡片（单选按钮组）

用于从一组预定义选项中单选一个值，适合切换模式、场景选择等场景。选项以按钮组形式展示，选中项以淡蓝色高亮。

```yaml
items:
  - type: radio
    entity: input_select.icon_animation_mode
    name: 动画设置
    compact: true                        # 可选：紧凑模式，隐藏标题栏
    map_table:
      "on":
        shake:
          text: 晃动
          icon: mdi:animation
          color: "#16160e"
        rotate:
          text: 旋转
          icon: mdi:reload
          color: "#16160e"
```

**配置项说明：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `entity` | ✅ | `string` | - | 实体 ID（`input_select` / `select` 等） |
| `name` | ❌ | `string` | 实体 friendly_name | 卡片标题 |
| `compact` | ❌ | `boolean` | `false` | 紧凑模式：隐藏标题栏和当前值显示，缩小选项间距和字号 |
| `per_row` | ❌ | `number` | - | 每行显示的选项数（1~6），设置后使用 CSS Grid 严格分行排列；不设置则保持自动换行 |
| `map_table` | ✅ | `object` | - | 选项映射表，定义每个选项的图标/文本/颜色（支持 `on`/`off` 分组格式） |
| `update_interval` | ❌ | `number` | `0` | 单独刷新间隔（秒），覆盖弹窗级别的刷新间隔 |
| `confirm` | ❌ | `boolean` | `false` | 切换前是否需要确认弹窗 |

> `map_table` 支持两种格式：
> 1. `{ "值1": {...}, "值2": {...} }` — 直接映射
> 2. `{ "on": { "值1": {...} }, "off": { "值2": {...} } }` — 按主状态分组

用于在弹窗中显示设备图片，支持背景图片、光晕效果和位置调整。

```yaml
items:
  - type: picture
    bg_image: /local/house/冰箱.png          # 背景图片路径
    bg_image_position: [0, 0, 0.8, 0]       # 图片位置微调 [left, top, right, bottom]
    show_button_background: false            # 是否显示按钮背景
    halo_entity: switch.bingxiang            # 光晕控制实体，on 状态时显示光晕
```

**配置项说明：**

| 配置项 | 必填 | 类型 | 说明 |
|--------|:----:|------|------|
| `bg_image` | ❌ | `string` | 背景图片 URL（支持 `/local/xxx.png` 等相对路径） |
| `bg_image_position` | ❌ | `array` | 图片位置微调，4 个浮点值 `[left, top, right, bottom]`，控制图片的 `object-position` |
| `show_button_background` | ❌ | `boolean` | 是否显示按钮卡片的灰色背景，默认 `true`，设为 `false` 时仅显示图片 |
| `halo_entity` | ❌ | `string` | 控制光晕效果的实体 ID。实体为 on 时图片下方显示暖色光晕 |

> `halo_entity` 通常配置为对应设备的开关实体，设备开启时图片显示光晕效果，提供直观的视觉反馈。

---

## 十五、自定义样式

### 方式一：卡片整体样式

```yaml
style:
  width: 350px                         # 卡片宽度
  height: auto                         # 卡片高度
  background: 'linear-gradient(135deg, #667eea, #764ba2)'  # 渐变背景
  border-radius: 24px                  # 圆角
  backdrop-filter: blur(20px)          # 背景模糊
  box-shadow: 0 8px 32px rgba(0,0,0,0.2)  # 阴影
```

### 方式二：按选择器覆盖内部元素（高级）

```yaml
style:
  - selector: '.room-card .grouped-btn'    # CSS选择器
    background: 'rgba(255,255,255,0.1)'
    border-radius: 16px
    box-shadow: 0 4px 12px rgba(0,0,0,0.1)
  - class: 'primary-text'                  # 也可用class名
    font-size: 16px
    color: '#3498db'
    font-weight: 500
  - class: 'room-name'
    font-size: 14px
    color: '#7f8c8d'
```

> `selector` 和 `class` 二选一即可。`selector` 写完整 CSS 选择器，`class` 只需要写类名。

---

## 十六、Way 计算引擎

Way 引擎可以为实体计算各种统计数据（如"今天开了几次"、"今天一共开了多久"等）。

```yaml
buttons:
  - type: socket
    entity: switch.plug1
    way: today_usage_time              # 计算方式
    format: '今日已开启{_default}'     # 显示格式
```

> `way` 写的是"计算方式"，`format` 写的是"显示格式"。`{_default}` 是单实体模式下的默认实体别名，会被计算结果替换。

### format 占位符规则

format 模板中使用 `{键名}` 来引用计算结果，具体规则取决于实体数量和 way 数量：

| 场景 | 可用的占位符 | 示例 |
|------|------------|------|
| 单实体 + 单 way | `{_default}` 或 `{way名}` | `{today_usage_count}` |
| 单实体 + 多 way | 只能用 `{way名}` | `{today_usage_time}` + `{today_usage_count}` |
| 多实体 | 只能用 `{别名.way名}` | `{plug1.today_usage_time}` |

> **说明**：单实体模式下，实体别名为 `_default`。单 way 时两种写法等价；多 way 时 `{_default}` 无法区分不同 way 的结果，必须用 way 名引用。

### 所有可用的 way

#### 通用
| way 名称 | 说明 | 示例结果 |
|---------|------|---------|
| `state` | 取原始状态值 | `on` / `off` |
| `friendly_state` | 显示中文友好状态 | `开启` / `关闭` |
| `last_changed` | 距上次状态变化过了多久 | `2时15分前` |
| `last_updated` | 距上次更新过了多久 | `5分前` |
| `round` | 保留小数位数（通过 `decimals` 指定位数，默认1位） | `25.7` / `3.14` |

#### 开关型 - 今日统计
| way 名称 | 说明 | 示例结果 |
|---------|------|---------|
| `today_usage_count` | 今日开启次数 | `5` |
| `today_usage_time` | 今日累计开启时长 | `3时20分` |
| `today_on_count` | 同 today_usage_count | `5` |
| `today_off_count` | 今日关闭次数 | `3` |
| `on_duration` | 当前已持续开启时长 | `1时30分` |
| `off_duration` | 当前已持续关闭时长 | `30分` |
| `last_on_time` | 最后一次开启的时间 | `14:30` |
| `last_off_time` | 最后一次关闭的时间 | `09:15` |
| `first_on_time` | 今日首次开启时间 | `07:00` |

#### 开关型 - 昨日统计
| way 名称 | 说明 |
|---------|------|
| `yesterday_usage_count` | 昨日开启次数 |
| `yesterday_usage_time` | 昨日累计开启时长 |
| `yesterday_on_count` | 昨日开启次数 |
| `yesterday_off_count` | 昨日关闭次数 |

#### 开关型 - 最近一次使用
| way 名称 | 说明 | 示例结果 |
|---------|------|---------|
| `last_usage_time` | 最后一次使用时长（最近一次完整 on 会话的持续时长，回溯 30 天） | `35分` |

> **说明**：`last_usage_time` 在实体**当前正开启**时返回本次已运行时长并附加 `(运行中)`（如 `35分(运行中)`）；当前已关闭时统计最近一次"开启→关闭"的持续时长。若回溯 30 天内从未开启、或该段起点早于 30 天窗口（无法确定真实时长），返回 `--`。因运行中数值持续增长，该 way 属于时间依赖型（引擎自动 5 秒刷新）。

#### 数值型 - 今日统计
| way 名称 | 说明 | 示例结果 |
|---------|------|---------|
| `today_max` | 今日最大值 | `28.5°C` |
| `today_min` | 今日最小值 | `22.1°C` |
| `today_avg` | 今日平均值 | `25.3°C` |
| `today_sum` | 今日累计值 | `3.5kWh` |
| `today_range` | 今日波动幅度 | `6.4°C` |
| `today_max_time` | 最大值出现时间 | `14:30` |
| `today_min_time` | 最小值出现时间 | `06:00` |

#### 数值型 - 昨日统计
| way 名称 | 说明 |
|---------|------|
| `yesterday_max` | 昨日最大值 |
| `yesterday_min` | 昨日最小值 |
| `yesterday_avg` | 昨日平均值 |
| `yesterday_sum` | 昨日累计值 |
| `yesterday_max_time` | 昨日最大值时间 |
| `yesterday_min_time` | 昨日最小值时间 |

#### 趋势
| way 名称 | 说明 | 示例结果 |
|---------|------|---------|
| `trend` | 对比昨日同时段 | `↑2.5°C` 或 `↓1.0°C` 或 `持平` |

### round 用法示例

`round` 用于将传感器值保留指定小数位数，适合温度、湿度等存在多位小数的传感器。

```yaml
# 默认保留1位小数
buttons:
  - type: socket
    entity: sensor.temperature
    way: round
    unit: °C

# 指定保留2位小数
buttons:
  - type: socket
    entity: sensor.humidity
    way: round
    decimals: 2
    unit: '%'

# 不保留小数（取整）
buttons:
  - type: socket
    entity: sensor.power
    way: round
    decimals: 0
    unit: W
```

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `decimals` | `number` | `1` | 保留小数位数。`0` = 取整，`1` = 1位小数，`2` = 2位小数，以此类推 |

> `round` 仅对数字类型的实体状态生效，非数字值（如 `on`/`off`/`unavailable`）会原样返回。

### 多实体 + 多 way 示例

```yaml
buttons:
  - type: socket
    entities:                             # 方式一：用 entities 定义多个实体
      plug1: switch.plug1
      plug2: switch.plug2
    way:
      plug1: ['today_usage_time', 'today_usage_count']  # 给插头1两个way
      plug2: state                                      # 插头2取原始状态
    format: '插头1: {plug1.today_usage_time}(用了{plug1.today_usage_count}次) | 插头2: {plug2.state}'
    unit: ''                             # 单位
```

### 用 entity 的单个 way （单实体时）

```yaml
buttons:
  - type: socket
    entity: switch.plug1
    way: today_usage_count               # 今日使用次数
    format: '今天用了{_default}次'       # 显示格式（也可写 {today_usage_count}）
```

### 单实体 + 多 way

单实体配置多个 way 时，format 中必须用 way 名引用，不能用 `{_default}`：

```yaml
buttons:
  - type: socket
    entity: switch.plug1
    way: ['today_usage_time', 'today_usage_count']   # 同时计算时长和次数
    format: '今日开启{today_usage_time}，共{today_usage_count}次'
```

> 注意：单实体 + 单 way 时 `{_default}` 和 `{way名}` 都可以用；单实体 + 多 way 时只能用 `{way名}`；多实体时用 `{别名.way名}`。

### 单实体 + 多 way（含最近一次使用）+ 统计明细气泡

将次数、今日累计、最近一次使用合并到一行展示：

```yaml
buttons:
  - type: sensor
    entity: switch.kongqizhaguo
    icon: mdi:pot
    name: 今日使用
    show_name: false
    way:
      - today_usage_count
      - today_usage_time
      - last_usage_time
    format: '今天{today_usage_count}次 · 共{today_usage_time} · 上次{last_usage_time}'
```

> - `last_usage_time`：最后一次使用时长，详见上文「所有可用的 way」。
> - 当该行作为 **title_entities（标题实体值）** 展示时，点击右侧值文本会自动弹出**统计明细气泡**（径向模糊遮罩）：顶部按每个配置的 way 显示统计块；`today_*` 时下方展示今日逐段使用记录；配置了 `last_usage_time` 时展示「近30天使用柱状图」（数据来自卡片顶层 `api_base_url`/`key` 的外部 API）。

---

## 十七、前端 Jinja2 模板引擎

按钮的 `primary` 文本、`content` 字段等位置支持使用 **HA 兼容的 Jinja2 模板语法** 来动态渲染数据。所有模板均由前端引擎 `_TemplateEngine` 同步解析，**零网络延迟**。

```yaml
buttons:
  - type: lights
    card:
      - entity: light.living
        name: 客厅灯
    primary: '{{ states("light.living") }}'   # 显示灯的状态
```

> 🚀 **V4.0.6+ 增强**：前端引擎已从轻量子集升级为**完整 Jinja2 兼容引擎**，支持 `{% for %}`、过滤器链 `\| map \| list \| sum`、正则、`selectattr`、时间函数等绝大多数 HA 模板功能。复杂模板无需再走后端。

### 17.1 基础语法

**变量替换：**
```yaml
primary: '当前的温度是 {{ states("sensor.temp") }} 度'
primary: '家里的湿度是 {{ state_attr("sensor.humidity", "unit_of_measurement") }}'
```

**{% set %} 变量：**
```yaml
primary: |
  {% set power = states('sensor.power') | float %}
  {% set energy = states('sensor.energy') | float %}
  功率 {{ power }}W，今日用电 {{ energy }}kWh
```

**{% if %} 条件：**
```yaml
primary: |
  {% set temp = states('sensor.temp') | float %}
  {% if temp > 30 %}
    高温 🔥
  {% elif temp > 20 %}
    舒适 ✅
  {% else %}
    低温 ❄️
  {% endif %}
```

**内联三元：**
```yaml
primary: '{{ "开启" if states("light.living") == "on" else "关闭" }}'
```

**{% for %} 循环：**
```yaml
primary: |
  {% for item in daylist %}
    {{ item.e_gas }}元
  {% else %}
    无数据
  {% endfor %}
```

循环内可用变量：`loop.index`（1起始）、`loop.index0`（0起始）、`loop.first`、`loop.last`、`loop.length`。

### 17.2 内置函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `states(entity_id)` | 取实体状态值 | `{{ states('sensor.temp') }}` |
| `state_attr(entity_id, attr)` | 取实体属性（**保留原始类型**：数组/对象不会丢失） | `{{ state_attr('sensor.xxx', 'daylist') }}` |
| `is_state(entity_id, value)` | 判断实体状态 | `{{ is_state('light.living', 'on') }}` |
| `state_default(entity_id, default)` | 带默认值的状态取值 | `{{ state_default('sensor.xxx', '--') }}` |
| `float(val)` / `float(val, default)` | 转浮点数 | `{{ float(states('sensor.power'), 0) }}` |
| `int(val)` / `int(val, default)` | 转整数 | `{{ int(states('sensor.count'), 0) }}` |
| `iif(cond, true, false)` | 条件函数 | `{{ iif(temp > 30, '热', '凉') }}` |
| `now()` | 当前本地时间 | `{{ now().year }}-{{ now().month }}` |
| `utcnow()` | 当前 UTC 时间 | `{{ utcnow() }}` |
| `as_timestamp(dt)` | 时间转 unix 秒 | `{{ as_timestamp(now()) }}` |
| `as_datetime(ts)` | unix 秒转时间 | `{{ as_datetime(1700000000) }}` |
| `as_local(dt)` | UTC → 本地 | `{{ as_local(utcnow()) }}` |
| `relative_time(dt)` | 相对时间文本 | `{{ relative_time(sensor.last_changed) }} → "5分钟前"` |
| `today_at('08:30')` | 今日指定时刻 | `{{ today_at('08:00') }}` |
| `min(a, b, ...)` | 最小值 | `{{ min(t1, t2, t3) }}` |
| `max(a, b, ...)` | 最大值 | `{{ max(v1, v2) }}` |
| `is_number(val)` | 判断是否为数字 | `{{ is_number(states('sensor.xxx')) }}` |
| `contains(list, item)` | 是否包含 | `{{ contains(daylist, 'abc') }}` |
| `log(val, base)` | 对数 | `{{ log(100, 10) }}` |
| `sqrt(val)` | 平方根 | `{{ sqrt(144) }}` |

### 17.3 过滤器（管道操作符 `|`）

过滤器将前一个表达式的输出作为输入，链式处理：

```yaml
primary: '{{ states("sensor.power") | float(0) | round(1) }}W'
```

#### 类型转换

| 过滤器 | 说明 | 示例 |
|--------|------|------|
| `float(default)` | 转浮点数 | `states('sensor.x') \| float(0)` |
| `int(default)` | 转整数 | `states('sensor.x') \| int(0)` |
| `round(precision)` | 四舍五入 | `3.14159 \| round(2)` → `3.14` |
| `string` | 转字符串 | `value \| string` |
| `bool` | 转布尔值 | `value \| bool` |
| `list` | 确保为数组 | `value \| list` |

#### 字符串操作

| 过滤器 | 说明 | 示例 |
|--------|------|------|
| `lower` | 转小写 | `'Hello' \| lower` → `hello` |
| `upper` | 转大写 | `'Hello' \| upper` → `HELLO` |
| `trim` | 去除首尾空白 | `'  a  ' \| trim` → `a` |
| `replace(a, b)` | 替换全部 | `'a,b,c' \| replace(',', '/')` |
| `length` | 长度 | `[1,2,3] \| length` → `3` |

#### 数组操作

| 过滤器 | 说明 | 示例 |
|--------|------|------|
| `first` | 第一个元素 | `list \| first` |
| `last` | 最后一个元素 | `list \| last` |
| `sum` | 求和 | `[1,2,3] \| sum` → `6` |
| `join(sep)` | 合并为字符串 | `list \| join(', ')` |
| `map(attribute='prop')` | 提取属性 | `daylist \| map(attribute='e_gas')` |
| `map('float')` | 批量转浮点 | `list \| map('float')` |
| `map('int')` | 批量转整数 | `list \| map('int')` |
| `sort(attribute=X, reverse=true)` | 排序 | `list \| sort(attribute='name')` |
| `selectattr(attr, op, val)` | 按属性筛选 | `list \| selectattr('age', 'gt', 18)` |
| `rejectattr(attr, op, val)` | 按属性排除 | `list \| rejectattr('status', 'eq', 'off')` |
| `select(op, val)` | 按值选择 | `list \| select('gt', 10)` |
| `reject(op, val)` | 按值排除 | `list \| reject('eq', '')` |

支持的操作符：`eq` / `ne` / `lt` / `gt` / `le` / `ge` / `contains` / `startswith` / `endswith` / `truthy`

#### JSON & URL

| 过滤器 | 说明 | 示例 |
|--------|------|------|
| `to_json` | 转 JSON 字符串 | `obj \| to_json` |
| `from_json` | JSON 转对象 | `str \| from_json` |
| `urlencode` | URL 编码 | `'a=b' \| urlencode` → `a%3Db` |

#### 正则

| 过滤器 | 说明 | 示例 |
|--------|------|------|
| `regex_match(p, i?)` | 是否匹配（返回 bool） | `'abc' \| regex_match('^a')` |
| `regex_replace(p, r, i?)` | 正则替换全部 | `'a1b2' \| regex_replace('\\\d+', 'X')` |
| `regex_findall(p)` | 查找所有匹配 | `'a1b2' \| regex_findall('\\\d+')` → `['1','2']` |

> 第三个参数 `i` 可选，设为 `true` 时忽略大小写。

#### 时间戳

| 过滤器 | 说明 | 示例 |
|--------|------|------|
| `timestamp_custom(fmt, local?)` | 格式化时间戳 | `ts \| timestamp_custom('%Y-%m-%d')` |
| `timestamp_local` | 转本地时间字符串 | `ts \| timestamp_local` |

`%Y`=年 `%m`=月 `%d`=日 `%H`=时 `%M`=分 `%S`=秒 `%I`=12时制 `%p`=AM/PM

#### 默认值

| 过滤器 | 说明 | 示例 |
|--------|------|------|
| `default(val)` | 空值时返回默认值 | `value \| default('未知')` |

### 17.4 运算符

| 优先级 | 运算符 | 说明 |
|--------|--------|------|
| 1 | `()` `.` `[]` | 分组、属性访问、下标 |
| 2 | `\| filter(args)` | 管道过滤器 |
| 3 | `*` `/` | 乘除 |
| 4 | `+` `-` | 加减 |
| 5 | `<` `>` `<=` `>=` `==` `!=` | 比较（返回布尔） |
| 6 | `not` | 逻辑非 |
| 7 | `and` | 逻辑与 |
| 8 | `or` | 逻辑或 |
| 9 | `a if cond else b` | 三元条件 |

### 17.5 空白控制

使用 `{%-` 和 `-%}` 控制标签前后的空白：

```jinja2
{%- if daylist and daylist | length > 0 -%}
  {% for item in daylist %}
    {{ item.value }}
  {%- endfor %}
{%- else -%}
  无数据
{%- endif %}
```

`{%-` 删除标签前的空白（含换行），`-%}` 删除标签后的空白。

`{{-` 和 `-}}` 同理。

注释：`{# 注释内容 #}` 不会被渲染。

### 17.6 完整示例：天然气余额预测

以下模板**无需 `server_explain`**，前端引擎即可完整解析：

```yaml
buttons:
  - icon: mdi:fire
    primary: >-
      {% set sensor = 'sensor.tian_ran_qi_2_new_2' %}
      {% set balance = states(sensor) | float(0) %}
      {% set daylist = state_attr(sensor, 'daylist') %}

      {# 根据余额动态设置文字颜色 #}
      {% set text_color = '#d9383a' if balance < 20 else '#006e54' %}

      天然气余额：<span style="color: {{ text_color }}; font-weight: bold;">{{ balance }} 元</span>，

      {%- if daylist and daylist | length > 0 %}
        {%- set e_gas_list = daylist | map(attribute='e_gas') | map('float') | list %}
        {%- set f_gas_list = daylist | map(attribute='f_gas') | map('float') | list %}
        {%- set avg_e_gas = e_gas_list | sum / e_gas_list | length %}
        {%- set avg_f_gas = f_gas_list | sum / f_gas_list | length %}
        {%- set days_left = (balance / avg_e_gas) | round(0) if avg_e_gas > 0 else 0 %}
        可用 {{ days_left }} 天，每天用气 {{ avg_f_gas | round(2) }} 方
      {%- else %}
        暂无历史数据无法预测
      {%- endif %}
```

### 17.7 server_explain：后端渲染（仅限 HA 独有函数）

以下场景仍需 `server_explain: true` 走后端渲染：

- `expand('group.xxx')` — 展开组成员列表
- `area_id('living_room')` / `device_id('sensor.xxx')` — 需要 HA 设备注册表
- `closest()` / `distance()` — 需要地理坐标计算

```yaml
buttons:
  - icon: mdi:fire
    primary: >-
      {% set entities = expand('group.living_room') %}
      {% for entity in entities %}
        {{ entity.name }}：{{ entity.state }}
      {% endfor %}
    server_explain: true   # ← 只有这个仍需后端
```

> 绝大多数 Jinja2 功能已由前端引擎实现，**95% 以上的模板不再需要 `server_explain`**。

### 17.8 配置说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `server_explain` | `boolean` | `false` | `true` 时将模板发送到 HA 后端渲染（仅限 HA 独有函数如 `expand()`） |
| `primary_update_interval` | `number` | `10` | primary 文本更新间隔（秒），`0` 表示实时更新（每次 hass 推送都重新渲染） |

> **注意**：`server_explain: true` 的模板通过 HA REST API（`POST /api/template`）渲染，存在约 10-50ms 网络延迟。后端不可用时自动降级到前端引擎。

---

## 十八、配置共享

如果你有多个房间卡片，它们可以共享按钮配置。这样改一个地方，所有卡片都生效。

### 第一步：在"源卡片"中注册配置

在按钮的 `tap_action` 中添加 `config_id`：

```yaml
# 卡片A：定义共享配置
buttons:
  - type: lights
    tap_action:
      action: call-service
      service: light.turn_on
      service_data:
        entity_id: light.living
      config_id: living_light_config      # 给这个动作起个名字
```

### 第二步：在"目标卡片"中引用

```yaml
# 卡片B：引用卡片A的配置
buttons:
  - type: lights
    tap_action:
      action: call-service
      card_config:                        # 配置引用
        from_config_id: living_light_config  # 引用哪个配置
        get_type: action                    # 提取类型：all/entity/action
        replace_config:                     # 可以替换部分字段
          service_data.entity_id: light.bedroom  # 把灯换成卧室的
```

> `get_type` 有三种：`all` 取完整配置，`entity` 只取第一个实体ID，`action` 只取交互动作。

### 第三步（高级）：tabs_config 组合引用 — 从多个配置中组合新的弹窗

除了在 `card_config.from_config_id` 中引用整个 action 配置外，还可以使用 `tabs_config` 将多个已注册的配置**组合成一个新的选项卡弹窗**。这对于将不同设备（如冰箱、微波炉、电饭锅）的独立弹窗配置合并为一个"厨具"弹窗非常实用。

#### 核心概念

| 概念 | 说明 |
|------|------|
| **config_id** | 在 `tap_action` 或 `tabs` 数组元素上声明的唯一标识，配置会被自动注册到全局 Store |
| **tabs_config** | 在 `service_data.tabs` 中使用，通过 `from_config_id` 数组引用多个已注册的配置，展开为选项卡 |
| **展开规则** | 被引用的配置如果有 `tabs` → 展开为多个选项卡；有 `rows` → 作为一个选项卡；有 `cards` → 自动转为 `rows` 作为一个选项卡 |
| **混用** | `tabs_config` 和手动定义的选项卡可以在同一个 `tabs` 数组中混用，按顺序排列 |

#### 注册配置的三种位置

`config_id` 可以写在以下位置，都会被自动扫描并注册到 Store：

**位置1：`tap_action` 内部（原有功能）**

注册的是整个 action 对象（含 `config_id` + `service_data` 等），适合被 `card_config.from_config_id` 引用。

```yaml
buttons:
  - name: 冰箱
    entity: switch.bingxiang
    tap_action:
      config_id: bingxiang              # 注册 ID
      action: call-service
      service: modern_room_card.show_free_layout_popup
      service_data:
        title: 冰箱
        width: 360px
        cards:
          - row: 1
            items:
              - type: picture
                bg_image: /local/house/冰箱.png
```

**位置2：`tabs` 数组元素内部（新增，专用于 tabs_config 引用）**

注册的是该 tab 对象（含 `config_id` + `rows` + `entity` 等），适合被 `tabs_config.from_config_id` 引用为单个选项卡。

```yaml
buttons:
  - type: dynamic_icon
    name: 厨具
    tap_action:
      action: call-service
      service: modern_room_card.show_free_layout_popup
      service_data:
        title: 厨具
        tabs:
          - name: 电饭锅
            config_id: dian_fan_guo     # 注册 ID（在 tabs 数组内）
            entity: sensor.chunmi_cn_xxx_status
            entity_value:
              - Delay
              - Keep Warm
              - Busy
            rows:
              - row: 1
                items:
                  - type: picture
                    bg_image: /local/house/电饭锅.png
          - name: 空气炸锅
            config_id: kongqizhaguo      # 注册 ID
            entity: switch.kongqizhaguo
            entity_value: "on"
            rows:
              - row: 1
                items:
                  - type: picture
                    bg_image: /local/house/空气炸锅.png
          - name: 微波炉
            config_id: weibolu          # 注册 ID
            entity: switch.weibolu
            entity_value: "on"
            rows:
              - row: 1
                items:
                  - type: picture
                    bg_image: /local/house/微波炉.png
```

> **注意**：`tabs` 数组内的 `config_id` 和 `tap_action` 内的 `config_id` 互不冲突，因为它们注册的内容类型不同（tab 级 vs action 级），同一 ID 不应重复使用。

#### 使用 tabs_config 组合引用

在另一个按钮的 `service_data.tabs` 中，使用 `tabs_config` 将上述已注册的配置组合为新的弹窗：

```yaml
buttons:
  - name: 全部厨具
    icon: mdi:countertop
    tap_action:
      action: call-service
      service: modern_room_card.show_free_layout_popup
      service_data:
        title: 全部厨具
        width: 430px
        popup_position: center
        display_only:
          - "on"
          - Delay
          - Keep Warm
          - Busy
          - "off"
          - Idle
        auto_redirect: true
        tabs:
          - tabs_config:                           # 组合引用
              from_config_id:
                - config_id: bingxiang              # 引用冰箱的 tap_action 配置
                  name: 冰箱                         # 覆盖选项卡名称
                  icon: mdi:fridge                   # 覆盖选项卡图标
                  entity: switch.bingxiang           # 覆盖选项卡 entity
                  entity_value: "on"                  # 覆盖选项卡 entity_value
                  replace_config:                    # 替换配置中的指定键
                    entity_value: "on"
                - config_id: dian_fan_guo           # 引用电饭锅的 tab 配置
                  name: 电饭锅
                - config_id: kongqizhaguo           # 引用空气炸锅的 tab 配置
                - config_id: weibolu                # 引用微波炉的 tab 配置
          - name: 其他设备                           # 混用手动定义的选项卡
            entity: switch.other
            entity_value: "on"
            rows:
              - row: 1
                items:
                  - type: picture
                    bg_image: /local/house/其他.png
```

#### from_config_id 引用项的字段说明

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `config_id` | ✅ | `string` | 要引用的已注册配置 ID |
| `name` | ❌ | `string` | 覆盖选项卡显示名称（不指定则沿用原配置的 name） |
| `icon` | ❌ | `string` | 覆盖选项卡图标（如 `mdi:fridge`，不指定则沿用原配置的 icon） |
| `entity` | ❌ | `string` | 覆盖选项卡实体 ID（用于 `display_only` 过滤和 `auto_redirect` 跳转） |
| `entity_value` | ❌ | `string`/`array` | 覆盖选项卡实体匹配值（用于 `display_only` 和 `auto_redirect` 判断） |
| `replace_config` | ❌ | `object` | 替换解析结果中的指定键值对（详见下文） |

#### 展开规则详解

`tabs_config` 根据**被引用配置的结构**自动决定如何展开：

| 被引用配置结构 | 展开方式 | 典型场景 |
|---------------|---------|---------|
| 有 `tabs` 数组（action 级注册，`service_data.tabs` 存在） | **展开为多个选项卡**，每个子 tab 独立展示 | 引用一个含多个 tabs 的弹窗配置，拆分为独立选项卡 |
| 有 `tabs` 数组（tab 级注册，顶层 `tabs` 存在） | **展开为多个选项卡** | 同上 |
| 有 `rows` 数组 | **作为一个选项卡** | 引用单个 tab 配置，直接作为选项卡 |
| 有 `cards` 数组（无 tabs） | **自动将 `cards` 转为 `rows`，作为一个选项卡** | 引用使用 `cards` 布局的弹窗配置 |
| 仅有 `entity` | **构造最小选项卡**（含 entity + entity_value） | 引用简单实体配置 |

**示例：被引用配置含 tabs 时展开为多个选项卡**

假设 `chuju` 注册的配置含 3 个 tabs（电饭锅、空气炸锅、微波炉），则：

```yaml
tabs:
  - tabs_config:
      from_config_id:
        - config_id: chuju      # 展开为 3 个选项卡
```

等效于：

```yaml
tabs:
  - name: 电饭锅
    entity: sensor.chunmi_cn_xxx_status
    entity_value: [Delay, Keep Warm, Busy]
    rows: [...]
  - name: 空气炸锅
    entity: switch.kongqizhaguo
    entity_value: "on"
    rows: [...]
  - name: 微波炉
    entity: switch.weibolu
    entity_value: "on"
    rows: [...]
```

如果只想引用其中一个，直接使用子 tab 的 `config_id`：

```yaml
tabs:
  - tabs_config:
      from_config_id:
        - config_id: dian_fan_guo   # 只引用电饭锅
```

#### replace_config 替换配置

每个引用项都可以使用 `replace_config` 对展开后的选项卡配置进行**整项替换**（不做深度合并）。支持两种方式：

**方式1：简单键名** — 直接替换顶层键，如果顶层不存在则递归搜索并替换首个匹配。

```yaml
- config_id: bingxiang
  name: 冰箱
  replace_config:
    entity_value: "on"              # 替换 entity_value 字段
```

**方式2：点号路径** — 精确定位嵌套对象中的属性。

```yaml
- config_id: bingxiang
  replace_config:
    service_data.display_only:      # 精确替换 service_data.display_only
      - "on"
      - "off"
```

> `replace_config` 是**整项替换**而非深度合并。例如替换 `entity_value` 时，新值完全覆盖旧值（数组替换数组）。

#### 混用 tabs_config 和手动选项卡

`tabs_config` 引用项和手动定义的选项卡可以自由混排，按出现顺序组合：

```yaml
tabs:
  - tabs_config:
      from_config_id:
        - config_id: bingxiang
          name: 冰箱
  - name: 烤箱                       # 手动定义的选项卡
    entity: switch.oven
    entity_value: "on"
    rows:
      - row: 1
        items:
          - type: picture
            bg_image: /local/house/烤箱.png
  - tabs_config:
      from_config_id:
        - config_id: weibolu
  - name: 洗碗机                     # 又一个手动选项卡
    entity: switch.dishwasher
    rows: [...]
```

最终渲染的选项卡顺序为：冰箱 → 烤箱 → 微波炉 → 洗碗机。

#### 覆盖字段的优先级

当引用项指定了覆盖字段（如 `name`、`icon`、`entity`、`entity_value`）时：

1. 引用项中的覆盖字段 **优先级最高**，会替换原配置中的同名值
2. 未指定的字段 **沿用原配置的值**
3. `replace_config` 在覆盖字段之后应用，可以替换任意层级的键值

```
优先级：replace_config > 引用项覆盖字段 > 原配置值
```

#### tabs_config 自身的 config_id（可选）

如果组合后的弹窗本身也想被其他地方引用，可以在 `tabs_config` 上添加 `config_id`：

```yaml
tabs:
  - tabs_config:
      config_id: chuju_all            # 可选：注册组合后的配置
      from_config_id:
        - config_id: bingxiang
          name: 冰箱
        - config_id: weibolu
```

#### 循环引用保护

系统内置了循环引用检测。如果 A 引用 B，B 又引用 A，会自动跳过并输出警告日志，不会导致无限循环。

#### 完整示例：厨房场景

**步骤1：在厨具按钮中注册各设备配置**

```yaml
buttons:
  - type: dynamic_icon
    name: 厨具
    icon: mdi:countertop
    color: "#74787c"
    show_badge: true
    loop_display: true
    display_time: 3
    rules:
      - condition:
          entity: sensor.chunmi_cn_404489380_eh1_status_p_2_1
          operator: "=="
          value: [Delay, Keep Warm, Busy]
        icon: mdi:stove
        color: "#f58220"
        animation: breathe
        name: 电饭锅
    tap_action:
      config_id: chuju                    # 注册厨具弹窗（action 级，含 tabs）
      action: call-service
      service: modern_room_card.show_free_layout_popup
      service_data:
        title: 厨具
        width: 430px
        popup_position: center
        display_only: ["on", Delay, Keep Warm, Busy, "off", Idle]
        auto_redirect: true
        tabs:
          - name: 电饭锅
            config_id: dian_fan_guo        # 注册电饭锅 tab（tab 级）
            entity: sensor.chunmi_cn_404489380_eh1_status_p_2_1
            entity_value: [Delay, Keep Warm, Busy]
            rows:
              - row: 1
                per_line: 1
                title: 电饭锅
                show_title: false
                items:
                  - type: picture
                    show_button_background: false
                    halo_entity: input_boolean.chu_fang_dian_fan_guo
                    bg_image: /local/house/电饭锅.png
                    bg_image_position: [0, 0, 0.8, 0]
          - name: 空气炸锅
            config_id: kongqizhaguo         # 注册空气炸锅 tab
            entity: switch.kongqizhaguo
            entity_value: "on"
            rows:
              - row: 1
                per_line: 1
                title: 空气炸锅
                show_title: false
                items:
                  - type: picture
                    show_button_background: false
                    bg_image: /local/house/空气炸锅1.png
                    bg_image_position: [0, 0, 0.8, 0]
          - name: 微波炉
            config_id: weibolu             # 注册微波炉 tab
            entity: switch.weibolu
            entity_value: "on"
            rows:
              - row: 1
                per_line: 1
                title: 微波炉
                show_title: false
                items:
                  - type: picture
                    show_button_background: false
                    halo_entity: switch.weibolu
                    bg_image: /local/house/微波炉.png
                    bg_image_position: [0, 0, 0.8, 0]
```

**步骤2：在另一个按钮中组合引用**

```yaml
  - name: 冰箱
    entity: switch.canting_bingxiang_chazuo
    on_icon: mdi:fridge
    off_icon: mdi:fridge
    on_color: "#f58220"
    off_color: "#74787c"
    tap_action:
      config_id: bingxiang                # 注册冰箱弹窗（action 级）
      action: call-service
      service: modern_room_card.show_free_layout_popup
      popup_position: clone_button_left
      service_data:
        title: 冰箱
        width: 360px
        cards:
          - row: 1
            per_line: 1
            title: 冰箱
            show_title: false
            items:
              - type: picture
                show_button_background: false
                bg_image: /local/house/冰箱.png
                halo_entity: switch.canting_bingxiang_chazuo
                bg_image_position: [0, 7, 0.8, 0]
```

**步骤3：创建组合弹窗（全厨房设备）**

```yaml
  - name: 全部厨房
    icon: mdi:fridge-outline
    tap_action:
      action: call-service
      service: modern_room_card.show_free_layout_popup
      service_data:
        title: 全部厨房设备
        width: 430px
        popup_position: center
        auto_redirect: true
        display_only: ["on", Delay, Keep Warm, Busy, "off", Idle]
        tabs:
          - tabs_config:
              from_config_id:
                - config_id: bingxiang      # 引用冰箱弹窗（有 cards → 转为 1 个 tab）
                  name: 冰箱
                  icon: mdi:fridge
                  entity: switch.canting_bingxiang_chazuo
                  entity_value: "on"
                - config_id: dian_fan_guo    # 引用电饭锅 tab
                - config_id: kongqizhaguo    # 引用空气炸锅 tab
                - config_id: weibolu        # 引用微波炉 tab
          - name: 其他                      # 混入手动选项卡
            entity: switch.other_kitchen
            entity_value: "on"
            rows:
              - row: 1
                items:
                  - type: picture
                    bg_image: /local/house/其他.png
```

---

## 十九、平面户型图

需要在 person 配置中引用一个 JSON 文件（内容为yaml），里面定义了每个房间的形状（多边形坐标）。

### 准备坐标文件

文件路径示例：`/local/pobaby_package/point.json` ，数据是以 JSON 文件存储，内容为 YAML 格式定义的房间坐标，与温湿度卡片公用同一套坐标，房间精灵只取坐标数据。

```yaml
rooms:
  - id: 次卧
    name: 次卧
    points: 14.5000,151.6875 129.5000,151.6875 129.5000,278.6875 14.5000,278.6875
    labelX: "72"
    labelY: "185"
    dataX: "72"
    dataY: "220"
    room-data_font_size_round: 60,1
    room-label_font_size: 55
    room-unit_display:
      temperature: true
      humidity: true
  - id: 厨房
    name: 厨房
    points: >-
      136.5000,136.6875 245.5000,136.6875 245.5000,199.6875
      136.5000,199.6875
    labelX: "191"
    labelY: "138"
    dataX: "191"
    dataY: "185"
    room-data_font_size_round: 60,1
    room-label_font_size: 55
    room-unit_display:
      temperature: true
      humidity: true

```

> `points` 格式：`x1,y1 x2,y2 x3,y3 ...` 用空格分隔坐标对。
> `labelX/labelY` 是房间名称显示位置，`dataX/dataY` 是数据显示位置。

### 在 person 配置中引用

```yaml
person:
  - main_entity: binary_sensor.living_motion
    room_point_from: /local/point.json    #如果放在/local/pobaby_package/point.json，则可以不填写，否则手动指定
    rooms:
      客厅: binary_sensor.living_motion
      卧室: binary_sensor.bedroom_motion
    corner_radius: 8                     # 房间圆角大小
    room_name_font_size: 16              # 房间名字体
    person_icon:                          # 有人图标自定义（可选）
      size: 30px                          # 图标大小
      top: 20px                           # 向下偏移
      left: 10px                          # 向右偏移
      color: rgb(39, 174, 96)            # 图标颜色
```

YAML 格式也同样支持。

---

### 外部 API 历史数据

本卡片已适配 [HA 数据统一存储系统](https://github.com/chjspp520/ha_data_store/releases)，只需在卡片顶层配置 `api_base_url` 和 `key`，该卡片下的所有请求历史数据都会走该路径。

```yaml
type: custom:room-elves-card
primary_text_variant: minimal
theme: input_select.theme
dark_light_theme: dark,light
head_columns: 7
head_columns_2: 5
primary: true
primary_update_interval: 5
head: true
icon_animation: input_select.icon_animation_mode
mobile_kiosk_entity: input_boolean.full
show_animation: input_boolean.show_animation
api_base_url: xxxxxxxxxx        # 数据统一存储系统 API 地址
key: xxxxxxxxxxxx               # API 密钥
```

卡片会自动从外部 API 拉取历史状态数据，用于时间轴和趋势显示。

### 实体配置上报（report）

本卡片支持将自身配置中提取的全部实体（`entity_id` / `name` / `icon` / `room_name`）上报到 [HA 数据统一存储系统](https://github.com/chjspp520/ha_data_store/releases) 后端，供后端生成实体健康等报表数据。多个卡片共用同一个上报按钮，点击一次即聚合所有卡片实例的实体统一上报。

```yaml
type: custom:room-elves-card
api_base_url: /api/ha_data_store/    # 数据统一存储系统 API 地址
key: xxxxxxxxxxxx                     # API 密钥
report: input_button.report          # 触发上报的按钮实体
report_unique_priority: room         # 上报去重策略（可选）
report_name_priority: name,alias,entity_id   # 上报名称取值优先级（可选，任意一张卡片配置即可全局生效）
```

**上报机制：**
- 所有 `room-elves-card` 卡片共用同一 `report` 按钮实体，点击一次只聚合上报一次（前端全局协调，避免重复请求）。
- 按钮类（`input_button` / `button`）通过 `state` 或 `last_triggered` 变化触发；开关类（`switch` / `input_boolean`）通过 `off → on` 触发。
- 上报内容由各卡片递归扫描自身配置提取实体（自动跳过 `_REPORT_SKIP_KEYS` 黑名单与非法域），实体名/图标缺失时从 HA 状态回退，`room_name` 在头部卡片固定为 `头部`，其余取卡片顶层 `room_name`。

**去重策略（`report_unique_priority`）：**

| 取值 | 说明 |
|------|------|
| `room` | 按 `entity_id` 去重，同一实体多处出现时**优先保留属于真实房间**的一份（`room_name` 非空且非 `头部`） |
| `head` | 按 `entity_id` 去重，同一实体多处出现时**优先保留位于头部**的一份（`room_name` 为 `头部`） |
| `none` | 不去重，原样全量上报（默认值，不配置时为此模式） |

> 后端不会干预前端上传的数据，因此重复实体需由前端按 `report_unique_priority` 自行去重。配置为 `room` 或 `head` 时，若两份出现均非对应优先类型，则保留先出现的一份。

**名称优先级（`report_name_priority`）：**

控制上报到后端时实体的 `name` 字段从哪个来源取值，为逗号分隔的取值顺序，从左至右取第一个非空值：

| 取值 | 说明 |
|------|------|
| `name` | 卡片内部配置的 `name`（config 中该实体节点的 `name` 字段） |
| `alias` | 用户在 HA 中定义的实体名称（`friendly_name`） |
| `entity_id` | 实体 ID |

```yaml
report_name_priority: name,alias,entity_id   # 优先取卡片 name，其次 HA 别名，最后实体 ID
```

> 不配置时默认 `name,alias,entity_id`（即旧的"卡片 name > HA 别名 > 实体 ID"取值逻辑）。想优先用 HA 中定义的实体名，可配置为 `alias,name,entity_id`。

**全局生效说明：**

由于所有 `room-elves-card` 卡片共用同一 `report` 按钮、点击一次聚合上报全部卡片，`report_name_priority` 支持**配置一次、全局生效**：

- **只需在任意一张卡片**（建议在主卡片/头部卡片）配置 `report_name_priority`，其它未单独配置的卡片在聚合上报时**自动沿用**该优先级。
- 若某张卡片**单独配置**了自己的 `report_name_priority`，则该卡片优先用自己独立的优先级（覆盖全局）。
- 即使只在**一个房间**卡片配置了 `report_name_priority`，所有房间的实体上报都会遵循该优先级。

```yaml
# 主卡片/头部卡片配置一次即可全局生效
report_name_priority: alias,name,entity_id
```

## 二十、ECharts 图表与外部 API

卡片内置了 ECharts 图表功能，用于渲染曲线图、环形图、饼图、南丁格尔玫瑰图、热力图、日历图、混合图表和桑基图等。

**文件路径：** 所有前端外部资源文件统一存放在 `www/pobaby_package/js/` 目录下：
- ECharts：`www/pobaby_package/js/echarts.min.js`
- Leaflet CSS：`www/pobaby_package/js/leaflet.css`
- Leaflet JS：`www/pobaby_package/js/leaflet.js`

**加载策略：** 优先使用本地文件，当目录中没有对应文件时，卡片会自动从 CDN 拉取。

**依赖 ECharts 的图表类型：** `chart_line`、`chart_pie`、`chart_pie_full`、`chart_nightingale`、`chart_heatmap`、`chart_calendar`、`chart_mixed`，以及插座桑基图。详见 [6.21 图表卡片概览](#621-图表卡片概览)。

**无需 ECharts 的图表类型：** `chart_gauge`（纯 SVG）、`chart_progress`（纯 CSS）、`chart_bar`（纯 CSS）。

## 二十一、弹窗系统（Popup System）

Room Elves Card 的弹窗系统是所有交互控制的核心载体——点击按钮弹出控制面板、空调调节面板、灯光面板等，都是通过统一的弹窗引擎实现的。本节详细说明弹窗系统的架构、配置和行为。

### 21.1 弹窗架构概览

所有弹窗通过统一的 `showPopup(options)` 方法创建，该方法返回一个 `closePopup()` 函数供外部调用关闭弹窗。

**弹窗打开流程：**

1. 解析 `options` 参数
2. 通过 `_zIndexManager` 分配动态 Z-Index（支持多层弹窗嵌套）
3. 非嵌套弹窗时，先移除同类型的已有弹窗和遮罩
4. 创建背景遮罩（`popup-overlay`）
5. 创建弹窗主体 DOM，调用 `content()` 函数生成内容
6. 收集弹窗内所有定时器，关闭时统一清理
7. 根据触发按钮位置计算弹窗位置，选择动画方向
8. 添加 `.visible` 类触发动画

**弹窗关闭流程：**

1. 清理所有局部定时器、ECharts 实例、IntersectionObserver
2. 释放 Z-Index
3. 执行关闭动画后移除 DOM
4. 移除遮罩、克隆按钮、光晕层
5. 调用 `onClose` 回调

**点击遮罩关闭：** 默认行为，点击弹窗外的半透明遮罩区域即可关闭弹窗。

### 21.2 弹窗类型一览

每种按钮类型都有对应的专属弹窗，点击按钮后自动触发：

| 按钮类型 | 弹窗方法 | CSS 类名 | 功能说明 |
|----------|----------|----------|----------|
| `lights` | `showLightControlPopup()` | `light-control-popup` | 灯光控制面板（亮度/色温/颜色/分组/批量操作） |
| `light` | `showLightCardPopup()` | `light-card-popup` | 单灯控制面板 |
| `ac` | `showAcControlPopup()` | `ac-control-popup` | 空调控制面板（温度/模式/风速） |
| `socket` | `showSocketControlPopup()` | `socket-control-popup` | 插座控制面板（批量开关） |
| `consumables` | `showConsumablesPopup()` | `consumables-popup` | 耗材/电池面板 |
| `media` | `showMediaControlPopup()` | `media-control-popup` | 媒体控制面板 |
| `curtain` | `showCurtainControlPopup()` | `curtain-control-popup` | 窗帘控制面板（百分比/双层/开合模式） |
| `clothes_dryer` | `showClothesDryerPopup()` | — | 晾衣架控制面板（拖拽/收藏位置） |
| `fan` | — | — | 风扇控制面板（风速/摇头） |
| `device` / `heater` | `showDevicePopup()` | `device-popup` | 通用设备/暖气控制面板 |
| `scene_mode` | `showSceneModeBubble()` | — | 情景模式气泡选择面板 |
| `popup_card`（tap_action） | `handlePopupCardAction()` | `custom-card-popup` | 自定义 HA 卡片弹窗 |
| `call-service`（特定服务） | `showFreeLayoutPopup()` | `free-layout-popup` | 自由布局控制面板 |
| 人在传感器 | `showPersonPopup()` | `person-popup` | 人员活动弹窗（时间轴/户型图） |
| 自动化 | `showAutomationPopup()` | `automation-popup` | 自动化管理面板 |
| 概览栏 | `showOverviewControlPopup()` | `overview-control-popup` | 概览控制弹窗 |

> `showDevicePopup()` 是路由分发器，根据按钮的 `type` 字段分派到各专用弹窗方法。

### 21.3 弹窗位置系统（popup_position）

通过 `popup_position` 配置项控制弹窗相对于触发按钮的弹出位置。

#### 支持的位置值

| 位置值 | 别名 | 效果 |
|--------|------|------|
| `center` | — | 视口居中 |
| `clone_button_top` | `up`、`top` | 触发按钮上方 |
| `clone_button_down` | `down`、`bottom` | 触发按钮下方 |
| `clone_button_left` | `left` | 触发按钮左侧 |
| `clone_button_right` | `right` | 触发按钮右侧 |
| `clone_button_upper_left` | — | 触发按钮左上方 |
| `clone_button_upper_right` | — | 触发按钮右上方 |
| `clone_button_lower_left` | — | 触发按钮左下方 |
| `clone_button_lower_right` | — | 触发按钮右下方 |
| 不配置（默认） | — | 自动选择最佳位置 |

#### 偏移值语法

支持在位置值后附加自定义偏移量，格式为 `"位置, 偏移量"`：

```yaml
popup_position: "clone_button_down, 30px"    # 按钮下方，偏移30px
popup_position: "center, -10px"               # 居中，向上偏移10px
```

默认偏移量为 25px。

#### 自动定位算法（不配置 popup_position 时）

当未指定位置时，系统自动选择最佳弹出方向，优先级为：**右 → 左 → 空间更大的一侧 → 上下**。算法会计算按钮四周的可用空间，选择能完整容纳弹窗的方向。

#### 边界保护

- **非居中位置**：水平+垂直方向均 clamp 到安全区域，确保弹窗不超出视口
- **居中位置**：仅垂直边界保护，水平方向严格居中
- **人在传感器弹窗**：自适应高度，超出时限制 maxHeight 并启用滚动

### 21.4 弹窗动画

弹窗支持多种出现/消失动画，系统会根据弹窗位置自动选择最合适的动画方向。

| 动画类 | 效果 | 时长 | 触发条件 |
|--------|------|------|----------|
| `popup-fade-in` | 淡入 + 缩放（0.95→1.0） | 0.2s | 默认动画 |
| `popup-center-fade-in` | 居中淡入 + 缩放 | 0.2s | 居中弹出时 |
| `popup-slide-from-right` | 从右侧滑入 | 0.25s | 按钮在弹窗左侧 |
| `popup-slide-from-left` | 从左侧滑入 | 0.25s | 按钮在弹窗右侧 |
| `popup-slide-from-bottom` | 从下方滑入 | 0.25s | 按钮在弹窗上方 |
| `popup-slide-from-top` | 从上方滑入 | 0.25s | 按钮在弹窗下方 |
| `heater-popup-anim` | 弹性缩放动画 | 0.4s | heater 类型弹窗专用 |

**动画方向智能选择：** 系统根据克隆按钮与弹窗的相对位置自动选择滑入方向——按钮在左则从右滑入，按钮在上则从下滑入，以此类推。

### 21.5 弹窗宽度（width）

多种按钮类型支持通过 `width` 配置项控制弹窗宽度：

```yaml
buttons:
  - type: curtain
    entity: cover.living_curtain
    width: 560px                     # 弹窗宽度
```

**宽度处理逻辑：**

| 配置值 | 效果 |
|--------|------|
| 不配置 | 使用各弹窗类型的默认宽度 |
| 具体值（如 `400px`、`560px`） | 固定为该宽度 |
| `auto` | 不限制宽度，由内容自适应 |
| 百分比（如 `80%`） | 基于视口宽度计算 |

> 移动端会自动限制弹窗高度不超过视口的 60%，确保操作便利性。

### 21.6 自动关闭定时器（close_time）

部分弹窗类型支持配置自动关闭倒计时，用户无操作到达时间后弹窗自动关闭。

```yaml
buttons:
  - type: lights
    card:
      - entity: light.bed_light
        name: 床头灯
    close_time: 300                  # 300秒（5分钟）后自动关闭
```

| 配置值 | 效果 |
|--------|------|
| `0` | 不自动关闭 |
| `> 0` 的数字 | 指定秒数后自动关闭 |

**用户操作取消自动关闭：** 在自动关闭倒计时期间，用户进行以下操作会重置定时器：

- 滑块拖动（`input` 事件）
- 颜色选择（`change` 事件）
- 点击操作（`click` 事件）

**灯光关闭自动关闭弹窗：** 当灯光弹窗中的灯被关闭后，200ms 后弹窗自动关闭。

### 21.7 自动弹窗（auto_open_entity）

当指定实体变为 `on` 时自动打开弹窗，适合告警联动场景（如门窗传感器触发时自动弹出面板）。

#### 配置方式

```yaml
buttons:
  - type: lights
    card:
      - entity: light.bed_light
    tap_action:
      auto_open_entity: binary_sensor.front_door    # 触发实体
      auto_open_delay: 3000                          # 延迟弹出（毫秒）
      auto_close: true                               # 实体变off时自动关闭弹窗
```

#### 配置项说明

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `auto_open_entity` | ✅ | `string` | 无 | 触发实体 ID，该实体变为 `on` 时自动打开弹窗 |
| `auto_open_delay` | ❌ | `number` | `0` | 延迟弹出时间（毫秒），延迟后再次检查实体仍为 `on` 才弹出，避免短暂触发时误弹 |
| `auto_close` | ❌ | `boolean` | `false` | 触发实体变为 `off` 时是否自动关闭弹窗。`false` 时实体变 `off` 不影响已打开的弹窗 |

#### 行为规则

| 场景 | 行为 |
|------|------|
| 页面加载时实体已为 `on` | 自动弹出弹窗 |
| 运行中实体从 `off` 变为 `on` | 自动弹出弹窗 |
| 实体从 `on` 变为 `off` | 默认不关闭弹窗；配置了 `auto_close: true` 时自动关闭 |
| 用户手动关闭弹窗 | 标记 `dismissed`，本轮 `on` 周期内不再自动弹出 |
| 实体变 `off` 后再次变 `on` | 重置 `dismissed` 状态，可再次自动弹出 |
| 配置了 `auto_open_delay` | 延迟后再次检查实体仍为 `on` 且弹窗未打开才弹出 |

### 21.8 自定义卡片弹窗（popup_card）

通过 `tap_action: popup_card` 可以在弹窗中嵌入任意 HA 卡片，实现完全自定义的控制面板。

#### 基本用法

```yaml
buttons:
  - entity: switch.some_switch
    name: 自定义面板
    tap_action:
      action: popup_card
      card:                                # 嵌入的 HA 卡片配置
        type: entities
        entities:
          - switch.some_switch
          - sensor.some_sensor
      popup_position: center               # 弹窗位置
      width: 500px                         # 弹窗宽度
```

#### 配置项

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `card` | ✅ | `object` | 无 | 要嵌入的 HA 卡片配置对象（标准 HA 卡片格式） |
| `popup_position` | ❌ | `string` | `null` | 弹窗位置（见 21.3 节） |
| `width` | ❌ | `string` | `null` | 弹窗宽度，支持具体值（`500px`）、百分比（`80%`）、`auto`（内容自适应） |

**width 详细处理：**

| 配置值 | 效果 |
|--------|------|
| 不配置 | `min-width: 380px, max-width: 95%` |
| `"auto"` | 不限制宽度，由内容决定 |
| `"500px"` | 固定宽度 500px |
| `"80%"` | 视口宽度的 80% |

**vertical-stack 类型特殊处理：** 当嵌入的卡片为 `vertical-stack` 类型时，自动创建折叠/展开功能，可收起/展开内含的子卡片。

### 21.9 弹窗内选项卡（Tabs）

弹窗内支持选项卡分组，将多个控制面板组织在不同选项卡中。详细配置请参见第八节"弹窗中的选项卡（Tabs）"。

**选项卡核心功能速览：**

| 功能 | 配置项 | 说明 |
|------|--------|------|
| 自动跳转 | `auto_redirect: true` | 自动跳转到最近开启的设备选项卡 |
| 条件过滤 | `display_only: ["on","Delay"]` | 仅显示实体值匹配的选项卡 |
| 分组显示 | `belong: "客厅"` | 按房间/区域分组显示选项卡 |
| 禁用选项卡 | `disabled: true` | 禁用该选项卡（灰色不可点击） |
| 角标 | `badge: {entity, ...}` | 选项卡显示徽标 |
| 实体匹配 | `entity` + `entity_value` | 用于高亮/自动跳转 |
| 每行数量 | `table_per_line: 3` | 每行显示的选项卡数 |
| 固定宽度 | `table_one_width: "60px"` | 每个选项卡的固定宽度 |

### 21.10 弹窗 DOM 结构

弹窗的标准 DOM 结构如下：

```
shadowRoot
├── div.popup-overlay                    ← 背景遮罩层
│   ├── data-z-index-id="N"              ← Z-Index 管理器 ID
│   ├── data-popup-class-name="xxx"      ← 关联的弹窗类名
│   ├── style.touch-action="none"        ← 移动端防触摸穿透
│   └── .no-blur（条件）                 ← overlayBlur=false 时添加
│
├── div.clone-glow-layer                 ← 光晕层（grouped-btn时创建）
│
├── div.grouped-btn.clone                ← 克隆的触发按钮（视觉锚点）
│
└── div.{className}.popup-fade-in        ← 弹窗主体
    └── [content() 生成的DOM]
        ├── div.popup-header             ← 标题栏
        │   └── h3.popup-title           ← 标题文本
        └── div.popup-content            ← 内容区域（可滚动）
```

### 21.11 Z-Index 层栈管理

弹窗系统内置了 `_zIndexManager` 来管理多层弹窗的 Z-Index，支持弹窗嵌套而不会出现层级错乱。

**Z-Index 计算公式：**

- `zIndex = baseZIndex + (level * layerGap * 2) + 2`
- `overlayZIndex = zIndex - 2`

其中 `baseZIndex = 1000`，`layerGap = 10`。

**每层弹窗的层级结构（从低到高）：**

1. overlay 遮罩层（overlayZIndex）
2. glow-layer 光晕层（overlayZIndex + 1）
3. clone-button 克隆按钮（overlayZIndex + 2）
4. popup 弹窗主体（zIndex — 最高）

**功能特性：**

- 新弹窗入栈时，自动禁用下层 overlay 的交互（防止穿透点击）
- 弹窗关闭后，自动恢复顶层 overlay 的交互
- 通过 WeakRef 检测已回收的 DOM，自动垃圾回收
- 最大栈深度 100 层，防止异常嵌套

### 21.12 滚动穿透防护

弹窗打开时，系统自动启用三层滚动穿透防护，确保弹窗内滚动不会影响背景页面：

1. **CSS `overscroll-behavior: contain`** — 阻止下拉刷新和过度滚动传播
2. **Body 物理锁定** — 设置 `position: fixed; overflow: hidden; top: -scrollY`，彻底禁用背景滚动
3. **弹窗内可滚动容器** — `overscroll-behavior: contain` + MutationObserver 自动检测新增的可滚动元素

**自动触发时机：**

- 第一个弹窗入栈时启用锁定
- 最后一个弹窗出栈时解除锁定

### 21.13 确认对话框（confirm）

部分操作（如情景模式执行、按钮点击）支持配置确认对话框，防止误操作：

```yaml
buttons:
  - type: button
    entity: input_button.test
    confirm: true                          # 点击时弹出确认对话框
```

确认对话框使用独立的 `showConfirmDialog()` 方法，不通过 `showPopup()` 创建，样式更轻量。

### 21.14 各按钮类型的弹窗专用配置汇总

| 按钮类型 | 弹窗配置项 | 默认值 | 说明 |
|----------|-----------|--------|------|
| `lights` / `light` | `close_time` | `0` | 自动关闭倒计时（秒） |
| `lights` / `light` | `show_duration` | `false` | 按钮上显示已开启时长 |
| `curtain` | `width` | `560px` | 弹窗宽度 |
| `curtain` | `popup_position` | `null` | 弹窗位置 |
| `curtain` | `layer_mode` | `double` | 单层/双层模式 |
| `curtain` | `open_mode` | `double` | 对开/同向开合 |
| `ac` | `width` | `auto` | 弹窗宽度 |
| `ac` | `popup_position` | `null` | 弹窗位置 |
| `ac` | `power_entity` | 无 | 年累计用电量实体 |
| `ac` | `power_display_entity` | 无 | 当前功率实体 |
| `ac` | `humidity_entity` | 无 | 湿度传感器实体 |
| `ac` | `current_temperature` | 无 | 室温传感器实体 |
| `ac` | `page_1` | 无 | 第二页类型：`power_page` / `duration_page` / `both_page`，配置后启用双页滑动模式 |
| `ac` | `api_base_url` | 继承顶层 | API 接口地址（日历图表数据源） |
| `ac` | `key` | 继承顶层 | API 密钥 |
| `clothes_dryer` | `width` | `440px` | 弹窗宽度 |
| `clothes_dryer` | `locker` | `true` | 锁定模式（禁用拖拽） |
| `scene_mode` | `width` | `400px` | 气泡/进度面板宽度 |
| `scene_mode` | `fold` | `false` | 动作列表默认展开 |
| `scene_mode` | `verify_timeout` | `10` | 验证超时秒数 |
| `popup_card` | `width` | `null` | 弹窗宽度 |
| `popup_card` | `popup_position` | `null` | 弹窗位置 |
| 通用 | `popup_position` | `null` | 弹窗位置（见 21.3 节） |
| 通用 | `auto_open_entity` | 无 | 自动弹窗触发实体 |

---

### 自由布局弹窗（show_free_layout_popup）

自由布局弹窗是 Room Elves Card 中最灵活、最常用的弹窗形式。它允许你在弹窗中自由排列各种控制卡片（开关、传感器、选择器、图表等），支持选项卡分组、行分组、跨行跨列、条件过滤等高级功能，可以快速搭建出复杂的设备控制面板。

### 21.15 触发方式

自由布局弹窗通过 `tap_action: call-service` 触发，服务名为 `room_card.show_free_layout_popup` 或 `modern_room_card.show_free_layout_popup`（两者等价）。

```yaml
buttons:
  - entity: switch.some_switch
    name: 控制面板
    tap_action:
      action: call-service
      service: room_card.show_free_layout_popup
      service_data:
        title: 我的控制面板
        cards: [...]
```

> 也可以通过 `tap_action: popup_card` 触发自定义卡片弹窗（见 21.8 节），两者区别：`popup_card` 嵌入单个 HA 原生卡片，`show_free_layout_popup` 使用卡片内置的丰富卡片类型系统。

### 21.16 顶层配置项

```yaml
tap_action:
  action: call-service
  service: room_card.show_free_layout_popup
  popup_position: center                # 弹窗位置（可放在 tap_action 层，优先级更高）
  auto_open_entity: binary_sensor.xxx   # 自动弹窗实体（放在 tap_action 层）
  auto_open_delay: 2000                 # 延迟弹出毫秒（放在 tap_action 层）
  auto_close: true                      # 自动关闭（放在 tap_action 层）
  service_data:
    title: 控制面板                      # 弹窗标题
    show_title: true                     # 是否显示标题栏
    width: 360px                         # 弹窗宽度
    cards: [...]                         # 卡片列表（与 tabs 互斥）
    # tabs: [...]                        # 选项卡列表（与 cards 互斥）
    layout: grid                         # 布局方式（仅 cards 传统模式）
    grid_config:                         # 网格配置
      columns: 2
      gap: 10
    title_entities: [...]                # 标题右侧实体
    auto_redirect: false                 # 自动跳转到设备开启的选项卡
    display_only:                        # 仅显示实体值匹配的选项卡
      - 'on'
    table_per_line: null                 # 每行选项卡数
    table_one_width: null                # 选项卡固定宽度
    update_interval: 0                   # 更新间隔（秒）
    style: ''                            # 自定义 CSS
    popup_position: center               # 弹窗位置（也可放 service_data 内）
```

**完整配置项说明：**

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `title` | ❌ | `string` | `控制面板` | 弹窗标题文本 |
| `show_title` | ❌ | `boolean` | `true` | 是否显示标题栏，设为 `false` 时隐藏整个标题区域 |
| `width` | ❌ | `string` | `auto` | 弹窗宽度，支持 `auto`（自适应，最小 300px）、具体值（`360px`）、百分比（`80%`） |
| `cards` | ❌ | `array` | `[]` | 卡片列表（非选项卡模式），与 `tabs` 互斥 |
| `tabs` | ❌ | `array` | `null` | 选项卡列表（选项卡模式），与 `cards` 互斥 |
| `layout` | ❌ | `string` | `grid` | 布局方式：`grid`（网格）/ `flex`（弹性）/ `custom`（自定义，仅 cards 传统模式生效） |
| `grid_config` | ❌ | `object` | `{columns:2,gap:10}` | 网格配置，含 `columns`（列数）和 `gap`（间距 px） |
| `title_entities` | ❌ | `array` | `[]` | 标题右侧实体配置（见 21.20 节） |
| `auto_redirect` | ❌ | `boolean` | `false` | 自动跳转到设备开启的选项卡（见 21.21 节） |
| `display_only` | ❌ | `array` | `null` | 仅显示实体值匹配的选项卡（见 21.22 节） |
| `table_per_line` | ❌ | `number` | `null` | 每行显示的选项卡数量 |
| `table_one_width` | ❌ | `string` | `null` | 每个选项卡的固定最小宽度（如 `80px`） |
| `update_interval` | ❌ | `number` | `0` | 定时刷新间隔（秒），0 = 跟随 HA 实时推送 |
| `style` | ❌ | `string` | `''` | 追加到弹窗的自定义 CSS 字符串 |
| `popup_position` | ❌ | `string` | `null` | 弹窗位置（见 21.3 节），tap_action 层优先级高于 service_data 内 |

> `cards` 和 `tabs` 不能同时配置，否则报错。

### 21.17 两种内容模式

#### Cards 模式（非选项卡）

Cards 模式有两种结构，系统自动检测。

**结构一：Row 分组模式（推荐，支持行标题、行内跨列）**

当 `cards` 数组中第一项包含 `row` 和 `items` 字段时，自动进入 Row 分组模式：

```yaml
cards:
  - row: 1                         # 行号，决定排列顺序
    per_line: 2                    # 每行显示几个卡片
    title: 灯光控制                # 行标题（可选）
    show_title: true               # 是否显示标题（默认 true）
    title_entities: [...]          # 行级标题右侧实体（可选）
    items:                         # 该行的卡片列表
      - type: switch
        entity: switch.light1
        name: 客厅灯
      - type: switch
        entity: switch.light2
        name: 卧室灯
  - row: 2
    per_line: 3
    title: 传感器
    items:
      - type: sensor
        entity: sensor.temperature
        name: 温度
      - type: sensor
        entity: sensor.humidity
        name: 湿度
      - type: sensor
        entity: sensor.pm25
        name: PM2.5
```

**结构二：传统布局模式（简单网格排列）**

直接列出卡片，使用 `layout` 和 `grid_config` 控制布局：

```yaml
layout: grid
grid_config:
  columns: 2
  gap: 10
cards:
  - type: sensor
    entity: sensor.temperature
    name: 温度
  - type: switch
    entity: switch.plug
    name: 插座
  - type: select
    entity: select.mode
    name: 模式
```

#### Tabs 模式（选项卡分组）

使用选项卡将内容分为多个面板，每个选项卡有独立的行内容：

```yaml
tabs:
  - name: 客厅
    icon: mdi:sofa
    entity: switch.living_light      # 绑定实体（用于高亮/跳转）
    entity_value: 'on'              # 实体匹配值
    rows:
      - row: 1
        per_line: 2
        items:
          - type: switch
            entity: switch.living_light
            name: 主灯
          - type: switch
            entity: switch.living_floor_lamp
            name: 落地灯
  - name: 卧室
    icon: mdi:bed
    entity: switch.bedroom_light
    rows:
      - row: 1
        per_line: 2
        items:
          - type: switch
            entity: switch.bedroom_light
            name: 卧室灯
```

### 21.18 弹窗内支持的卡片类型

自由布局弹窗内置了 30+ 种卡片类型，可直接在 `items` 中使用：

| type 值 | 说明 | 主要配置项 |
|---------|------|-----------|
| `sensor` | 传感器数值 | `entity`, `name`, `unit`, `icon`, `layout`(mini/full) |
| `switch` | 开关控制 | `entity`, `name`, `icon` |
| `toggle` | 切换开关 | `entity`, `on_icon`, `off_icon`, `on_color`, `off_color` |
| `select` | 下拉选择器 | `entity`, `name` |
| `number` | 数值输入 | `entity`, `name`, `min`, `max`, `step` |
| `text` | 文本输入 | `entity`, `name` |
| `slider` | 滑块控制 | `entity`, `min`, `max`, `step` |
| `button` | 按压按钮 | `entity`, `name`, `icon`, `show_duration`, `confirm` |
| `light` | 灯光控制 | `entity`, `name`（含亮度/色温调节） |
| `cover` | 遮盖控制 | `entity`, `name` |
| `curtain` | 窗帘控制 | `entity`, `fabric_entity`, `sheer_entity` |
| `ac` | 空调控制 | `entity` |
| `fan` | 风扇控制 | `entity` |
| `media` | 媒体控制 | `entity` |
| `clothes_dryer` | 晾衣架控制 | `entity`, `light_entity` |
| `radio` | 单选按钮组 | `entity`, `options`, `compact` |
| `button_group` | 按钮组 | `buttons`, `direction`, `on_color`, `off_color`, `show_name` |
| `action` | 快捷操作/情景 | `name`, `icon`, `scenes`, `scene_mode` |
| `chart` / `chart_line` | 折线图 | `entity`, `name` |
| `chart_gauge` | 仪表盘图 | `entity`, `name` |
| `chart_progress` | 进度条 | `entity`, `name` |
| `chart_bar` | 柱状图 | `entity`, `name` |
| `chart_pie` | 环形图 | `entity`, `name` |
| `chart_pie_full` | 完整饼图 | `entity`, `name` |
| `chart_mixed` | 混合图表 | `entity`, `name` |
| `chart_nightingale` | 南丁格尔玫瑰图 | `entity`, `name` |
| `chart_heatmap` | 日历热力图 | `entity`, `name` |
| `chart_calendar` | 日历图 | `entity`, `name` |
| `timeline` | 时间轴 | `entity`, `map_table`, `api_base_url` |
| `picture` | 图片展示 | `bg_image`, `halo_entity`, `bg_image_position` |
| `html` | 自定义 HTML | `content` |
| `user` | 用户信息 | `persons` |
| `usage` | 使用量统计 | `entity`, `name` |
| `weather` | 天气预报 | `weather`（多地区数组）, `height`, `compact` |
| `nas` | NAS 服务器状态卡片 | `power_switch`, `storage_summary`, `array_01`, `array_02` |
| `printer` | 打印机用量统计卡片（日历热力图 / 墨盒详情 / 用墨占比环形图） | `entity`, `name`, `colors`, `api_base_url`, `key`, `today_print` |
| `fnos` | 飞牛 fnOS 全实体卡片（主机 / 存储 / Docker / 虚拟机 / 应用） | `entity`, `name`, `icon`, `accent`, `popup_width`, `popup_position`, `confirm_power` |
| `daily_report` | 今日家庭日报卡片 | `entity`, `refresh`, `hide_room`, `env_from_config_id`, `width` |
| `esxi` | ESXi 虚拟化卡片（主机状态 / 虚拟机批量操作 / 屏幕墙三选项卡） | `entity`, `hosts`, `vms`, `exclude`, `default_vm`, `show_screen`, `show_refresh`, `show_sync`, `confirm_power_off`, `width` |
| `bill` | 个人账单卡片（概览 / 分析 / 日历 / 查询 / 历史五选项卡） | `api_base_url`, `key`, `name`, `icon`, `subtitle`, `accent`, `page_size`, `recent_days`, `source`, `direction` |
| `dingdong` | 叮咚门铃卡片（抓拍 / 实时画面 + 按天回看时间轴 + 设置 + 诊断四选项卡） | `entity`, `name`, `date`, `show_live`, `events_limit`, `shots_limit`, `videos_limit`, `hero_ratio`, `hero_max_height`（见 6.47） |
| `card` | 自定义卡片 | 标准 HA 卡片配置 |
| `conditional_tabs` | 条件选项卡 | 条件控制 Tab 显示 |

**每个卡片通用字段：**

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `update_interval` | `number` | `0` | 单独的刷新间隔（秒），覆盖弹窗级别的 `update_interval` |
| `layout` | `string` | `normal` | 卡片布局：`normal`（标准）/ `mini` / `min`（紧凑） |
| `show_name` | `boolean` | `true` | 是否显示名称 |
| `row_column` | `string` | 无 | 跨行跨列配置（见 21.19 节） |
| `position` | `object` | 无 | 传统模式网格位置 `{row, column}` |
| `size` | `object` | 无 | 传统模式跨列跨行 `{width, height}` |

**天气卡片 (`type: weather`) 专用字段：**

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `weather` | `array` | 无 | 天气地区数组，每项含 `name`、`entity`、`api_base_url`、`living_index` |
| `height` | `string` | 无 | 卡片高度，支持 `210px`、`100%` 等 CSS 值。适用于 head 模式网格中撑满单元格 |
| `compact` | `boolean` | `false` | 紧凑模式 |
| `show_details` | `boolean` | `true` | 是否显示湿度/风/气压等详情指标 |
| `show_title` | `boolean` | `true` | 是否显示"天气预报"标题 |
| `max_days` | `number` | `7` | 预报天数 |
| `background` | `string` | 无 | 背景色 |

**天气卡片配置示例（head 模式内嵌）：**

```yaml
buttons:
  - type: card
    row_column: 2,2-5
    card_config:
      type: weather
      background: transparent
      height: 100%                        # 撑满网格单元格高度
      weather:
        - name: 未央区
          entity: weather.qweather_pro_wei_yang_weather
          living_index: 穿衣指数,洗车指数    # 首页只显示这两项指数（气泡始终显示全部）
        - name: 西乡县
          entity: weather.qweather_pro_xi_xiang_weather
```

### 21.19 跨行跨列布局（row_column）

在 Row 分组模式的 `items` 中，可以通过 `row_column` 让卡片占据多个网格单元，格式为 `'序号,行数-列数'`：

```yaml
items:
  - type: sensor
    entity: sensor.temperature
    name: 温度
    row_column: '1,1-2'           # 序号1，占1行2列（跨2列宽）
  - type: switch
    entity: switch.light1
    name: 灯1
    row_column: '2,1-1'           # 序号2，占1行1列
  - type: switch
    entity: switch.light2
    name: 灯2
    row_column: '3,1-1'           # 序号3，占1行1列
  - type: chart_line
    entity: sensor.power
    name: 功率曲线
    row_column: '4,2-2'           # 序号4，占2行2列（大图表）
```

**规则：**

- 只要 items 中有任意一个配置了 `row_column`，该行组就切换为 CSS Grid 跨行跨列模式
- 没有 `row_column` 的 item 按 1×1 自动排列
- `per_line` 作为列数参考
- `row_column` 只影响同一个 row 组内的布局

**常见布局示例：**

| row_column | 效果 | 适用场景 |
|------------|------|----------|
| `'1,1-2'` | 1行2列（跨2列） | 宽传感器、滑块 |
| `'1,2-2'` | 2行2列（方形） | 大图表 |
| `'1,1-1'` | 1×1 标准卡片 | 普通 |
| `'1,2-3'` | 2行3列 | 大型图表/控制区 |

### 21.20 标题右侧实体（title_entities）

在弹窗标题栏右侧或行标题右侧显示实体状态/快捷操作，支持三种模式：

#### 模式一：传感器模式

显示实体当前值或 Way 计算结果：

```yaml
title_entities:
  - entity: switch.dian_fan_guo
    icon: mdi:stove
    name: 今日使用次数
    show_name: false
    way: today_usage_count           # Way 计算方式
    format: '今天用了{_default}次'   # Way 格式模板
```

支持 `way`、`format`、`unit` 等 Way 计算引擎字段（详见第十六节）。

#### 模式二：控制按钮模式

显示可点击的控制按钮，支持多实体批量操作：

```yaml
title_entities:
  - entities:
      - light.keting_dadeng
      - light.keting_xuanguan
    name: 灯光
    icon: mdi:lightbulb-group
    tap_action:
      action: toggle               # 点击切换所有灯的开关
```

#### 模式三：快捷操作模式

显示情景模式快捷按钮：

```yaml
title_entities:
  - type: action
    name: 情景
    icon: mdi:palette
    scenes:
      - name: 全关
        actions:
          - entities:
              客厅灯: light.keting_dadeng
            value: "off"
    scene_mode: bubble              # bubble | direct
```

**title_entities 每项字段：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `entity` | ❌* | `string` | 单实体 ID |
| `entities` | ❌* | `array` | 多实体 ID 数组（批量操作） |
| `name` | ❌ | `string` | 显示名称 |
| `icon` | ❌ | `string` | 图标 |
| `show_name` | ❌ | `boolean` | 是否显示名称（默认 `true`） |
| `way` | ❌ | `string/array` | Way 计算方式（详见第十六节） |
| `format` | ❌ | `string` | Way 显示格式模板 |
| `unit` | ❌ | `string` | 单位 |
| `tap_action` | ❌ | `object` | 点击动作（详见第七节） |
| `type` | ❌ | `string` | 设为 `'action'` 启用快捷操作模式 |
| `scenes` | ❌ | `array` | 快捷操作情景列表（type=action 时） |

> `entity` 和 `entities` 至少配置一个（type=action 除外）。

### 21.21 自动跳转（auto_redirect）

当选项卡中绑定了 `entity` 和 `entity_value` 时，开启 `auto_redirect` 可自动跳转到最近开启的设备选项卡。

```yaml
auto_redirect: true
tabs:
  - name: 客厅
    entity: switch.living_light
    entity_value: 'on'
    rows: [...]
  - name: 卧室
    entity: switch.bedroom_light
    entity_value: 'on'
    rows: [...]
```

**跳转规则：**

| 场景 | 行为 |
|------|------|
| `auto_redirect: false`（默认） | 始终激活第一个非禁用且可见的 Tab |
| `auto_redirect: true` | 在所有 `entity` + `entity_value` 匹配的 Tab 中，选择 `last_changed` 时间最新的跳转 |
| 无匹配 | 降级为第一个非禁用且可见的 Tab |
| 禁用的 Tab | 不参与自动跳转 |
| 被 displayOnly 隐藏的 Tab | 不参与自动跳转 |

### 21.22 条件过滤（display_only）

仅显示实体状态匹配指定值的选项卡，未匹配的选项卡自动隐藏。

```yaml
display_only:
  - 'on'
  - Delay
  - Keep Warm
tabs:
  - name: 设备A
    entity: switch.device_a          # 绑定实体
    rows: [...]
  - name: 设备B
    entity: select.device_b          # 如果 state 为 "Delay" 则显示
    rows: [...]
```

**过滤规则：**

| 条件 | 结果 |
|------|------|
| `display_only` 未配置或为空 | 所有 Tab 可见 |
| Tab 未配置 `entity` | 始终可见 |
| 实体不存在或状态为 `unavailable`/`unknown` | 始终可见 |
| 实体状态匹配 `display_only` 中任一项 | 可见 |
| 实体状态不匹配 | 隐藏 |

**实时更新：** 当实体状态变化时，系统自动更新 Tab 可见性。如果当前激活的 Tab 被隐藏，自动切换到第一个可见 Tab。

**空状态提示：** 当所有 Tab 都不可见时，弹窗显示提示信息："N个设备中没有现在处于开启的设备"。

### 21.23 选项卡高级配置

#### 选项卡完整字段

| 字段 | 必填 | 类型 | 默认值 | 说明 |
|------|:----:|------|--------|------|
| `name` | ❌ | `string` | `Tab N` | 选项卡显示名称 |
| `icon` | ❌ | `string` | 无 | 选项卡图标 |
| `belong` | ❌ | `string` | 无 | 所属分组（用于按楼层/区域分组显示） |
| `entity` | ❌ | `string` | 无 | 绑定实体 ID（用于高亮/自动跳转/display_only） |
| `entity_value` | ❌ | `string/array` | 无 | 实体匹配值，支持数组（任一匹配即算） |
| `rows` | ❌ | `array` | `[]` | 选项卡内容行（与 items 格式相同） |
| `disabled` | ❌ | `boolean` | `false` | 是否禁用（灰色不可点击） |
| `badge` | ❌ | `string/number` | 无 | 角标固定值 |
| `badge_entity` | ❌ | `string` | 无 | 角标动态取值实体（实体值作为角标数字） |
| `config_id` | ❌ | `string` | 无 | 注册 ID（供 tabs_config 引用，详见第十八节） |

#### 选项卡分组（belong）

当任何 Tab 配置了 `belong` 时，选项卡按 `belong` 值分组显示，每组有标签 + 按钮容器。无 `belong` 的 Tab 平铺到导航栏最前面。

```yaml
tabs:
  - name: 客厅灯
    belong: 1楼                     # 属于"1楼"分组
    rows: [...]
  - name: 客厅空调
    belong: 1楼
    rows: [...]
  - name: 主卧灯
    belong: 2楼                     # 属于"2楼"分组
    rows: [...]
```

#### 选项卡高亮

当 Tab 配置了 `entity` + `entity_value` 且实体状态匹配时，选项卡按钮自动高亮显示。

#### 选项卡宽度控制

```yaml
table_per_line: 3                   # 每行显示3个选项卡按钮
table_one_width: 80px               # 每个选项卡最小宽度80px
```

两者可同时使用，`table_per_line` 控制换行，`table_one_width` 控制按钮宽度。

### 21.24 行分组高级功能

#### 行级标题右侧实体

每行可以独立配置 `title_entities`，格式与弹窗顶层的 `title_entities` 相同：

```yaml
cards:
  - row: 1
    title: 灯光控制
    title_entities:
      - entity: switch.all_lights
        icon: mdi:lightbulb-group
        tap_action:
          action: toggle
    items: [...]
```

#### 行级详情链接（show_more_info）

在行标题右侧显示详情链接，点击弹出更多信息：

```yaml
cards:
  - row: 1
    title: 空调
    show_more_info: popup_card       # 显示"详情>>>"链接
    card:                             # 点击后弹出的自定义卡片
      type: entities
      entities:
        - climate.living
    items: [...]
```

| show_more_info 值 | 效果 |
|-------------------|------|
| `popup_card` | 在标题右侧显示"详情>>>"链接，点击弹出 `card` 配置的自定义卡片 |
| 不配置 | 不显示详情链接 |

### 21.25 布局模式详解

#### grid 布局（默认）

CSS Grid 网格，通过 `grid_config` 控制列数和间距：

```yaml
layout: grid
grid_config:
  columns: 3        # 3列网格
  gap: 12           # 间距12px
```

CSS 效果：`display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;`

#### flex 布局

弹性换行布局，卡片宽度自适应：

```yaml
layout: flex
grid_config:
  gap: 8
```

CSS 效果：`display: flex; flex-wrap: wrap; gap: 8px;`

#### custom 布局

不应用任何预设样式，完全由 `style` 字段自定义。

> **注意**：`layout` 仅在 Cards 传统模式（非 Row 分组模式）下生效。Row 分组模式和 Tabs 模式由 `per_line` 和 `row_column` 控制布局。

### 21.26 完整配置示例

#### 示例一：简单开关面板

```yaml
buttons:
  - entity: switch.some_switch
    name: 控制
    tap_action:
      action: call-service
      service: room_card.show_free_layout_popup
      service_data:
        title: 客厅控制
        width: 360px
        cards:
          - row: 1
            per_line: 2
            title: 灯光
            items:
              - type: switch
                entity: switch.living_ceiling
                name: 天花灯
              - type: switch
                entity: switch.living_floor_lamp
                name: 落地灯
          - row: 2
            per_line: 3
            title: 插座
            items:
              - type: switch
                entity: switch.plug1
                name: 插座1
              - type: switch
                entity: switch.plug2
                name: 插座2
              - type: switch
                entity: switch.plug3
                name: 插座3
```

#### 示例二：选项卡 + 自动跳转 + 条件过滤

```yaml
buttons:
  - entity: switch.main
    name: 全屋控制
    tap_action:
      action: call-service
      service: room_card.show_free_layout_popup
      service_data:
        title: 全屋设备
        width: 430px
        auto_redirect: true
        display_only:
          - 'on'
        tabs:
          - name: 客厅
            icon: mdi:sofa
            entity: switch.living_main
            entity_value: 'on'
            rows:
              - row: 1
                per_line: 2
                items:
                  - type: switch
                    entity: switch.living_light
                    name: 主灯
                  - type: switch
                    entity: switch.living_ac
                    name: 空调
          - name: 卧室
            icon: mdi:bed
            entity: switch.bedroom_main
            entity_value: 'on'
            rows:
              - row: 1
                per_line: 2
                items:
                  - type: switch
                    entity: switch.bedroom_light
                    name: 卧室灯
                  - type: switch
                    entity: switch.bedroom_ac
                    name: 空调
```

#### 示例三：跨行跨列 + 传感器 + 标题实体

```yaml
buttons:
  - entity: switch.main
    name: 智能面板
    tap_action:
      action: call-service
      service: room_card.show_free_layout_popup
      service_data:
        title: 客厅
        width: auto
        title_entities:
          - entity: sensor.living_temperature
            name: 温度
            icon: mdi:thermometer
          - entities:
              - light.living_ceiling
              - light.living_floor_lamp
            name: 灯光
            icon: mdi:lightbulb-group
            tap_action:
              action: toggle
        cards:
          - row: 1
            per_line: 3
            title: 环境
            items:
              - type: sensor
                entity: sensor.living_temperature
                name: 温度
                unit: °C
                row_column: '1,1-1'
              - type: sensor
                entity: sensor.living_humidity
                name: 湿度
                unit: '%'
                row_column: '2,1-1'
              - type: sensor
                entity: sensor.living_pm25
                name: PM2.5
                row_column: '3,1-1'
          - row: 2
            per_line: 2
            title: 控制
            items:
              - type: switch
                entity: switch.living_light
                name: 主灯
                row_column: '1,1-2'
              - type: select
                entity: select.ac_mode
                name: 空调模式
                row_column: '2,1-1'
              - type: number
                entity: number.ac_temp
                name: 温度
                min: 16
                max: 30
                step: 1
                row_column: '3,1-1'
          - row: 3
            per_line: 1
            title: 功率曲线
            items:
              - type: chart_line
                entity: sensor.living_power
                name: 功率
                row_column: '1,1-1'
```

#### 示例四：选项卡分组（belong）+ 角标

```yaml
service_data:
  title: 全屋灯光
  auto_redirect: true
  tabs:
    - name: 客厅主灯
      icon: mdi:ceiling-light
      belong: 1楼
      entity: light.living_ceiling
      entity_value: 'on'
      badge_entity: sensor.living_power
      rows:
        - row: 1
          per_line: 2
          items:
            - type: switch
              entity: light.living_ceiling
              name: 天花灯
            - type: switch
              entity: light.living_floor_lamp
              name: 落地灯
    - name: 客厅灯带
      icon: mdi:led-strip
      belong: 1楼
      entity: light.living_led
      entity_value: 'on'
      rows:
        - row: 1
          per_line: 2
          items:
            - type: light
              entity: light.living_led
              name: 灯带
    - name: 主卧灯
      icon: mdi:lamp
      belong: 2楼
      entity: light.bedroom
      entity_value: 'on'
      rows:
        - row: 1
          per_line: 2
          items:
            - type: switch
              entity: light.bedroom
              name: 主灯
```

#### 示例五：自动弹窗（告警联动）

```yaml
buttons:
  - entity: binary_sensor.front_door
    name: 门磁
    tap_action:
      action: call-service
      service: room_card.show_free_layout_popup
      auto_open_entity: binary_sensor.front_door    # 门打开时自动弹出
      auto_open_delay: 3000                          # 延迟3秒（防误触）
      auto_close: true                               # 门关闭后自动关闭弹窗
      service_data:
        title: 前门状态
        cards:
          - row: 1
            per_line: 1
            items:
              - type: sensor
                entity: binary_sensor.front_door
                name: 门状态
              - type: timeline
                entity: binary_sensor.front_door
                name: 今日活动
```

### 21.27 参数优先级速查

| 参数 | 优先级规则 |
|------|-----------|
| `popup_position` | `tap_action.popup_position` > `service_data.popup_position` |
| `auto_open_entity` | 放在 `tap_action` 层级（非 service_data 内部） |
| `auto_open_delay` | 放在 `tap_action` 层级 |
| `auto_close` | 放在 `tap_action` 层级 |
| `update_interval` | 卡片级 > 弹窗级 > 默认(0) |

---

## 二十二、程序扩展坞（Dock）

程序扩展坞是一个从屏幕右侧滑入的快捷启动栏，支持复用头部模式的全部按钮类型和动作系统。

### 22.1 基础配置

在卡片配置中添加 `dock` 数组：

```yaml
type: custom:room-elves-card
dock:
  - name: api
    primary: API
    entity: input_boolean.api_gateway_man_close
    on_icon: mdi:lan-connect
    off_icon: mdi:lan-disconnect
    on_color: "#007b43"
    off_color: "#b94047"
    tap_action:
      action: toggle
  - name: HA-TCP
    primary: HA-TCP
    entity: switch.nps_server
    on_icon: mdi:lan-connect
    off_icon: mdi:lan-disconnect
    tap_action:
      action: toggle
```

### 22.2 支持的按钮类型

dock 条目支持头部模式的所有按钮类型，用法与 `buttons` 配置完全一致：

| 类型 | 说明 | 示例 |
|---|---|---|
| 无 type | 普通开关按钮 | 默认 toggle 动作 |
| `type: light` | 灯光按钮 | 显示灯光颜色/状态 |
| `type: curtain` | 窗帘按钮 | 显示窗帘开关状态 |
| `type: sensor` | 传感器按钮 | 显示传感器数值 |
| `type: scene_mode` | 情景模式按钮 | 一键切换场景 |
| `type: dynamic_icon` | 动态图标 | 支持规则匹配和动画 |

```yaml
dock:
  - type: light
    name: 客厅灯
    entity: light.living_room
  - type: curtain
    name: 窗帘
    entity: cover.curtain
  - type: scene_mode
    name: 离家
    scenes:
      - name: 全部关闭
        actions:
          - service: light.turn_off
            target:
              entity_id: all
```

### 22.3 Primary 文本

dock 条目支持 `primary` 字段，在图标下方显示文本，支持 Jinja2 模板：

```yaml
dock:
  - name: api
    primary: "{{ states('input_boolean.api_gateway_man_close') }}"
    entity: input_boolean.api_gateway_man_close
```

### 22.4 右上角三角状态指示器

dock 条目会自动在按钮右上角显示一个斜三角状态指示器，支持三种模式。

**模式一：`preset_xx` 预设映射（推荐）**

通过 `icon_text: preset_xx` 快速根据实体状态显示对应文字。除 `preset_state` 外，还支持 `preset_ac`（空调）、`preset_fan`（风扇）、`preset_humidifier`（加湿器）、`preset_qweather`（和风天气）、`preset_media`（媒体播放器）：

```yaml
dock:
  - name: 网关
    entity: input_boolean.api_gateway_man_close
    icon_text: preset_state             # 自动显示 开/关/家/离
    on_icon: mdi:lan-connect
    off_icon: mdi:lan-disconnect
```

当前支持的 `icon_text` 预设：

| 预设名称 | 适用实体 | 数据源 | 状态映射 |
|---------|----------|--------|---------|
| `preset_state` | 任意 | `state` | `on` → 开，`off` → 关，`open` → 开，`closed` → 关，`home` → 家，`not_home` → 离 |
| `preset_ac` | `climate.*` | `state`（hvac_mode） | `cool` → 冷，`heat` → 热，`dry` → 湿，`fan_only` → 风，`auto` → 自，`off` → 关 |
| `preset_qweather` | `weather.*` | `attributes.qweather_icon` | `100` → 晴，`104` → 阴，`308` → 暴雨，`400` → 雪，`502` → 霾 … |
| `preset_fan` | `fan.*` | `attributes.preset_mode` | `直吹风` → 直，`自然风` → 自，`智能风` → 智，`睡眠风` → 睡，`off` → 关 |
| `preset_humidifier` | `humidifier.*` | `attributes.mode` | `恒湿` → 恒，`睡眠` → 睡，`强力` → 强，`off` → 关 |
| `preset_media` | `media_player.*` | `state` | `playing` → 放，`paused` → 停，`idle` → 闲，`standby` → 候，`on` → 开，`off` → 关 |

> 预设文件在 `modules/presets/dynamic-icon-presets.js` 的 `ICON_TEXT_PRESETS` 中注册，可自由扩展。

**`preset_ac` 示例**（空调，匹配 `climate.state`）：

```yaml
- type: ac
  entity: climate.ceshi
  icon_text: preset_ac          # 制冷显示"冷"(蓝)，制热显示"热"(橙)，关闭显示"关"
```

**`preset_fan` / `preset_humidifier` 示例**（读 attribute；设备关闭时显示"关"）：

```yaml
- entity: fan.xxx
  icon_text: preset_fan          # 自然风→自，睡眠风→睡，关闭→关

- entity: humidifier.xxx
  icon_text: preset_humidifier   # 恒湿→恒，强力→强，关闭→关
```

> **说明**：`preset_fan` / `preset_humidifier` 的模式名在 attribute（`preset_mode` / `mode`）中，`state` 只有 on/off。设备关闭时（`state == 'off'`）优先显示"关"，避免残留 attribute 导致错误显示。斜三角背景色跟随图标颜色实时变化。

**模式二：Jinja2 模板/自定义文字**

通过 `icon_text` 直接定义显示内容，支持 Jinja2 模板语法：

```yaml
dock:
  - name: api
    entity: input_boolean.api_gateway_man_close
    icon_text: "{{ '开' if is_state('entity_id', 'on') else '关' }}"
```

```yaml
dock:
  - name: 设置
    icon_text: S                        # 静态文字，不依赖实体
    icon: mdi:cog
```

**模式三：自动推断（兜底）**

当 `icon_text` 未配置但条目有 `entity` 时，自动显示实体状态的缩写：

| 实际状态 | 三角显示 |
|---|---|
| `on` | 开 |
| `off` / `closed` | 关 |
| `open` | 开 |
| `home` | 家 |
| `not_home` | 离 |
| `unavailable` | 不显示 |
| 短文本(≤4字) | 原文 |
| 长文本 | 截断加 `…` |

**关于背景色**：三角背景色自动跟随实体的 `on_color` / `off_color`（取半透明处理）。三角圆角可通过 CSS 变量 `--icon-radius` 全局调整，默认 8px（非 dock 按钮）或 10px（dock 按钮）。

### 22.5 触发按钮位置

通过 `dock_trigger_position` 调整右侧触发按钮的垂直位置：

```yaml
dock_trigger_position: center    # top / center（默认）/ bottom，或 "30%" 等百分比
dock:
  - name: api
    ...
```

### 22.6 交互方式

- **点击触发按钮**：打开/关闭扩展坞
- **点击扩展坞内按钮**：执行动作后自动关闭
- **点击扩展坞外部区域**：自动关闭扩展坞

### 22.7 外观行为

- dock 栏高度自适应条目数量，最小高度 120px
- 面板上下各留 40px 间距，不顶到屏幕边沿
- 继承 `show_animation` 设置（关闭时禁用按钮动画）

---

## 二十三、能耗中心卡片（energy_center）

能耗中心卡片是一个三区合一的弹出式卡片，用于展示全屋能耗数据的全景视图：

- **上部分**：今日/本月/今年用电量 + 运行设备数
- **中部分**：3D 房间能耗地图（Three.js，支持拖拽旋转、点击房间联动）
- **下部分**：设备用电排行榜（支持日/月/年切换，点击房间过滤）

### 23.1 基础配置

通过按钮的 `tap_action` → `action: popup_card` 弹出：

```yaml
buttons:
  - name: 全屋用电量
    icon: mdi:flash
    tap_action:
      action: popup_card
      popup_position: center
      width: 400px
      card:
        type: energy_center
```

`api_base_url` 和 `key` 继承自卡片顶层配置，无需在 `card` 中重复填写。

### 23.2 隐藏指定房间

```yaml
card:
  type: energy_center
  hide_room: 儿童房外,次卧外,楼道,客厅外
```

多个房间名用逗号分隔。隐藏的房间不会出现在 3D 地图、排行榜和统计中。

### 23.3 自定义标题

```yaml
card:
  type: energy_center
  name: 全屋用电量
```

不配置时默认显示"能耗中心"。

### 23.4 概览弹窗快捷入口

在概览弹窗（overview-control-popup）中，配置 `type: energy` + `utilities.电力.hide_room` 后，点击"用电量"行会自动弹出能耗中心卡片：

```yaml
overview:
  - type: energy
    name: 能耗
    icon: mdi:transmission-tower
    utilities:
      电力:
        entity: sensor.ele_xxx
        power: sensor.quanwu_zongglv
        power_onsumption: sensor.quan_wu_ri_yong_dian_liang
        hide_room: 儿童房外,次卧外,楼道,客厅外
        tap_action:
          card:
            type: energy_center
```

### 23.5 交互行为

- **点击房间**：在 3D 地图上点击任意房间，会在点击位置附近弹出气泡，显示该房间的能耗概况（总用电量、运行/设备数、设备能耗排行 Top 8）。
- **点击空白**：关闭气泡，排行榜恢复为全屋排行。
- **拖拽/缩放**：单指拖动旋转视角，双指捏合缩放（移动端），滚轮缩放（桌面端）。

### 23.6 数据来源

| 周期 | 数据接口 | 说明 |
|------|----------|------|
| 日 | `_loadDeviceUsageDataAllRooms()` | 含运行中设备实时数据，走全局缓存 |
| 月 | `_loadRankingData('monthly', 'YYYY-MM')` | 月度排行榜聚合数据 |
| 年 | `_loadRankingData('yearly', 'YYYY')` | 年度排行榜聚合数据 |

日/月/年通过底部选项卡切换，切换时自动重新加载对应周期数据。

### 23.7 交互说明

- **3D 地图拖拽**：鼠标拖拽旋转视角，滚轮缩放
- **点击房间**：3D 柱体高亮呼吸 + 外发光，底部排行榜过滤为该房间设备
- **点击空白**：恢复自动旋转，排行榜回到全屋
- **日/月/年切换**：顶部标签和排行榜数据同步更新

### 23.8 主题适配

- 3D 场景背景色、标签文字颜色、灯光强度自动适配暗色/亮色主题

---

## 二十四、水温卡片（water_temp）

水温卡片是一个可视化温度传感器数据的卡片，以水填充动画的形式直观展示水温：

- 水填充高度 = 当前温度在 `[min_temp, max_temp]` 范围内的百分比
- 填充颜色从底部蓝色渐变到顶部当前温度对应色（蓝→青→绿→橙→红）
- 气泡数量随温度升高而增多，在 fill 区域内随机上升
- 水面有摇晃晃动 + 波面涟漪动画

### 24.1 基础配置

在自由布局弹窗的 `items` 中配置：

```yaml
items:
  - type: water_temp
    entity: sensor.water_temperature
    name: 热水器水温
    min_temp: 0
    max_temp: 80
    width: 80%
    height: 90%
    tap_action:
      action: more-info
```

### 24.2 配置项说明

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|--------|:----:|------|--------|------|
| `type` | ✅ | `string` | - | 必须为 `water_temp` |
| `entity` | ✅ | `string` | - | 水温传感器实体 ID |
| `name` | ❌ | `string` | 实体 `friendly_name` | 显示名称（当前版本不显示） |
| `min_temp` | ❌ | `number` | `0` | 温度下限 |
| `max_temp` | ❌ | `number` | `100` | 温度上限 |
| `unit` | ❌ | `string` | 实体 `unit_of_measurement` 或 `℃` | 温度单位 |
| `width` | ❌ | `string` | `100%` | 卡片宽度（支持 px / %） |
| `height` | ❌ | `string` | `180px` | 卡片高度（支持 px / %） |
| `tap_action` | ❌ | `object` | - | 点击动作（支持所有标准 tap_action 类型） |

### 24.3 动画说明

| 动画 | 作用 | 参数 |
|------|------|------|
| **wt-waterShake** | fill 整体左右摇晃模拟水晃动 | rotate ±0.5°~±0.8°，transform-origin: center bottom |
| **wt-waveRipple** | 水面波面涟漪效果 | translateY ±2px + scaleX 0.95~1.1 + opacity 变化 |
| **wt-gas-bubble** | 气泡从底部随机上升到顶部消失 | translateY 0→-120px，opacity 0→1→0，scale 0.8→1.1→0.8 |

### 24.4 完整示例

```yaml
items:
  - type: picture
    row_column: 1,1-2
    show_button_background: false
    bg_image: /local/device.png
    halo_entity: input_boolean.device
  - type: water_temp
    entity: sensor.water_temperature
    min_temp: 0
    max_temp: 80
    width: 80%
    height: 90%
    tap_action:
      action: more-info
```
- 卡片背景使用 CSS 变量 `--room-popup-bg`，跟随卡片主题

---

## 二十五、调试信息管理系统

卡片内置了一套统一的**调试信息管理系统**（`DebugManager`），实现了"**一个公共方法，三处同步**"的调试信息查看机制，方便排查卡片/模块问题。

### 25.1 三处同步

模块调用调试方法后，调试信息会**同时**同步到以下三个地方：

| 同步位置 | 说明 |
|---------|------|
| **调试卡片** | 卡片内置 `debug_card` 弹窗，顶部模块开关列表，下方直接显示该模块发来的完整调试文本 |
| **浏览器控制台** | 模块调用 `send()` 后，控制台实时输出 `[room-elves][模块名] ...` |
| **控制台命令** | `roomElvesDebug()` 命令入口，随时切换模块开关、查看已发送调试信息 |

三者开关状态与信息**完全一致、双向同步**：控制台命令开启某模块后，调试卡片对应开关自动高亮；卡片点开关，控制台命令状态同步。

### 25.2 调试卡片（debug_card）

在按钮配置中使用 按钮 `tap_action` 弹窗内 `card.type: debug_card`：

```yaml

buttons:
  - name: 调试
    tap_action:
      action: popup_card
      card:
        type: debug_card
        name: 调试信息
        width: 560px
```

调试卡片布局：
- **顶部**：一排模块开关（点击开启 / 再次点击关闭）
- **下方**：固定信息展示区，点击开关直接显示该模块的调试文本
- 关闭弹窗再打开，自动恢复上次激活的模块

> **debug_card 头部选项卡**：弹窗头部含「调试 / 性能 / 版本 / 数据库」四个选项卡。
> - **调试**：模块开关 + 调试文本直显（本节前述功能）
> - **性能**：运行态性能指标（更新耗时 / 帧率 / 索引 / 定时器 / 后端请求等 13 项 + 控制台命令），**详见 25.6**
> - **版本**：卡片/后端版本信息 + HA 服务器信息概览 + 系统资源 24h 趋势图 + 已注册调试模块
> - **数据库**：内置数据库浏览器（表选择 + 字段选择 + 多条件筛选 + 浏览/修改模式原地编辑 + 前端 SQL 执行 + 分页/表头排序），详见 25.2.2

### 25.2.1 版本选项卡（v5.6.2 起）

「版本」选项卡用于查看卡片/后端版本与服务器运行状态。其中 **HA 服务器信息** 与 **系统资源** 数据来自后端 `ha_data_store`（需 **v3.1.0+**）：

- **卡片/后端版本信息**：Room Elves Card 与 HA 数据统一存储系统的当前版本号（后端版本统一带 `v` 前缀）；行内名称可点击查看详情（带 `more` 提示），版本号可点击查看版本历史，右上角为"新版本"角标与刷新按钮。
  - **Room Elves Card 详情气泡**（点击名称）：顶部为当前版本号 + GitHub 地址（可点击跳转），下方为 **卡片结构模块树**——"卡片结构"标题（右端合计模块总数）+ 各目录分组（core / infra / render / popup / cards / events / utils / presets）。每个目录为一级分组，**默认折叠、点击展开**，展开后逐条显示该目录模块名称与功能简介（内容硬编码自 `room-elves-code-tree.md`）。
  - **HA数据统一存储系统详情气泡**（点击名称）：本地访问地址 / 数据库地址 / **数据库大小（右侧带「压缩」按钮**，点击调用后端 `db_maintain` 执行 VACUUM，完成后 toast 提示压缩前后大小/节省/压缩率）/**数据表（显示 `x 张 / xxx 条` 含合计记录数）** 及各表行数。
  - **版本历史气泡**（点击版本号）：带标题栏（`版本历史 · xxx`）+ 版本列表；**最新版本整行绿色高亮并标注 `Latest` 徽标**。
- **版本历史缓存**：结果缓存在浏览器本地，**同一浏览器 6 小时内刷新页面不再重新请求 GitHub**（内存副本 10 分钟）；
  感到过时可在「版本」选项卡点手动刷新（会清掉持久缓存并重新拉取）。GitHub 限流（403/429）时会进入 1 小时冷却期，冷却状态同样持久化，避免反复撞限流。
- **HA服务器信息**：数据源为后端实体 `sensor.ha_data_store_db_viewer_url` 的 `attributes.system`（每 10 分钟刷新）。精简概览卡展示 **HA版本 / 内存 / 硬盘 / 运行时长** 四项，各项独立交互：
  - **HA版本**：`mdi:home-assistant` 图标 + "HA版本"文字 + 版本号；点击弹**版本信息气泡**（HA核心版本、前端版本、安装方式、服务器名称、更新于）。
  - **内存 / 硬盘**：**圆环占用图**（58px 圆环，名称与占用百分比居中于环内，下方显示"已用 / 总量"）；实时百分比与已用/总量读取自 `sensor.ha_data_store_memory_usage` / `disk_usage`（30 秒刷新），缺失时回退仅显示总容量。
  - **运行时长**：文字按规则本地化——≥ 24h 显示 `x.x 天`、1~24h 显示 `x.x 小时`、< 1h 显示 `x 分钟`；点击弹**安装时间 + 运行时长**气泡。
- **系统资源**：内嵌一张 ECharts 折线图，近 24 小时 **CPU / 内存 / 硬盘** 三条占用曲线同图显示；首次切换到「版本」选项卡时自动懒加载。数据来自三个资源传感器：
  - `sensor.ha_data_store_cpu_usage`（CPU 占用率）
  - `sensor.ha_data_store_memory_usage`（内存占用）
  - `sensor.ha_data_store_disk_usage`（硬盘已用）
  - 后端每 30 秒刷新；传感器需运行一段时间积累历史后，24h 曲线才完整。
- **已注册调试模块**：列出所有接入 `DebugManager` 的模块及其说明。

> ⚠️ **依赖**：以上服务器/系统资源数据需后端 **HA 数据统一存储系统 v3.1.0+** 提供；后端未升级时，HA服务器信息区显示占位提示，不影响卡片其它功能。
>
> 📌 **提示**：Room Elves Card 详情中的模块树为静态硬编码（与 `room-elves-code-tree.md` 结构文档同步维护），仅用于结构浏览。

### 25.2.2 数据库选项卡（v5.6.4 起）

「数据库」选项卡内置**数据库浏览器**，与后端 `ha_data_store` 的 `db_viewer` 数据/提交接口一致，面向移动端做了紧凑化改造。顶部工具栏为一行**文字按钮**：

```
选择表 ▾   [字段] [筛选] [浏览/修改] [SQL]
```

- 带 `.fcount` 的红色角标在按钮右上角，显示当前生效数量（已选字段数 / 生效筛选数）。
- 字段 / 筛选 / SQL 三个面板**互斥展开**（同时只开一个）；按钮展开时紫色实底高亮。
- 分页区（`dbg-db-pager`）固定在面板下方、表格上方，并按当前内容切换显示。

**字段选择**：
- 点「字段」展开字段勾选面板（复选框 chips，内部限高滚动）；面板右下角紫色「隐藏」按钮收起。
- **选中数据表后字段面板自动展开**，方便直接勾选要显示的列；勾选即时刷新表格。
- 「字段」角标 = 当前已勾选的列数。

**多条件筛选**：
- 点「筛选」展开筛选区：每行 = 字段 + 操作符 + 值（可多条）。操作符同 `db_viewer`：等于 / 不等于 / 包含 / 大于 / 小于 / 大于等于 / 小于等于 / 为空 / 不为空（后两者无需值）。
- 「应用筛选」→ 以 `filter=<JSON>` 参数提交（`[{col,op,val}]`）回到第 1 页并自动收起；「清除」取消全部筛选。
- 筛选可与字段勾选、表头排序、分页叠加使用。

**浏览 / 修改模式（原地编辑）**：
- 默认「浏览」；切到「修改」后**点击单元格**即进入编辑（移动端无 `dblclick`，故用单击，桌面双击第一击同样开启）。
- 编辑时输入框**铺满覆盖原单元格**（视觉上在原位置修改），单元格紫色描边高亮；单元格正下方出现操作条：「表名.列名 · 行ID」+「确定」（紫色）/「取消」，支持 `Enter`=确定、`Esc`=取消。
- 「确定」提交 `POST /api/ha_data_store/db_viewer/update`，body：`{ table, row_id, column, value }`（空输入 → `NULL`），成功后原地回显新值。

**SQL 执行**：
- 点「SQL」展开面板：等宽输入框（`Ctrl/Cmd+Enter` 快捷执行）+「执行」/「清空」+ 状态行。
- SELECT 结果表格**直接显示在主数据表格区域**（可上下/左右滚动）；底部 pager 变为 `SQL · 共 N 条` 翻页。
- UPDATE/INSERT/DELETE 等写语句 → 主区显示"受影响行数：N"，pager 仅显示受影响提示。
- 提交 `POST /api/ha_data_store/db_viewer/sql`，body：`{ sql, page, page_size: 100 }`。

> ⚠️ **提示**：
> - 单元格编辑/SQL 的读、改、执行接口均复用卡片配置的 `key`（与 `db_viewer` 一致，后端需允许修改）；
> - 浏览表、SQL 结果的表格均在 `dbg-db-data` 内部滚动，列宽可依赖表头排序时的自动适配；
> - SQL 写入类语句请谨慎执行，涉及真实数据修改。

### 25.3 浏览器控制台命令

在浏览器控制台（F12）输入：

```js
roomElvesDebug()                        // 帮助 + 所有模块开关状态
roomElvesDebug('list')                  // 列出已注册模块
roomElvesDebug('<模块名>')               // 切换开关（如 entity-report）
roomElvesDebug('<模块名>', true/false)   // 显式开/关
roomElvesDebug('all')                   // 全部开启
roomElvesDebug('none')                  // 全部关闭
roomElvesDebug('view', '<模块名>')       // 查看该模块已发送的调试信息
roomElvesDebug('dump', '<模块名>')       // 输出该模块 dump() 缓冲数据
roomElvesDebug('clear', '<模块名>')      // 清空该模块缓冲
```

示例：

```js
roomElvesDebug('entity-report')            // 开启上报模块调试
roomElvesDebug('entity-report', false)     // 关闭上报模块调试
roomElvesDebug('view', 'entity-report')    // 查看上报模块已发送的调试信息
```

### 25.4 已接入的调试模块

| 模块 | 说明 | 接入方式 |
|------|------|---------|
| `action-log` | 用户操作记录埋点 | `register` + `dump`（完整操作记录字段） |
| `entity-report` | 实体提取上报 | `register` + `send`（完整实体字段） |

### 25.5 给新模块加调试信息

任何模块只需两步即可接入调试信息（遵循 `DebugManager` 公共接口）：

```js
import { DebugManager } from '../core/debug.js';

// 1. 注册模块名（让它在调试卡片顶部出现开关按钮）
DebugManager.register('my-module', { describe: '我的模块说明' });

// 2. 发送调试文本（自动同步到调试卡片 + 控制台）
DebugManager.send('my-module', '这是一条调试信息');
```

如需查看模块的完整缓冲数据，可额外实现 `dump` 返回 `{ title, text }`：

```js
DebugManager.register('my-module', {
  describe: '说明',
  dump: () => ({ title: '标题', text: '多行文本' }),
});
```

### 25.6 性能选项卡（v5.9.0 起）

> 本节对应 25.2 节里提到的「性能」选项卡 —— 它一直是 `debug_card` 的四个选项卡之一，此前误置为独立章节，现已并入本章。

「性能面板」是 `debug_card` 弹窗里的一个**独立选项卡**（懒加载：不点开就没有任何开销），把卡片历次性能优化（实体精准更新、订阅过滤、定时器合并、首屏加载等）变成**常驻可见的量化指标**。

在它之前，每次验证"到底快了没有"都要临时往代码里插 `performance.now()`，测完再删 —— 既没法对比，也没有性能回归预警。

**两个入口：界面**（适合边操作边看）与**控制台命令**（适合复现卡顿时取证，不用开着弹窗）。

#### 25.6.1 界面入口

调试卡片弹窗头部有「调试 / 性能 / 版本 / 数据库」四个选项卡，点「性能」即可。

```yaml
buttons:
  - name: 调试
    tap_action:
      action: popup_card
      card:
        type: debug_card
        name: 调试信息
```

面板布局为 **4 行长文本 + 3×3 指标网格 + 口径说明**，每 2 秒刷新一次。**所有格子都可以点击**，点开后弹出该指标的完整明细气泡。

| 位置 | 指标 | 一句话说明 |
|------|------|-----------|
| 长文本 1 | **hass 更新耗时** | 最近 10 帧的耗时，**并单独给出"有效帧"** |
| 长文本 2 | **最慢步骤** | 更新链里当前最耗时的那一步 |
| 长文本 3 | **资源占用** | JS 堆用量 / 上限 |
| 长文本 4 | **主线程** | 定时器实际漂移 + 近 30 秒长任务 |
| 网格 | **帧率** | rAF 采样（仅面板可见时计数） |
| 网格 | **更新频率** | hass 更新次数 / 秒 |
| 网格 | **订阅遗漏** | 索引里有、订阅集里没有的实体数（>0 标红） |
| 网格 | **订阅实体** | 全页所有卡的订阅实体数（点开有按域分组） |
| 网格 | **定时器数** | 活跃定时器数量（点开有间隔/存活/来源） |
| 网格 | **DOM 索引** | 实体 DOM 索引规模（点开有覆盖率与命中率） |
| 网格 | **DOM 节点** | 节点总数 + 最重的子树 |
| 网格 | **缓存条目** | AC 图标 / 状态映射 / AC 日历缓存 |
| 网格 | **卡片规模** | 卡片实例数 + 各卡片耗时排行 |

> 📌 「一键复制」按钮会导出**完整快照文本**（含原始样本序列、环境信息、UA 等），内容比面板上看到的多，适合贴给别人排查；
> **现已同时包含「性能事件流」日志**（定时器 / 订阅 / 索引 / 慢步骤 / hass / 弹窗 / 气泡 / 子卡 / 网络，最新 500 条），一次粘贴即可带走现场，不必再单独点「复制日志」。
> 标题行右侧还有 **「后台」** 按钮：开启后**关掉面板仍继续采集**，重开面板即可看到这期间的数据（口径变化见 25.6.4）。

#### 25.6.2 各指标的读法

#### 有效帧：为什么"平均 0.1ms"不能直接看

hass 每次状态推送都会触发更新链，但绝大多数帧会被**订阅过滤**直接早退（0.0ms）。实测中 `_updateEntitySubscriptions` 出现 47 次时，真正执行实体更新的 `updateEntityStates` 可能只有 5 次 —— 42 个空帧会把真实重活平均掉。

所以面板把耗时分成两段：

```
全帧 平均                 0.1ms      ← 含大量早退帧，横向对比用
有效帧 次数               5/10（执行了实体更新的帧）
有效帧 平均               0.7ms      ← 真实更新链耗时看这个
```

**判断标准**：看「有效帧 平均」。它代表"真的干了活的那一帧花了多久"。

#### 帧率 / 主线程 / 长任务

浏览器**不提供 CPU 占用率 API**（安全边界），所以用三个代理指标：

| 指标 | 判断 |
|------|------|
| **帧率** | 应稳定在 60fps（高刷屏 120）。持续偏低先排查是否被环境限制（浏览器缩放、非整数 DPR、远程桌面），再看卡片 |
| **延迟（定时器漂移）** | 正常 < 5ms。持续偏高说明主线程被占用 |
| **长任务（>50ms）** | 有次数就点开看明细（时间点 + 时长）。**长任务才是卡顿的直接证据**，比百分比直观 |

#### 订阅遗漏：唯一能自动发现"漏订阅"的指标

```
遗漏数    0
结论      索引中的实体全部已在订阅集内
索引实体数 88
订阅实体数 271
统计范围   全页 9 张卡片
```

口径：**索引 = 已渲染且被 DOM 标记依赖的实体**；**订阅集 = 配置扫描出来的实体**。

- **索引有、订阅没有 → 真 Bug**：该实体变化时更新链会被订阅过滤拦掉，界面不刷新。这是 `>0` 会标红的原因。
- **订阅有、索引没有 → 正常**：配置声明了但当前没渲染出对应 DOM（比如弹窗没打开）。

**理想值恒为 0。** 一旦为正，点开明细会列出具体是哪些实体。

#### DOM 索引：覆盖率 18% 不等于故障

点开「DOM 索引」会看到四段，其中两段最容易被误读：

```
── 覆盖率对账 ──      （全页 9 张卡片）
全页使用的实体            483 个
索引实体数                88
索引覆盖率                18%
配置有·索引无             395 个（未渲染出 DOM，当前无需更新）
　其中无订阅              218 个（渲染出 DOM 后会漏刷新）
健康判据                  索引 ⊆ 订阅（「订阅遗漏」为 0）；18% 这类覆盖率低不代表故障
```

- **覆盖率低是正常的**：索引只登记"当前渲染出 DOM 的实体"。未展开的弹窗、未激活的 tab、其他卡片没渲染的部分都不该在里面 —— 483 里的大部分属于此类。
- **真正的健康判据是 `索引 ⊆ 订阅`**（即「订阅遗漏」= 0）。索引里的实体变化会走精准更新，只要它同时在订阅集里，更新链就不会被拦掉。
- **「其中无订阅」才是嫌疑**：这些实体一旦渲染出 DOM 就会漏刷新。现在无害（没 DOM 就没有要更新的东西）。

```
── 精准更新命中 ──    （本卡片 · 采样窗口内）
精准路径调用              40 次
回退全量                  0 次（0%）
平均命中元素              0.0 个/次
```

- **回退全量**是这一段的重点：它表示"索引不可用 → 该次更新退化成全量 `querySelectorAll`"。**理想值 0%**。曾经有个 Bug 让索引全量重建恒为空，表现就是 **100% 回退**，而当时没有任何指标能看出来。
- **命中 0 个/次不是故障**：本卡片索引里只有它自己渲染出的实体，而变更的实体很可能在别的卡片上（多卡片页面极常见）。

#### 定时器明细：间隔 + 存活 + 来源

```
── 定时器明细 ──      （间隔 / 已存活 / 注册来源）
interval #59              2000 ms · 存活 16.2 秒
　↳ 来源                 ()=>{if(!this._isPageVisible)return;this._unifiedTim
interval #134             2000 ms · 存活 11.5 秒
　↳ 来源                 ()=>this._perfTick()
```

- **来源**是回调函数体的源码片段。之所以不用调用栈：打包压缩后 `stack` 只剩 `at e (room-elves-card.js:1:1234567)`，列号能对比但完全不可读；而函数体源码仍保留 `this._unifiedTimerInterval` 这类可辨认特征。
- **判据**：同间隔的定时器看"来源"是否相同 —— **不同 = 各自独立（正常）**，**相同 = 可能重复注册**（这才是泄漏）。
- **存活时间远超预期的定时器**要警惕，例如某个 5 秒定时器已经跑了 3 小时且不再需要。
- 面板自身的「刷新定时器」和「帧率采样 rAF」也会计入，属预期。

#### 后端请求：谁在频繁打后端

```
── 后端请求 ──        （按次数降序）
请求总数                  44
接口数                    13
ha_data_store/query       19 次 · 平均 84.6ms · 最大 109ms
room-elves-card/releases  1 次 · 平均 1161ms · 最大 1161ms
```

用 `PerformanceObserver` 旁路采集**所有** fetch / xhr（零侵入，不改任何一处 `fetch()` 调用），归类键取 URL 末两段路径（去掉 query，使不同参数归为一类）。

- **次数高**的接口，说明有轮询在打它（ikuai-card 3s / fnos 3s / 使用量日历 10s 都是自管轮询）
- **耗时长**的接口（如 800ms+ 的版本检查）会拖慢启动
- **失败请求**（HTTP ≥ 400）会单独标出
- 这里也会包含 HA 自身的请求（如语言包、`ha_data_store`），属预期 —— 它是"整个页面的网络活动"

#### 各卡片耗时：定位"哪张卡在拖累"

```
── 各卡片耗时 ──      （本采样窗口 · 按平均降序）
客厅                      平均 0.1ms · 最大 0.6ms · 10 帧
注意                      仅 1/9 张有样本 —— 打点只对本卡片开启
取全量                    控制台执行 roomElvesPerf.start() 可对所有卡片开打点
```

> ⚠️ **打点是逐卡开关的**：打开面板只会给"面板所在的那张卡"开打点，所以界面入口通常只列出 1 张。**要比较全部卡片，必须用下面的控制台命令**（`roomElvesPerf.start()` 会给所有卡片开打点）。

#### 25.6.3 浏览器控制台命令（roomElvesPerf）

在浏览器控制台（F12）输入 `roomElvesPerf`，或在代码里用 `window.roomElvesPerf`。

**为什么需要它**：性能数据原本只有"打开弹窗 → 切到性能选项卡"才可见，而真实排查场景往往是"页面卡了，但我不能一边开着弹窗一边复现"。控制台 API 让同一套指标可以**不打开界面**就采集与导出。

> ⚠️ **重要前提**：打点默认只在**面板可见**时开启（否则会白白消耗 CPU）。所以直接 `snap()` 通常拿不到数据 —— 必须先用 `start()` 或 `run()` **显式打开采样**。`run()` 会自动处理这个流程。

#### 命令一览

```js
roomElvesPerf.help()        // 帮助 + 用法
roomElvesPerf.run(10)       // ★ 采样 10 秒 → 打印完整快照 → 自动停止
roomElvesPerf.start()       // 开始采样（不打印，后续用 snap() 取）
roomElvesPerf.stop()        // 停止采样
roomElvesPerf.snap()        // 立即打印完整快照（内容 = 面板「一键复制」），并返回文本
roomElvesPerf.index()       // 实体 DOM 索引详情（覆盖率 / 精准更新命中 / 漏订阅排查）
roomElvesPerf.steps()       // 更新链各步骤耗时
roomElvesPerf.subs()        // 订阅实体（全页，按域分组）
roomElvesPerf.cards()       // 各卡片一览（索引 / 订阅 / 节点数 / 耗时）
roomElvesPerf.perf()        // 各卡片耗时排行（哪张卡最慢）
roomElvesPerf.net()         // 后端请求统计（次数 / 平均 / 最大 / 失败）
roomElvesPerf.log(true)     // 事件流开关（定时器 / 订阅 / 更新链 / 索引 / hass / 弹窗 / 气泡 / 子卡 / 网络）
roomElvesPerf.logText()     // 打印事件流文本（= 面板「日志」区「复制日志」的内容）
roomElvesPerf.bg(true)      // ★ 后台运行：关掉面板后**继续采集**（**全局开关** · 仅本次会话，不落盘）
```

#### 25.6.4 后台运行（关掉面板后继续采）

面板标题行右侧有个 **「后台」** 按钮（控制台等价命令 `roomElvesPerf.bg(true/false)`）。

> **这是一个全局开关**（`modules/infra/perf-switch.js` 里的一个变量，**所有卡片共用同一个值**）：
> 在任意一张卡片的调试弹窗上点「后台」、或执行 `roomElvesPerf.bg(true)`，都是**同一件事**；
> 之后**新建的卡片自动继承**（不需要再点一次），也不会出现"某张卡把全局关掉"；
> **刷新页面恢复默认「关」**（会话级，不写 localStorage）。
打开它的效果是：**关闭性能面板之后，采集继续进行** —— 之后任何时候重新打开面板，就能看到这段时间累积的数据（更新链耗时、事件流、后端请求）。适合"我先复现卡顿，再打开面板看"的场景。

> 设计上刻意做了**采集与刷新分离**：
> - **保留（采集层）**：帧耗时样本、更新链各步骤打点、索引命中统计、**事件流**（定时器 / 订阅 / 索引 / hass / 弹窗 / 气泡 / 子卡 / 网络）、长任务与后端请求观测器；
> - **停掉（刷新层）**：面板的 2 秒刷新定时器（含全量 DOM 统计）与帧率采样的 `requestAnimationFrame`。
>
> 也就是说，后台运行**不会**留下"每 2 秒跑一次全量 DOM 查询"或"60fps 常驻 rAF"这类与省性能背道而驰的开销 —— 这正是它与"最小化性能开销"能共存的原因。

**两个必须知道的口径变化**（面板与快照都会如实标注）：

| 指标 | 后台运行期间 |
|---|---|
| 更新链步骤 | 显示为**「后台运行期间累计」**（刷新层停了 ⇒ 不再每 30 秒重置窗口） |
| 帧率 / 主线程延迟 | **不采样**（两者都依赖刷新层）；重开面板后会清零并重新采样，不会引用关闭前的陈旧值 |
| 长任务 / 后端请求 | **继续采样**（观测器是廉价旁路） |

> ⚠️ 开关**仅本次会话生效，不写入 localStorage** —— 刷新页面即回到默认关闭，避免"某次开启后忘了关"。
> `roomElvesPerf.stop()` 会**连带结束后台运行**（避免"以为停了其实还在采"）。

> 💡 **多窗口/多标签**：控制台 API 作用于**当前页面**的卡片。想在另一个 HA 窗口做性能检测，就在**那个窗口**的控制台执行 `roomElvesPerf.run(10)` 或 `bg(true)` —— 采到的自然是那个窗口的数据。


#### 最常用：一条命令完成"取证"

```js
roomElvesPerf.run(10)
```

等价于 `start()` → 等待 10 秒 → `snap()` → `stop()`。**适合"复现卡顿后立刻取证"**：

1. 控制台执行 `roomElvesPerf.run(10)`
2. 立刻去操作页面（点开弹窗、切标签、触发那些你觉得卡的动作）
3. 10 秒后自动输出完整快照，采样同时停止

`snap()` 返回的是**文本**，所以也可以接后续处理：

```js
const text = roomElvesPerf.snap();
copy(text);            // 部分浏览器支持
// 或
console.log(text.length, '字符');
```

#### 与 roomElvesDebug 的区别

| 命令 | 面向 | 用途 |
|------|------|------|
| `roomElvesDebug()` | **调试信息模块系统** | 开关各模块的调试输出、查看模块发送的文本（见 25 节） |
| `roomElvesPerf` | **性能指标** | 采集/导出运行时的耗时、内存、索引、定时器、网络数据 |

两者互不依赖，可同时使用。

#### 命令输出示例

```js
roomElvesPerf.net()
```

```
[room-elves] 后端请求
请求总数  44
接口数  13
ha_data_store/query  19 次 · 平均 84.6ms · 最大 109ms
room-elves-card/releases  1 次 · 平均 1161ms · 最大 1161ms
```

```js
roomElvesPerf.perf()
```

```
[room-elves] 各卡片耗时排行
卡片实例  9 张
有耗时样本  9 张
客厅  平均 1.24ms · 最大 3.80ms · 42 帧
主卧  平均 0.62ms · 最大 1.10ms · 42 帧
```

#### 25.6.4 四个典型排查场景

#### 场景一：页面整体卡顿

```js
roomElvesPerf.run(10)          // 采集期间复现卡顿
```

看快照里的三处：

1. **`[主线程]` 的长任务** —— 有次数和明细（时间点 + 时长），这是卡顿的直接证据
2. **`[更新链步骤耗时]`** —— 哪一步最慢。如果 `updateEntityStates` 占大头，看「精准更新命中」的回退率
3. **`[各卡片耗时]`** —— 哪张卡均值最高

#### 场景二：某个控件不刷新

```js
roomElvesPerf.index()
```

看「订阅遗漏」：

- **> 0** → 该实体在索引里但不在订阅集中 → 实体变化时更新链被拦掉了，附带的实体名就是嫌疑人
- **= 0 但界面确实没刷新** → 看「精准更新命中」的**回退全量**是否为 0%。如果索引覆盖不全，某个控件可能没被纳入更新集

#### 场景三：怀疑定时器泄漏

```js
roomElvesPerf.snap()     // 看 [活跃定时器]
```

关注两点：

- **同间隔的定时器来源是否相同** —— 相同 = 可能重复注册
- **存活时间**是否远超预期（例如弹窗已关，但某个 2 秒定时器还在跑）

更快的定位方式：面板底部的「日志（事件流）」区（或 `roomElvesPerf.logText()`）按时间列出**每一笔**
定时器注册 / 清除，含「来源片段」（回调源码摘要）—— 直接看是谁注册的、什么时候清的。

#### 场景四：后端接口被频繁调用

```js
roomElvesPerf.net()
```

次数高的接口说明有轮询在打它。对照「活跃定时器」的间隔一起看 —— 通常两者能对上（如 10 秒的定时器 → 10 秒一次的 API 调用）。

#### 场景五：想知道「刚才到底发生了什么」

```js
roomElvesPerf.log(true)      // 打开事件流（面板可见时会自动开；这条用于不开面板时）
// …复现问题…
roomElvesPerf.logText()      // 打印事件流（最新在前）；也可用面板「复制日志」
```

事件流包含九类：

| 类型 | 内容 |
|---|---|
| `定时器` | 注册 / 清除，含间隔、`#id`、**来源片段**与 tag（如 `+interval #124 2000ms 来源 ()=>this._perfTick()`） |
| `订阅` | 订阅集重建：前后条数 + 配置版本 |
| `索引` | 实体 DOM 索引重建：全量 / 子树 + 实体数 + 耗时 |
| `步骤` | 更新链**慢步骤**（≥1ms）+ 耗时 |
| `hass` | 每次 hass 更新帧：变更实体数 / 是否走了重活 / 帧耗时 |
| `弹窗` | 弹窗生命周期：`+打开 类型 标题=… 来源 渲染 Xms / 插入+登记 Yms / 合计 Zms 节点 N 子卡 M`、`-关闭 类型 标题=… 存活 Xs 原因=… 清理 定时器 N · 图表 M · 索引 K`、`↻替换 类型 标题=…（旧弹窗直接移除）`。**标题**从弹窗 DOM 取（`showPopup` 没有 title 选项，标题由各卡 content 自建）：`[class*="popup-title"]` → `[class*="popup-header"]` 内的标题 → 任意 `h1~h4`，最多 24 字（多出的 `…`）；取不到就不写 `标题=`，不添噪音。打开/关闭/替换**三行都带**，便于配对。关闭原因只有「点击遮罩」能自动判定，其余如实记为「程序调用」（调用方可传参覆盖） |
| `气泡` | 气泡生命周期：`+气泡 类型 来源=<实体\|.类名\|<标签名>\|虚拟定位目标（无 DOM）> 构建 Xms / 定位 Yms 节点 N 子卡 M`、`-气泡 类型 存活 Xs 原因=…`。**构建** = 目标测量 + 内容解析 + 插入（内容多时主要花在这）；**定位** = 测量与放置（多次强制布局，同规模气泡可能差数倍，用它区分）。来源取不到类名时退化成 `<div>` 这类标签名（`className` 被赋成 undefined 会变成字符串 "undefined"，不再原样照抄）；调用方只传 `buttonRect`/点击点时会临时造一个纯对象作 target，此时标注 **`虚拟定位目标（无 DOM）`**。关闭原因自动区分 `点击遮罩` / `点击外部` / `再次点击目标` / `程序调用`，程序关闭路径（卡片销毁 / 切页）走 `_closeBubble` 也留痕 |
| `子卡` | **卡片工厂**（所有子卡的单一漏斗）：`+子卡 <type> 实体=… <内部容器\|外部卡容器\|HA 自定义元素\|创建失败\|创建失败（抛错）> 创建 Xms 节点 N`。`type: card` 带 `card_config` 会递归解包 ⇒ 两行（外层 + 真实类型）。**抛错路径也留痕**（行尾 `错误=…`），且异常照旧向上抛 |

> 弹窗 / 气泡日志里的 `子卡 N` 就来自这里（**工厂产出**，普通 `div` 容器也算）；`HA M` 则是带 `hass` 的自定义元素 / `hui-*`（与"需要传 hass 的元素"同一判据，二者由单测守着一致）。
| `网络` | fetch / xhr 完成 + 耗时（沿用面板的 PerformanceObserver；同一条请求**跨卡片去重**，因为观察器是每卡一个）。补发的老请求会带真实发生时刻：`ha_data_store/query  371.8ms @63.0s前` —— 观察器 `buffered: true` 会把打开面板前已完成的请求一次性补收，行首的 `-0.0s` 是**写入时间**，两者并存才不会误读成"刚刚打了 30 个请求"。4xx/5xx 追加 `状态=404` |

面板里的「日志」区另有 `暂停 / 清空 / 复制日志` 三个按钮；同一份缓冲也挂在调试卡片的
`perf-log` 开关下（`dump`），两条出口共用一份文本。

**成本**：默认关闭，调用方一律 `if (perfLog.enabled) …` —— 关闭时连字符串都不拼；
打开由「面板可见」驱动（面板一关就停），另给 `roomElvesPerf.log(true/false)` 手动开关；
缓冲是固定 **1000 条**的环形数组（九类事件约覆盖 25~30 秒），同 kind + 同内容 50ms 内合并为 `×N`；「复制日志 / 一键复制」默认导出最新 **500 条**（面板内嵌日志区显示最新 40 条）。

#### 25.6.5 为什么它自己不耗性能

性能工具最怕"测量本身成为负担"。本面板有三层约束：

| 约束 | 做法 |
|------|------|
| **零常驻成本** | 所有打点（hass 耗时 / 步骤耗时 / 更新计数）与定时器、观测器、rAF 采样都只在**面板已构建且可见**时生效。面板没打开时，`_perfRecordHassStart()` / `_perfStepBegin()` 直接返回 0，调用方连 `performance.now()` 都不调 |
| **不可见即停** | 切到「调试」「版本」等其他选项卡时，**打点与 rAF 采样全部停止**（不只是不刷新显示）。原先只跳过了刷新，打点照跑，已修正 |
| **零行为改动** | 唯一插入点是 hass 更新链的计时包装，不改变任何内部逻辑 |

**保留项**（成本可忽略且有用）：

- **2 秒刷新定时器**：它是"检测面板是否可见"的唯一手段（卡片拿不到选项卡切换钩子），一次 `getClientRects()` 的开销可忽略
- **长任务观测器**：回调只在真的发生 >50ms 阻塞时触发，本身接近零成本；切走期间的长任务对"那一刻为什么卡"仍有诊断价值

> 📌 控制台命令 `start()` 会**显式打开所有卡片的打点**；`stop()` 后若面板不存在，会把定时器 / rAF / 观测器全部释放，不留残留。

#### 25.6.6 口径备忘（这些数容易被误读）

| 现象 | 是不是故障 | 说明 |
|------|-----------|------|
| **索引覆盖率只有 18%** | ❌ 不是 | 索引只登记"当前渲染出 DOM 的实体"，未展开的弹窗不该在里面。判据是「订阅遗漏」= 0 |
| **平均命中元素 0.0 个/次** | ❌ 不是 | 变更的实体不在本卡片索引里（多卡片页面常见），同时也说明精准更新对本卡片暂无收益 |
| **各卡片耗时只列出 1 张** | ❌ 不是 | 打点是逐卡开关的，用 `roomElvesPerf.start()` 才能采集全部 |
| **活跃定时器里有个 2000ms** | ❌ 不是 | 那是统一定时器（低频刷新调度器），看「来源」可确认；面板自身的刷新定时器也计入 |
| **后端请求里出现 HA 自身接口** | ❌ 不是 | 采集范围是"整个页面的网络活动"，不只卡片自己的 API |
| **「订阅遗漏」> 0** | ✅ **是** | 真 Bug：该实体变化时界面不会刷新。明细里会列出具体实体 |
| **「回退全量」占比高** | ✅ **是** | 精准更新没在生效（退化成全量遍历），通常是索引覆盖问题 |
| **长任务次数持续 > 0** | ✅ **是** | 主线程被阻塞，点开看时间点与时长 |

#### 25.6.7 三点补充说明

1. **为什么没有"CPU 占用率"**：浏览器不提供读取进程/线程 CPU 占用的 API（安全边界）。用主线程延迟 / 长任务 / 帧率三个标准代理指标代替 —— 它们比一个 `7% → 18%` 的百分比更能定位真问题。
2. **版本信息**：面板首个快照行显示卡片版本号，便于确认运行的是哪一版。
3. **数据窗口**：耗时类指标的统计窗口为**近 30 秒**（每 15 个刷新周期重置一次），避免"平均"一直反映很久以前的帧而看不出当下退化。耗时样本保留最近 10 帧。

---

## 二十六、配置速查表

| 顶层配置 | 说明 | 必须 |
|---------|------|:----:|
| `type: custom:room-elves-card` | 卡片类型标识 | ✅ |
| `room_name` | 房间名称 | 建议 |
| `head` | 是否头部模式 | 否 |
| `mode` | 显示模式 | 否 |
| `entities` | 传感器列表 | 否 |
| `buttons` | 按钮配置 | 否 |
| `automation` | 自动化列表 | 否 |
| `person` | 人员配置 | 否 |
| `overview` | 概览栏配置 | 否 |
| `notice` | 公告栏配置 | 否 |
| `theme` | 主题 | 否 |
| `dark_light_theme` | 暗/亮主题对 | 否 |
| `show_animation` | 动画开关 | 否 |
| `style` | 自定义样式 | 否 |
| `heartbeat_packet` | 心跳包 | 否 |
| `entities_tap_action` | 全局 entities 点击动作配置 | 否 |
| `prohibit_homepage_scroll` | 禁止滚动 | 否 |
| `performance_mode` | 性能模式（auto/desktop/mobile） | 否 |
| `head_columns` | head模式列数，默认6 | 否 |
| `head_rows` | head模式行数，默认auto | 否 |

| 按钮配置 | 说明 | 必须 |
|---------|------|:----:|
| `type` | 按钮类型 | 否 |
| `entity` | 实体ID | 视类型 |
| `name` | 显示名称 | 否 |
| `icon` | 图标 | 否 |
| `on_icon` | 开启图标 | 否 |
| `off_icon` | 关闭图标 | 否 |
| `on_color` | 开启颜色 | 否 |
| `off_color` | 关闭颜色 | 否 |
| `card` | 设备列表 | 视类型 |
| `tap_action` | 点击动作 | 否 |
| `primary` | 主文本 | 否 |
| `show_badge` | 角标 | 否 |
| `badge_entity` | 角标实体 | 否 |
| `badge` | 条件角标数组（独立按钮） | 否 |
| `confirm` | 需要确认 | 否 |
| `close_time` | 弹窗自动关闭秒数 | 否 |
| `show_duration` | 显示持续时长 | 否 |
| `width` | 弹窗宽度 | 否 |
| `per_line` | 每行几个 | 否 |
| `row_column` | 网格位置（head按钮/弹窗item） | 否 |
| `tabs_by` | 聚合弹窗按字段分组 | 否 |
| `group_lights_by_room` | 灯光弹窗按房间分组 | 否 |
| `way` | 计算方式 | 否 |
| `format` | 显示格式 | 否 |
| `rules` | 动态图标规则 | dynamic_icon专用 |
| `global_exception` | 批量操作时跳过此实体 | 否 |
| `light_entity` | 灯光实体 | clothes_dryer专用 |
| `locker` | 锁定模式（默认true） | clothes_dryer专用 |
| `collect_position` | 收藏位置 | clothes_dryer专用 |

| 图表卡片类型 | 渲染方式 | 数据源 | 说明 |
|-------------|----------|--------|------|
| `chart_gauge` | SVG | 单实体 | 仪表图，支持 severity 颜色分段 |
| `chart_progress` | CSS | 多实体(cards) | 多进度条，自动颜色分级 |
| `chart_bar` | CSS | 单实体历史 | 柱状图，支持聚合计算 |
| `chart_line` / `chart` | ECharts | 单实体历史 | 平滑曲线趋势图 |
| `chart_pie` | ECharts | 多实体(cards) | 环形图，中心显示总计 |
| `chart_pie_full` | ECharts | 多实体(chart) | 完整饼图，带图例和标签 |
| `chart_nightingale` | ECharts | 多实体(chart) | 南丁格尔玫瑰图 |
| `chart_heatmap` | ECharts | 实体属性/API | 年度日历热力图 |
| `chart_calendar` | ECharts | 实体属性/API | 月历+年/月/日柱状图，双系列 |
| `chart_mixed` | ECharts | 多实体属性/API | 柱+线+面积组合图，三级下钻 |

| 配置共享 | 说明 | 必须 |
|---------|------|:----:|
| `config_id` | 配置注册 ID（写在 `tap_action` 或 `tabs` 元素内） | 注册时必填 |
| `card_config.from_config_id` | 引用已注册的配置 ID | 引用时必填 |
| `card_config.get_type` | 提取类型：`all` / `entity` / `action` | 否，默认 `all` |
| `card_config.replace_config` | 替换解析结果中的指定键 | 否 |
| `tabs_config.from_config_id` | 组合引用多个配置为选项卡 | tabs_config必填 |
| `tabs_config.from_config_id[].config_id` | 引用的配置 ID | ✅ |
| `tabs_config.from_config_id[].name` | 覆盖选项卡名称 | 否 |
| `tabs_config.from_config_id[].icon` | 覆盖选项卡图标 | 否 |
| `tabs_config.from_config_id[].entity` | 覆盖选项卡实体 | 否 |
| `tabs_config.from_config_id[].entity_value` | 覆盖选项卡实体匹配值 | 否 |
| `tabs_config.from_config_id[].replace_config` | 替换展开后选项卡的指定键 | 否 |
| `tabs_config.config_id` | 为组合后的配置注册 ID（可选） | 否 |

---

## 二十七、常见问题

### Q: 卡片显示"加载中"或空白
A: 检查 JS 和 CSS 文件是否已放到 HA 的 `www` 文件夹，并在仪表板资源中正确添加。

### Q: 按钮点了没反应
A: 确认实体的 Entity ID 是否正确。可以在 HA 的"开发者工具 → 状态"中复制正确的 ID。

### Q: 图标显示不出来
A: 检查图标名称是否正确，以 `mdi:` 开头，如 `mdi:lightbulb`。完整的图标列表可以在 https://pictogrammers.com/library/mdi/ 查询。

### Q: 卡片样式不对（比如透明背景变成白色）
A: 检查 `theme` 配置。如果使用 `transparent` 主题，需要在卡片的 `style` 中设置合适的 `background`。

### Q: 图片/图标闪烁
A: 这是正常的，HA 状态刷新时图标会重新渲染。如果频繁闪烁，检查是否有多个实体状态在快速变化。

### Q: 弹窗打不开或打开了盖不住
A: 可能是 Z-Index 栈出现问题。试试刷新页面。

### Q: 多个 Room Elves Card 在一页上，点击弹窗互相干扰
A: 使用 `prohibit_homepage_scroll` 配置，或者刷新页面重新加载。

### Q: way 计算显示 -- 或没有数据
A: way 计算需要历史数据。确认 HA 已经记录了足够的历史记录（至少包含当天数据）。刚重启 HA 后历史数据可能需要几分钟才能查询到。

### Q: 如何在卡片内调整弹窗宽度
A: 在按钮上设置 `width: 500`（数字，单位为像素）。

---

## 二十八、后记

Room Elves Card 是一个功能非常丰富的卡片，上面涵盖了它的绝大部分功能。由于卡片本身的代码规模接近 15 万行，功能点非常多，如果某个具体功能没有覆盖到，或者配置中遇到问题，欢迎进一步询问。


