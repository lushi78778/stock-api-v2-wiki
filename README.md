# Stock API v2 开放平台接入说明

欢迎使用 **Stock API v2**。本开放平台提供 A 股行情、交易日历、板块行情、板块成分股、涨停池、外盘股票/ETF、外盘商品等只读数据接口，适合用于量化脚本、内部看板、选股工具、数据校验任务或自有系统的数据补全。

本文先给出线上地址、Token、认证方式和可直接复制的请求示例；更多接口参数可以继续查看左侧接口文档，或进入 Swagger/OpenAPI 文档按接口在线调试。

## 线上地址

| 项目 | 地址 | 说明 |
|------|------|------|
| **线上门户 / API 根地址** | `https://stock.xray.top/` | 注册、登录、Token 管理、接口调用都使用这个域名 |
| **OpenAPI 文档** | `https://stock.xray.top/v3/api-docs` | 机器可读的 OpenAPI JSON，可导入 Postman、Apifox、Knife4j 等工具 |
| **开放接口前缀** | `/api/v2/open/**` | 所有开放行情接口都在这个前缀下 |

下文所有接口路径均为**相对路径**，实际请求时请拼在根地址后，例如：

`GET /api/v2/open/meta/ping` → `https://stock.xray.top/api/v2/open/meta/ping`

## Token 使用方式

Token 9 已重置。为避免明文泄露，文档不再记录真实 Token；请在门户的 **Token 管理** 中复制最新明文，并只放在本地环境变量或私有配置里。

```text
stk_你的Token明文
```

使用时放在 `Authorization` 请求头里，格式如下：

```http
Authorization: Bearer stk_你的Token明文
Accept: application/json
```

注意事项：

- `Bearer` 和 Token 之间必须有一个空格。
- Token 不要拼在 URL 参数里，统一放在 Header。
- 如果后续再次重置 Token，旧明文会立即失效，需要替换脚本、定时任务、Postman 环境变量里的值。
- 开放行情接口通常需要 `market:read` 权限。

## 快速开始

### 1. 连通性探测

先调用 Ping 接口确认 Token 可用：

```bash
export BASE_URL="https://stock.xray.top"
export TOKEN="stk_你的Token明文"

curl -sS "$BASE_URL/api/v2/open/meta/ping" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

成功响应示例：

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

只要 `code` 为 `0`，说明认证链路可用。若返回 `40101`，通常是 Token 错误、Token 已被重置或缺少 `Bearer ` 前缀。

### 2. 查询多只股票日 K

接口：

```text
GET /api/v2/open/market/bars/daily
```

示例请求：

```bash
curl -sS "$BASE_URL/api/v2/open/market/bars/daily?symbols=000001,000002,600519,300750&start=2026-05-13&end=2026-05-13&limit=20" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

示例响应节选：

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "adj": "none",
    "items": [
      {
        "symbol": "000001",
        "tradeDate": "2026-05-13",
        "open": 11.25,
        "high": 11.28,
        "low": 11.11,
        "close": 11.14,
        "volume": 1017974,
        "amount": 1136724107.4,
        "amplitude": 1.51,
        "changePercent": -0.98,
        "changeAmount": -0.11,
        "turnoverRate": 0.52
      },
      {
        "symbol": "000002",
        "tradeDate": "2026-05-13",
        "open": 4.08,
        "high": 4.1,
        "low": 3.98,
        "close": 3.99,
        "volume": 1308767,
        "amount": 524880558.92,
        "amplitude": 2.93,
        "changePercent": -2.68,
        "changeAmount": -0.11,
        "turnoverRate": 1.35
      },
      {
        "symbol": "600519",
        "tradeDate": "2026-05-13",
        "open": 1354.5,
        "high": 1358.6,
        "low": 1338.0,
        "close": 1344.09,
        "volume": 56968,
        "amount": 7653257144.0,
        "amplitude": 1.52,
        "changePercent": -0.77,
        "changeAmount": -10.46,
        "turnoverRate": 0.45
      },
      {
        "symbol": "300750",
        "tradeDate": "2026-05-13",
        "open": 431.01,
        "high": 436.58,
        "low": 427.08,
        "close": 434.05,
        "volume": 316858,
        "amount": 13668347813.82,
        "amplitude": 2.2,
        "changePercent": 0.65,
        "changeAmount": 2.8,
        "turnoverRate": 0.74
      }
    ],
    "count": 4,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": null,
    "hasMore": false
  },
  "requestId": "req_9461dc23ba0a4c309cd0fd5b58e56737",
  "ts": "2026-05-18T07:33:47.867926"
}
```

常用参数说明：

| 参数 | 必填 | 示例 | 说明 |
|------|------|------|------|
| `symbols` | 是 | `000001,000002` | 多个股票代码用英文逗号分隔 |
| `start` | 是 | `2026-05-13` | 起始交易日 |
| `end` | 是 | `2026-05-13` | 结束交易日 |
| `adj` | 否 | `none` / `hfq` | 复权方式，默认不复权 |
| `limit` | 否 | `20` | 本页返回条数 |
| `cursor` | 否 | 上一页 `nextCursor` | 翻页游标 |

### 3. 查询批量板块日 K

接口：

```text
GET /api/v2/open/market/boards/bars/daily
```

示例请求：

```bash
curl -sS "$BASE_URL/api/v2/open/market/boards/bars/daily?boardTypes=industry&start=2026-05-13&end=2026-05-13&limit=5" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

示例响应节选：

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "boardType": "industry",
        "boardCode": "BK0420",
        "tradeDate": "2026-05-13",
        "open": 4639.29,
        "high": 4666.91,
        "low": 4615.52,
        "close": 4662.48,
        "volume": 10730791,
        "amount": 4447815521.0,
        "amplitude": 1.11,
        "changePercent": 0.34,
        "changeAmount": 15.97,
        "turnoverRate": 1.01
      },
      {
        "boardType": "industry",
        "boardCode": "BK0421",
        "tradeDate": "2026-05-13",
        "open": 8855.17,
        "high": 8909.26,
        "low": 8834.44,
        "close": 8902.54,
        "volume": 8022760,
        "amount": 4809349836.0,
        "amplitude": 0.85,
        "changePercent": 0.57,
        "changeAmount": 50.68,
        "turnoverRate": 0.62
      },
      {
        "boardType": "industry",
        "boardCode": "BK0422",
        "tradeDate": "2026-05-13",
        "open": 7897.3,
        "high": 7935.39,
        "low": 7858.77,
        "close": 7933.47,
        "volume": 6474812,
        "amount": 6560009657.0,
        "amplitude": 0.97,
        "changePercent": 0.3,
        "changeAmount": 23.84,
        "turnoverRate": 1.22
      },
      {
        "boardType": "industry",
        "boardCode": "BK0424",
        "tradeDate": "2026-05-13",
        "open": 29986.06,
        "high": 30171.62,
        "low": 29856.43,
        "close": 29971.0,
        "volume": 4661096,
        "amount": 4194045837.0,
        "amplitude": 1.05,
        "changePercent": -0.19,
        "changeAmount": -56.96,
        "turnoverRate": 1.28
      },
      {
        "boardType": "industry",
        "boardCode": "BK0427",
        "tradeDate": "2026-05-13",
        "open": 10770.47,
        "high": 11093.32,
        "low": 10770.47,
        "close": 11017.24,
        "volume": 136019775,
        "amount": 109746895211.0,
        "amplitude": 3.0,
        "changePercent": 2.46,
        "changeAmount": 264.91,
        "turnoverRate": 3.03
      }
    ],
    "count": 5,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImJvYXJkX2JhcnNfYmF0Y2gi...省略",
    "hasMore": true
  },
  "requestId": "req_3fafa2521b6c4fc08731a9dce9c724c7",
  "ts": "2026-05-18T07:33:47.88235"
}
```

### 4. 查询涨停池

接口：

```text
GET /api/v2/open/market/pools/limit-up
```

示例请求：

```bash
curl -sS "$BASE_URL/api/v2/open/market/pools/limit-up?trade_date=2026-05-13&limit=5" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/json"
```

示例响应节选：

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "items": [
      {
        "tradeDate": "2026-05-13",
        "symbol": "000533",
        "name": "顺钠股份",
        "changePercent": 9.9777,
        "latestPrice": 14.77,
        "amount": 1251483440.0,
        "limitUpFund": 146229572.0,
        "firstLimitUpTime": "095648",
        "lastLimitUpTime": "095924",
        "limitUpStatistics": "1/1",
        "consecutiveLimitUpDays": 1,
        "industryName": "电网设备"
      },
      {
        "tradeDate": "2026-05-13",
        "symbol": "000601",
        "name": "韶能股份",
        "changePercent": 10.0124,
        "latestPrice": 8.9,
        "amount": 659260992.0,
        "limitUpFund": 269956099.0,
        "firstLimitUpTime": "093018",
        "lastLimitUpTime": "093018",
        "limitUpStatistics": "2/2",
        "consecutiveLimitUpDays": 2,
        "industryName": "电力"
      },
      {
        "tradeDate": "2026-05-13",
        "symbol": "000720",
        "name": "新能泰山",
        "changePercent": 10.0176,
        "latestPrice": 6.26,
        "amount": 745240736.0,
        "limitUpFund": 92232586.0,
        "firstLimitUpTime": "093506",
        "lastLimitUpTime": "093506",
        "limitUpStatistics": "5/3",
        "consecutiveLimitUpDays": 1,
        "industryName": "电网设备"
      },
      {
        "tradeDate": "2026-05-13",
        "symbol": "000767",
        "name": "晋控电力",
        "changePercent": 10.1075,
        "latestPrice": 5.12,
        "amount": 927343392.0,
        "limitUpFund": 188257909.0,
        "firstLimitUpTime": "093300",
        "lastLimitUpTime": "093300",
        "limitUpStatistics": "2/2",
        "consecutiveLimitUpDays": 2,
        "industryName": "电力"
      },
      {
        "tradeDate": "2026-05-13",
        "symbol": "000811",
        "name": "冰轮环境",
        "changePercent": 9.9965,
        "latestPrice": 31.8,
        "amount": 1940045760.0,
        "limitUpFund": 69140005.0,
        "firstLimitUpTime": "143051",
        "lastLimitUpTime": "143051",
        "limitUpStatistics": "3/2",
        "consecutiveLimitUpDays": 1,
        "industryName": "通用设备"
      }
    ],
    "count": 5,
    "total": null,
    "totalRelation": "unknown",
    "nextCursor": "c1.eyJ2IjoxLCJyZXNvdXJjZSI6ImxpbWl0X3VwX3Bvb2wi...省略",
    "hasMore": true
  },
  "requestId": "req_c2e57e58c51d48e8976c4d4dcc7fb62b",
  "ts": "2026-05-18T07:33:47.881186"
}
```

## JavaScript 示例

Node.js 18+ 或现代浏览器都可以使用 `fetch`。服务端脚本建议使用完整 URL：

```javascript
const BASE_URL = 'https://stock.xray.top';
const TOKEN = 'stk_你的Token明文';

async function request(path) {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: {
      Authorization: `Bearer ${TOKEN}`,
      Accept: 'application/json',
      'X-Client-Name': 'example-script',
    },
  });

  const body = await res.json();
  if (!res.ok || body.code !== 0) {
    throw new Error(`API error: http=${res.status}, code=${body.code}, message=${body.message}`);
  }
  return body.data;
}

const data = await request('/api/v2/open/market/bars/daily?symbols=000001,000002&start=2026-05-13&end=2026-05-13&limit=10');
console.log(data.items);
```

## Python 示例

```python
import requests

BASE_URL = "https://stock.xray.top"
TOKEN = "stk_你的Token明文"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "X-Client-Name": "example-python",
}

resp = requests.get(
    f"{BASE_URL}/api/v2/open/market/bars/daily",
    params={
        "symbols": "000001,000002",
        "start": "2026-05-13",
        "end": "2026-05-13",
        "limit": 10,
    },
    headers=headers,
    timeout=15,
)
body = resp.json()

if resp.status_code != 200 or body.get("code") != 0:
    raise RuntimeError(body)

for row in body["data"]["items"]:
    print(row["tradeDate"], row["symbol"], row["close"], row["changePercent"])
```

## 响应结构

开放接口统一返回 JSON 信封：

```json
{
  "code": 0,
  "message": "success",
  "data": {},
  "requestId": "req_xxxxxxxx",
  "ts": "2026-05-18T10:18:00.000000"
}
```

字段说明：

| 字段 | 说明 |
|------|------|
| `code` | 业务状态码，`0` 表示成功 |
| `message` | 状态说明 |
| `data` | 具体业务数据，列表接口通常包含 `items`、`count`、`nextCursor`、`hasMore` |
| `requestId` | 请求 ID，排查问题时建议一并提供 |
| `ts` | 服务端响应时间 |

分页接口常见结构：

```json
{
  "items": [],
  "count": 20,
  "total": null,
  "totalRelation": "unknown",
  "nextCursor": "eyJvZmZzZXQiOjIwfQ==",
  "hasMore": true
}
```

当 `hasMore` 为 `true` 时，把 `nextCursor` 原样传回下一次请求的 `cursor` 参数即可继续翻页。

## 常见错误码及处理

| code | HTTP | 含义 | 你可以怎么做 |
|------|------|------|--------------|
| `0` | 200 | 成功 | 解析 `data` |
| `40001` | 400 | 参数非法 | 检查日期格式 `yyyy-MM-dd`、必填参数、代码是否用英文逗号分隔 |
| `40101` | 401 | 未授权 | 确认 Token 是否正确、是否带 `Bearer ` 前缀、Token 是否已重置 |
| `40301` | 403 | 无权限 | 确认 Token scope 是否包含 `market:read` |
| `40401` | 404 | 资源不存在 | 核对股票代码、板块代码、交易日是否有数据 |
| `42901` | 429 | 超出额度 | 降低调用频率，或在门户查看用量 |
| `50001` | 500 | 服务内部错误 | 记录 `requestId` 后反馈 |
| `50301` | 503 | 服务暂时不可用 | 稍后重试，或调用 `/api/v2/open/market/health` 检查只读库状态 |

详情见 [错误码说明](guide/errors.md)。

## 文档导航

- [认证与 Token](guide/auth.md)：请求头、scope、可选 Header。
- [响应格式与分页](guide/response.md)：`items`、`nextCursor`、`hasMore` 的使用方式。
- [错误码说明](guide/errors.md)：错误码含义和排查建议。
- 左侧侧边栏：全部开放接口的参数表、curl 示例、字段表和 JSON 示例。

## 示例数据说明

文档中的行情示例主要使用 **2026-05-13** 交易日数据，外盘商品示例使用 **2026-05-15**。实际查询时，把 `tradeDate`、`start`、`end` 换成你需要的交易日即可。

如果需要在工具里调试，可以先访问 `https://stock.xray.top/v3/api-docs` 获取 OpenAPI JSON，再导入 Postman、Apifox 或 Knife4j；调用时统一添加：

```http
Authorization: Bearer stk_你的Token明文
Accept: application/json
```
