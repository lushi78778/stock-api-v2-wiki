# 涨停池

## 接口用途

查询涨停池 zt_pool 数据，可按单日或区间。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/pools/limit-up`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `trade_date` | query | date | 否 | 单日 |
| `start` | query | date | 否 | 区间起 |
| `end` | query | date | 否 | 区间止 |
| `cursor` | query | string | 否 | 上一页 nextCursor |
| `limit` | query | integer | 否 | 本页条数 |
| `includeTotal` | query | boolean | 否 | 是否返回精确 total |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/pools/limit-up?trade_date=2026-05-13&limit=5" \
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
| `requestId` | `req_24aa79fc4e084fb2a3122927741f066d` |
| `ts` | 2026-05-17T20:15:11.873007 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 5 |
| `data.total` | — |
| `data.hasMore` | true |
| `data.nextCursor` | c1.eyJ2IjoxLCJyZXNvdXJjZ… |

### `data.items` 表格（2026-05-13）

| tradeDate | symbol | name | changePercent | amount | latestPrice | limitUpFund | firstLimitUpTime | lastLimitUpTime | limitUpStatistics | consecutiveLimitUpDays | industryName |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-13 | 000533 | 顺钠股份 | 9.978 | 1.251e+09 | 14.77 | 1.462e+08 | 095648 | 095924 | 1/1 | 1 | 电网设备 |
| 2026-05-13 | 000601 | 韶能股份 | 10.01 | 6.593e+08 | 8.9 | 2.7e+08 | 093018 | 093018 | 2/2 | 2 | 电力 |
| 2026-05-13 | 000720 | 新能泰山 | 10.02 | 7.452e+08 | 6.26 | 9.223e+07 | 093506 | 093506 | 5/3 | 1 | 电网设备 |
| 2026-05-13 | 000767 | 晋控电力 | 10.11 | 9.273e+08 | 5.12 | 1.883e+08 | 093300 | 093300 | 2/2 | 2 | 电力 |
| 2026-05-13 | 000811 | 冰轮环境 | 9.996 | 1.94e+09 | 31.8 | 6.914e+07 | 143051 | 143051 | 3/2 | 1 | 通用设备 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-13",
        "symbol": "000533",
        "name": "顺钠股份",
        "changePercent": 9.9777,
        "latestPrice": 14.77,
        "amount": 1251483440.0,
        "limitUpFund": 146229572.0,
        "firstLimitUpTime": "095648",
        "lastLimitUpTime": "095924",
        "limitUpStatistics": "1/1",
        "consecutiveLimitUpDays": 1,
        "industryName": "电网设备"
      },
      {
        "tradeDate": "2026-05-13",
        "symbol": "000601",
        "name": "韶能股份",
        "changePercent": 10.0124,
        "latestPrice": 8.9,
        "amount": 659260992.0,
        "limitUpFund": 269956099.0,
        "firstLimitUpTime": "093018",
        "lastLimitUpTime": "093018",
        "limitUpStatistics": "2/2",
        "consecutiveLimitUpDays": 2,
        "industryName": "电力"
      },
      {
        "tradeDate": "2026-05-13",
        "symbol": "000720",
        "name": "新能泰山",
        "changePercent": 10.0176,
        "latestPrice": 6.26,
        "amount": 745240736.0,
        "limitUpFund": 92232586.0,
        "firstLimitUpTime": "093506",
        "lastLimitUpTime": "093506",
        "limitUpStatistics": "5/3",
        "consecutiveLimitUpDays": 1,
        "industryName": "电网设备"
      },
      {
        "tradeDate": "2026-05-13",
        "symbol": "000767",
        "name": "晋控电力",
        "changePercent": 10.1075,
        "latestPrice": 5.12,
        "amount": 927343392.0,
        "limitUpFund": 188257909.0,
        "firstLimitUpTime": "093300",
        "lastLimitUpTime": "093300",
        "limitUpStatistics": "2/2",
        "consecutiveLimitUpDays": 2,
        "industryName": "电力"
      },
      {
        "tradeDate": "2026-05-13",
        "symbol": "000811",
        "name": "冰轮环境",
        "changePercent": 9.9965,
        "latestPrice": 31.8,
        "amount": 1940045760.0,
        "limitUpFund": 69140005.0,
        "firstLimitUpTime": "143051",
        "lastLimitUpTime": "143051",
        "limitUpStatistics": "3/2",
        "consecutiveLimitUpDays": 1,
        "industryName": "通用设备"
      }
    ],
    "count": 5,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImxpbWl0X3VwX3Bvb2wiLCJvcmRlciI6WyJ0cmFkZURhdGUiLCJzeW1ib2wiXSwia2V5cyI6eyJ0cmFkZURhdGUiOiIyMDI2LTA1LTEzIiwic3ltYm9sIjoiMDAwODExIn0sImZpbHRlcnMiOnsic3RhcnQiOiIyMDI2LTA1LTEzIiwiZW5kIjoiMjAyNi0wNS0xMyJ9LCJpc3N1ZWRBdCI6IjIwMjYtMDUtMTdUMjA6MTU6MTEuODcyODA0KzA4OjAwIn0",
    "hasMore": true
  },
  "requestId": "req_24aa79fc4e084fb2a3122927741f066d",
  "ts": "2026-05-17T20:15:11.873007"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
