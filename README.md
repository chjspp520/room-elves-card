
# Room Elves Card - 房间精灵卡片 完整使用说明

<img width="430" height="932" alt="1" src="https://github.com/user-attachments/assets/8d854761-0073-4f19-9f3b-0e7f14485919" />
<img width="470" height="1002" alt="1" src="https://github.com/user-attachments/assets/f1525554-3592-44c1-855c-464b1b3e40ad" />

# Room Elves Card - 房间精灵卡片 完整使用说明(适用于v5.1.13)



## 一、卡片简介

**Room Elves Card**（房间精灵卡片）是一款功能极为强大的 Home Assistant 自定义卡片，旨在将一个房间（或全屋）的所有设备状态与控制能力集中到一张卡片中，实现"一卡掌控全家"的智能家居体验。

> **作者声明**：本卡片及推荐搭配的 [温湿度卡片](https://github.com/chjspp520/wenshidu-card)、[电力卡片](https://github.com/chjspp520/electricity-info-card)、[HA 数据统一存储系统](https://github.com/chjspp520/ha_data_store) 均由 **chjspp520** 制作维护。
>
> **免责声明**：作者仅提供软件功能，不对数据泄露提供安全保障。数据安全由用户自行负责，使用本软件即代表接受本条款（适用法律以所在地为准）。

### 核心特性

- **30+ 种设备卡片类型支持**：灯光（单灯/灯组）、空调、插座/开关、耗材/电池、暖气/新风机、媒体播放器（支持后台播放/api 列表）、窗帘（单层/双层）、晾衣架（机械仿真拖拽）、风扇、通用设备、动态图标、时间轴、情景模式、快捷操作、按钮组、用户卡片、天气、电话/话费、健康数据、传感器、开关、选择器、数字输入、滑块、文本、按钮、图片、仪表图/进度条/柱状图/曲线图/环形图/饼图/热力图/日历图/混合图表等
- **丰富的弹出控制面板**：每种设备类型都有专属弹窗——灯光面板支持亮度/色温调节、按房间分组、批量开关；空调面板可调温度/模式/风速；窗帘面板支持百分比滑块控制、单双层切换；晾衣架面板带机械仿真拖拽和收藏位置；情景模式支持执行进度展示和状态验证
- **两种显示模式**：
  - **普通模式**：左侧显示房间名称和传感器数据，右侧显示设备操作按钮，适合单房间展示
  - **头部模式（head）**：所有按钮铺满卡片，顶部可显示概览栏（灯光/空调/插座/耗材/环境/人员/能耗统计），适合放在页面顶部作为全屋控制中心
- **通用动作系统（tap_action）**：统一的动作引擎覆盖所有可点击位置，支持 `toggle`（自动推断服务切换开关）、`set_value`（智能推断服务设置目标值）、`quick-action`（快捷操作/情景模式）、`more-info`、`navigate`、`call-service`、`popup_card`、`card`（弹出设备内置控制弹窗）等 10 种动作类型，`toggle` 和 `set_value` 还支持多实体批量操作
- **选项卡系统**：弹窗内支持选项卡分组，具备图标、高亮、自动跳转、条件过滤（display_only）、禁用、角标、分组归属（belong）等高级功能，支持按楼层/区域分组展示
- **程序扩展坞（Dock）**：从屏幕右侧滑入的快捷启动栏，支持头部模式全部按钮类型和动作系统，点击触发按钮展开/收起
- **独立卡片模式（Standalone）**：将单个设备控制面板直接作为一张卡片使用，支持空调、窗帘、媒体、晾衣架、图表等 20+ 种独立卡片类型
- **平页多屏模式**：头部模式下支持多页按钮，横向滑动切换页面，底部圆点指示器显示当前页
- **图表卡片系统**：内置 10 种图表类型——仪表图（纯 SVG）、进度条（纯 CSS）、柱状图（纯 CSS）、曲线图/环形图/饼图/南丁格尔玫瑰图/热力图/日历图/混合图表（ECharts），以及插座功率流向桑基图
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

- **HA 数据统一存储系统** ([ha_data_store](https://github.com/chjspp520/ha_data_store)) — ⚠️ **深度依赖集成**。本卡片已深度适配该集成，通过其 API 接口读取历史数据、播放列表（媒体卡片）、健康数据等。建议优先安装配置。
- **温湿度卡片** ([wenshidu-card](https://github.com/chjspp520/wenshidu-card)) — 房间温湿度传感器数据可视化卡片，支持实时数据展示和历史曲线
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

当 `head: true` 且按钮数量超过一页时，可以通过 `buttons_2`、`buttons_3`…… 等配置将按钮分到多个页面，通过横向滑动切换页面，底部圆点指示器显示当前页位置。

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
| `overview` | ❌ | `array` | `[]` | ⚠️ **仅 head 模式可用**，非 head 模式下配置无效。全屋设备态势概览栏，显示在卡片顶部，支持环境（温湿度）、人员（在家状态）、能耗（用电/功率/余额）、天气（多城市预报）等类型。灯光/空调/插座/耗材概览在 head 模式下自动统计，无需手动配置（详见第十一节） |
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

**常规设备类型：**

| `standalone_type` | 说明 | 实体域 |
|-------------------|------|--------|
| `ac` | 空调控制面板（温度/模式/风速/摆风/使用统计） | `climate` |
| `curtain` | 窗帘控制面板（百分比滑块/双层/开合模式） | `cover` |
| `media` | 媒体控制面板（开关/播放控制） | `media_player` |
| `clothes_dryer` | 晾衣架控制面板（拖拽/收藏位置/灯光联动） | `cover` / `switch` |
| `nas` | NAS 服务器状态卡片（硬盘状态/电源控制/温度风扇） | HP iLO 集成实体 |
| `printer` | 打印机用量统计卡片（墨量/日/月/年用量/累计统计） | `sensor` |
| `fnnas` | 飞牛 NAS 管理卡片（系统信息/电源/Docker/虚拟机管理） | fn_nas 集成实体 |
| `entities_health` | 实体健康状态卡片（按房间/按状态展示全屋实体在线离线情况） | `sensor` |
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

> **注意：** 独立卡片模式与普通/头部模式互斥。配置了 `standalone_type` 后，`head`、`buttons`、`entities`、`overview` 等字段均无效。

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

### 6.8 电话/话费 (type: phone)

显示手机话费余额、流量使用情况等。

```yaml
  - type: phone
    config:                                   # 方式一：使用 config 对象
      monthly_consumption_entity: sensor.phone_monthly
      account_balance_entity: sensor.phone_balance
      points_entity: sensor.phone_points
      total_data_entity: sensor.phone_total
      used_data_entity: sensor.phone_used
      remaining_data_entity: sensor.phone_remaining
      ...（更多字段见下）
```

电话费用支持的所有实体字段：
- `monthly_consumption_entity` - 月消费
- `account_balance_entity` - 账户余额
- `points_entity` - 积分
- `total_data_entity` - 总流量
- `used_data_entity` - 已用流量
- `remaining_data_entity` - 剩余流量
- `data_usage_rate_entity` - 流量使用率
- `total_call_entity` - 总通话时长
- `used_call_entity` - 已用通话
- `remaining_call_entity` - 剩余通话
- `call_usage_rate_entity` - 通话使用率

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
| `card` | ❌ | `array` | 功能开关卡片列表，使用统一卡片系统渲染，2 列网格布局 |

**交互功能说明：**

1. **机械仿真拖拽**：弹窗中的晾衣架可视化区域支持触摸/鼠标拖拽，直接拖动晾杆到目标位置（`locker: false` 时可用）
2. **升降按钮**：提供上升/停止/下降三个按钮，长按持续移动
3. **收藏位置**：一键快速移动到预设位置，带平滑过渡动画，当前位置匹配时按钮高亮（`locker: false` 时显示）
4. **灯光控制**：
   - 壳体右上角的灯光按钮可直接切换 `light_entity` 开关
   - 灯光开启时，壳体下方出现暖黄色倒置梯形光晕照射效果（上窄下宽）
   - 光晕效果实时响应灯光状态变化
5. **功能卡片**：底部 2 列网格展示功能开关卡片；配置了 `light_entity` 时，灯光开关会自动插入首位，无需在 `card` 中手动添加
6. **位置反转自动适配**：自动检测 cover 实体的 `position_reverse` 属性，适配不同品牌晾衣架的正反转逻辑

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

---

### 6.35 使用量日历卡片 (type: usage_calendar)

使用量日历卡片用于展示任意实体的用量/能耗/时长数据，支持日历视图和年/月/日 ECharts 图表视图。数据来源既可以是 [HA 数据统一存储系统](https://github.com/chjspp520/ha_data_store/releases)（ha_data_store）API，也可以是实体属性。

**四个选项卡视图：**

| 选项卡 | 说明 |
|------|------|
| 日历 | 月历网格，每个单元格显示当日用量和时长，点击有数据的日期弹出详情 |
| 年 | 年度柱状图（ECharts），显示所有可用年份的用量/能耗对比 |
| 月 | 月度柱状图（ECharts），显示选定年份 12 个月的用量/能耗对比 |
| 日 | 日度柱状图（ECharts），显示选定月份每日的用量/能耗对比 |

**数据源配置：**

支持两种数据源，优先使用 API，未配置 API 时使用实体属性。

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
- **年选项卡**：直接显示年度柱状图，无导航栏
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
| `calculate` | number | `1.0` | 费用换算系数 |

---

### 6.36 打印机用量统计卡片 (type: printer)

打印机用量统计卡片用于展示打印机（如 HP）的墨量、日/月/年用量、累计统计。数据来源为打印机用量统计实体（`sensor.hp_printer_yong_liang_tong_ji`）的 `attributes`。

点击按钮弹出打印机用量统计面板，支持通过 `popup_card` 或 `card` 动作打开。

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
      action: popup_card                 # 或 action: card（走独立弹窗）
      popup_position: clone_button_top
      width: 400px                       # 外层弹窗宽度（可选）
      card:
        type: printer
        name: HP Printer 用量统计        # 可选，弹窗标题，默认同上
        entity: sensor.hp_printer_yong_liang_tong_ji  # 可选，默认此实体
```

#### 配置字段

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `name` | 否 | `string` | 弹窗标题（显示在顶部） |
| `entity` | 否 | `string` | 打印机用量统计实体 ID，默认 `sensor.hp_printer_yong_liang_tong_ji` |
| `width` | 否 | `string` | `card` 动作下弹窗宽度（默认 `560px`），`popup_card` 下用 `tap_action.width` |
| `popup_position` | 否 | `string` | 弹窗位置（默认 `center`），`popup_card` 下用 `tap_action.popup_position` |

#### 卡片布局

```
┌─────────────────────────────┐
│ 🖨  HP Printer 用量统计      │  ← 标题 + 最新日期
│    HP Printer · 最近更新 xx  │
├─────────────────────────────┤
│ 墨量概览                     │  ← 区块标题（带分割线）
│ [█ 黑色 0%  已换5次·累计198] │  ← 墨盒卡（≤20% 标红）
│ [█ 青色 17% 已换7次·累计408] │
│ [█ 品红 7% ...]  [█ 黄色 7%] │
├─────────────────────────────┤
│ 今日用量 · 2026-08-05        │
│ [🖨 3] [⇄ 0] [⧉ 0] [🖯 0] [⚠ 0]│
├─────────────────────────────┤
│ 月度统计                     │
│ 月份     打印  扫描  复印 ... │
├─────────────────────────────┤
│ 累计总量                     │
│ [8758] [1015] [154] [0] [67] │
├─────────────────────────────┤
│ 近日记录                     │
│ 日期     打印  扫描  复印 ... │  ← 日期列自适应宽度，0 值留空
└─────────────────────────────┘
```

#### 交互说明

- **墨量概览**：显示 4 色墨盒的剩余百分比（带进度条）、替换次数和累计使用量，剩余 ≤20% 时百分比标红
- **今日用量**：显示最新日期当天的打印/扫描/复印/传真/卡纸五项指标
- **月度统计 / 近日记录**：表格展示，日期/月份列按内容自适应宽度，数值为 0 的格子留空不显示
- **累计总量**：打印机累计打印/扫描/复印/传真/卡纸总数

> **依赖说明**：打印机卡片数据来源于打印机用量统计实体（`sensor.hp_printer_yong_liang_tong_ji`），需安装对应打印机状态统计集成生成该实体。页面纯 DOM 构建（无 `innerHTML` 拼接），CSS 全部外置到 `room-elves-card-styles.css`。

---

### 6.37 飞牛 NAS 管理卡片 (type: fnnas)

飞牛 NAS 管理卡片用于展示飞牛 NAS 系统信息，并支持系统电源管理、Docker 容器管理、虚拟机管理。数据来源于 [fn_nas 集成](Y:\custom_components\fn_nas) 生成的传感器 / 开关 / 按钮实体。

点击按钮弹出飞牛 NAS 管理面板，支持通过 `popup_card` 或 `card` 动作打开。

卡片从上到下分为 **6 个区域**：

| 区域 | 内容 |
|------|------|
| 1. 卡片标题 | 名称 + 分割线 |
| 2. 系统信息 | 内存总大小/已使用、系统运行时长、主板温度、CPU 温度 |
| 3. 硬盘信息 | 各磁盘状态（型号 + 状态/温度 + 健康状态，`disk_1`、`disk_2`...） |
| 4. 系统管理 | 电源管理（关机/开机）、重启主机 |
| 5. Docker 管理 | 容器列表，支持启动/停止/重启 + 状态显示 |
| 6. 虚拟机管理 | 虚拟机列表，支持启动/停止/重启 + 状态显示 |

#### 配置示例

```yaml
  - entity: input_boolean.fn_nas
    type: sensor
    name: 飞牛NAS
    icon: mdi:nas
    tap_action:
      action: popup_card                 # 或 action: card（走独立弹窗）
      width: 480px
      card:
        type: fnnas
        name: 飞牛 NAS
        system:
          # --- 系统信息 ---
          system_status: sensor.fei_niu_nasxi_tong_jian_kong_xi_tong_zhuang_tai      # 系统状态（含运行时长属性）
          memory_available: sensor.fei_niu_nasxi_tong_jian_kong_ke_yong_nei_cun      # 内存（含总内存/已用内存属性）
          cpu_temp: sensor.fei_niu_nasxi_tong_jian_kong_cpuwen_du                    # CPU 温度（可选）
          motherboard_temp: sensor.fei_niu_nasxi_tong_jian_kong_zhu_ban_wen_du       # 主板温度（可选）
        control:
          # --- 系统管理 ---
          power: switch.fei_niu_nasxi_tong_dian_yuan                                 # 电源开关
          reboot: button.fei_niu_nasxi_tong_zhong_qi                                 # 重启主机按钮
        disk:
          # --- 硬盘信息（按分组显示，每组可多个磁盘 disk_1/disk_2...） ---
          - name: 系统
            disk_1: sensor.colorful_sl500_2tb_ying_pan_..._zhuang_tai
          - name: 存储
            disk_1: sensor.wdc_wd40efrx_68n32n0_ying_pan_..._zhuang_tai
            disk_2: sensor.wdc_wd40efrx_68n32n0_ying_pan_..._zhuang_tai
        # --- Docker 管理（显式配置每个容器） ---
        docker:
          - name: XiaomiMusic
            status: sensor.xiaomusic_zhuang_tai
            switch: switch.xiaomusic_rong_qi
            restart: button.xiaomusic_zhong_qi
          - name: go2rtc
            status: sensor.go2rtc_zhuang_tai
            switch: switch.go2rtc_rong_qi
            restart: button.go2rtc_zhong_qi
        # --- 虚拟机管理（显式配置每台虚拟机） ---
        vm:
          - name: Windows 7
            status: sensor.windows_7_zhuang_tai
            switch: switch.windows_7_dian_yuan
            restart: button.windows_7_zhong_qi
          - name: Ubuntu
            status: sensor.ubuntu_zhuang_tai
            switch: switch.ubuntu_dian_yuan
            restart: button.ubuntu_zhong_qi
```

#### 配置字段

**顶层：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `name` | 否 | `string` | 卡片标题（默认 `飞牛 NAS`） |
| `system` | 否 | `object` | 系统信息配置块（见下表） |
| `control` | 否 | `object` | 系统管理配置块（`power` / `reboot`） |
| `disk` | 否 | `array` | 硬盘分组数组，每项 `{ name, disk_1, disk_2... }` |
| `docker` | 否 | `array` | Docker 容器数组，每项 `{ name, status, switch, restart }` |
| `vm` | 否 | `array` | 虚拟机数组，每项 `{ name, status, switch, restart }` |

**`system` 配置块：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `system_status` | 否 | `string` | 系统状态传感器，读取 `运行时间` 属性 |
| `memory_available` | 否 | `string` | 可用内存传感器，读取 `总内存 (GB)`、`已用内存 (GB)` 属性 |
| `cpu_temp` | 否 | `string` | CPU 温度传感器 |
| `motherboard_temp` | 否 | `string` | 主板温度传感器 |

**`control` 配置块：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `power` | 否 | `string` | 电源开关（`switch.xxx_power`） |
| `reboot` | 否 | `string` | 重启主机按钮（`button.xxx_reboot`） |

**`disk` 数组每项（硬盘分组）：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `name` | 否 | `string` | 分组名（如 `系统` / `存储`，显示为组标签） |
| `disk_1` / `disk_2` ... | 否 | `string` | 该组磁盘传感器，可多个（`disk_1`、`disk_2`...），可为状态或温度传感器 |

**`docker` / `vm` 数组每项：**

| 字段 | 必填 | 类型 | 说明 |
|------|:----:|------|------|
| `name` | 是 | `string` | 容器/虚拟机名称（显示在行内） |
| `status` | 否 | `string` | 状态传感器实体 ID |
| `switch` | 否 | `string` | 启动/停止开关实体 ID |
| `restart` | 否 | `string` | 重启按钮实体 ID |

> **向后兼容**：旧的扁平写法（`power_switch`/`reboot_button`、`system` 内 `disk_N`、`docker_status_prefix` + `docker_containers` 等）仍可使用，但推荐使用上面的 `system` / `control` / `disk` / `docker` / `vm` 嵌套结构。

#### 磁盘说明

磁盘通过 `disk` 数组分组配置，支持多组（如 系统 / 存储），每组内可多个磁盘（`disk_1`、`disk_2`...）。磁盘可为**状态传感器**或**温度传感器**：

- **状态传感器**：`state` 为 `空闲中` / `活动中`，`attributes` 含 `硬盘型号`、`健康状态`（良好/异常）、`状态`、`总容量`、`序列号`、`通电时间` 等
- **温度传感器**：`state` 为温度数值，`attributes` 含 `健康状态`

**显示样式**：硬盘信息区域采用与 NAS 卡片一致的**拟物硬盘槽位**风格（金属拉丝纹理 + LED 状态灯 + 图标 + 容量），所有磁盘在**同一横向槽位行**排列（过多时自动换行），槽位顶部显示所属分组名（如 `系统` / `存储`）。健康状态正常显示绿色呼吸灯、异常显示红色闪烁灯。

#### 交互说明

- **系统信息**：内存显示"已用/总 GB"，温度自动补 `°C` 单位
- **硬盘信息**：拟物硬盘槽位，显示分组名 + 图标 + 型号 + 容量 + LED 状态灯；**点击槽位弹出硬盘详情气泡**（型号、序列号、容量、健康状态、通电时间、温度等）
- **系统管理**：电源开关点击直接切换；重启主机点击弹出确认对话框
- **Docker / 虚拟机**：每行显示名称 + 运行状态徽标 + 启动/停止/重启按钮；重启操作弹出确认对话框
- 容器/虚拟机的状态根据其状态实体判断：`on`/`运行中`/`running` 视为运行中

> **依赖说明**：飞牛 NAS 卡片数据来源于 [fn_nas 集成](Y:\custom_components\fn_nas)。使用前需先安装并配置 fn_nas 集成生成对应实体。页面纯 DOM 构建（无 `innerHTML` 拼接），CSS 全部外置到 `room-elves-card-styles.css`。

---

### 6.38 爱快路由管理卡片 (type: ikuai)

爱快路由管理卡片用于展示爱快路由器运行状态，并支持 Docker 容器与虚拟机管理。数据来源于 [ikuai_router 集成](Y:\custom_components\ikuai_router) 生成的 sensor / switch / camera 实体。

卡片采用**三选项卡结构**（默认在"路由系统"），点击按钮弹出管理面板，支持通过 `popup_card` 或 `card` 动作打开。

**选项卡**：

| 选项卡 | 内容 |
|--------|------|
| 路由系统 | 系统信息、硬件信息（折叠）、在线客户端、网络信息、应用流量（环形图）、路由器管理 |
| Docker | 容器列表，显示名称/状态/IP/CPU 占用，支持启停 + 日志查看 |
| 虚拟机 | 每台 VM 的画面（开机显示摄像头画面，关机显示占位）、核心/内存/CPU 占用、启停开关 |

#### 配置示例

```yaml
  - entity: input_boolean.ikuai
    type: sensor
    name: 爱快
    icon: mdi:router-network
    tap_action:
      action: popup_card
      width: 400px
      card:
        type: ikuai
        name: 爱快
        router:
          - sys_info: sensor.ikuai_overview
            name: 系统信息
          - hardware_info: sensor.ikuai_system_info
            name: 硬件信息
          - online_client: sensor.ikuai_online_client
            name: 在线客户端
          - network_info: sensor.ikuai_iface_check
            name: 网络信息
          - app_flow_1d: sensor.ikuai_app_flow_1d
            name: 1天应用流量
          - app_flow_1h: sensor.ikuai_app_flow_1h
            name: 1小时应用流量
          - app_flow_30min: sensor.ikuai_app_flow_30min
            name: 30分钟应用流量
        network_control:
          - mac_address: text.ikuai_mac_input
          - allow: button.ikuai_yun_xu_lian_wang
          - reject: button.ikuai_jin_zhi_lian_wang
        network_traffic:
          - speed: 网速
            upload: sensor.ikuai_upload
            download: sensor.ikuai_download
          - total: 合计流量
            upload: sensor.ikuai_totalup
            download: sensor.ikuai_totaldown
        log:
          - log: sensor.ikuai_audit_url_log
        docker:
          - name: NextTerminal
            entity: switch.ikuai_docker_nextterminal
          - name: AdGuardHome
            entity: switch.ikuai_docker_adguardhome
        vm:
          - name: win7
            entity: switch.ikuai_vm_win7
            camera: camera.ikuai_vm_win7
```

#### 配置项说明

| 配置项 | 必填 | 类型 | 说明 |
|--------|:----:|------|------|
| `type` | ✅ | `string` | `ikuai` |
| `name` | 否 | `string` | 卡片标题（默认 `爱快`） |
| `width` | 否 | `string` | 弹窗宽度（默认 `400px`） |
| `router` | 否 | `array` | 路由系统区域数组，按数组顺序渲染 |
| `router[].sys_info` | 否 | `string` | 系统信息实体（`sensor.ikuai_overview`） |
| `router[].hardware_info` | 否 | `string` | 硬件信息实体（`sensor.ikuai_system_info`，折叠显示） |
| `router[].online_client` | 否 | `string` | 在线客户端实体（`sensor.ikuai_online_client`） |
| `router[].network_info` | 否 | `string` | 网络信息实体（`sensor.ikuai_iface_check`） |
| `router[].app_flow_1d` | 否 | `string` | 1天应用流量实体（`sensor.ikuai_app_flow_1d`） |
| `router[].app_flow_1h` | 否 | `string` | 1小时应用流量实体（`sensor.ikuai_app_flow_1h`） |
| `router[].app_flow_30min` | 否 | `string` | 30分钟应用流量实体（`sensor.ikuai_app_flow_30min`） |
| `network_control` | 否 | `array` | 在线客户端联网控制配置 |
| `network_control[].mac_address` | 否 | `string` | MAC 地址写入实体（`text.ikuai_mac_input`） |
| `network_control[].allow` | 否 | `string` | 允许联网按钮（`button.ikuai_yun_xu_lian_wang`） |
| `network_control[].reject` | 否 | `string` | 禁止联网按钮（`button.ikuai_jin_zhi_lian_wang`） |
| `network_traffic` | 否 | `array` | 流量图表配置（点击系统信息标题栏速度区域弹出 ECharts 流量图表） |
| `network_traffic[].speed` | 否 | `string` | 网速分组（值可为标题，如 `网速`） |
| `network_traffic[].upload` | 否 | `string` | 上行速度实体 |
| `network_traffic[].download` | 否 | `string` | 下行速度实体 |
| `network_traffic[].total` | 否 | `string` | 合计流量分组（值可为标题，如 `合计流量`） |
| `log` | 否 | `array` | 客户端访问历史配置 |
| `log[].log` | 否 | `string` | 访问历史实体（`sensor.ikuai_audit_url_log`） |
| `docker` | 否 | `array` | Docker 容器数组 |
| `docker[].name` | 否 | `string` | 容器显示名 |
| `docker[].entity` | ✅ | `string` | 容器电源开关实体（`switch.ikuai_docker_*`） |
| `vm` | 否 | `array` | 虚拟机数组 |
| `vm[].name` | 否 | `string` | 虚拟机显示名 |
| `vm[].entity` | ✅ | `string` | 虚拟机电源开关实体（`switch.ikuai_vm_*`） |
| `vm[].camera` | 否 | `string` | VM 画面摄像头实体（`camera.ikuai_vm_*`） |

#### 交互说明

- **系统信息**：运行时长 / CPU（占用+温度）/ 内存（已用+总量）每行一条；标题栏右侧显示实时上/下行速度（配置 `network_traffic` 后点击速度区域弹出流量图表）
- **硬件信息**：整合在系统信息内，默认折叠，点击展开显示 CPU / 内存 / 硬盘 / 主板
- **在线客户端**：名称+IP 小字、上行/下行速度与流量两行显示、按 IP 升序排列、刷新保持滚动位置；客户端名称中的 `%20`/`%` 自动替换为 `_`
  - **联网开关**：根据 `client.reject`（0 允许 / 1 禁止）显示开关状态（允许绿色、禁止红色）；点击开关先把 MAC 写入 `mac_address` 实体，再根据当前状态按 allow/reject 按钮（用开关模拟点击按钮）
  - **访问历史**：配置 `log` 后点击客户端名称/单元格弹出气泡，显示该客户端（按 MAC 过滤）的访问历史（时间/应用名/访问地址/备注）
- **网络信息**：线路检测状态 chips + 各接口 IP/连接数/上下行速度/累计流量；点击接口名弹出详情气泡（线路检测信息 + 流量信息）
- **流量图表**：配置 `network_traffic` 后点击系统信息标题栏速度区域弹出气泡，标题"流量"，右侧"1小时/12小时/1天"周期切换按钮，上方实时速度曲线 + 下方累计流量曲线（ECharts 渲染，气泡宽度为卡片宽度的 90%）
- **应用流量**：近30分钟/1小时/1天合并为一个区域，标题栏切换按钮 + SVG 环形图（中心总量 + 协议占比图例），单位智能换算 B→MB/GB/TB
- **路由器管理**：重启、重连 WAN，均弹出确认对话框
- **Docker / 虚拟机**：每行显示名称 + 状态徽标 + 启停开关；Docker 支持查看日志气泡
- **虚拟机画面**：开机显示摄像头实体画面（HA 系统自带 picture 卡片），关机显示"已关机"占位；信息栏含全屏按钮，点击弹出全屏 VM 画面弹窗

#### 刷新机制

卡片只构建一次 DOM，**周期刷新仅更新各数据容器内部内容**（不重建结构），保留选项卡状态、VM 画面、折叠状态、滚动位置。默认每 10 秒局部刷新一次。

> **依赖说明**：爱快路由卡片数据来源于 [ikuai_router 集成](Y:\custom_components\ikuai_router)。使用前需先安装并配置该集成生成对应实体。页面纯 DOM 构建（无 `innerHTML` 拼接），CSS 全部外置到 `room-elves-card-styles.css`。

### 6.39 实体健康状态卡片 (type: entities_health)

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

---

## 七、通用动作系统（tap_action）

所有支持 `tap_action` 的位置（按钮、title_entities、entities 区域、传感器卡片等）共享同一套动作执行引擎。动作类型统一，配置方式一致，`set_value` 和 `toggle` 还支持 `entities` 多实体批量操作。

### 统一动作清单

| action | 说明 | 支持多实体 | 必需参数 |
|--------|------|:----------:|----------|
| `toggle` | 切换开关状态（on↔off），自动推断服务 | ✅ | `entity` 或 `entities` |
| `set_value` | 设置实体目标值，自动推断服务（最灵活） | ✅ | `entity` 或 `entities` + `value` |
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
| `phone` | 话费信息面板 | 余额/流量/通话 |
| `health` | 健康数据面板 | 步数/心率等 |
| `scene_mode` | 情景模式气泡 | 气泡选择/执行进度 |

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

灯光、插座、耗材等弹窗以及自由布局弹窗（`show_free_layout_popup` / `popup_card`）都支持使用选项卡来分类显示设备。选项卡功能非常丰富，支持图标、高亮、自动跳转、条件过滤、禁用、角标等。

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
```

---

### 11.11 公告栏（Notice Bar）

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

当 `head: true` 且按钮数量超过一页时，可以通过 `buttons_2`、`buttons_3`…… 等配置将按钮分到多个页面，通过横向滑动切换页面，底部圆点指示器显示当前页位置。

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
| `printer` | 打印机用量统计卡片 | `entity`、`name` |
| `fnnas` | 飞牛 NAS 管理卡片 | `name`、`system_status`、`power_switch`、`docker_containers`、`vms` |

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
| `phone` | `showPhonePopup()` | `phone-control-popup` | 话费面板 |
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
| `printer` | 打印机用量统计卡片 | `entity`, `name` |
| `fnnas` | 飞牛 NAS 管理卡片 | `name`, `system_status`, `power_switch`, `docker_containers`, `vms` |
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

## 二十五、常见问题

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

## 二十七、后记

Room Elves Card 是一个功能非常丰富的卡片，上面涵盖了它的绝大部分功能。由于卡片本身的代码规模接近 9 万行，功能点非常多，如果某个具体功能没有覆盖到，或者配置中遇到问题，欢迎进一步询问。

