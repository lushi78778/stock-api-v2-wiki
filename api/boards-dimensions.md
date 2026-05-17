# 板块维度列表

## 接口用途

板块字典：代码、名称、类型、是否有效。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/boards/dimensions`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `isActive` | query | integer | 否 | 1 有效 0 无效 |
| `boardType` | query | string | 否 | industry / concept |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/boards/dimensions?boardType=industry&limit=3" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

## 响应

> **注意：** 下列数据来自本地实调（`http://127.0.0.1:8788`），行情类示例交易日为 **2026-05-13**。

### 响应信封

| 字段 | 值 |
|------|-----|
| `code` | 0 |
| `message` | success |
| `requestId` | `req_160db501870e4535947579bf81389b14` |
| `ts` | 2026-05-17T20:15:11.887711 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 3 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-13）

| boardCode | boardName | boardType | isActive | firstSeenDate | lastSeenDate |
| --- | --- | --- | --- | --- | --- |
| BK0420 | 航空机场 | industry | 1 | 2026-04-17 | 2026-05-15 |
| BK0421 | 铁路公路 | industry | 1 | 2026-04-21 | 2026-05-15 |
| BK0422 | 物流 | industry | 1 | 2026-04-20 | 2026-05-15 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "boardCode": "BK0420",
        "boardName": "航空机场",
        "boardType": "industry",
        "isActive": 1,
        "firstSeenDate": "2026-04-17",
        "lastSeenDate": "2026-05-15"
      },
      {
        "boardCode": "BK0421",
        "boardName": "铁路公路",
        "boardType": "industry",
        "isActive": 1,
        "firstSeenDate": "2026-04-21",
        "lastSeenDate": "2026-05-15"
      },
      {
        "boardCode": "BK0422",
        "boardName": "物流",
        "boardType": "industry",
        "isActive": 1,
        "firstSeenDate": "2026-04-20",
        "lastSeenDate": "2026-05-15"
      }
    ],
    "count": 3,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImJvYXJkX2RpbWVuc2lvbnMiLCJvcmRlciI6WyJib2FyZFR5cGUiLCJpc0FjdGl2ZSIsImJvYXJkQ29kZSJdLCJrZXlzIjp7ImJvYXJkVHlwZSI6ImluZHVzdHJ5IiwiaXNBY3RpdmUiOiIxIiwiYm9hcmRDb2RlIjoiQkswNDIyIn0sImZpbHRlcnMiOnsiaXNBY3RpdmUiOiIiLCJib2FyZFR5cGUiOiJpbmR1c3RyeSJ9LCJpc3N1ZWRBdCI6IjIwMjYtMDUtMTdUMjA6MTU6MTEuODg3NjEyKzA4OjAwIn0",
    "hasMore": true
  },
  "requestId": "req_160db501870e4535947579bf81389b14",
  "ts": "2026-05-17T20:15:11.887711"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
