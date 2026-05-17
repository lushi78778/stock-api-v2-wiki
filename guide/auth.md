# 认证与 Token

## 你怎么传 Token

所有 `/api/v2/open/**` 接口都需要在请求头携带：

```http
Authorization: Bearer stk_你的明文Token
Accept: application/json
```

你可以这样理解：`Bearer` 后面有一个空格，再拼接完整 Token；不要把 Token 写在 URL 里。

## 可选请求头

| Header | 必填 | 说明 |
|--------|------|------|
| `Authorization` | 是 | `Bearer <Token>` |
| `Accept` | 建议 | 填 `application/json` |
| `X-Request-Id` | 否 | 你自己的请求 ID，便于和日志对齐 |
| `X-Client-Name` | 否 | 调用方名称，例如 `my-quant-bot` |

## scope 是什么

Token 会绑定权限范围。行情只读接口通常需要 **`market:read`**。如果 scope 不匹配，你会收到 `40301`。

连通性探测接口会回显当前 Token 的 `scope`，方便你自查：

```json
{
  "code": 0,
  "data": {
    "tokenId": 3,
    "scope": "market:read",
    "path": "/api/v2/open/meta/ping"
  }
}
```

## Token 从哪来、丢了怎么办

- **获取：** 登录门户 → Token 管理 → 申请并通过审核 → 复制明文（只显示一次）。
- **遗失：** 在门户对对应 Token 执行重置，会得到新的明文；旧 Token 立即失效。
- **禁用：** 在门户禁用后，所有请求返回 `40101`。
