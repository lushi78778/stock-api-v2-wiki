# 个股日快照（批量）

## 接口用途

查询个股基本信息日快照（动态列）。

> 注意：同时传 trade_date 与 start/end 时，以 start/end 为准。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/snapshots/daily`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `symbols` | query | string | 是 | 逗号分隔 |
| `trade_date` | query | date | 否 | 单日，与 start/end 二选一 |
| `start` | query | date | 否 | 区间起 |
| `end` | query | date | 否 | 区间止 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/snapshots/daily?symbols=000001&trade_date=2026-05-13&limit=1" \
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
| `requestId` | `req_c2083a532f0c4fe3a918cc04c24926b0` |
| `ts` | 2026-05-17T20:15:11.847049 |

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
  "requestId": "req_c2083a532f0c4fe3a918cc04c24926b0",
  "ts": "2026-05-17T20:15:11.847049"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
