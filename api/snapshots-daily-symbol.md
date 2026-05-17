# 个股日快照（单券）

## 接口用途

单只股票日快照；区间无数据返回 404。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/snapshots/daily/{symbol}`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `symbol` | path | string | 是 | 证券代码 |
| `trade_date` | query | date | 否 | 交易日 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/snapshots/daily/{symbol}/000001?trade_date=2026-05-13" \
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
| `requestId` | `req_4303d90bef714d52b7ecadd664442073` |
| `ts` | 2026-05-17T20:15:11.859474 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 1 |
| `data.total` | — |
| `data.hasMore` | false |
| `data.nextCursor` | — |

### `data.items` 表格（2026-05-13）

| tradeDate | symbol | name | latestPrice | totalMarketValue | floatMarketValue | totalShares | floatShares | industryName | listingDate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | 000001 | 平安银行 | 11.14 | 2.162e+11 | 2.162e+11 | 1.941e+10 | 1.941e+10 | 银行Ⅱ | 1991-04-03 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-13",
        "symbol": "000001",
        "name": "平安银行",
        "latestPrice": 11.14,
        "totalMarketValue": 216181928725.72,
        "floatMarketValue": 216178391274.42,
        "totalShares": 19405918198.0,
        "floatShares": 19405600653.0,
        "industryName": "银行Ⅱ",
        "listingDate": "1991-04-03"
      }
    ],
    "count": 1,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": null,
    "hasMore": false
  },
  "requestId": "req_4303d90bef714d52b7ecadd664442073",
  "ts": "2026-05-17T20:15:11.859474"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
