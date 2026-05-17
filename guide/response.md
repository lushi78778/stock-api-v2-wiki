# 响应格式与分页

## 统一信封

每次响应都是同一套结构：

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | number | `0` 表示成功 |
| `message` | string | 成功一般为 `success` |
| `data` | object / null | 业务数据；失败时为 `null` |
| `requestId` | string | 排障用，建议日志里记下 |
| `ts` | string | 服务端时间（上海时区） |

## 列表型 data

多数查询接口的 `data` 包含：

| 字段 | 说明 |
|------|------|
| `items` | 当前页数据行数组 |
| `count` | 本页条数 |
| `total` | 精确总数（仅 `includeTotal=true` 时可能有值） |
| `nextCursor` | 下一页游标；没有下一页时为 `null` |
| `hasMore` | 是否还有下一页 |

**注意：** `nextCursor` 是不透明字符串，请原样作为下一请求的 `cursor` 参数传回，不要自行解析或修改。

## 分页示例

第一页：

```bash
curl -sS "$BASE_URL/api/v2/open/market/securities?limit=2" \
  -H "Authorization: Bearer $TOKEN"
```

若 `hasMore` 为 `true`，第二页：

```bash
curl -sS "$BASE_URL/api/v2/open/market/securities?limit=2&cursor=上一页的nextCursor" \
  -H "Authorization: Bearer $TOKEN"
```

## 日期格式

查询参数中的日期统一为 **`yyyy-MM-dd`**（ISO-8601 日历日），例如 `2026-05-13`。
