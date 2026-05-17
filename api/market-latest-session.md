# 最新可用交易日

## 接口用途

查询核心数据集最新交易日。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/meta/latest-session`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/meta/latest-session" \
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
| `requestId` | `req_82a9981a9d954a76ac2f5d46a6e24df9` |
| `ts` | 2026-05-17T20:15:11.615392 |

### `data` 字段（2026-05-13）

| latestOpenDate | latestConceptListDate | latestIndustryListDate | latestConceptHistoryDate | latestIndustryHistoryDate | latestConceptConstituentDate | latestIndustryConstituentDate | latestStockRawDate | latestStockHfqDate | latestStockInfoDate | latestLimitUpPoolDate | latestExternalMarketDate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | 2026-05-15 | 2026-05-15 | 2026-05-15 | 2026-05-15 | 2026-05-15 | 2026-05-15 | 2026-05-15 | 2026-05-15 | 2026-05-15 | 2026-05-15 | 2026-05-14 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "latestOpenDate": "2026-05-15",
    "latestConceptListDate": "2026-05-15",
    "latestIndustryListDate": "2026-05-15",
    "latestConceptHistoryDate": "2026-05-15",
    "latestIndustryHistoryDate": "2026-05-15",
    "latestConceptConstituentDate": "2026-05-15",
    "latestIndustryConstituentDate": "2026-05-15",
    "latestStockRawDate": "2026-05-15",
    "latestStockHfqDate": "2026-05-15",
    "latestStockInfoDate": "2026-05-15",
    "latestLimitUpPoolDate": "2026-05-15",
    "latestExternalMarketDate": "2026-05-14",
    "latestExternalCommodityDate": "2026-05-15"
  },
  "requestId": "req_82a9981a9d954a76ac2f5d46a6e24df9",
  "ts": "2026-05-17T20:15:11.615392"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
