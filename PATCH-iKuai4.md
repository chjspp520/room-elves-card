# iKuai 4.0 兼容补丁（`{code, results}` 信封）

## 问题

iKuai 3.x OpenAPI 的响应信封是：

```json
{ "Result": 30000, "Data": { ... } }
```

iKuai 4.0（实测 4.0.315）改成了：

```json
{ "code": 0, "message": "Success", "results": { ... } }
```

卡片在 `_ikuaiAllApiCall()` 里只判断 `i.Result`：4.0 下 `Number(undefined)` 不是有限数，于是走
`{ok:true, data:i.Data||{}}`，`data` 变成空对象——"iKuai 全览" 的四个页签
（应用类型 / 连接类型 / 访问记录 / 历史记录）全部空白。

## 修复（解析层，一行分支）

在 `const n=Number(i.Result);` **之前**插入：

```js
if(typeof i.code==="number"){return 0===i.code?{ok:!0,data:i.results||{},raw:i}:{ok:!1,error:"iKuai 返回 "+i.code+"："+String(i.message||i.ErrMsg||"")}}
```

- `code === 0`：把 `results` 作为 `data` 返回；
- `code !== 0`：报 `"iKuai 返回 <code>：<message>"`；
- 3.x 的 `Result/Data` 逻辑**原样保留**，双向兼容（3.x 信封没有顶层 `code` 字段，不会误入新分支）。

下游无需改动：4.0 `results` 的键与旧 `Data` 一致（`terminal_flow` / `conn`+`conn_num` / `data`+`total`），
`_ikuaiAllApiPageRows()` 取数组、`_ikuaiAllApiPageInfo()` 取 `total` 的逻辑全部命中。

`_ikuaiAllApiBatch()` 当前在 bundle 中没有调用点（四个页签都走 `_ikuaiAllApiCall`），无需处理；
即使将来启用，它的逐条回退路径也调用 `_ikuaiAllApiCall`，可继承本补丁。

## 对构建前源码的等价修改

如果直接改构建前的源码：在 iKuai API 调用的响应解析处（`await resp.json()` 之后）加同样的分支——
先判断 `typeof json.code === "number"`（4.0 信封），命中则按 `code`/`results` 处理，
否则再走原有的 `Result`/`Data` 逻辑。

## 自动补丁脚本

对 release 附件的 `room-elves-card.js` 直接打补丁（压缩后的变量名自动适配）：

```python
#!/usr/bin/env python3
# 用法: python patch_ikuai4.py room-elves-card.js
import hashlib, re, sys

path = sys.argv[1]
src = open(path, 'rb').read().decode('utf-8')

m = re.search(r'const (\w+)=Number\((\w+)\.Result\);', src)
if not m:
    sys.exit('未找到 Result 解析锚点（可能已适配或压缩结构变化），请人工确认')

obj = m.group(2)  # 响应对象变量名，当前构建为 i
ins = ('if(typeof %(o)s.code==="number"){return 0===%(o)s.code?'
       '{ok:!0,data:%(o)s.results||{},raw:%(o)s}:'
       '{ok:!1,error:"iKuai 返回 "+%(o)s.code+"："+String(%(o)s.message||%(o)s.ErrMsg||"")}}'
       ) % {'o': obj}

if ins in src:
    sys.exit('已经打过补丁')

out = src[:m.start()] + ins + src[m.start():]
data = out.encode('utf-8')
open(path, 'wb').write(data)
print('patched: %d bytes (+%d), sha256 %s'
      % (len(data), len(data) - len(src.encode('utf-8')), hashlib.sha256(data).hexdigest()))
```

对 v6.14.72 release 附件（4,548,556 B）执行结果：**4,548,711 B（+155 B）**，
SHA-256 `5b8b4570f2cd762716b27235c62f183d9acc299ed8967cd9c173b8714befdec2`。

打完补丁后建议同步重新生成 `.gz`（HA 优先返回 `.gz`，只换 `.js` 不生效）。

## 验证

- `node --check room-elves-card.js` 通过；
- 抽取 `_ikuaiAllApiCall` 用 node 单测：

| 模拟响应 | 结果 |
|---|---|
| 3.x `{Result:30000, Data:{a:1}}` | `{ok:true, data:{a:1}}` |
| 3.x `{Result:20001, ErrMsg:"bad"}` | `{ok:false, error:"iKuai 返回 20001：bad"}` |
| 4.0 `{code:0, results:{terminal_flow,conn,data,total}}` | `{ok:true, data:{terminal_flow,conn,data,total}}` |
| 4.0 `{code:1, message:"fail-reason"}` | `{ok:false, error:"iKuai 返回 1：fail-reason"}` |
| 4.0 `{code:500, ErrMsg:"legacy-msg"}` | `{ok:false, error:"iKuai 返回 500：legacy-msg"}` |

- `.gz` 解压回读与 `.js` 逐字节一致。

实测环境：iKuai 4.0.315，补丁后四个页签恢复正常渲染；3.x 逻辑未改动。
