# 数据覆盖范围

## 接口用途

统计数据集日期覆盖与行数。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/meta/coverage`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `start` | query | date | 否 | 起始日 |
| `end` | query | date | 否 | 结束日 |
| `datasets` | query | string | 否 | 数据集列表 |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/meta/coverage?start=2026-05-13&end=2026-05-13" \
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
| `requestId` | `req_488acc5b1fc4431499d04fc0aa314335` |
| `ts` | 2026-05-17T20:15:11.747021 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 13 |
| `data.total` | — |
| `data.hasMore` | false |
| `data.nextCursor` | — |

### `data.items` 表格（2026-05-13）

| dataset | minDate | maxDate | tradeDays | rowCount |
| --- | --- | --- | --- | --- |
| trade_calendar | 2026-05-13 | 2026-05-13 | 1 | 1 |
| board_industry_list | 2026-05-13 | 2026-05-13 | 1 | 496 |
| board_concept_list | 2026-05-13 | 2026-05-13 | 1 | 486 |
| board_concept_history | 2026-05-13 | 2026-05-13 | 1 | 486 |
| board_industry_history | 2026-05-13 | 2026-05-13 | 1 | 496 |
| board_concept_constituent | 2026-05-13 | 2026-05-13 | 1 | 60430 |
| board_industry_constituent | 2026-05-13 | 2026-05-13 | 1 | 16788 |
| stock_hist_raw_daily | 2026-05-13 | 2026-05-13 | 1 | 5493 |
| stock_hist_hfq_daily | 2026-05-13 | 2026-05-13 | 1 | 5493 |
| stock_individual_info_daily | 2026-05-13 | 2026-05-13 | 1 | 5517 |
| zt_pool | 2026-05-13 | 2026-05-13 | 1 | 113 |
| external_market_daily | 2026-05-13 | 2026-05-13 | 1 | 18 |
| external_commodity_daily | 2026-05-13 | 2026-05-13 | 1 | 5 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "dataset": "trade_calendar",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 1
      },
      {
        "dataset": "board_industry_list",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 496
      },
      {
        "dataset": "board_concept_list",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 486
      },
      {
        "dataset": "board_concept_history",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 486
      },
      {
        "dataset": "board_industry_history",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 496
      },
      {
        "dataset": "board_concept_constituent",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 60430
      },
      {
        "dataset": "board_industry_constituent",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 16788
      },
      {
        "dataset": "stock_hist_raw_daily",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 5493
      },
      {
        "dataset": "stock_hist_hfq_daily",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 5493
      },
      {
        "dataset": "stock_individual_info_daily",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 5517
      },
      {
        "dataset": "zt_pool",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 113
      },
      {
        "dataset": "external_market_daily",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 18
      },
      {
        "dataset": "external_commodity_daily",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 5
      }
    ],
    "count": 13,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": null,
    "hasMore": false
  },
  "requestId": "req_488acc5b1fc4431499d04fc0aa314335",
  "ts": "2026-05-17T20:15:11.747021"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
