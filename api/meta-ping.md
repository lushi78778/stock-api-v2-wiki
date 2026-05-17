# 连通性探测（Ping）

## 接口用途

确认 Token 有效、开放链路通畅，不访问业务库。

> 你可以这样理解：上线前先 Ping，再拉大批量行情。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/meta/ping`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |

### 请求示例

```bash
export BASE_URL="https://stock.xray.top"
export TOKEN="stk_ZjgzN2ViMTAtMTFjNS00ZjA5LWI0YzgtNzdmMGU0MDM4YmE5"

curl -sS "$BASE_URL/api/v2/open/meta/ping" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

## 响应

> **注意：** 下列数据来自线上实调（`https://stock.xray.top`），Token 9 已重置并验证可用。

### 响应信封

| 字段 | 值 |
|------|-----|
| `code` | 0 |
| `message` | success |
| `requestId` | `req_8c4b0cb1263742109c0c8e4b2ba8d8b9` |
| `ts` | 2026-05-18T07:33:37.862993 |

### `data` 字段（2026-05-13）

| message | tokenId | scope | path |
| --- | --- | --- | --- |
| open api reachable | 9 | market:read | /api/v2/open/meta/ping |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "message": "open api reachable",
    "tokenId": 9,
    "scope": "market:read",
    "path": "/api/v2/open/meta/ping"
  },
  "requestId": "req_8c4b0cb1263742109c0c8e4b2ba8d8b9",
  "ts": "2026-05-18T07:33:37.862993"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
