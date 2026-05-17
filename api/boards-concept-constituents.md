# 概念板块成分股

## 接口用途

某概念板块在指定交易日的成分股列表。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/boards/concept/{board_code}/constituents`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `board_code` | path | string | 是 | 板块代码 |
| `trade_date` | query | date | 是 | 交易日 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/boards/concept/{board_code}/constituents/BK0425/constituents?trade_date=2026-05-13&limit=2" \
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
| `requestId` | `req_ab396257c1f44338b6acf4cacd1c7aa0` |
| `ts` | 2026-05-17T20:15:11.94417 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 2 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-13）

| tradeDate | symbol | name | boardCode | changePercent | changeAmount | volume | amount | turnoverRate | latestPrice | sequenceNo | amplitude |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | 000010 | *ST美丽 | BK0425 | 0 | 0 | 704417 | 1.943e+08 | 8.11 | 2.73 | 38 | 7.33 |
| 2026-05-13 | 000032 | 深桑达Ａ | BK0425 | 2.28 | 0.43 | 300378 | 5.75e+08 | 2.64 | 19.25 | 11 | 4.46 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK0425",
        "symbol": "000010",
        "name": "*ST美丽",
        "sequenceNo": 38,
        "changePercent": 0.0,
        "changeAmount": 0.0,
        "latestPrice": 2.73,
        "amount": 194280044.23,
        "volume": 704417,
        "turnoverRate": 8.11,
        "amplitude": 7.33,
        "highPrice": 2.86,
        "lowPrice": 2.66,
        "openPrice": 2.73,
        "prevClose": 2.73,
        "peDynamic": 28.98,
        "pb": 10.66
      },
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK0425",
        "symbol": "000032",
        "name": "深桑达Ａ",
        "sequenceNo": 11,
        "changePercent": 2.28,
        "changeAmount": 0.43,
        "latestPrice": 19.25,
        "amount": 574961765.09,
        "volume": 300378,
        "turnoverRate": 2.64,
        "amplitude": 4.46,
        "highPrice": 19.46,
        "lowPrice": 18.62,
        "openPrice": 18.65,
        "prevClose": 18.82,
        "peDynamic": -70.97,
        "pb": 3.17
      }
    ],
    "count": 2,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImJvYXJkX2NvbmNlcHRfY29uc3RpdHVlbnRzIiwib3JkZXIiOlsic3ltYm9sIl0sImtleXMiOnsic3ltYm9sIjoiMDAwMDMyIn0sImZpbHRlcnMiOnsidHJhZGVEYXRlIjoiMjAyNi0wNS0xMyIsImJvYXJkQ29kZSI6IkJLMDQyNSJ9LCJpc3N1ZWRBdCI6IjIwMjYtMDUtMTdUMjA6MTU6MTEuOTQ0MDQ1KzA4OjAwIn0",
    "hasMore": true
  },
  "requestId": "req_ab396257c1f44338b6acf4cacd1c7aa0",
  "ts": "2026-05-17T20:15:11.94417"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
