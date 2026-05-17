# 批量板块成分股

## 接口用途

跨板块、跨日期批量拉成分股。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/boards/constituents`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `boardTypes` | query | string | 否 | 板块类型 |
| `boardCodes` | query | string | 否 | 板块代码 |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `withStockInfo` | query | boolean | 否 | 是否补充个股信息，默认 true |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/boards/constituents?boardTypes=industry&boardCodes=BK0420&start=2026-05-13&end=2026-05-13&limit=2" \
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
| `requestId` | `req_6942ca541bfa4d38bc1e0ea66b7481b3` |
| `ts` | 2026-05-17T20:15:12.009465 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 2 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-13）

| tradeDate | symbol | name | boardCode | boardType | changePercent | changeAmount | volume | amount | turnoverRate | latestPrice | sequenceNo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | 000089 | 深圳机场 | BK0420 | industry | -0.29 | -0.02 | 88063 | 6.057e+07 | 0.43 | 6.87 | 12 |
| 2026-05-13 | 000099 | 中信海直 | BK0420 | industry | 0.29 | 0.05 | 84027 | 1.471e+08 | 1.08 | 17.57 | 9 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "boardType": "industry",
        "tradeDate": "2026-05-13",
        "boardCode": "BK0420",
        "symbol": "000089",
        "name": "深圳机场",
        "sequenceNo": 12,
        "latestPrice": 6.87,
        "changePercent": -0.29,
        "changeAmount": -0.02,
        "volume": 88063,
        "amount": 60567084.76,
        "amplitude": 0.87,
        "highPrice": 6.91,
        "lowPrice": 6.85,
        "openPrice": 6.9,
        "prevClose": 6.89,
        "turnoverRate": 0.43,
        "peDynamic": 13.64,
        "pb": 1.19,
        "floatMarketValue": 14088538231.29,
        "totalMarketValue": 14088786526.83,
        "totalShares": 2050769509.0,
        "floatShares": 2050733367.0,
        "industryName": "航空机场",
        "listingDate": "1998-04-20"
      },
      {
        "boardType": "industry",
        "tradeDate": "2026-05-13",
        "boardCode": "BK0420",
        "symbol": "000099",
        "name": "中信海直",
        "sequenceNo": 9,
        "latestPrice": 17.57,
        "changePercent": 0.29,
        "changeAmount": 0.05,
        "volume": 84027,
        "amount": 147124404.16,
        "amplitude": 1.6,
        "highPrice": 17.61,
        "lowPrice": 17.33,
        "openPrice": 17.6,
        "prevClose": 17.52,
        "turnoverRate": 1.08,
        "peDynamic": 36.59,
        "pb": 2.47,
        "floatMarketValue": 13630281307.09,
        "totalMarketValue": 13630281307.09,
        "totalShares": 775770137.0,
        "floatShares": 775770137.0,
        "industryName": "航空机场",
        "listingDate": "2000-07-31"
      }
    ],
    "count": 2,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImJvYXJkX2NvbnN0aXR1ZW50c19iYXRjaCIsIm9yZGVyIjpbInRyYWRlRGF0ZSIsImJvYXJkVHlwZSIsImJvYXJkQ29kZSIsInN5bWJvbCJdLCJrZXlzIjp7InRyYWRlRGF0ZSI6IjIwMjYtMDUtMTMiLCJib2FyZENvZGUiOiJCSzA0MjAiLCJib2FyZFR5cGUiOiJpbmR1c3RyeSIsInN5bWJvbCI6IjAwMDA5OSJ9LCJmaWx0ZXJzIjp7ImJvYXJkVHlwZXMiOlsiaW5kdXN0cnkiXSwiYm9hcmRDb2RlcyI6WyJCSzA0MjAiXSwic3RhcnQiOiIyMDI2LTA1LTEzIiwid2l0aFN0b2NrSW5mbyI6dHJ1ZSwiZW5kIjoiMjAyNi0wNS0xMyJ9LCJpc3N1ZWRBdCI6IjIwMjYtMDUtMTdUMjA6MTU6MTIuMDA5MzQxKzA4OjAwIn0",
    "hasMore": true
  },
  "requestId": "req_6942ca541bfa4d38bc1e0ea66b7481b3",
  "ts": "2026-05-17T20:15:12.009465"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
