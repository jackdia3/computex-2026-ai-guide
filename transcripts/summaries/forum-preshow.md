# COMPUTEX 2026 Pre-show Forum「The AI Era」重點摘要

> 原片：https://www.youtube.com/watch?v=XFGPfkQXuwY（2:09:40，COMPUTEX TAIPEI）
> 摘要驗證日：2026-06-03 / 非官方整理（合理使用），完整內容請看原片

## 一句話總結

這場展前論壇把「AI together」具體化為系統工程：agentic devices、AI infrastructure、enterprise AI governance、smart retail 與 healthcare AI 都不再只談模型，而是談雲端、edge、資料、實體場域、治理與產業生態如何一起落地。

## 重點時間軸

| 時間戳 | 主題/發表 | 重點 |
|---|---|---|
| [0:00] | 主持人開場 | COMPUTEX 2026 主題為 AI together，展覽 6/2-6/5，聚焦 AI computing、robotics and smart mobility、next-gen communications、sustainable innovation。 |
| [4:04] | TCA Chairman Jun Shen Chen 開幕 | AI 從 compute competition 進入 system value，重點是 system integration、real-world deployment、ecosystem collaboration。 |
| [5:04] | 六場議題介紹 | 開場列出 Google Cloud、MediaTek、McKinsey、鴻海研究院、E Ink、Acer Medical；但本逐字稿正文未收錄 Google Cloud 主講段落。 |
| [10:33] | MediaTek Joe Chen：AI everywhere | Agentic AI 將改變產品型態與 UX，從 smartphone 走向 agentic AI devices。 |
| [17:45] | MediaTek：agentic UX 五特徵 | Proactive/realtime、personalized memory、interactive collaboration、continuous learning、privacy。 |
| [21:27] | MediaTek：生活情境 | AI glasses + phone 的旅遊推薦、車內/手機 agent 協作提醒洗衣、work agent 協助 email 決策。 |
| [27:36] | MediaTek：四層架構 | Edge layer、system layer、application layer、infrastructure layer；強調 compute/power、agentic OS、developer ecosystem、cloud interconnect。 |
| [37:44] | McKinsey Ryan Fletcher：AI has physicality | AI 的擴張由 power、cooling、networking、compute 四個實體系統共同限制。 |
| [40:48] | McKinsey：power crunch | 北美 AI data center power demand 2025 已佔 4%，2030 估 14%，但增量供給只有部分已規劃。 |
| [43:51] | McKinsey：cooling | Data center cooling 24/7 且高度集中，從 air cooling 到 liquid / direct-to-chip cooling 的規模化服務能力是關鍵。 |
| [46:56] | McKinsey：network wall | Compute FLOPS 20 年大幅成長，但 interconnect bandwidth 成長落差導致 GPU idle 與價值流失。 |
| [50:58] | McKinsey：better tokens / cheaper tokens | Frontier systems 像 Formula 1 garage，效率型 inference 像製造工廠，兩者需要不同 AI factories。 |
| [57:02] | Honghai Research Institute Wayne Lee：enterprise AI security | AI 不是 perfect by default；agentic AI 會自行採取行動，需要比例原則、邊界與責任分層。 |
| [1:06:14] | Wayne Lee：shadow AI / shadow agents | 技術採用會走阻力最小路徑，員工自帶 AI 工具後，企業將面對非授權 agent 的管理問題。 |
| [1:08:15] | Wayne Lee：agents as non-human employees | Agent 需要像員工一樣 onboarding、authentication、authorization、clearance。 |
| [1:18:27] | Wayne Lee：governance layers | 責任不應全丟給 IT，需 legal、organization、technical 三層共同承擔。 |
| [1:22:28] | E Ink JM Hong：AI-powered retail | 實體店仍重要，AI 與 e-paper / ESL 讓價格、促銷、庫存與媒體更動態。 |
| [1:25:31] | E Ink：Simple Mart ESL | 與 Simple Mart 合作 800 店、300 萬個電子貨架標籤，形成 retail data infrastructure。 |
| [1:31:37] | E Ink：sensor + targeted media | 以壓力感測偵測商品被拿起，不收集個資也能推播商品資訊與促銷。 |
| [1:36:39] | E Ink：retail 3.0 | 從數位價格標籤進入 retail media，再接到 backend logistics，例如草莓庫存跨店調度。 |
| [1:45:48] | Acer Medical Ellen Lin：AI in healthcare | 從 predictive AI、generative agents、AIoT 到 AI-designed cancer vaccine，說明醫療 AI 的落地與限制。 |
| [1:48:50] | Acer Medical：predictive AI | 胸腔 X 光推估骨密度，眼底影像篩檢糖尿病視網膜病變、AMD、青光眼，降低醫療可近性落差。 |
| [1:55:00] | Acer Medical：health-check agents | 專科 agent 讀健檢報告、彼此討論後產生摘要，未來可與病人的個人 agent 溝通後續檢查。 |
| [1:58:02] | Acer Medical：local medical knowledge | 醫療 LLM 不能只靠網路語料，需台灣臨床指引、健康署文件與在地醫療用語。 |
| [2:02:07] | Acer Medical：AI gait / AIoT | AI gait 量化神經與步態變化，結合 wearable/chatbot 支援中風後管理。 |
| [2:06:11] | Acer Medical：cancer vaccine | 以 AI 設計癌症 neoantigen 樹突細胞療法，分享 compassionate use 個案。 |

## 依主題深入

### 1. 開場主軸：AI 從展示技術走向 system value

TCA Chairman Jun Shen Chen 在 [4:04]-[8:04] 說，AI 下一階段不再只看 models 或 compute power，而是 system integration、real-world deployment、ecosystem collaboration。這也定義了整場論壇：雲端、on-premise、edge、平台供應商與垂直應用必須一起成為可部署系統。

### 2. MediaTek：agentic AI devices 會改寫 UX 與商業生態

Joe Chen 在 [10:33]-[35:41] 把 agentic AI 從抽象概念拉到手機、眼鏡、車與工作場景。agentic UX 的五個特徵是主動即時、個人化記憶、多裝置互動協作、持續學習、隱私。MediaTek 的技術框架則分為 edge、system、application、infrastructure 四層：端側要處理 compute/power，系統層需要 agentic OS，應用層需要 developer toolkit 與 agentic ecosystem，雲端層則面對 per-watt performance、先進封裝與互連。

### 3. McKinsey：AI 的速度由 physical infrastructure 決定

Ryan Fletcher 在 [37:44]-[56:00] 強調 AI 有實體重量。Power、cooling、networking、compute 彼此耦合，任何一項都會拖慢整套系統。power 是 calendar，cooling 決定 adoption curve，networking 影響 utilization，compute 則是 system design decision。特別是 better tokens 與 cheaper tokens 的需求不同，未來至少需要兩種不同 AI factory。

### 4. 鴻海研究院：agentic AI 需要治理，不只是資安工具

Wayne Lee 在 [57:02]-[1:20:27] 從 AI imperfect by design 談到 prompt injection、data poisoning、shadow AI、shadow agents 與 agent authorization。他提醒 agentic AI 會自行採取行動，可能為完成目標採用不合比例的手段，因此需要可逆/不可逆、內部/外部、人類介入程度等分級；責任也必須分散在 legal、organization、technical 三層，而不只是 IT 部門。

### 5. E Ink：智慧零售的入口是電子貨架與可互動紙張

JM Hong 在 [1:22:28]-[1:44:48] 以 Simple Mart 800 店、300 萬個 ESL 為例，說明電子貨架標籤一旦部署，就不只是替代紙本價格牌，而是 retail data infrastructure。AI 可依店別與庫存做動態折扣、減少食物浪費，也能結合 pressure sensor、e-paper signage、店內導航與 retail media network，讓實體零售同時做促銷、資訊展示與物流回饋。

### 6. Acer Medical：醫療 AI 必須建立在可信知識與在地場景

Ellen Lin 在 [1:45:48]-[2:07:14] 把醫療 AI 分成 predictive AI、generative AI agents、AIoT 與 AI-designed cancer vaccine。predictive AI 已用於骨密度、糖尿病視網膜病變、AMD、青光眼篩檢，目標是縮小城鄉與跨島醫療差距；generative AI 則可用在健檢報告與 AI scribe，但醫療場景不能直接依賴一般 LLM，必須以在地臨床指引、醫療術語與族群差異建立知識基礎。

## 給觀展者的重點

6/5 觀展者可以把這場論壇當作看展框架：不要只看單一 AI 晶片或模型 demo，而要追問它屬於哪一層系統。看 AI device 時，注意是否真的能在 edge 與 cloud 間協作；看資料中心與伺服器時，除了 GPU 也要看 power、cooling、networking、rack design 與 utilization；看零售與醫療應用時，重點是資料如何進系統、如何保護隱私、如何把 AI 輸出接到實際作業流程。E Ink 現場提到可在 COMPUTEX booth 一站看材料、IC、面板與系統方案；Acer Medical 的案例則適合用來觀察 AI 是否真正降低醫療人力與可近性瓶頸。

## 金句（每段 ≤2 句原文引用 + 時間戳）

> "AI is moving from the era of compute competition into the era of system value." [4:04]

> "AI has physicality. It has a real address." [37:44]

> "Power is really becoming the calendar of AI for us today." [43:51]

> "Coming up with the idea and the innovation is 10% of the problem." [46:56]

> "Agents are nonhuman employee." [1:08:15]

> "You need to treat agents as human beings not a program because when it comes to program everything is predefined but AI isn't." [1:20:27]

> "Acer medical's mission is to make AI serve the core need of humans which is healthcare." [2:04:09]
