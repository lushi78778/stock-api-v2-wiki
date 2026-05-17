# 批量板块日 K

## 接口用途

一次查询多个板块的日 K。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/boards/bars/daily`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `boardTypes` | query | string | 否 | industry/concept |
| `boardCodes` | query | string | 否 | 逗号分隔 |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/boards/bars/daily?boardTypes=industry&boardCodes=BK0420&start=2026-05-13&end=2026-05-13&limit=2" \
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
| `requestId` | `req_3797a8c8561d46dc862ec06c99c65dbf` |
| `ts` | 2026-05-17T20:15:11.992544 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 1 |
| `data.total` | — |
| `data.hasMore` | false |
| `data.nextCursor` | — |

### `data.items` 表格（2026-05-13）

| tradeDate | boardCode | boardType | open | high | low | close | changePercent | changeAmount | volume | amount | turnoverRate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | BK0420 | industry | 4639 | 4667 | 4616 | 4662 | 0.34 | 15.97 | 10730791 | 4.448e+09 | 1.01 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "boardType": "industry",
        "boardCode": "BK0420",
        "tradeDate": "2026-05-13",
        "open": 4639.29,
        "high": 4666.91,
        "low": 4615.52,
        "close": 4662.48,
        "volume": 10730791,
        "amount": 4447815521.0,
        "amplitude": 1.11,
        "changePercent": 0.34,
        "changeAmount": 15.97,
        "turnoverRate": 1.01
      }
    ],
    "count": 1,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": null,
    "hasMore": false
  },
  "requestId": "req_3797a8c8561d46dc862ec06c99c65dbf",
  "ts": "2026-05-17T20:15:11.992544"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
