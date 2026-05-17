# 证券检索（分页）

## 接口用途

按代码或名称模糊搜索证券主数据。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/securities`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `q` | query | string | 否 | 匹配代码或名称 |
| `code` | query | string | 否 | 仅匹配代码 |
| `name` | query | string | 否 | 仅匹配名称 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/securities?q=银行&limit=5" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

## 响应

### 响应示例（JSON）

```json
{"code":0,"data":{"items":[{"symbol":"000001","name":"平安银行"}],"count":1}}
```

### 响应字段（节选）

| 字段 | 说明 |
|------|------|
| `code` | 0 为成功 |
| `data.items` | 数据行 |
| `data.nextCursor` | 下一页游标 |
| `data.hasMore` | 是否还有下一页 |

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
