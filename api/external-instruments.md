# 外盘标的/商品列表

## 接口用途

外盘股票/ETF 与商品期货标的字典。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/external/instruments`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `assetType` | query | string | 否 | market 或 commodity |
| `q` | query | string | 否 | 关键词 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/external/instruments?limit=3" \
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
| `requestId` | `req_a6946921cf4643c3a62b846f0d209f19` |
| `ts` | 2026-05-17T20:15:12.049358 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 3 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-13）

| name | assetType | code | sourceSymbol | sourceMarket | currency | unit | firstTradeDate | lastTradeDate | count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 布伦特原油 | commodity | brent_oil | OIL | SINA_FOREIGN | USD | barrel | 2026-04-01 | 2026-05-15 | 32 |
| 铜 | commodity | copper | HG | SINA_FOREIGN | USD | pound | 2026-04-01 | 2026-05-15 | 32 |
| 黄金 | commodity | gold | XAU | SINA_FOREIGN | USD | troy_ounce | 2026-04-01 | 2026-05-15 | 32 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "assetType": "commodity",
        "code": "brent_oil",
        "sourceSymbol": "OIL",
        "name": "布伦特原油",
        "sourceMarket": "SINA_FOREIGN",
        "currency": "USD",
        "unit": "barrel",
        "firstTradeDate": "2026-04-01",
        "lastTradeDate": "2026-05-15",
        "count": 32
      },
      {
        "assetType": "commodity",
        "code": "copper",
        "sourceSymbol": "HG",
        "name": "铜",
        "sourceMarket": "SINA_FOREIGN",
        "currency": "USD",
        "unit": "pound",
        "firstTradeDate": "2026-04-01",
        "lastTradeDate": "2026-05-15",
        "count": 32
      },
      {
        "assetType": "commodity",
        "code": "gold",
        "sourceSymbol": "XAU",
        "name": "黄金",
        "sourceMarket": "SINA_FOREIGN",
        "currency": "USD",
        "unit": "troy_ounce",
        "firstTradeDate": "2026-04-01",
        "lastTradeDate": "2026-05-15",
        "count": 32
      }
    ],
    "count": 3,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImV4dGVybmFsX2luc3RydW1lbnRzIiwib3JkZXIiOlsiYXNzZXRUeXBlIiwiY29kZSIsInNvdXJjZVN5bWJvbCJdLCJrZXlzIjp7ImNvZGUiOiJnb2xkIiwiYXNzZXRUeXBlIjoiY29tbW9kaXR5Iiwic291cmNlU3ltYm9sIjoiWEFVIn0sImZpbHRlcnMiOnsiYXNzZXRUeXBlIjoiIiwicSI6IiJ9LCJpc3N1ZWRBdCI6IjIwMjYtMDUtMTdUMjA6MTU6MTIuMDQ5Mjc0KzA4OjAwIn0",
    "hasMore": true
  },
  "requestId": "req_a6946921cf4643c3a62b846f0d209f19",
  "ts": "2026-05-17T20:15:12.049358"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
