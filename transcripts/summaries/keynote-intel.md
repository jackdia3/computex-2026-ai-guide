# Intel COMPUTEX 2026 Keynote 重點摘要

> 原片：https://www.youtube.com/watch?v=1h_zY377urU（1:06:21，Intel）
> 摘要驗證日：2026-06-03 / 非官方整理（合理使用），完整內容請看原片

## 一句話總結

Intel 以「open ecosystem + x86 + 18A + rack-scale AI」為主軸，將 PC、edge、physical AI、foundational data center 與 emerging intelligence center 串成一套從 silicon 到 system 的 AI 時代策略。

## 重點時間軸

| 時間戳 | 主題/發表 | 重點 |
|---|---|---|
| [0:02] | 開場影片 | 強調 silicon、open platforms、shared standards、partnerships 與 unified architecture。 |
| [2:03] | Lip-Bu Tan 開場 | 連結 Silicon Valley 與 Taiwan Silicon Island，回顧台灣半導體與 Intel 40 年合作。 |
| [5:08] | CEO 執行主軸 | Tan 表示 Intel 要回到工程核心，execution、focus、deliver 是接下來的重點。 |
| [7:11] | 四大 compute ecosystem | PC、edge/agentic AI/physical AI、foundational data centers、emerging intelligence centers。 |
| [10:15] | Alex 談 PC 與 18A | Intel 18A 進入 full scale，Core Ultra Series 3 有超過 300 個設計，Core Series 3 已超過 70 個設計。 |
| [15:37] | Arc G3 handheld gaming | Arc G3 針對掌機遊戲調校，逐字稿提到相較競品快 40%、同效能半功耗、AAA 遊戲 1080p。 |
| [17:39] | Edge 與 physical AI | Series 3 進入 edge，超過 130 個設計、4,000 多個 edge ecosystem partners，涵蓋製造、機器人、零售等。 |
| [19:46] | Perplexity hybrid agentic inference | Perplexity Computer 在 Core Ultra Series 3 上做本地敏感資料分類，雲端只處理可外送資料。 |
| [25:03] | x86 與 CPU core | Tan 強調 x86 仍是資料中心主流，P-core/E-core 分別面向效能與效率。 |
| [29:10] | Xeon 6 Plus | Xeon 6 Plus 以 288 E-cores、576MB L3 cache、Intel 18A，主打雲端與網路基礎設施密度。 |
| [32:14] | Agentic AI 改變資料中心 | Kavoke 說 agentic AI 不只是 LLM 推論，還會用工具、讀寫檔案、檢查規則，使 CPU 需求提高。 |
| [35:17] | CPU/GPU workload demo | 傳統 inference GPU-heavy；agentic pipeline 中 linting、web fetch、compile、unit test 分散到 Xeon 6 P-core/E-core。 |
| [38:23] | Rack-scale blueprints | Intel 推出基於 open standards 的 rack-scale blueprints，分 agentic performance 與 agent density。 |
| [40:24] | Foxconn 合作 | Foxconn 與 Intel 合作開發基於 Xeon 的 rack-scale AI infrastructure。 |
| [44:28] | SambaNova 合作 | SM50 rack-scale AI infrastructure 使用 Xeon 6 + SambaNova RDU，展示 CPU/RDU/GPU 異質 disaggregated inference。 |
| [47:34] | Vista / Vector Core Compute | Robert Smith 談企業 AI agent 需求，VC2 以 disaggregated inference 改造既有 data center。 |
| [51:35] | Purpose-built silicon | Intel 宣布進入 custom silicon 市場，提到 Google IPU 與 Ericsson 下一代 infrastructure silicon。 |
| [55:39] | Brain-trained / bio / industrial partners | Echo Neuro、Greenstone、Hitachi、Siemens 分別代表腦啟發運算、生醫、工業與半導體價值鏈合作。 |
| [1:02:46] | 收束 | Tan 重申 PC、edge、agentic physical AI、data center、emerging intelligence center 的整體機會。 |

## 依主題深入

### 1. Intel 把台灣定位成 ecosystem 共同體

Tan 在 [2:03]-[5:08] 把 Intel 的故事放在 Silicon Valley 與 Taiwan Silicon Island 的脈絡中，回顧新竹科學園區、TSMC 創立前後的半導體發展，也強調台灣 OEM/ODM、設計到製造的完整鏈條對 Intel 成長的重要性。這不是單純致意，而是為後面「built together」的主軸鋪陳。

### 2. 18A 從旗艦 PC 擴到主流與掌機

Alex 在 [10:15]-[13:18] 說 Core Ultra Series 3 是 Intel 第一個 18A 產品，面向 premium mobile performance 與 battery life；接著 Core Series 3 把相同 IP 下放到 mainstream market。到 [15:37]-[16:38]，Arc G3 則把 Core Ultra Series 3 衍生能力推進 handheld gaming，主打效能穩定與省電。

### 3. On-device AI 與 hybrid agentic inference

Perplexity 段落 [19:46]-[24:59] 是 keynote 的 AI PC 使用情境核心：本地模型先判斷 NDA、dealroom files、財務模型與白板資料哪些不能出裝置，再讓雲端大型模型處理外部研究與報告生成。Tan 與 Aravind 的共識是未來同時需要更多 data center compute 與 local machine compute。

### 4. Xeon 6 Plus 與 agentic data center 的 CPU 復權

Kavoke 在 [29:10]-[37:21] 把 foundational workloads 與 intelligence at scale 放在一起：資料中心既要跑 5G、database、cloud services，也要承接 AI inference。Agentic AI 的差異在於它用 goals 而非單一 prompts，會重複 planning、acting、reflecting，並在工具呼叫、檔案讀寫、規則檢查中大量使用 CPU。

### 5. Rack-scale 與異質 disaggregated inference

[38:23]-[50:34] 由 Intel、Foxconn、SambaNova、Vista 串起 rack-scale 故事。Intel 強調不採 one-size-fits-all，而是以 open standards blueprint、Xeon 6 P-core/E-core、RDU、GPU 等異質架構配合不同 agentic workload。SambaNova demo 中，Xeon 做 tooling execution、RDU 做 decode/token generation、GPU 做 prompt caching 與 prefill。

### 6. Purpose-built silicon 延伸到 hyperscaler、telco、生醫與工業

[51:35]-[1:01:44] 轉向 custom silicon 與垂直合作。Intel 提到已為 Google 提供 infrastructure processing unit，也與 Ericsson 合作下一代 infrastructure silicon；後續 Echo Neuro、Greenstone、Hitachi、Siemens 則把 AI silicon 延伸到腦訓練演算法、生醫資料處理、量子/工業與半導體設計製造流程。

## 給觀展者的重點

6/5 觀展者若要把 Intel keynote 轉成現場觀展路線，可以優先看三類東西：第一，搭載 Core Ultra Series 3 / Core Series 3 的 AI PC、輕薄筆電與 handheld gaming 裝置；第二，Intel pavilion 提到的 edge / physical AI 應用，特別是製造、機器人、零售等垂直場景；第三，伺服器與 rack-scale AI infrastructure 相關展示，重點不是單顆 GPU，而是 Xeon 6、Xeon 6 Plus、rack design、ODM 夥伴與異質 inference 架構如何組成系統。

## 金句（每段 ≤2 句原文引用 + 時間戳）

> "Our future is with ecosystems." [0:02]

> "Execution has always always at the top of my list." [5:08]

> "The silicon we are building now will be for human use and the digital agent use." [8:11]

> "Hybrid agentic inference is how we maximize token value per watt per user." [20:49]

> "The CPU orchestrates the show." [34:15]

> "AI at scale will require heterogeneous computing." [43:28]
