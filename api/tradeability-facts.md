# 个股可交易原始事实

## 接口用途

返回日 K 与涨停池相关原始字段，不做可买判断。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/tradeability/facts`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `symbols` | query | string | 是 | 逗号分隔 |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/tradeability/facts?symbols=000001&start=2026-05-13&end=2026-05-13&limit=1" \
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
| `requestId` | `req_3c4fa33f98ce487591675368f5f439e1` |
| `ts` | 2026-05-17T20:15:12.035927 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 1 |
| `data.total` | — |
| `data.hasMore` | false |
| `data.nextCursor` | — |

### `data.items` 表格（2026-05-13）

| tradeDate | symbol | name | open | high | low | close | changePercent | changeAmount | volume | amount | turnoverRate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | 000001 | — | 11.25 | 11.28 | 11.11 | 11.14 | -0.98 | -0.11 | 1017974 | 1.137e+09 | 0.52 |

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
        "name": null,
        "open": 11.25,
        "high": 11.28,
        "low": 11.11,
        "close": 11.14,
        "volume": 1017974,
        "amount": 1136724107.4,
        "amplitude": 1.51,
        "changePercent": -0.98,
        "changeAmount": -0.11,
        "turnoverRate": 0.52,
        "firstLimitUpTime": null,
        "lastLimitUpTime": null,
        "breakLimitUpCount": null,
        "consecutiveLimitUpDays": null,
        "limitUpFund": null,
        "limitUpStatistics": null
      }
    ],
    "count": 1,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": null,
    "hasMore": false
  },
  "requestId": "req_3c4fa33f98ce487591675368f5f439e1",
  "ts": "2026-05-17T20:15:12.035927"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
