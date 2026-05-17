# 概念板块清单

## 接口用途

指定交易日的概念板块排行快照。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/boards/concept`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `trade_date` | query | date | 是 | 交易日 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/boards/concept?trade_date=2026-05-13&limit=3" \
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
| `requestId` | `req_9f43a44f689545ad9d02050f1f8317b2` |
| `ts` | 2026-05-17T20:15:11.916123 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 3 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-13）

| tradeDate | boardCode | boardName | rankNo | changePercent | changeAmount | turnoverRate | leadingStockName | latestPrice | upCount | downCount | totalMarketValue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | BK1152 | 高带宽内存 | 1 | 4.75 | 107.2 | 7.88 | 圣泉集团 | 2363 | 27 | 1 | 1.85e+12 |
| 2026-05-13 | BK0685 | 举牌 | 2 | 4.52 | 137.2 | 0.73 | 可川科技 | 3174 | 4 | 1 | 1.034e+11 |
| 2026-05-13 | BK0674 | 蓝宝石 | 3 | 4.47 | 199.6 | 7.57 | 奥瑞德 | 4662 | 16 | 2 | 8.691e+11 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK1152",
        "boardName": "高带宽内存",
        "rankNo": 1,
        "changePercent": 4.75,
        "changeAmount": 107.25,
        "turnoverRate": 7.88,
        "upCount": 27,
        "downCount": 1,
        "leadingStockName": "圣泉集团",
        "latestPrice": 2362.78,
        "totalMarketValue": 1845695728000.0
      },
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK0685",
        "boardName": "举牌",
        "rankNo": 2,
        "changePercent": 4.52,
        "changeAmount": 137.18,
        "turnoverRate": 0.73,
        "upCount": 4,
        "downCount": 1,
        "leadingStockName": "可川科技",
        "latestPrice": 3174.05,
        "totalMarketValue": 103407861000.0
      },
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK0674",
        "boardName": "蓝宝石",
        "rankNo": 3,
        "changePercent": 4.47,
        "changeAmount": 199.62,
        "turnoverRate": 7.57,
        "upCount": 16,
        "downCount": 2,
        "leadingStockName": "奥瑞德",
        "latestPrice": 4661.74,
        "totalMarketValue": 869078656000.0
      }
    ],
    "count": 3,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImJvYXJkX2NvbmNlcHRfbGlzdCIsIm9yZGVyIjpbImNoYW5nZVBlcmNlbnQiLCJyYW5rTm8iLCJib2FyZENvZGUiXSwia2V5cyI6eyJjaGFuZ2VQZXJjZW50IjoiNC40NzAwIiwiYm9hcmRDb2RlIjoiQkswNjc0IiwicmFua05vIjoiMyJ9LCJmaWx0ZXJzIjp7InRyYWRlRGF0ZSI6IjIwMjYtMDUtMTMifSwiaXNzdWVkQXQiOiIyMDI2LTA1LTE3VDIwOjE1OjExLjkxNjAzOCswODowMCJ9",
    "hasMore": true
  },
  "requestId": "req_9f43a44f689545ad9d02050f1f8317b2",
  "ts": "2026-05-17T20:15:11.916123"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
