# 行业板块成分股

## 接口用途

某行业板块在指定交易日的成分股列表。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/boards/industry/{board_code}/constituents`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `board_code` | path | string | 是 | 如 BK0420 |
| `trade_date` | query | date | 是 | 交易日 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/boards/industry/{board_code}/constituents/BK0420/constituents?trade_date=2026-05-13&limit=3" \
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
| `requestId` | `req_c6d7c9bf740842cf9c3bbc9442561769` |
| `ts` | 2026-05-17T20:15:11.929555 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 3 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-13）

| tradeDate | symbol | name | boardCode | changePercent | changeAmount | volume | amount | turnoverRate | latestPrice | sequenceNo | amplitude |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | 000089 | 深圳机场 | BK0420 | -0.29 | -0.02 | 88063 | 6.057e+07 | 0.43 | 6.87 | 12 | 0.87 |
| 2026-05-13 | 000099 | 中信海直 | BK0420 | 0.29 | 0.05 | 84027 | 1.471e+08 | 1.08 | 17.57 | 9 | 1.6 |
| 2026-05-13 | 002928 | 华夏航空 | BK0420 | 0.74 | 0.06 | 294834 | 2.422e+08 | 2.31 | 8.22 | 4 | 2.82 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK0420",
        "symbol": "000089",
        "name": "深圳机场",
        "sequenceNo": 12,
        "changePercent": -0.29,
        "changeAmount": -0.02,
        "latestPrice": 6.87,
        "amount": 60567084.76,
        "volume": 88063,
        "turnoverRate": 0.43,
        "amplitude": 0.87,
        "highPrice": 6.91,
        "lowPrice": 6.85,
        "openPrice": 6.9,
        "prevClose": 6.89,
        "peDynamic": 13.64,
        "pb": 1.19
      },
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK0420",
        "symbol": "000099",
        "name": "中信海直",
        "sequenceNo": 9,
        "changePercent": 0.29,
        "changeAmount": 0.05,
        "latestPrice": 17.57,
        "amount": 147124404.16,
        "volume": 84027,
        "turnoverRate": 1.08,
        "amplitude": 1.6,
        "highPrice": 17.61,
        "lowPrice": 17.33,
        "openPrice": 17.6,
        "prevClose": 17.52,
        "peDynamic": 36.59,
        "pb": 2.47
      },
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK0420",
        "symbol": "002928",
        "name": "华夏航空",
        "sequenceNo": 4,
        "changePercent": 0.74,
        "changeAmount": 0.06,
        "latestPrice": 8.22,
        "amount": 242231511.0,
        "volume": 294834,
        "turnoverRate": 2.31,
        "amplitude": 2.82,
        "highPrice": 8.32,
        "lowPrice": 8.09,
        "openPrice": 8.09,
        "prevClose": 8.16,
        "peDynamic": 19.6,
        "pb": 2.64
      }
    ],
    "count": 3,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImJvYXJkX2luZHVzdHJ5X2NvbnN0aXR1ZW50cyIsIm9yZGVyIjpbInN5bWJvbCJdLCJrZXlzIjp7InN5bWJvbCI6IjAwMjkyOCJ9LCJmaWx0ZXJzIjp7InRyYWRlRGF0ZSI6IjIwMjYtMDUtMTMiLCJib2FyZENvZGUiOiJCSzA0MjAifSwiaXNzdWVkQXQiOiIyMDI2LTA1LTE3VDIwOjE1OjExLjkyOTQ3NiswODowMCJ9",
    "hasMore": true
  },
  "requestId": "req_c6d7c9bf740842cf9c3bbc9442561769",
  "ts": "2026-05-17T20:15:11.929555"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
