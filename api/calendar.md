# 交易日历

## 接口用途

查询区间内每日是否开市。不传 start/end 时返回当月。

> 注意：isOpen=1 表示开市。

## 请求

- **方法：** `GET`
- **路径：** `/api/v2/open/market/calendar`

### 请求参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `Authorization` | header | string | 是 | Bearer Token |
| `start` | query | date | 否 | 起始 |
| `end` | query | date | 否 | 结束 |

### 请求示例

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/market/calendar?start=2026-05-13&end=2026-05-13" \
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
| `requestId` | `req_c940165d6e064ee1bf601cb650dc4f78` |
| `ts` | 2026-05-17T20:15:11.808914 |

### 分页信息

| 分页字段 | 值 |
|----------|-----|
| `data.count` | 1 |
| `data.total` | — |
| `data.hasMore` | false |
| `data.nextCursor` | — |

### `data.items` 表格（2026-05-13）

| tradeDate | open |
| --- | --- |
| 2026-05-13 | True |

### 完整 JSON（节选）

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-13",
        "open": true
      }
    ],
    "count": 1,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": null,
    "hasMore": false
  },
  "requestId": "req_c940165d6e064ee1bf601cb650dc4f78",
  "ts": "2026-05-17T20:15:11.808914"
}
```

### 可能出现的错误

- `40101` Token 无效
- `40301` scope 不足
- `40001` 参数错误
- `40401` 无数据
- `42901` 限流
