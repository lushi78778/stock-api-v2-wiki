# 外盘股票/ETF 日 K

## 接口用途

external_market_daily 日线数据。

> 示例日期 2026-05-13 为文档演示用，请按库内实际日期查询。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/external/markets/daily`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `tickers` | query | string | 否 | 逗号分隔，如 NVDA,SPY |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/external/markets/daily?start=2026-05-13&end=2026-05-13&limit=2" \
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
| `requestId` | `req_97ed06ef8be648e3a26dcc85c5ae0202` |
| `ts` | 2026-05-17T20:15:12.063248 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 2 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-13）

| tradeDate | name | volume | amount | ticker | sourceSymbol | closeTimeUtc8 | sourceMarket | openPrice | closePrice | highPrice | lowPrice |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | Applied Materials | 7.839e+06 | — | AMAT | AMAT | 2026-05-14T04:00 | US | 435.9 | 436.6 | 440.5 | 422.3 |
| 2026-05-13 | AMD | 3.042e+07 | — | AMD | AMD | 2026-05-14T04:00 | US | 457 | 445.5 | 459.5 | 432.6 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-13",
        "ticker": "AMAT",
        "sourceSymbol": "AMAT",
        "closeTimeUtc8": "2026-05-14T04:00",
        "name": "Applied Materials",
        "sourceMarket": "US",
        "openPrice": 435.91,
        "closePrice": 436.61,
        "highPrice": 440.5,
        "lowPrice": 422.3,
        "volume": 7839354.0,
        "amount": null
      },
      {
        "tradeDate": "2026-05-13",
        "ticker": "AMD",
        "sourceSymbol": "AMD",
        "closeTimeUtc8": "2026-05-14T04:00",
        "name": "AMD",
        "sourceMarket": "US",
        "openPrice": 457.035,
        "closePrice": 445.5,
        "highPrice": 459.5,
        "lowPrice": 432.65,
        "volume": 30423201.0,
        "amount": null
      }
    ],
    "count": 2,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImV4dGVybmFsX21hcmtldF9kYWlseSIsIm9yZGVyIjpbInRyYWRlRGF0ZSIsImNvZGUiLCJzb3VyY2VTeW1ib2wiXSwia2V5cyI6eyJ0cmFkZURhdGUiOiIyMDI2LTA1LTEzIiwiY29kZSI6IkFNRCIsInNvdXJjZVN5bWJvbCI6IkFNRCJ9LCJmaWx0ZXJzIjp7InRpY2tlcnMiOltdLCJlbmQiOiIyMDI2LTA1LTEzIiwic3RhcnQiOiIyMDI2LTA1LTEzIn0sImlzc3VlZEF0IjoiMjAyNi0wNS0xN1QyMDoxNToxMi4wNjMxNDYrMDg6MDAifQ",
    "hasMore": true
  },
  "requestId": "req_97ed06ef8be648e3a26dcc85c5ae0202",
  "ts": "2026-05-17T20:15:12.063248"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
