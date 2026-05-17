# Stock API v2 开放平台

欢迎使用 Stock API v2。你可以通过 HTTP 接口读取 A 股行情、板块数据、涨停池、外盘标的等只读数据，用于量化研究、看板展示或自有系统的数据补全。

所有开放接口均返回 JSON，成功时 `code` 为 `0`；鉴权方式为请求头 `Authorization: Bearer <你的 Token>`。

---

## 快速开始

### 1. 注册账号

1. 打开平台的**用户门户**（与 API 同域或门户子域，由部署方提供入口）。
2. 使用邮箱完成注册：先调用 `POST /api/v2/public/register/code` 获取验证码，再调用 `POST /api/v2/public/register/verify` 完成验证。
3. 按引导绑定 TOTP（双因素认证），之后即可登录。

> **注意：** 注册与登录走 Cookie 会话，不需要 API Token。Token 只在调用 `/api/v2/open/**` 开放行情接口时使用。

### 2. 申请并获取 API Token

1. 登录门户后，进入 **Token 管理** 页面。
2. 提交 Token 申请，勾选需要的权限范围（行情只读一般为 `market:read`）。
3. 等待审核通过后，在 Token 列表中**复制明文 Token**（形如 `stk_xxxxxxxx`）。明文只显示一次，请妥善保存。

你也可以在门户查看已有 Token 的状态（启用/禁用），但无法再次查看完整明文；遗失后需要重置或重新申请。

### 3. 发起第一个请求

下面用 **连通性探测** 接口验证 Token 是否可用。把 `YOUR_TOKEN` 换成你的明文 Token，把 `BASE_URL` 换成实际 API 地址（本地调试常用 `http://127.0.0.1:8788`）。

**curl：**

```bash
export BASE_URL="http://127.0.0.1:8788"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/meta/ping" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

**JavaScript（fetch）：**

```javascript
const BASE_URL = 'http://127.0.0.1:8788';
const TOKEN = 'stk_你的Token明文';

const res = await fetch(`${BASE_URL}/api/v2/open/meta/ping`, {
  headers: { Authorization: `Bearer ${TOKEN}`, Accept: 'application/json' },
});
const body = await res.json();
console.log(body);
```

成功时你会看到 `code: 0`，`data.message` 为 `open api reachable`。接下来可以阅读侧边栏中的各接口说明，按需拉取行情。

---

## 常见错误码及处理

| code | HTTP | 含义 | 你可以怎么做 |
|------|------|------|----------------|
| `0` | 200 | 成功 | 正常解析 `data` |
| `40001` | 400 | 参数非法 | 对照文档检查日期格式、必填参数 |
| `40101` | 401 | 未授权 | 检查 Token 是否正确、是否带 `Bearer ` 前缀 |
| `40301` | 403 | 无权限 | 确认 Token scope 是否包含 `market:read` |
| `40401` | 404 | 资源不存在 | 核对 symbol、板块代码、交易日是否有数据 |
| `42901` | 429 | 超出额度 | 降低调用频率，或在门户查看用量 |
| `50001` | 500 | 服务内部错误 | 带上 `requestId` 联系支持 |
| `50301` | 503 | 服务暂时不可用 | 稍后重试，或查看健康检查接口 |

更多说明见 [错误码说明](guide/errors.md)。

---

## 文档导航

- [认证与 Token](guide/auth.md) — 请求头、scope、可选 Header
- [响应格式与分页](guide/response.md) — `items`、`nextCursor` 怎么用
- 左侧侧边栏 — 按模块浏览全部开放接口

---

## 数据示例日期

文档中的行情示例多使用 **2026-05-13** 交易日数据（如行业板块清单）。若你本地库日期不同，把 `trade_date` / `start` / `end` 换成你环境中确有数据的日期即可。
