# COMPUTEX 2026 AI Guide

> ⚠️ **非官方專案 / Unofficial** — 本專案與 COMPUTEX、外貿協會（TAITRA）、台北市電腦公會（TCA）無任何關係，為個人觀展者整理的公開資訊彙整。
>
> 給 AI 助理讀的 COMPUTEX 2026 攤位 / 觀展結構化資料 — 讓任何 AI（ChatGPT / Claude / Gemini）能直接幫你規劃逛展路線、找攤位、避坑。
>
> Structured COMPUTEX Taipei 2026 booth & visitor data, optimized for AI assistants.

**展期**：2026/06/02 – 06/05　**大眾日**：6/5（南港 09:30-15:30 / 世貿 09:30-16:30）
**資料驗證日**：2026-06-01（6/3 增補展期資訊）　**性質**：非官方整理，攤位號對官方參展商查詢逐筆驗證

---

## 🤖 怎麼用（3 種方式）

### 方式 1：貼網址給 AI（最簡單）

把這段貼給任何能上網的 AI（ChatGPT / Claude / Gemini / Perplexity）：

```
請讀取 https://jackdia3.github.io/computex-2026-ai-guide/llms-full.txt
然後幫我規劃 6/5 COMPUTEX 行程：我想看 AI 伺服器跟機器人，下午 3 點要離開。
```

> 備用網址（若上面打不開）：`https://raw.githubusercontent.com/jackdia3/computex-2026-ai-guide/main/llms-full.txt`

### 方式 2：複製內容貼給 AI（AI 不能上網時用）

開啟 [llms-full.txt](https://jackdia3.github.io/computex-2026-ai-guide/llms-full.txt) → 全選複製 → 貼到 AI 對話框 → 接著問你的行程問題。內容約 800 行，多數 AI 都吃得下。

### 方式 3：人類直接看 / 列印

- 🖨 **[一頁攻略 PDF（A4 雙面）](print/cheatsheet-a4.pdf)** — 下載直接列印帶去現場（[HTML 原始檔](print/cheatsheet-source.html)可自行修改）
- 📊 **[攻略簡報（12 張 PPTX）](slides/computex-2026-slides.pptx)** — 圖文版攻略，適合分享給朋友 / 社群內部講解用
- [觀展資訊](docs/visiting-info.md) — 票務 / 入場 / 避坑清單
- [必看攤位導覽](docs/booth-guide.md) — 攤位號 + 可以問 PM 什麼

---

## 📁 內容結構

```
computex-2026-ai-guide/
├── llms.txt              ← AI 入口（llmstxt.org 標準）
├── llms-full.txt         ← 全部內容單一檔（AI 一次讀完）
├── data/
│   ├── exhibitors.json   ← 19 家精選攤位（號碼已驗證）+ 60+ 家 zone 級資料
│   ├── halls.json        ← 三館樓層展區 / 開放時間 / 交通 / 票務
│   ├── tour-routes.json  ← 官方導覽團 12 條路線
│   └── videos.json       ← 140 支影片索引（keynote + 官方頻道，含摘要狀態）
├── docs/
│   ├── visiting-info.md  ← 觀展資訊（人類可讀版）
│   ├── booth-guide.md    ← 必看攤位導覽 + BC Award 得獎攤位 + 展期發表（人類可讀版）
│   ├── computex-online.md ← COMPUTEX Online 線上平台指南（不能到場 / 展後回看）
│   └── video-summaries.md ← 影音內容重點整理（81 支影片 AI 摘要導覽）
├── transcripts/
│   └── summaries/        ← Keynote / COMPUTOUR / 開箱影片摘要（黃仁勳 keynote 含 20 發表時間戳）
├── scripts/              ← 影片字幕 pipeline（yt-dlp 抓字幕 → 清洗 → 索引，可增量重跑）
├── print/
│   ├── cheatsheet-a4.pdf     ← 一頁攻略印刷版（A4 雙面）
│   └── cheatsheet-source.html ← 印刷版原始檔（可自行修改重印）
└── slides/
    ├── computex-2026-slides.pptx ← 攻略簡報（12 張，圖文版）
    └── SOURCES.md                 ← 簡報圖片來源聲明
```

## ⚡ 30 秒重點

| 重點 | 內容 |
|---|---|
| 入場 | **科技／相關產業工作者 → 現場辦專業人士登錄（免費，6/2-6/5 全展期，現場審核）**；一般民眾 → NT$200 購票（僅 6/5） |
| ⏰ 硬限制 | 6/5 南港 15:30 關 / 世貿 16:30 關 / 未滿 18 歲不能入場 / 現場售票至 15:00 |
| 🚀 InnoVEX | 新創展區（近 500 家、22 國）開放至 6/5；Pitch 頒獎典禮 6/4 已辦完 |
| 🏆 BC Award | 得獎名單 6/2 公布（NVIDIA 年度大獎 / ASUS 10 獎）；南港 2 館 4F R 區入口左側展示區一站看完 |
| 📺 不能到場 | [COMPUTEX Online](docs/computex-online.md)：官方 YouTube 免費看 COMPUTOUR 逛展 / 開箱節目 / 演講回放，展後仍可看 |
| 🎬 沒空看影片 | [影音重點整理](docs/video-summaries.md)：黃仁勳 2hr keynote → 20 個發表時間戳摘要；81 支影片 AI 整理 |
| 交通 | 兩館之間捷運約 30-40 分鐘；14:00-14:45 是壅塞高峰（整理者經驗估計） |

## 📌 資料來源與授權

- **資料來源**：COMPUTEX 官方網站、官方參展商查詢系統、官方攻略手冊、TCA 官方導覽團路線（皆為公開可取得之資訊）
- **資料性質**：本 repo 僅彙整**事實性資訊**（廠商名稱、攤位號碼、展區位置、開放時間）並附上整理者自行撰寫的觀展建議；不包含官方文件之圖片、版面或完整文件重製
- **驗證方式**：攤位號於 2026-06-01 對官方參展商查詢逐筆比對；2026-06-03 增補展期資訊（BC Award 得獎名單、重大發表、線上平台）
- **免責**：非官方專案，與 COMPUTEX / TAITRA / TCA 無關。現場請以官方 APP 與最新公告為準；本資料若有錯誤，整理者不負任何責任
- **授權**：整理內容採 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hant)；展會相關名稱與原始資訊之權利屬各權利人所有

## 🛡️ 權利人聲明（Takedown）

若 COMPUTEX 主辦單位（TAITRA / TCA）或任何參展廠商認為本 repo 內容不妥，請開 [Issue](../../issues) 或透過 GitHub 聯絡整理者，**將於收到通知後 48 小時內配合移除或修改**。本專案目的為協助觀展者並推廣展會，無任何商業用途。

## 🙋 維護

整理：[Jack Tseng](https://github.com/jackdia3)（個人專案）
發現資料錯誤？開 [Issue](../../issues) 或直接 PR。
