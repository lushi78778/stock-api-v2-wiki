# 板块股票池（去重）

## 接口用途

从成分股提取去重 symbol/name，便于后续批量拉 K 线。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/boards/symbols`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `boardTypes` | query | string | 否 | 板块类型 |
| `boardCodes` | query | string | 否 | 板块代码 |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/boards/symbols?boardTypes=industry&boardCodes=BK0420&start=2026-05-13&end=2026-05-13&limit=3" \
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
| `requestId` | `req_157d40ad4df54a8f8cc34b6006fce844` |
| `ts` | 2026-05-17T20:15:12.022796 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 3 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-13）

| symbol | name |
| --- | --- |
| 000089 | 深圳机场 |
| 000099 | 中信海直 |
| 002928 | 华夏航空 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "symbol": "000089",
        "name": "深圳机场"
      },
      {
        "symbol": "000099",
        "name": "中信海直"
      },
      {
        "symbol": "002928",
        "name": "华夏航空"
      }
    ],
    "count": 3,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImJvYXJkX3N5bWJvbHMiLCJvcmRlciI6WyJzeW1ib2wiXSwia2V5cyI6eyJzeW1ib2wiOiIwMDI5MjgifSwiZmlsdGVycyI6eyJzdGFydCI6IjIwMjYtMDUtMTMiLCJib2FyZFR5cGVzIjpbImluZHVzdHJ5Il0sImVuZCI6IjIwMjYtMDUtMTMiLCJib2FyZENvZGVzIjpbIkJLMDQyMCJdfSwiaXNzdWVkQXQiOiIyMDI2LTA1LTE3VDIwOjE1OjEyLjAyMjcyMiswODowMCJ9",
    "hasMore": true
  },
  "requestId": "req_157d40ad4df54a8f8cc34b6006fce844",
  "ts": "2026-05-17T20:15:12.022796"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
