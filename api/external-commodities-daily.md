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

curl -sS "$BASE_URL/api/v2/open/market/external/commodities/daily?start=2026-05-15&end=2026-05-15&limit=2" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

## 响应

> **注意：** 下列数据来自本地实调（`http://127.0.0.1:8788`），行情类示例交易日为 **2026-05-15（商品库示例日）**。

### 响应信封

| 字段 | 值 |
|------|-----|
| `code` | 0 |
| `message` | success |
| `requestId` | `req_2c4feaf6c4fa49f88ff640cbd7beec4d` |
| `ts` | 2026-05-17T20:15:12.075664 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 2 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-15（商品库示例日））

| tradeDate | volume | commodity | displayName | sourceSymbol | barTimeUtc8 | sourceMarket | openPrice | closePrice | highPrice | lowPrice | settlePrice |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | 1.837e+05 | brent_oil | 布伦特原油 | OIL | 2026-05-15T00:00 | SINA_FOREIGN | 106.6 | 109 | 109.7 | 106.3 | — |
| 2026-05-15 | 0 | copper | 铜 | HG | 2026-05-15T00:00 | SINA_FOREIGN | 658 | 629.2 | 658.7 | 627 | 0 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-15",
        "commodity": "brent_oil",
        "displayName": "布伦特原油",
        "sourceSymbol": "OIL",
        "barTimeUtc8": "2026-05-15T00:00",
        "sourceMarket": "SINA_FOREIGN",
        "openPrice": 106.58,
        "closePrice": 109.04,
        "highPrice": 109.68,
        "lowPrice": 106.26,
        "settlePrice": null,
        "volume": 183748.0,
        "openInterest": 0.0,
        "currency": "USD",
        "unit": "barrel"
      },
      {
        "tradeDate": "2026-05-15",
        "commodity": "copper",
        "displayName": "铜",
        "sourceSymbol": "HG",
        "barTimeUtc8": "2026-05-15T00:00",
        "sourceMarket": "SINA_FOREIGN",
        "openPrice": 658.0,
        "closePrice": 629.2,
        "highPrice": 658.7,
        "lowPrice": 627.05,
        "settlePrice": 0.0,
        "volume": 0.0,
        "openInterest": 0.0,
        "currency": "USD",
        "unit": "pound"
      }
    ],
    "count": 2,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImV4dGVybmFsX2NvbW1vZGl0eV9kYWlseSIsIm9yZGVyIjpbInRyYWRlRGF0ZSIsImNvZGUiLCJzb3VyY2VTeW1ib2wiXSwia2V5cyI6eyJ0cmFkZURhdGUiOiIyMDI2LTA1LTE1IiwiY29kZSI6ImNvcHBlciIsInNvdXJjZVN5bWJvbCI6IkhHIn0sImZpbHRlcnMiOnsiY29tbW9kaXRpZXMiOltdLCJzdGFydCI6IjIwMjYtMDUtMTUiLCJlbmQiOiIyMDI2LTA1LTE1In0sImlzc3VlZEF0IjoiMjAyNi0wNS0xN1QyMDoxNToxMi4wNzU1MTcrMDg6MDAifQ",
    "hasMore": true
  },
  "requestId": "req_2c4feaf6c4fa49f88ff640cbd7beec4d",
  "ts": "2026-05-17T20:15:12.075664"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
