# aiseenlab.com brand page

> Public source, all rights reserved (see `LICENSE`). Live: https://aiseenlab.com (also www) · Cloudflare Pages project `aiseenlab-site`.

A single bilingual (中文 / English) page linking to:
- AI Visibility Audit — https://audit.aiseenlab.com ([source](https://github.com/ohomygood/ai-visibility-audit))
- X Engagement List (Chrome extension, not in the Chrome Web Store yet) — https://xeng.aiseenlab.com ([source](https://github.com/ohomygood/x-engagement-extension))

```bash
python3 scripts/build.py                 # -> site/
npx wrangler pages deploy site --project-name aiseenlab-site --branch main
```
No images, no payment QR, no trackers. The build fails if WeChat/QR copy or an image appears.
