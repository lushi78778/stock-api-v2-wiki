# 行业板块清单

## 接口用途

指定交易日的行业板块排行快照。

> 示例使用 2026-05-13 行情：BK1323 综合电力设备商涨幅约 6.88%。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/boards/industry`

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

curl -sS "$BASE_URL/api/v2/open/market/boards/industry?trade_date=2026-05-13&limit=3" \
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
| `requestId` | `req_43b58b69787c4cae85423aff6a7fcdd7` |
| `ts` | 2026-05-17T20:15:11.902057 |

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
| 2026-05-13 | BK1323 | 综合电力设备商 | 1 | 6.88 | 111.3 | 5.89 | 上海电气 | 1730 | 2 | 0 | 2.833e+11 |
| 2026-05-13 | BK1305 | 燃料电池 | 2 | 5.82 | 22.14 | 5.19 | 亿华通-U | 402.8 | 1 | 0 | 6.607e+09 |
| 2026-05-13 | BK1625 | 钨 | 3 | 5.46 | 491.1 | 6.57 | 翔鹭钨业 | 9488 | 4 | 0 | 2.895e+11 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK1323",
        "boardName": "综合电力设备商",
        "rankNo": 1,
        "changePercent": 6.88,
        "changeAmount": 111.33,
        "turnoverRate": 5.89,
        "upCount": 2,
        "downCount": 0,
        "leadingStockName": "上海电气",
        "latestPrice": 1729.52,
        "totalMarketValue": 283310736000.0
      },
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK1305",
        "boardName": "燃料电池",
        "rankNo": 2,
        "changePercent": 5.82,
        "changeAmount": 22.14,
        "turnoverRate": 5.19,
        "upCount": 1,
        "downCount": 0,
        "leadingStockName": "亿华通-U",
        "latestPrice": 402.8,
        "totalMarketValue": 6607416000.0
      },
      {
        "tradeDate": "2026-05-13",
        "boardCode": "BK1625",
        "boardName": "钨",
        "rankNo": 3,
        "changePercent": 5.46,
        "changeAmount": 491.12,
        "turnoverRate": 6.57,
        "upCount": 4,
        "downCount": 0,
        "leadingStockName": "翔鹭钨业",
        "latestPrice": 9487.7,
        "totalMarketValue": 289515968000.0
      }
    ],
    "count": 3,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImJvYXJkX2luZHVzdHJ5X2xpc3QiLCJvcmRlciI6WyJjaGFuZ2VQZXJjZW50IiwicmFua05vIiwiYm9hcmRDb2RlIl0sImtleXMiOnsiY2hhbmdlUGVyY2VudCI6IjUuNDYwMCIsImJvYXJkQ29kZSI6IkJLMTYyNSIsInJhbmtObyI6IjMifSwiZmlsdGVycyI6eyJ0cmFkZURhdGUiOiIyMDI2LTA1LTEzIn0sImlzc3VlZEF0IjoiMjAyNi0wNS0xN1QyMDoxNToxMS45MDE5MjcrMDg6MDAifQ",
    "hasMore": true
  },
  "requestId": "req_43b58b69787c4cae85423aff6a7fcdd7",
  "ts": "2026-05-17T20:15:11.902057"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
