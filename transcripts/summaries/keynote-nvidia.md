# NVIDIA GTC Taipei 2026 Keynote 重點摘要

> 原片：https://www.youtube.com/watch?v=wSp6AiNIrsY（1:57:53，NVIDIA 官方頻道）
> 講者：Jensen Huang（黃仁勳）/ 日期：2026-06-01 / 摘要驗證日：2026-06-03
> 本摘要為非官方整理（合理使用），完整內容請看原片。

## 一句話總結

黃仁勳宣告「有用的 AI（useful AI）已經到來」：Agentic AI 成為新的運算模式（模型 + harness + 工具 + runtime），NVIDIA 為此推出全面量產的 Vera Rubin 平台、專為 agent 設計的 Vera CPU、與 Microsoft/聯發科合作重新發明 PC 的 RTX Spark，以及 Cosmos 3 / Alpamayo 2 / Isaac GR00T 三大 Physical AI 發表。整場 keynote 的核心論點：token 已成為有利潤的營收單位，「算力即營收」，而台灣供應鏈是這一切的起點。

## 重大發表時間軸

| 時間戳 | 發表 | 重點 | 展場哪裡看得到 |
|---|---|---|---|
| [5:51] | Agentic AI 元年宣言 | 兩年前預告的 agentic AI 已正式到來，AI 從生成式進化為「會做事」的有用 AI。 | 世貿一館 AI 機器人區（立端 A1227a、所羅門 A0811a 皆有 agentic demo） |
| [6:51] | GitHub commits 數據 | 2023 年 3 億次、2024 年 4 億次、2025 年 5 億次；2026 前幾個月已近三倍。3 兆美元的工程師薪資正產出約 9 兆美元的生產力。 | 無展出（論述） |
| [10:55] | Agent = 新運算模式 | 模型（大腦）+ harness（身體）+ 工具/技能 + runtime（工作坊）。現場展示 Claude Code、Codex 生成程式、GIF、CAD 檔。 | 無展出（概念） |
| [14:56] | CUDA-X 函式庫開放給 agent | 千個 CUDA-X 庫（cuLitho、cuOpt、cuDSS、AIQ、Aerial、Warp、Parabricks）將附帶「skills 說明書」讓 AI agent 直接調用。 | 無展出 |
| [24:01] | Vera Rubin 平台 | 不是單一晶片：Rubin GPU + Vera CPU + BlueField-4 + CX9 + 軟體棧 DOA + 全程加密的機密運算。全公司 4 萬名工程師投入。 | 南港 1 館 4F 鴻海／仁寶／神雲等 ODM 攤液冷機櫃 |
| [26:03] | NVIDIA DSX：AI 工廠藍圖 | DSX SIM（Omniverse 數位孿生）、DSX OS、DSX LPS（同樣電力預算多放 GPU）、45°C 熱水冷、DSX Flex（電網互動）。2030 年前 100 GW AI 工廠上線。 | 南港 1 館 1F J 區（維諦 J0818、光寶 J0617a 電力/冷卻方案） |
| [40:19] | Vera Rubin 全面量產 | 供應鏈規模為 Grace Blackwell 兩倍；組裝一櫃從 2 小時縮到 5 分鐘。 | 南港 2 館 4F R 區 BC Award 展示區（年度大獎） |
| [42:21] | 供應鏈與晶片細節 | 7 種新晶片、台積電 3nm、CoWoS-R/L 封裝、HBM4（美光/SK 海力士/三星）、單板 6 兆電晶體、1.3 百萬個零件、第三代 MGX 機架。 | 南港 1 館 4F 鴻海／仁寶攤 |
| [43:23] | 低延遲推論機櫃 LPX | 鴻海、廣達組裝；256 顆 LPU、40 PB/s SRAM 頻寬。NVL72 拚最高吞吐、LPX 拚最低延遲。 | 用官方 APP 查 |
| [46:26] | Vera Rubin 實機亮相 | 五大機櫃同台：NVL72、LPX、Vera CPU 機櫃（256 CPU 液冷）、BlueField 儲存、Spectrum-X 乙太網（全球首款 200G 共封裝光學 CPO）。 | 鴻海攤有 CPO 共封裝光學展示 |
| [51:35] | Vera CPU | 首款「為 agent 而生」的 CPU：88 個 Olympus 核心、10 指令/時脈、3.6 TB/s 互連、PCIe Gen 6、LPDDR5X 1.2 TB/s、agent sandbox 效能 1.8 倍於 x86。 | 用官方 APP 查 |
| [1:03:46] | Vera CPU 實測數據 | SQL 快 3 倍；紐約證交所即時串流處理快 6 倍。 | 無展出（數據） |
| [1:08:53] | NVIDIA 企業 Agent 工具組 | 四要素：開源模型 + harness（Open Shell 開源安全沙盒、Hermes）+ 工具 + runtime。Red Hat、Canonical、Microsoft 將採用。 | 無展出 |
| [1:10:55] | Cadence 晶片設計 super agent | Codex/Claude Code 協調 + ChipStack agents + Nemotron，RTL 驗證週期快 40 倍以上，從數週縮到數小時。 | 無展出 |
| [1:16:00] | Nemotron 3 Ultra | 開源模型：全球首個 SSM 狀態空間模型 + MoE 混合架構，快 5 倍、便宜 30%，模型/資料/訓練腳本全開放。Nemotron 4 開發中。 | 無展出 |
| [1:21:03] | RTX Spark（重新發明 PC） | 與 Microsoft 三年合作 + 聯發科共同打造 N1X 晶片：Blackwell GPU（6144 CUDA 核心、1 PFLOP AI）+ 20 核 Grace CPU、128 GB 統一記憶體、台積電 3nm、700 億電晶體。 | 南港 1 館 4F 聯發科攤（AI PC 生態系區） |
| [1:31:12] | 三款 Windows 新產品線 | 桌機（MSI 製）、筆電、工作站全線。DGX Station for Windows：768 GB 記憶體、20 PFLOPS，可跑一兆參數模型。 | 南港 1 館 4F AI PC 生態系區（ASUS / MSI 攤） |
| [1:39:23] | Cosmos 3 | Physical AI 開源基礎模型，mixture of transformers 架構：可理解（VLM）、生成物理正確影片、模擬、直接當機器人 policy。 | 世貿一館機器人區（夥伴展示） |
| [1:43:27] | Alpamayo 2 + Hyperion | 自駕開源推理模型；全球 80% 車廠採用 Hyperion 平台、串接 97% 移動服務。「全球第一台會推理的自駕車」。 | 南港 1 館 4F 智慧移動與無人載具區 |
| [1:47:30] | Isaac GR00T 參考人形機器人 | 開放平台 + 參考實體機器人：Sharpa 製造、每手 25 自由度、全身 31 自由度、6 呎 150 磅、搭載 Jetson Thor。鎖定大學與研究機構。 | 世貿一館機器人區（研華、所羅門等攤） |

## 依主題深入

### AI 基礎設施（Vera Rubin / 資料中心）

- **Vera Rubin 全面量產**［40:19］：黃仁勳宣布 Vera Rubin 進入 full production，供應鏈規模是 Grace Blackwell 的兩倍；機架組裝時間從 2 小時縮短到 5 分鐘。台灣 150 家供應鏈夥伴、數百個廠區投入。
- **不只是 GPU，是整套系統**［24:01–25:02］：Vera Rubin = Rubin GPU（NVLink72）+ Vera CPU + BlueField-4 DPU + CX9 SuperNIC + 軟體棧 + 機密運算（資料靜止、傳輸、使用中全程加密）。黃仁勳稱之為「公司史上最有野心的計畫」。
- **製造細節**［42:21–45:25］：7 種新晶片、台積電 3nm 製程、CoWoS-R/L 封裝、HBM4（美光、SK 海力士、三星供應）。運算板有 6 兆電晶體、超過 18,000 個零件；整櫃 130 萬個零件、5,000 安培液冷匯流排。Microsoft、Dell、CoreWeave 已架起工程機架。
- **Vera CPU**［51:35–1:07:52］：「過去的 CPU 為人類而造，這顆為 agent 而造」。88 個 Olympus 核心、單體式網狀互連（無 chiplet 跨界損耗）、3.6 TB/s 互連頻寬、業界首發 PCIe Gen 6 與 LPDDR5X（1.2 TB/s）。記憶體延遲比 x86 低 40%、agent sandbox 效能 1.8 倍。實測：SQL 快 3 倍、紐約證交所即時串流處理快 6 倍。
- **NVIDIA DSX：AI 工廠藍圖**［26:03–29:08］：從晶片、機架、網路、電力、冷卻到電網的全棧參考設計。DSX SIM 用 Omniverse 數位孿生先模擬再建廠；DSX LPS 解決資料中心過度配置電力（最多 40%）問題；45°C 熱水冷技術省水省電；DSX Flex 讓 AI 工廠跟電網雙向協作。預估 2030 年前全球將有 100 GW AI 工廠上線，每 GW 建置成本將達 800–1,000 億美元。
- **核心論點：算力即營收**［34:12–39:19］：每 token 都有利潤，因此「每瓦吞吐量 = 營收」。NVIDIA 系統的 token 成本是全球最低，「不是低 10%，是低數個數量級」。

### 個人 AI 運算（RTX Spark / DGX Station）

- **40 年來首次重新發明 PC**［1:20:03–1:24:04］：與 Microsoft 合作三年的成果，RTX Spark 是首發產品。N1X 晶片由 NVIDIA + 聯發科共同設計：Blackwell GPU（6,144 CUDA 核心、1 PFLOP AI 效能）+ 20 核 Grace CPU、NVLink 融合、128 GB 統一記憶體、台積電 3nm、700 億電晶體。
- **跑得動所有 CUDA 軟體**［1:26:06］：33 年來所有 NVIDIA 軟體（生醫、地震處理、天文物理、CUDA 全家桶）+ 所有 Windows 應用都完整支援。
- **本地 agent 應用展示**［1:27:07–1:29:11］：在 RTX Spark 上用 Open Shell 沙盒 + Hermes harness 連雲端 Claude Sonnet 設計房子 — agent 自己操作 Rhino 建模、匯出 Blender 渲染、用 Flux 2 模型轉照片級成像。
- **Adobe 重寫核心**［1:30:12］：Photoshop / Premiere 為 RTX Spark 重新設計，快 2 倍，並內建 MCP server 讓 agent 直接操作。
- **完整產品線**［1:31:12–1:34:18］：桌機、筆電、工作站全線。桌上型主機 24/7 跑 agent「沒有計量焦慮」（meter free）；DGX Station for Windows 有 768 GB 記憶體、20 PFLOPS、8 TB/s 頻寬，可在桌邊跑一兆參數模型。
- **十年後的 PC**［1:34:18–1:36:20］：黃仁勳預言家家都會有「AI 超級電腦」跑各種 agent，「它會更像 R2-D2 或 C3PO，而不像現在的 PC」。

### 機器人與 Physical AI（Jetson Thor / GR00T / Isaac）

- **Cosmos 3**［1:39:23–1:42:26］：Physical AI 的開源基礎模型，採 mixture of transformers 架構（自回歸 transformer 推理 + diffusion transformer 生成）。四種用法：VLM 看懂物理世界、世界模型生成物理正確影片、模擬器閉環訓練、直接當機器人 policy。「對 Physical AI 來說，算力就是資料」。
- **Alpamayo 2 自駕**［1:43:27–1:45:29］：開源自駕推理模型，搭配 Hyperion 平台（全球 80% 車廠採用）與 Halos 作業系統，串接 97% 移動服務。現場播放 Mercedes 實車展示——車輛邊開邊說明決策，「全球第一台會推理的自駕車」。
- **Isaac GR00T 參考人形機器人**［1:46:29–1:50:36］：完整人形機器人開發平台（模型 + 資料生成 + 模擬 + runtime），新增「參考機器人」：Sharpa 製造、每手 25 自由度、全身 31 自由度、6 呎高 150 磅、搭載 Jetson Thor。定位類比 PC 的「公板」，先給大學和研究機構。
- **資料是最大瓶頸**［1:38:23］：機器人需要第一人稱視角資料，但世界上影片多是第三人稱。NVIDIA 路徑：遙操作示範 → Omniverse 模擬 → 世界基礎模型自舉。

### 軟體與模型（Nemotron / Cosmos / Open Shell）

- **Nemotron 3 Ultra**［1:16:00–1:18:03］：開源模型，全球首個 SSM（狀態空間模型）+ MoE 混合架構，比同級開源模型快 5 倍、總成本低 30%。模型、訓練資料、訓練腳本全開放。Nemotron 4 已在開發。
- **NVIDIA 企業 Agent 工具組**［1:08:53–1:11:57］：企業建 agent 的四要素 — 模型（Nemotron）、harness（Open Shell / Hermes）、工具（CUDA-X + skills）、runtime。Open Shell 為開源安全沙盒，Red Hat、Canonical、Microsoft 都將採用。
- **Cadence 晶片設計 super agent**［1:11:57–1:15:00］：Codex / Claude Code 協調 ChipStack agents 做 RTL 驗證（模擬 + formal verification），週期快 40 倍以上。黃仁勳：「NVIDIA 有數千名晶片設計師，將僱用數十萬個 Cadence super agents。」
- **合作夥伴**：CrowdStrike、Palantir、SAP、ServiceNow 等都將用此工具組打造自己的 agent。
- **CUDA-X 庫對 agent 開放**［14:56–16:57］：上千個 CUDA-X 庫（cuLitho 微影、cuOpt 最佳化、Parabricks 基因組學等）將附上 agent 可讀的 skills 說明書。

### 台灣相關（供應鏈 / 台廠合作）

- **「回家了」**［3:29］：keynote 在台北舉行，全台 70 個分會場同步直播。黃仁勳帶父母到場。
- **GDP 預測**［5:51］：黃仁勳引述「台灣今年 GDP 成長將接近 10%」。
- **供應鏈規模**［44:24–45:25］：Vera Rubin 由台灣 150 家供應鏈夥伴、數百個廠區生產。「我們與台灣一起重新發明了 AI 時代的運算。」
- **台積電**［42:21］：Vera Rubin 七種晶片都用 3nm 製程，CoWoS-R/L 封裝、矽光子 COUPE 製程。
- **鴻海、廣達**［43:23–44:24］：負責組裝 LPX 低延遲推論機櫃；Vera CPU 機櫃。
- **聯發科**［1:24:04–1:26:06］：與 NVIDIA 共同設計 RTX Spark 的 N1X 晶片，黃仁勳稱「這是世界打造過最驚人的晶片」。
- **台灣 AI 雲**［33:12］：台灣 GMI 列入 NVIDIA 全球 AI 雲夥伴名單。
- **MSI**［1:32:16］：RTX Spark 桌上型主機由微星打造。

## 給觀展者的 action items（6/5 大眾日）

1. **南港 2 館 4F R 區入口「BC Award 展示區」**：Vera Rubin NVL72 拿下年度大獎（Best Choice of the Year + Golden + 永續三冠），一站看完得獎產品。
2. **南港 1 館 4F AI PC 生態系區**（鴻海 / 仁寶 / 聯發科 / ASUS / MSI）：keynote 主角實物大本營 — 鴻海液冷機架 + CPO 共封裝光學、仁寶液冷方案、聯發科可問 RTX Spark / N1X 晶片合作。
3. **世貿一館 AI 機器人區**（所羅門 A0811a、立端 A1227a、機器人聯展 A0618）：對應 keynote 的 Jetson Thor / GR00T / Cosmos 生態。建議問：「你們的 demo 是真的 AI 規劃，還是寫死的腳本？」
4. **南港 1 館 1F J 區（電源/散熱）**（維諦 J0818、光寶 J0617a、雙鴻 J0806）：呼應 DSX「AI 工廠」論述 — 想理解「算力即營收」就去看電力與液冷怎麼解。建議問：「100kW 以下小型機房，瓶頸先卡電還是熱？」
5. **南港 1 館 4F 智慧移動與無人載具區**：Alpamayo 2 拿下 BC Award 車用技術獎，可看自駕生態。
6. 找不到攤位時用官方 APP（computextaipei.com.tw）查最新位置。

## 金句（合理使用，每段 ≤2 句原文引用）

1. **[9:53]**「Useful AI has arrived. AI is now a profit generator. AI is now a GDP generator.」— 整場 keynote 的核心宣言。
2. **[36:16]**「Compute is revenues. Performance per watt is your revenues.」— AI 工廠時代的商業邏輯。
3. **[8:53]**「People talk about AI reducing jobs. Complete nonsense.」— 黃仁勳對「AI 滅工作」的回擊。
4. **[53:37]**「All the CPUs of the past we built for humans. This CPU is built for agents.」— Vera CPU 的定位。
5. **[1:35:19]**「It becomes more like R2-D2 to you... than it feels like a PC to you.」— 對未來個人電腦的想像。

---

> 整理方式：本文依據 YouTube 自動字幕逐字稿整理，專有名詞拼寫已修正（如 Neotron → Nemotron、Alpamayo、Vera Rubin）。時間戳為逐字稿標記，可能與影片實際時間有 ±30 秒誤差。
