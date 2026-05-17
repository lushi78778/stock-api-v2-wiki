# 证券检索（单条）

## 接口用途

按 6 位代码精确查询一只证券。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/securities/{symbol}`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `symbol` | path | string | 是 | 证券代码 |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/securities/{symbol}/000001" \
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
| `requestId` | `req_b2bd126bc4604a5aad894f6ff9483bc2` |
| `ts` | 2026-05-17T20:15:11.796918 |

### `data` 字段（2026-05-13）

| symbol | name |
| --- | --- |
| 000001 | 平安银行 |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "symbol": "000001",
    "name": "平安银行"
  },
  "requestId": "req_b2bd126bc4604a5aad894f6ff9483bc2",
  "ts": "2026-05-17T20:15:11.796918"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
