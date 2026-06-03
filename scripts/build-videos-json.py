#!/usr/bin/env python3
"""從影片清單 + 字幕/摘要狀態生成 data/videos.json。

用法: python3 scripts/build-videos-json.py <影片清單檔>
清單格式: 標題|||時長|||video_id
"""
import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).parent.parent
RAW = REPO / "transcripts" / "raw"
CLEAN = REPO / "transcripts" / "clean"
SUMMARIES = REPO / "transcripts" / "summaries"


def categorize(title: str) -> str:
    if "COMPUTOUR" in title:
        return "computour"
    if "Pre-show Forum" in title:
        return "forum"
    if title.startswith("【COMPUTEX 2026】"):
        return "official"
    if title.startswith("【Technology Unboxing】"):
        return "unboxing"
    if title.startswith("【Featured Product】"):
        return "featured-product"
    if "BC Award" in title or "Best Choice Award" in title:
        return "bc-award"
    if "keynote" in title.lower():
        return "keynote"
    return "other"


# 分類 → 摘要合輯檔對照（worker 產出按分類合併，非每支一檔）
CATEGORY_SUMMARY_FILE = {
    "computour": "computour.md",
    "bc-award": "bc-award-videos.md",
    "unboxing": "unboxing.md",
    "featured-product": "featured-products.md",
    "forum": "forum-preshow.md",
}


def main():
    list_file = Path(sys.argv[1])
    videos = []

    # 官方頻道影片（從清單）
    for line in list_file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        parts = line.split("|||")
        if len(parts) != 3:
            continue
        title, duration, vid = parts[0].strip(), parts[1].strip(), parts[2].strip()
        cat = categorize(title)
        has_sub = bool(list(RAW.glob(f"{vid}.*.vtt")))
        has_clean = (CLEAN / f"{vid}.txt").exists()
        # 摘要在分類合輯檔內：合輯檔存在且該影片有逐字稿 → 視為已摘要
        summary_file = CATEGORY_SUMMARY_FILE.get(cat)
        has_summary = bool(summary_file) and (SUMMARIES / summary_file).exists() and has_clean
        videos.append({
            "id": vid,
            "title": title,
            "category": cat,
            "duration": duration if duration != "NA" else None,
            "url": f"https://www.youtube.com/watch?v={vid}",
            "channel": "COMPUTEX official",
            "transcript_status": "clean" if has_clean else ("raw" if has_sub else "pending"),
            "summary_status": "done" if has_summary else "pending",
            "summary_file": f"transcripts/summaries/{summary_file}" if has_summary else None,
        })

    # Keynotes（手動清單，官方頻道之外）
    keynotes = [
        {
            "id": "wSp6AiNIrsY",
            "title": "NVIDIA GTC Taipei 2026 Keynote | Full Replay (Jensen Huang)",
            "category": "keynote",
            "duration": "1:57:53",
            "url": "https://www.youtube.com/watch?v=wSp6AiNIrsY",
            "channel": "NVIDIA official",
        },
        {
            "id": "1h_zY377urU",
            "title": "Intel Computex Keynote 2026 (Lip-Bu Tan)",
            "category": "keynote",
            "duration": "1:06:21",
            "url": "https://www.youtube.com/watch?v=1h_zY377urU",
            "channel": "Intel official",
        },
    ]
    for k in keynotes:
        slug = "keynote-nvidia" if "NVIDIA" in k["title"] else "keynote-intel"
        k["transcript_status"] = "clean" if (CLEAN / f"{slug}.txt").exists() else "pending"
        has_summary = (SUMMARIES / f"{slug}.md").exists()
        k["summary_status"] = "done" if has_summary else "pending"
        k["summary_file"] = f"transcripts/summaries/{slug}.md" if has_summary else None
        videos.append(k)

    out = {
        "meta": {
            "title": "COMPUTEX 2026 Video Index (official channel + keynotes)",
            "title_zh": "COMPUTEX 2026 影片索引（官方頻道 + 各家 keynote）",
            "generated_at": str(date.today()),
            "source": "yt-dlp probe of youtube.com/@COMPUTEXTAIPEIshow + vendor official channels",
            "note_zh": "transcript_status: clean=已有逐字稿(本地) / raw=已抓字幕未清洗 / pending=尚無。summary_status: done=摘要已發布於 transcripts/summaries/",
            "copyright_note_zh": "影片內容著作權屬各原始頻道；本索引僅提供連結與非官方摘要（合理使用），完整逐字稿不公開發布。",
        },
        "stats": {
            "total": len(videos),
            "by_category": {},
        },
        "videos": videos,
    }
    for v in videos:
        cat = v["category"]
        out["stats"]["by_category"][cat] = out["stats"]["by_category"].get(cat, 0) + 1

    dst = REPO / "data" / "videos.json"
    dst.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"-> {dst}: {len(videos)} videos")
    print(json.dumps(out["stats"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
