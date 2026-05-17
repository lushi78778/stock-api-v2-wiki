# 个股日快照（批量）

## 接口用途

查询个股基本信息日快照（动态列）。

> 注意：同时传 trade_date 与 start/end 时，以 start/end 为准。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/snapshots/daily`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `symbols` | query | string | 是 | 逗号分隔 |
| `trade_date` | query | date | 否 | 单日，与 start/end 二选一 |
| `start` | query | date | 否 | 区间起 |
| `end` | query | date | 否 | 区间止 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/snapshots/daily?symbols=000001&trade_date=2026-05-13" \
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
