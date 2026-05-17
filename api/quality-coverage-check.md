# 区间数据覆盖检查

## 接口用途

检查区间内开市日数据是否齐全。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/quality/coverage-check`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `start` | query | date | 是 | 起始 |
| `end` | query | date | 是 | 结束 |
| `boardTypes` | query | string | 否 | industry/concept |
| `boardCodes` | query | string | 否 | 板块代码 |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/quality/coverage-check?start=2026-05-13&end=2026-05-13&boardTypes=industry&boardCodes=BK0420" \
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
| `requestId` | `req_e5c1e6b4ee3e4ac2aba83ee2b8f6fc92` |
| `ts` | 2026-05-17T20:15:11.769717 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 6 |
| `data.total` | — |
| `data.hasMore` | false |
| `data.nextCursor` | — |

### `data.items` 表格（2026-05-13）

| dataset | minDate | maxDate | tradeDays | rowCount | expectedOpenDays | missingOpenDates |
| --- | --- | --- | --- | --- | --- | --- |
| calendar_open | 2026-05-13 | 2026-05-13 | 1 | 1 | 1 | [] |
| board_industry_history | 2026-05-13 | 2026-05-13 | 1 | 1 | 1 | [] |
| board_industry_constituent | 2026-05-13 | 2026-05-13 | 1 | 14 | 1 | [] |
| stock_hist_raw_daily | 2026-05-13 | 2026-05-13 | 1 | 5493 | 1 | [] |
| stock_individual_info_daily | 2026-05-13 | 2026-05-13 | 1 | 5517 | 1 | [] |
| zt_pool | 2026-05-13 | 2026-05-13 | 1 | 113 | 1 | [] |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "start": "2026-05-13",
    "end": "2026-05-13",
    "items": [
      {
        "dataset": "calendar_open",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 1,
        "expectedOpenDays": 1,
        "missingOpenDates": []
      },
      {
        "dataset": "board_industry_history",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 1,
        "expectedOpenDays": 1,
        "missingOpenDates": []
      },
      {
        "dataset": "board_industry_constituent",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 14,
        "expectedOpenDays": 1,
        "missingOpenDates": []
      },
      {
        "dataset": "stock_hist_raw_daily",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 5493,
        "expectedOpenDays": 1,
        "missingOpenDates": []
      },
      {
        "dataset": "stock_individual_info_daily",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 5517,
        "expectedOpenDays": 1,
        "missingOpenDates": []
      },
      {
        "dataset": "zt_pool",
        "minDate": "2026-05-13",
        "maxDate": "2026-05-13",
        "tradeDays": 1,
        "rowCount": 113,
        "expectedOpenDays": 1,
        "missingOpenDates": []
      }
    ],
    "count": 6,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": null,
    "hasMore": false
  },
  "requestId": "req_e5c1e6b4ee3e4ac2aba83ee2b8f6fc92",
  "ts": "2026-05-17T20:15:11.769717"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
