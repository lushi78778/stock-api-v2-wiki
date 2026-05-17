# 只读库健康检查

## 接口用途

探活只读行情库连接。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/health`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/health" \
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
| `requestId` | `req_e3eb96bf4460490883976c92c996762e` |
| `ts` | 2026-05-17T20:15:11.58878 |

### `data` 字段（2026-05-13）

| message | ok | latencyMs | stockReadEnabled |
| --- | --- | --- | --- |
| ok | True | 0 | True |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "stockReadEnabled": true,
    "ok": true,
    "latencyMs": 0,
    "message": "ok"
  },
  "requestId": "req_e3eb96bf4460490883976c92c996762e",
  "ts": "2026-05-17T20:15:11.58878"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
