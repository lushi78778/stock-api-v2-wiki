# Stock API v2 开放平台

欢迎使用 **Stock API v2**。你可以通过 HTTPS 接口读取 A 股行情、板块、涨停池、外盘标的等只读数据，用于量化脚本、看板或自有系统的数据补全。

## 服务地址

| 项目 | 地址 |
|------|------|
| **API / 门户根地址** | `https://stock.xray.top` |
| **用户门户** | 同上（注册、登录、Token 管理、Knife4j 在线调试） |

下文所有接口路径均为**相对路径**，实际请求时请拼在根地址后，例如：

`GET /api/v2/open/meta/ping` → `https://stock.xray.top/api/v2/open/meta/ping`

开放行情接口前缀：`/api/v2/open/**`。响应为 JSON，成功时 `code` 为 `0`。请求头：

```http
Authorization: Bearer stk_你的Token明文
Accept: application/json
```

---

## 快速开始

### 1. 注册账号

1. 浏览器打开 **https://stock.xray.top** 进入用户门户。
2. 使用邮箱注册：先 `POST /api/v2/public/register/code` 获取验证码，再 `POST /api/v2/public/register/verify` 完成验证。
3. 按页面引导绑定 TOTP（双因素认证），然后登录。

> **注意：** 注册与登录走 Cookie 会话，**不需要** API Token。Token 仅在调用 `/api/v2/open/**` 时使用。

### 2. 申请并获取 API Token

1. 登录门户后，打开 **Token 管理**。
2. 提交申请，勾选权限（行情只读一般为 `market:read`）。
3. 审核通过后，在列表中**复制明文 Token**（形如 `stk_xxxxxxxx`）。明文**只显示一次**，请立即保存。

若 Token 遗失，可在门户重置；旧 Token 随即失效。

### 3. 发起第一个请求

用 **连通性探测** 确认 Token 是否可用：`GET /api/v2/open/meta/ping`

**curl：**

```bash
export TOKEN="stk_你的Token明文"

curl -sS "https://stock.xray.top/api/v2/open/meta/ping" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

**JavaScript（fetch）：**

```javascript
const TOKEN = 'stk_你的Token明文';

const res = await fetch('/api/v2/open/meta/ping', {
  headers: { Authorization: `Bearer ${TOKEN}`, Accept: 'application/json' },
});
// 浏览器同源访问门户时可用相对路径；脚本中请写完整地址：
// fetch('https://stock.xray.top/api/v2/open/meta/ping', { ... })
const body = await res.json();
console.log(body);
```

成功时你会看到 `code: 0`，`data.message` 为 `open api reachable`。接下来在左侧侧边栏按模块查阅各接口说明。

---

## 常见错误码及处理

| code | HTTP | 含义 | 你可以怎么做 |
|------|------|------|----------------|
| `0` | 200 | 成功 | 解析 `data` |
| `40001` | 400 | 参数非法 | 检查日期格式 `yyyy-MM-dd`、必填参数 |
| `40101` | 401 | 未授权 | 确认 Token、是否带 `Bearer ` 前缀 |
| `40301` | 403 | 无权限 | 确认 scope 含 `market:read` |
| `40401` | 404 | 资源不存在 | 核对代码、板块、交易日是否有数据 |
| `42901` | 429 | 超出额度 | 降频或在门户查看用量 |
| `50001` | 500 | 服务内部错误 | 记录 `requestId` 后反馈 |
| `50301` | 503 | 服务暂时不可用 | 稍后重试，或调用 `/api/v2/open/market/health` |

详情见 [错误码说明](guide/errors.md)。

---

## 文档导航

- [认证与 Token](guide/auth.md) — 请求头、scope、可选 Header
- [响应格式与分页](guide/response.md) — `items`、`nextCursor` 用法
- **侧边栏** — 全部开放接口（参数表、curl、2026-05-13 行情表格示例）

---

## 响应示例说明

各接口页中的 **`data.items` 表格** 使用 **2026-05-13** 交易日示例数据（如 `000001` 收盘 11.14、行业板块 BK1323 等），便于对照字段；表下附有 JSON 节选。外盘商品示例使用 **2026-05-15**。

查询时把 `trade_date` / `start` / `end` 换成你需要的交易日即可。
