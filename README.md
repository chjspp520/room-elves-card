

# Room Elves Card - 房间精灵卡片 完整使用说明

---适用于v2.x.x，部分说明不适用于与后续版本

## 一、卡片简介

**Room Elves Card**（房间精灵卡片）是一款功能非常强大的 Home Assistant 自定义卡片。它可以集中展示一个房间（或全屋）的所有设备状态，支持灯光、空调、插座、耗材、暖气、传感器、媒体设备等多种设备类型，并提供丰富的弹出控制面板、历史数据图表、平面户型图、天气、能耗等多种信息。

配置代码请前往：https://bbs.hassbian.com/thread-31645-1-1.html

卡片支持两种显示模式：

- **普通模式**：左侧显示房间名称和传感器数据，右侧显示设备操作按钮
- **头部模式（head）**：所有按钮铺满卡片，顶部可显示概览栏，适合放在页面顶部作为全屋控制中心

<div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap;">
  <img src="https://github.com/chjspp520/room-elves-card/blob/main/1.png" alt="截图" style="width: 30%; height: auto; margin: 5px;">
  <img src="https://github.com/chjspp520/room-elves-card/blob/main/2.png" alt="截图" style="width: 30%; height: auto; margin: 5px;">
  <img src="https://github.com/chjspp520/room-elves-card/blob/main/3.png" alt="截图" style="width: 30%; height: auto; margin: 5px;">
  <img src="https://github.com/chjspp520/room-elves-card/blob/main/GIF.gif" alt="截图" style="width: 80%; height: auto; margin: 5px;">

---

## 二、如何安装

1.  将文件 `room-elves-card.js` 和 `room-elves-card-styles.css` 放入 Home Assistant 配置目录下的 `www` 文件夹中。
2.  打开 Home Assistant 仪表盘，点击右上角的"编辑仪表盘"按钮。
3.  点击右下角的"添加卡片"按钮（+号）。
4.  在搜索框中搜索"Room Elves Card"或"房间精灵"。
5.  如果找不到，通常需要在 HA 侧边栏的"配置" → "仪表盘" → 右上角三点菜单 → "资源"中，添加一个 JavaScript 模块资源，路径填 `/local/room-elves-card.js`。添加后刷新页面即可找到。
6.  也可以直接使用 YAML 编辑模式添加：

```yaml
type: custom:room-elves-card
room_name: 客厅
```

---

## 三、基础配置结构

卡片的所有配置都写在 YAML 中（在 HA 添加卡片时的编辑界面里设置）。最外层的结构如下：

```yaml
type: custom:room-elves-card       # 固定写法，告诉 HA 使用这张卡片
room_name: 客厅                     # 房间名称，会显示在卡片上
mode: grouped                       # 显示模式，保持 groupd 即可
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
```

> 注意：YAML 配置对缩进非常敏感，请使用 2 个空格作为缩进，不要使用 Tab 键。

---

## 四、添加传感器数据区域（entities）

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

> 找实体 ID 的方法：在 HA 的"开发者工具" → "状态"中，可以看到所有可用的实体。

---

## 五、按钮配置详解（核心功能）

`buttons` 是卡片最重要的配置，每个按钮可以控制一种或一组设备。

### 5.1 灯光组 (type: lights)

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
      - entity: light.living_floor_lamp
        name: 落地灯
        room: 客厅
    group_lights_by_room: true             # 在弹窗中按房间分组显示
    show_badge: true                       # 显示已开启的灯的数量角标
    per_line: 2                            # 弹窗中每行显示几个灯
    close_time: 300                        # 自动关闭倒计时（秒），0=不自动关闭
```

### 5.2 单灯 (type: light)

控制单个灯。功能与灯光组类似，但只控制一个设备。

```yaml
  - type: light
    entity: light.bedroom_light             # 灯的实体ID
    name: 卧室灯
    on_color: '#f1c40f'
    off_color: '#95a5a6'
    show_duration: true                     # 显示已开启时长
```

### 5.3 空调 (type: ac)

显示空调状态，点击弹出空调控制面板（可调温度、模式、风速）。

```yaml
  - type: ac
    icon: mdi:air-conditioner
    card:
      - entity: climate.living_room          # 空调的实体ID
        name: 客厅空调
        room: 客厅
```

空调图标会根据运行模式自动变化（雪花=制冷、太阳=制热、水滴=除湿、风扇=吹风），并带有旋转动画。

### 5.4 插座/开关 (type: socket)

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
    show_badge: true
    per_line: 2
    shwo_sankey: false                       # 是否显示功率流向桑基图（需ECharts）
```

### 5.5 耗材/电池 (type: consumables)

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

### 5.6 暖气/新风机 (type: heater)

控制地暖、新风、换气等设备。配置在 `tap_action.card` 中。

```yaml
  - type: heater
    icon: mdi:radiator
    tap_action:
      card:
        wind:                                 # 吹风模式
          entity: switch.heater_wind
          icon: mdi:fan
        heat:                                 # 加热模式
          entity: select.heater_mode
          icon: mdi:fire
          options:                            # select实体对应的选项
            on:
              - 加热
              - 强热
        vent:                                 # 换气模式
          entity: switch.heater_vent
          icon: mdi:air-filter
        dehumidify:                           # 除湿模式
          entity: switch.heater_dehumidify
          icon: mdi:water-percent
```

### 5.7 媒体设备 (type: media)

控制电视、音响、投影仪等媒体播放设备。

```yaml
  - type: media
    entity: media_player.living_room_tv       # 媒体设备实体
    icon: mdi:television
    on_icon: mdi:television
    off_icon: mdi:television-off
    on_color: '#2ecc71'
    off_color: '#e74c3c'
```

### 5.8 通用设备 (type: device)

适用于门磁、窗磁、人体传感器等开关型设备。

```yaml
  - type: device
    entity: binary_sensor.front_door          # 设备实体
    icon: mdi:door
    on_icon: mdi:door-open                    # 开启时图标
    off_icon: mdi:door-closed                 # 关闭时图标
    on_color: '#e74c3c'
    off_color: '#2ecc71'
```

### 5.9 用户信息卡片 (type: user)

在卡片中嵌入一个用户信息卡，显示头像、位置、天气、导航等。

```yaml
  - type: user
    entity: person.zhangsan
    name: 张三
    avatar:                                   # 头像配置
      entity: sensor.zhangsan_avatar_url
      size: 48
    at_home:                                  # 在家状态
      entity: binary_sensor.zhangsan_home
      total_entity: sensor.family_members
      used_entity: sensor.at_home_count
    location:                                 # 位置
      entity: sensor.zhangsan_location
      show_location: sensor.location_address  # 显示地址
    city_entity: sensor.city_name
    weather_entity: weather.hefeng            # 天气实体
    temp_entity: sensor.outdoor_temp
    name_entity: sensor.zhangsan_display_name
    distance_entity: sensor.zhangsan_distance # 距离
    time_entity: sensor.zhangsan_arrive_time  # 预计到达时间
    navigation:                               # 导航配置（使用高德地图）
      amap_web_key: 你的高德Web端Key
      amap_web_js_key: 你的高德JS API Key
      home_coordinates: 116.397428,39.90923   # 家的经纬度
```

### 5.10 电话/话费 (type: phone)

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

### 5.11 健康 (type: health)

显示健康数据入口，点击弹出健康数据控制面板。

```yaml
  - type: health
    icon: mdi:heart-pulse
    user:                                     # 家庭成员列表
      - entity: sensor.step_count
        name: 步数
      - entity: sensor.heart_rate
        name: 心率
```

### 5.12 动态图标 (type: dynamic_icon)

这是最灵活的按钮类型。可以根据实体的不同状态，自动切换图标、颜色和动画。多条规则同时匹配时可以循环显示。

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
        animation: shake                    # 可用的动画：shake, rotate, blink, breathe, jump
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

**条件支持的操作符：**
| 操作符 | 说明 | 示例 |
|-------|------|------|
| `==` | 等于 | `value: 'on'` |
| `!=` | 不等于 | `value: 'off'` |
| `>` | 大于 | `value: '30'` |
| `<` | 小于 | `value: '10'` |
| `>=` | 大于等于 | `value: '60'` |
| `<=` | 小于等于 | `value: '20'` |
| `contains` | 包含 | `value: '异常'` |
| `between` | 在范围内 | `value: '20,30'`（表示20到30之间）|

**复合条件（AND/OR）：**
```yaml
      - condition:
          logic: and                      # 所有条件必须同时满足
          conditions:
            - entity: binary_sensor.door
              operator: '=='
              value: 'on'
            - entity: sensor.temperature
              operator: '>'
              value: '25'
        icon: mdi:door-open
        color: '#e74c3c'
```

支持的条件值也可以写成数组（相当于 OR）：
```yaml
          value: ['on', 'active', 'playing']   # 匹配其中任意一个就算满足
```

### 5.13 时间轴 (type: timeline)

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

### 5.14 内嵌卡片 (type: card)

在 head 模式中嵌入其他 HA 卡片（如天气预报、地图等）。

```yaml
  - type: card
    card_config:
      type: weather-forecast
      entity: weather.home
```

### 5.15 独立按钮（无 type）

如果不写 type，就是一个独立的开关按钮，只控制一个实体。

```yaml
  - entity: switch.some_switch          # 实体ID
    icon: mdi:toggle-switch             # 图标
    on_icon: mdi:toggle-switch          # 开启时图标
    off_icon: mdi:toggle-switch-off     # 关闭时图标
    on_color: '#2ecc71'                 # 开启时颜色
    off_color: '#e74c3c'                # 关闭时颜色
    name: 开关                          # 名称
```

---

## 六、按钮通用配置

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
| `show_badge` | 显示角标数字 | `true` |
| `badge_entity` | 指定实体值作为角标 | `sensor.count` |
| `confirm` | 点击是否需要确认 | `true` |
| `primary` | 按钮下方的文字 | `已开启3个` |
| `tap_action` | 点击动作（见下文） | 见下 |
| `width` | 弹窗宽度（像素） | `400` |
| `per_line` | 弹窗每行按钮数 | `3` |
| `popup_position` | 弹窗位置 | `top`, `bottom`, `left`, `right` |

**点击动作（tap_action）详解：**

```yaml
tap_action:
  action: toggle                     # 切换开关
```

可用的 action 值：

- **`toggle`** — 切换设备开关（最常用）
- **`toggle-all`** — 切换分组中所有设备的开关
- **`more-info`** — 弹出 HA 自带的详细信息弹窗
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

---

## 七、弹窗中的选项卡（Tabs）

灯光、插座、耗材等弹窗支持使用选项卡来分类显示设备：

```yaml
  - type: lights
    tabs:                                 # 启用选项卡模式
      - name: 客厅                        # 选项卡名称
        icon: mdi:sofa                    # 选项卡图标
        entity: binary_sensor.living_motion  # 用于判断设备是否在运行的实体（自动跳转用）
        entity_value: 'on'                # 匹配值
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
        icon: mdi:bed
        disabled: true                    # 禁用此选项卡
        rows:
          - row: 1
            items:
              - entity: light.bedroom_light
                name: 卧室灯
    display_only: ['on']                  # 仅显示设备开启的选项卡
    auto_redirect: true                   # 自动跳转到最后开启的设备对应的选项卡
```

---

## 八、人员/人在传感器（Person）

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
```

每个人物实体图标旁有个小历史图标，点击可查看该实体的历史记录时间轴。

---

## 九、自动化开关

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

## 十、概览栏（Overview Bar）- Head 模式专用

当 `head: true` 时，可以在卡片顶部显示一条全屋设备态势概览栏。它会自动统计各设备类型的运行状态数量，点击可弹出对应的控制面板。

### 10.1 灯光概览
自动从 `type: lights` 按钮中统计已开启的灯数量，无需额外配置。

### 10.2 空调概览
自动从 `type: ac` 按钮中统计已开启的空调数量。

### 10.3 插座概览
自动从 `type: socket` 按钮中统计已开启的插座数量。

### 10.4 耗材概览
自动从 `type: consumables` 按钮中统计已低于阈值的耗材数量。

### 10.5 环境概览（需配置）
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

### 10.6 人员概览（需配置）
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

### 10.7 能耗概览（需配置）
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

### 10.8 天气概览（需配置）

```yaml
overview:
  - type: weather
    entity: weather.hefeng_weather      # 建议使用和风天气集成
```

### 10.9 自定义设备概览（需配置）
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

### 10.10 其他概览配置项

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

## 十一、主题设置

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

---

## 十二、心跳包（检测卡片是否正常运行）

卡片可以定期向一个传感器写入递增的数值，用来判断卡片是否还在运行。如果写不进去了，说明卡片可能出问题了。

```yaml
heartbeat_packet:
  entity: sensor.room_card_heartbeat    # 用来接收心跳值的实体（必须是数字型传感器）
  interval: 10                          # 多少秒写入一次（建议10-60秒）
  whether_send: switch.heartbeat_enable # 一个开关实体控制是否发送（on=发送）
  show_breathe: true                    # 在房间名称旁边显示一个呼吸点
```

> 心跳值为递增整数（1, 2, 3...），可以在 HA 中创建一个 `input_number` 或 `sensor` 实体来接收。

---

## 十三、禁止首页滚动

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

> `way` 写的是"计算方式"，`format` 写的是"显示格式"。`{_default}` 会被计算结果替换。

### 所有可用的 way

#### 通用
| way 名称 | 说明 | 示例结果 |
|---------|------|---------|
| `state` | 取原始状态值 | `on` / `off` |
| `friendly_state` | 显示中文友好状态 | `开启` / `关闭` |
| `last_changed` | 距上次状态变化过了多久 | `2时15分前` |
| `last_updated` | 距上次更新过了多久 | `5分前` |

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
    format: '今天用了{_default}次'       # 显示格式
```

> 注意：单实体时在 format 中用 `{_default}`，多实体时用 `{别名.way名}`。

---

## 十七、HTML 模板引擎（用于 primary 文本）

按钮下方的"primary"文本支持使用模板来动态显示数据。

```yaml
buttons:
  - type: lights
    card:
      - entity: light.living
        name: 客厅灯
    primary: '{{states("light.living")}}'   # 显示灯的状态
```

### 模板语法入门

**1. 变量替换：**
```yaml
primary: '当前的温度是 {{t1}} 度'
primary: '家里的湿度是 {{s1}}%'
```

**2. 条件判断：**
```yaml
primary: '{{#if t1>30}}太热了！{{/if}} {{#if t1<10}}太冷了！{{/if}}'
```

**3. 数据计算函数：**

| 函数 | 说明 | 示例 |
|------|------|------|
| `SUM(a,b)` | 求和 | `{{SUM(t1,t2)}}` |
| `SUB(a,b)` | 相减 | `{{SUB(t1,5)}}` |
| `MUL(a,b)` | 相乘 | `{{MUL(power,0.001)}}` 转千瓦 |
| `DIV(a,b)` | 相除 | `{{DIV(used,total)}}` |
| `MAX(a,b)` | 最大值 | `{{MAX(t1,t2,t3)}}` |
| `MIN(a,b)` | 最小值 | `{{MIN(v1,v2)}}` |
| `AVG(a,b)` | 平均值 | `{{AVG(t1,t2,t3)}}` |
| `ABS(n)` | 绝对值 | `{{ABS(n)}}` |
| `ROUND(n,1)` | 四舍五入保留1位小数 | `{{ROUND(t1,1)}}` |
| `IF(条件,true值,false值)` | 条件判断 | `{{IF(t1>30,'很热','还好')}}` |
| `EACH_SUM(alias,'prop')` | 数组属性求和 | `{{EACH_SUM(items,'value')}}` |
| `EACH_AVG(alias,'prop')` | 数组属性平均 | `{{EACH_AVG(items,'price')}}` |
| `EACH_COUNT(alias)` | 数组元素个数 | `{{EACH_COUNT(items)}}` |

**4. 循环：**
```yaml
primary: '{{#each items as item}} 第{{item._index}}个: {{item.name}} {{/each}}'
```

**5. Javeler 风格模板（兼容 Jinja2）：**
```yaml
primary: |
  {% set total = states('sensor.power1') + states('sensor.power2') %}
  {% if total > 1000 %}
    当前功率偏高：{{ total }}W
  {% else %}
    当前功率正常：{{ total }}W
  {% endif %}
```

---

## 十八、配置共享（多个卡片共用配置）

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

---

## 十九、平面户型图

需要在 person 配置中引用一个 JSON 或 YAML 文件，里面定义了每个房间的形状（多边形坐标）。

### 准备坐标文件

文件路径示例：`/local/point.json`

```json
{
  "rooms": [
    {
      "id": "客厅",
      "points": "10,10 200,10 200,150 10,150",
      "labelX": 100,
      "labelY": 80,
      "dataX": 100,
      "dataY": 100
    },
    {
      "id": "卧室",
      "points": "210,10 400,10 400,150 210,150",
      "labelX": 305,
      "labelY": 80
    }
  ]
}
```

> `points` 格式：`x1,y1 x2,y2 x3,y3 ...` 用空格分隔坐标对。
> `labelX/labelY` 是房间名称显示位置，`dataX/dataY` 是数据显示位置。

### 在 person 配置中引用

```yaml
person:
  - main_entity: binary_sensor.living_motion
    room_point_from: /local/point.json
    rooms:
      客厅: binary_sensor.living_motion
      卧室: binary_sensor.bedroom_motion
    corner_radius: 8                     # 房间圆角大小
    room_name_font_size: 16              # 房间名字体
```

YAML 格式也同样支持。

---

## 二十、外部 API 历史数据

如果你的设备历史数据不在 HA 数据库中，而是在一个外部服务器上，可以配置 API 地址：

```yaml
buttons:
  - type: socket
    api_base_url: http://192.168.1.100:8080
    api_device_name: 客厅-插座1           # 格式：房间名-设备名
```

卡片会自动从外部 API 拉取历史状态数据，用于时间轴和趋势显示。

---

## 二十一、ECharts 图表

卡片内置了 ECharts 图表功能（用于桑基图、曲线图等）。需要将 `echarts.min.js` 放在 HA 的 `/local/` 目录下。

下载地址：https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js

如果 `/local/` 下没有这个文件，卡片会自动从 CDN 加载。

---

## 二十二、首次使用快速上手

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

## 二十三、常见问题

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

## 二十四、配置速查表

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
| `theme` | 主题 | 否 |
| `dark_light_theme` | 暗/亮主题对 | 否 |
| `show_animation` | 动画开关 | 否 |
| `style` | 自定义样式 | 否 |
| `heartbeat_packet` | 心跳包 | 否 |
| `prohibit_homepage_scroll` | 禁止滚动 | 否 |
| `performance_mode` | 性能模式 | 否 |
| `head_columns` | head模式列数 | 否 |

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
| `confirm` | 确认 | 否 |
| `width` | 弹窗宽度 | 否 |
| `per_line` | 每行几个 | 否 |
| `row_column` | 网格位置 | 否 |
| `way` | 计算方式 | 否 |
| `format` | 显示格式 | 否 |
| `rules` | 动态图标规则 | dynamic_icon专用 |

---

## 二十五、后记

Room Elves Card 是一个功能非常丰富的卡片，上面涵盖了它的绝大部分功能。由于卡片本身的代码规模接近 5 万行，功能点非常多，如果某个具体功能没有覆盖到，或者配置中遇到问题，欢迎进一步询问。
