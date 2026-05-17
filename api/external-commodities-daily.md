# 外盘商品/期货日 K

## 接口用途

external_commodity_daily 日线数据。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/external/commodities/daily`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `commodities` | query | string | 否 | 如 gold,copper |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/external/commodities/daily?start=2026-05-15&end=2026-05-15&limit=5" \
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
