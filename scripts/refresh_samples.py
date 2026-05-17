#!/usr/bin/env python3
"""Refresh api/*.md with 2026-05-13 real samples and tabular item display."""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

BASE = "http://127.0.0.1:8788"
TOKEN = "stk_NjYxMWZlZGEtOTU0MC00MWRmLWE1YzUtOTliNDBkMTViMTRm"
DATE = "2026-05-13"
ROOT = Path(__file__).resolve().parent.parent
API = ROOT / "api"

# file -> (curl_query_suffix, api_path_for_fetch)
ENDPOINTS: dict[str, tuple[str, str]] = {
    "meta-ping.md": ("", "/api/v2/open/meta/ping"),
    "market-health.md": ("", "/api/v2/open/market/health"),
    "market-latest-session.md": ("", "/api/v2/open/market/meta/latest-session"),
    "market-coverage.md": (f"?start={DATE}&end={DATE}", f"/api/v2/open/market/meta/coverage?start={DATE}&end={DATE}"),
    "quality-coverage-check.md": (
        f"?start={DATE}&end={DATE}&boardTypes=industry&boardCodes=BK0420",
        f"/api/v2/open/market/quality/coverage-check?start={DATE}&end={DATE}&boardTypes=industry&boardCodes=BK0420",
    ),
    "securities.md": ("?code=000001&limit=3", "/api/v2/open/market/securities?code=000001&limit=3"),
    "securities-symbol.md": ("", "/api/v2/open/market/securities/000001"),
    "calendar.md": (f"?start={DATE}&end={DATE}", f"/api/v2/open/market/calendar?start={DATE}&end={DATE}"),
    "bars-daily.md": (
        f"?symbols=000001,000002&start={DATE}&end={DATE}&limit=2",
        f"/api/v2/open/market/bars/daily?symbols=000001,000002&start={DATE}&end={DATE}&limit=2",
    ),
    "bars-daily-symbol.md": (
        f"?start={DATE}&end={DATE}",
        f"/api/v2/open/market/bars/daily/000001?start={DATE}&end={DATE}",
    ),
    "snapshots-daily.md": (
        f"?symbols=000001&trade_date={DATE}&limit=1",
        f"/api/v2/open/market/snapshots/daily?symbols=000001&trade_date={DATE}&limit=1",
    ),
    "snapshots-daily-symbol.md": (
        f"?trade_date={DATE}",
        f"/api/v2/open/market/snapshots/daily/000001?trade_date={DATE}",
    ),
    "pools-limit-up.md": (f"?trade_date={DATE}&limit=5", f"/api/v2/open/market/pools/limit-up?trade_date={DATE}&limit=5"),
    "boards-dimensions.md": ("?boardType=industry&limit=3", "/api/v2/open/market/boards/dimensions?boardType=industry&limit=3"),
    "boards-industry.md": (f"?trade_date={DATE}&limit=3", f"/api/v2/open/market/boards/industry?trade_date={DATE}&limit=3"),
    "boards-concept.md": (f"?trade_date={DATE}&limit=3", f"/api/v2/open/market/boards/concept?trade_date={DATE}&limit=3"),
    "boards-industry-constituents.md": (
        f"?trade_date={DATE}&limit=3",
        f"/api/v2/open/market/boards/industry/BK0420/constituents?trade_date={DATE}&limit=3",
    ),
    "boards-concept-constituents.md": (
        f"?trade_date={DATE}&limit=2",
        f"/api/v2/open/market/boards/concept/BK0425/constituents?trade_date={DATE}&limit=2",
    ),
    "boards-industry-bars.md": (
        f"?start={DATE}&end={DATE}",
        f"/api/v2/open/market/boards/industry/BK0420/bars/daily?start={DATE}&end={DATE}",
    ),
    "boards-concept-bars.md": (
        f"?start={DATE}&end={DATE}",
        f"/api/v2/open/market/boards/concept/BK0425/bars/daily?start={DATE}&end={DATE}",
    ),
    "boards-bars-daily-batch.md": (
        f"?boardTypes=industry&boardCodes=BK0420&start={DATE}&end={DATE}&limit=2",
        f"/api/v2/open/market/boards/bars/daily?boardTypes=industry&boardCodes=BK0420&start={DATE}&end={DATE}&limit=2",
    ),
    "boards-constituents-batch.md": (
        f"?boardTypes=industry&boardCodes=BK0420&start={DATE}&end={DATE}&limit=2",
        f"/api/v2/open/market/boards/constituents?boardTypes=industry&boardCodes=BK0420&start={DATE}&end={DATE}&limit=2",
    ),
    "boards-symbols.md": (
        f"?boardTypes=industry&boardCodes=BK0420&start={DATE}&end={DATE}&limit=3",
        f"/api/v2/open/market/boards/symbols?boardTypes=industry&boardCodes=BK0420&start={DATE}&end={DATE}&limit=3",
    ),
    "tradeability-facts.md": (
        f"?symbols=000001&start={DATE}&end={DATE}&limit=1",
        f"/api/v2/open/market/tradeability/facts?symbols=000001&start={DATE}&end={DATE}&limit=1",
    ),
    "external-instruments.md": ("?limit=3", "/api/v2/open/market/external/instruments?limit=3"),
    "external-markets-daily.md": (
        f"?start={DATE}&end={DATE}&limit=2",
        f"/api/v2/open/market/external/markets/daily?start={DATE}&end={DATE}&limit=2",
    ),
    "external-commodities-daily.md": (
        "?start=2026-05-15&end=2026-05-15&limit=2",
        "/api/v2/open/market/external/commodities/daily?start=2026-05-15&end=2026-05-15&limit=2",
    ),
}

# Prefer these columns when present (order matters)
PREFERRED_COLS = [
    "tradeDate", "symbol", "name", "boardCode", "boardName", "boardType",
    "rankNo", "open", "high", "low", "close", "changePercent", "changeAmount",
    "volume", "amount", "turnoverRate", "leadingStockName", "latestPrice",
    "ticker", "commodity", "assetType", "isOpen", "message", "tokenId", "scope", "path",
    "ok", "latencyMs", "stockReadEnabled",
]


def fetch(path: str) -> dict:
    req = urllib.request.Request(
        BASE + path,
        headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fmt_cell(v) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.4g}" if abs(v) < 1e12 else f"{v:.2e}"
    if isinstance(v, (dict, list)):
        s = json.dumps(v, ensure_ascii=False)
        return s if len(s) <= 40 else s[:37] + "…"
    return str(v)


def items_table(items: list) -> str:
    if not items:
        return "_（本示例 `items` 为空，请检查本地库是否已有该日数据。）_\n"
    if not isinstance(items[0], dict):
        return "| 值 |\n|----|\n" + "\n".join(f"| {fmt_cell(x)} |" for x in items) + "\n"

    keys: list[str] = []
    for k in PREFERRED_COLS:
        if any(k in row for row in items):
            keys.append(k)
    for row in items:
        for k in row:
            if k not in keys and k not in ("source", "raw_payload", "updated_at", "remark"):
                keys.append(k)
    keys = keys[:12]  # keep table readable

    header = "| " + " | ".join(keys) + " |"
    sep = "| " + " | ".join("---" for _ in keys) + " |"
    rows = ["| " + " | ".join(fmt_cell(row.get(k)) for k in keys) + " |" for row in items]
    return header + "\n" + sep + "\n" + "\n".join(rows) + "\n"


def envelope_table(body: dict) -> str:
    return (
        "| 字段 | 值 |\n|------|-----|\n"
        f"| `code` | {body.get('code')} |\n"
        f"| `message` | {body.get('message')} |\n"
        f"| `requestId` | `{body.get('requestId', '')}` |\n"
        f"| `ts` | {body.get('ts')} |\n"
    )


def data_meta_table(data: dict) -> str:
    if not isinstance(data, dict):
        return ""
    meta_keys = ["count", "total", "hasMore", "nextCursor", "adj"]
    present = [k for k in meta_keys if k in data]
    if not present:
        return ""
    lines = ["| 分页字段 | 值 |", "|----------|-----|"]
    for k in present:
        v = data[k]
        if k == "nextCursor" and v:
            v = str(v)[:24] + "…"
        if isinstance(v, bool):
            v = "true" if v else "false"
        lines.append(f"| `data.{k}` | {fmt_cell(v)} |")
    return "\n".join(lines) + "\n"


def build_response_section(body: dict, date_note: str) -> str:
    data = body.get("data")
    lines = [
        "## 响应",
        "",
        f"> **注意：** 下列数据来自本地实调（`{BASE}`），行情类示例交易日为 **{date_note}**。",
        "",
        "### 响应信封",
        "",
        envelope_table(body),
    ]

    if isinstance(data, dict) and "items" in data:
        items = data.get("items") or []
        lines += [
            "### 分页信息",
            "",
            data_meta_table(data) or "_本页无额外分页字段。_\n",
            f"### `data.items` 表格（{date_note}）",
            "",
            items_table(items if isinstance(items, list) else []),
        ]
    elif isinstance(data, dict):
        lines += [
            f"### `data` 字段（{date_note}）",
            "",
            items_table([data]),
        ]

    lines += [
        "### 完整 JSON（节选）",
        "",
        "```json",
        json.dumps(body, ensure_ascii=False, indent=2)[:3500],
        "```",
        "",
        "### 可能出现的错误",
        "",
        "- `40101` Token 无效",
        "- `40301` scope 不足",
        "- `40001` 参数错误",
        "- `40401` 无数据",
        "- `42901` 限流",
        "",
    ]
    return "\n".join(lines)


def patch_file(name: str, body: dict, fetch_path: str) -> None:
    path = API / name
    text = path.read_text(encoding="utf-8")
    # Align curl example query with fetch path
    if "curl -sS" in text and "?" in fetch_path:
        q = fetch_path.split("?", 1)[1]
        text = re.sub(
            r'(curl -sS "\$BASE_URL)(/api/v2/open/[^"?]+)(\?[^"]*)?"',
            rf'\1\2?{q}"',
            text,
            count=1,
        )

    date_note = DATE
    if "external-commodities" in name:
        date_note = "2026-05-15（商品库示例日）"

    new_resp = build_response_section(body, date_note)
    text = re.sub(r"\n## 响应\n[\s\S]*$", "\n" + new_resp, text)

    # Ensure curl uses 2026-05-13 in examples
    text = text.replace("trade_date=2026-04-17", f"trade_date={DATE}")
    text = text.replace(f"start=2026-04-17", f"start={DATE}")
    text = text.replace(f"end=2026-04-30", f"end={DATE}")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for name, (curl_suffix, fetch_path) in ENDPOINTS.items():
        try:
            body = fetch(fetch_path)
        except Exception as e:
            print(f"SKIP {name}: {e}")
            continue
        if body.get("code") != 0:
            print(f"WARN {name}: code={body.get('code')}")
        patch_file(name, body, fetch_path)
        print(f"OK {name}")
    print("done")


if __name__ == "__main__":
    main()
