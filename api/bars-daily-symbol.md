# 个股日 K（单券）

## 接口用途

等价于 symbols 只含一只的批量日 K。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/bars/daily/{symbol}`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `symbol` | path | string | 是 | 证券代码 |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `adj` | query | string | 否 | none/hfq |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/bars/daily/{symbol}/000001?start=2026-05-13&end=2026-05-13" \
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
| `requestId` | `req_3e22ad41a7894582ae91517bff4d3b5c` |
| `ts` | 2026-05-17T20:15:11.835136 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 1 |
| `data.total` | — |
| `data.hasMore` | false |
| `data.nextCursor` | — |
| `data.adj` | none |

### `data.items` 表格（2026-05-13）

| tradeDate | symbol | open | high | low | close | changePercent | changeAmount | volume | amount | turnoverRate | amplitude |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | 000001 | 11.25 | 11.28 | 11.11 | 11.14 | -0.98 | -0.11 | 1017974 | 1.137e+09 | 0.52 | 1.51 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "adj": "none",
    "items": [
      {
        "symbol": "000001",
        "tradeDate": "2026-05-13",
        "open": 11.25,
        "high": 11.28,
        "low": 11.11,
        "close": 11.14,
        "volume": 1017974,
        "amount": 1136724107.4,
        "amplitude": 1.51,
        "changePercent": -0.98,
        "changeAmount": -0.11,
        "turnoverRate": 0.52
      }
    ],
    "count": 1,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": null,
    "hasMore": false
  },
  "requestId": "req_3e22ad41a7894582ae91517bff4d3b5c",
  "ts": "2026-05-17T20:15:11.835136"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
