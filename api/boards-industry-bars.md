# 行业板块日 K

## 接口用途

单个行业板块的历史日 K。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/boards/industry/{board_code}/bars/daily`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `board_code` | path | string | 是 | 板块代码 |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/boards/industry/{board_code}/bars/daily/BK0420/bars/daily?start=2026-05-13&end=2026-05-13" \
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
| `requestId` | `req_50e02a90a4c042718407187d5fe9f8a7` |
| `ts` | 2026-05-17T20:15:11.957206 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 1 |
| `data.total` | — |
| `data.hasMore` | false |
| `data.nextCursor` | — |

### `data.items` 表格（2026-05-13）

| tradeDate | boardCode | open | high | low | close | changePercent | changeAmount | volume | amount | turnoverRate | amplitude |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | BK0420 | 4639 | 4667 | 4616 | 4662 | 0.34 | 15.97 | 10730791 | 4.448e+09 | 1.01 | 1.11 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
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
  "requestId": "req_50e02a90a4c042718407187d5fe9f8a7",
  "ts": "2026-05-17T20:15:11.957206"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
