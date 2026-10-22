"""Build the aiseenlab.com brand page into site/ (Cloudflare Pages project `aiseenlab-site`).

    python3 scripts/build.py              # product links -> custom domains (use once DNS is active)
    python3 scripts/build.py --pages-dev  # product links -> *.pages.dev (while custom domains are pending)
    npx wrangler pages deploy site --project-name aiseenlab-site --branch main

No payment QR / WeChat, no images. Claims kept honest: Gemini-only engine, extension not on sale yet.
"""
import pathlib, shutil, sys

PAGES_DEV = "--pages-dev" in sys.argv
AUDIT = "https://ai-visibility-audit-bvb.pages.dev" if PAGES_DEV else "https://audit.aiseenlab.com"
XENG = "https://xeng-site.pages.dev" if PAGES_DEV else "https://xeng.aiseenlab.com"
SITE = "https://aiseenlab.com"
CONTACT = "go_with_prob@mail.grokbot.com"

root = pathlib.Path(__file__).resolve().parents[1]
out = root / "site"
shutil.rmtree(out, ignore_errors=True); out.mkdir()

CSS = """body{font:16px/1.65 system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;margin:0;color:#111827;background:#fafafa}
header,main,footer{max-width:960px;margin:0 auto;padding:0 20px}header{display:flex;justify-content:space-between;align-items:center;padding-top:18px;padding-bottom:18px}
.brand{font-weight:800;font-size:20px;letter-spacing:.2px}.lang button{border:1px solid #d1d5db;background:#fff;border-radius:999px;padding:4px 12px;cursor:pointer;font:inherit;font-size:14px}
h1{font-size:34px;line-height:1.25;margin:26px 0 10px}.lead{font-size:19px;color:#374151;max-width:740px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin:34px 0}
.card{background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:24px;display:flex;flex-direction:column}
.card h2{margin:0 0 6px;font-size:22px}.tag{display:inline-block;font-size:13px;border-radius:999px;padding:2px 10px;margin-bottom:10px}
.live{background:#dcfce7;color:#166534}.soon{background:#fef3c7;color:#92400e}.card ul{padding-left:20px;margin:8px 0 18px}.card li{margin:4px 0}
.btn{margin-top:auto;align-self:flex-start;display:inline-block;padding:10px 18px;border-radius:999px;background:#2563eb;color:#fff;text-decoration:none;font-weight:600}
.muted{color:#6b7280;font-size:14px}footer{border-top:1px solid #e5e7eb;margin-top:40px;padding-top:18px;padding-bottom:40px}a{color:#2563eb}
[data-lang]{display:none}html[lang=en] [data-lang=en],html[lang=zh-CN] [data-lang=zh]{display:block}"""

T = {
 "en": dict(
  h1="Small, honest tools for being seen online.",
  lead="AI Seen Lab builds two small products: an audit that checks whether AI assistants can find and recommend your online store, and a Chrome extension that shows who engages with your posts on X.",
  a_name="AI Visibility Audit", a_tag="Live",
  a_pts=["Free quick check: can AI read your store, and does Gemini mention it?",
         "Full report: $19 USD one-off, delivered within 24 hours, with fix files you can apply.",
         "Engine today: Google Gemini only. ChatGPT and Perplexity are coming soon.",
         "Refund: full refund within 7 days if the report isn't delivered within 24 h or isn't useful (once per customer)."],
  a_btn="Open AI Visibility Audit →",
  x_name="X Engagement List (Chrome extension)", x_tag="Coming soon",
  x_pts=["Top commenters, replies you haven't answered, and accounts that don't follow you back.",
         "Runs in your own browser; data stays local. No X API, no password, never posts or follows for you.",
         "Not yet in the Chrome Web Store, so it isn't for sale yet."],
  x_btn="Learn more →",
  contact="Contact", disc="Independent project. Not affiliated with or endorsed by Google, OpenAI, Perplexity or X Corp; product names are used only to describe compatibility."),
 "zh": dict(
  h1="让你的店和内容被看见的小工具，说实话、不夸大。",
  lead="AI Seen Lab 做两个小产品：一个检查 AI 助手能否找到并推荐你的独立站；一个 Chrome 扩展，帮你看清谁在和你的 X 帖子互动。",
  a_name="AI 可见度体检", a_tag="已上线",
  a_pts=["免费快速检查：AI 能否读懂你的店？Gemini 会不会提到你？",
         "完整报告：一次性 19 美元，24 小时内交付，附可直接使用的修复文件。",
         "目前只使用 Google Gemini；ChatGPT 和 Perplexity 即将支持。",
         "退款：如果 24 小时内未交付或报告没有用，7 天内可全额退款（每位客户限一次）。"],
  a_btn="打开 AI 可见度体检 →",
  x_name="X 互动名单助手（Chrome 扩展）", x_tag="即将推出",
  x_pts=["评论排行、还没回复的评论、没有回关你的账号。",
         "在你自己的浏览器里运行，数据只存本地。不用 X API、不要密码，也不会替你发帖或关注。",
         "尚未上架 Chrome 网上应用店，所以暂不出售。"],
  x_btn="了解更多 →",
  contact="联系", disc="独立项目，与 Google、OpenAI、Perplexity 或 X Corp 无关联、未获其认可；产品名称仅用于说明兼容性。"),
}

def block(l, t):
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    return f"""<div data-lang="{l}"><h1>{t['h1']}</h1><p class="lead">{t['lead']}</p>
<div class="cards">
<section class="card"><span class="tag live">{t['a_tag']}</span><h2>{t['a_name']}</h2><ul>{li(t['a_pts'])}</ul><a class="btn" href="{AUDIT}/">{t['a_btn']}</a></section>
<section class="card"><span class="tag soon">{t['x_tag']}</span><h2>{t['x_name']}</h2><ul>{li(t['x_pts'])}</ul><a class="btn" href="{XENG}/">{t['x_btn']}</a></section>
</div></div>"""

def foot(l, t):
    return f"""<div data-lang="{l}"><p>{t['contact']}: <a href="mailto:{CONTACT}">{CONTACT}</a></p><p class="muted">{t['disc']}</p></div>"""

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Seen Lab — AI Visibility Audit · X Engagement List</title>
<meta name="description" content="AI Seen Lab: AI Visibility Audit (does Gemini recommend your store?) and X Engagement List (Chrome extension, coming soon).">
<link rel="canonical" href="{SITE}/"><style>{CSS}</style>
<script>(function(){{var p=null;try{{p=localStorage.getItem('asl_lang')}}catch(e){{}}if(!p)p=(navigator.language||'').toLowerCase().indexOf('zh')===0?'zh':'en';document.documentElement.lang=p==='zh'?'zh-CN':'en';}})();
function setLang(l){{document.documentElement.lang=l==='zh'?'zh-CN':'en';try{{localStorage.setItem('asl_lang',l)}}catch(e){{}}}}</script></head>
<body><header><div class="brand">AI Seen Lab</div><div class="lang"><button onclick="setLang('zh')">中文</button> <button onclick="setLang('en')">English</button></div></header>
<main>{block('en', T['en'])}{block('zh', T['zh'])}</main>
<footer>{foot('en', T['en'])}{foot('zh', T['zh'])}<p class="muted">© 2026 AI Seen Lab</p></footer></body></html>
"""
(out / "index.html").write_text(html, encoding="utf-8")
(out / "_headers").write_text("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: DENY
  Permissions-Policy: camera=(), microphone=(), geolocation=()
""")
low = html.lower()
assert "wechat" not in low and "微信" not in html and "qr" not in low and "<img" not in low, "forbidden content"
print("built", out, "links:", AUDIT, XENG)
