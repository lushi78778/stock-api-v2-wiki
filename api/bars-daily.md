# 个股日 K（批量）

## 接口用途

批量拉取多只股票的日 K 线。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/bars/daily`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `symbols` | query | string | 是 | 逗号分隔代码 |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `adj` | query | string | 否 | none 或 hfq |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/bars/daily?symbols=000001,000002&start=2026-05-13&end=2026-05-13&limit=2" \
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
| `requestId` | `req_5a385dbff82a4d6596242d87ababe58f` |
| `ts` | 2026-05-17T20:15:11.82208 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 2 |
| `data.total` | — |
| `data.hasMore` | false |
| `data.nextCursor` | — |
| `data.adj` | none |

### `data.items` 表格（2026-05-13）

| tradeDate | symbol | open | high | low | close | changePercent | changeAmount | volume | amount | turnoverRate | amplitude |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | 000001 | 11.25 | 11.28 | 11.11 | 11.14 | -0.98 | -0.11 | 1017974 | 1.137e+09 | 0.52 | 1.51 |
| 2026-05-13 | 000002 | 4.08 | 4.1 | 3.98 | 3.99 | -2.68 | -0.11 | 1308767 | 5.249e+08 | 1.35 | 2.93 |

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
      },
      {
        "symbol": "000002",
        "tradeDate": "2026-05-13",
        "open": 4.08,
        "high": 4.1,
        "low": 3.98,
        "close": 3.99,
        "volume": 1308767,
        "amount": 524880558.92,
        "amplitude": 2.93,
        "changePercent": -2.68,
        "changeAmount": -0.11,
        "turnoverRate": 1.35
      }
    ],
    "count": 2,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": null,
    "hasMore": false
  },
  "requestId": "req_5a385dbff82a4d6596242d87ababe58f",
  "ts": "2026-05-17T20:15:11.82208"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
