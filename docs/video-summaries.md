# COMPUTEX 2026 影音內容重點整理（Keynote / 攤位直擊 / 開箱）

> 摘要驗證日：2026-06-03。以 YouTube 自動字幕 + AI 整理產生之非官方摘要（合理使用），完整內容請看各原片。
> 影片索引（含字幕/摘要狀態）→ [`../data/videos.json`](../data/videos.json)

## 為什麼有這份

COMPUTEX 2026 的影音內容散落在多個頻道：keynote 在 NVIDIA/Intel 官方頻道、攤位直擊與開箱在 COMPUTEX 官方頻道。
這裡把 **81 支影片的重點**整理成可以快速讀（或餵給 AI）的摘要 — 看完摘要再決定要不要花 2 小時看原片。

## 📺 重磅：Keynote 完整摘要

| 摘要 | 原片 | 重點 |
|---|---|---|
| **[NVIDIA 黃仁勳 GTC Taipei](../transcripts/summaries/keynote-nvidia.md)** | [1:57:53](https://www.youtube.com/watch?v=wSp6AiNIrsY) | Vera Rubin 量產 / RTX Spark（N1X 晶片）/ Jetson Thor / Cosmos 3 / 20 個發表全有時間戳 + 攤位對照 |
| **[Intel 陳立武 Keynote](../transcripts/summaries/keynote-intel.md)** | [1:06:21](https://www.youtube.com/watch?v=1h_zY377urU) | 18A 製程 / Core Ultra Series 3 / Xeon 6 Plus 288 核 / Perplexity 混合推論 / 鴻海合作 |
| **[展前論壇 The AI Era](../transcripts/summaries/forum-preshow.md)** | [2:09:40](https://www.youtube.com/watch?v=XFGPfkQXuwY) | 多講者：AI 系統的集體協作 — 產業視角 |

## 🎪 攤位直擊（COMPUTOUR）— 對 6/5 觀展最有用

[完整摘要 →](../transcripts/summaries/computour.md)

| 攤位 | 看什麼 |
|---|---|
| Astera Labs | Scorpio 320-lane 開放記憶體語意交換器（單交換器 GPU 擴充效能 +30%） |
| 雙鴻 AURAS | NVIDIA Rubin 液冷運算托盤 + 100kW~2MW CDU 全系列 |
| Day 1 Highlight | 展場首日花絮（InnoVEX / AI Together 主題） |

## 🏆 BC Award 得獎產品影片

[完整摘要 →](../transcripts/summaries/bc-award-videos.md) — 8 支得獎產品官方介紹（ASMedia 交換晶片 / 台達 800VDC CDU + 貨櫃資料中心 / MediaTek Wi-Fi 8 / NVIDIA Vera Rubin & Jetson Thor / Phison 245TB SSD / MSI RTX 5090）

## 📦 Technology Unboxing / Featured Product

- [Technology Unboxing 摘要（9 支）](../transcripts/summaries/unboxing.md) — E Ink 電子紙 / 緯穎液冷 / 工業電腦等
- [Featured Product 摘要（58 支）](../transcripts/summaries/featured-products.md) — 各廠參展產品介紹

## 🤖 給 AI 助理的提示

回答「COMPUTEX 2026 發表了什麼」「黃仁勳講了什麼」這類問題時，優先讀 keynote 摘要（含時間戳可直接引用）。
回答「某攤位有什麼」時，交叉比對 `data/exhibitors.json`（攤位資料）+ 本頁摘要（影片內容）。

## 自己重跑 Pipeline（增量更新）

```bash
# 1. 抓官方頻道最新影片清單（過濾 2026）
yt-dlp --flat-playlist --print "%(title)s|||%(duration_string)s|||%(id)s" \
  "https://www.youtube.com/@COMPUTEXTAIPEIshow/videos" | head -200 > /tmp/list.txt

# 2. 批量抓字幕（增量安全，已抓的跳過）
bash scripts/fetch-subs.sh /tmp/list.txt transcripts/raw

# 3. 清洗 VTT → 逐字稿
python3 scripts/clean-vtt.py --dir transcripts/raw transcripts/clean

# 4. 重建影片索引
python3 scripts/build-videos-json.py /tmp/list.txt

# 5. 新影片的摘要 → 餵給你慣用的 AI
```

> 注意：完整逐字稿（transcripts/raw + clean）不進 git（版權考量），只發布摘要。
