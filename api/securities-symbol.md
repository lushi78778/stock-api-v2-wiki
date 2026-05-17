# 证券检索（单条）

## 接口用途

按 6 位代码精确查询一只证券。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/securities/{symbol}`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `symbol` | path | string | 是 | 证券代码 |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/securities/{symbol}/000001" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

## 响应

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
