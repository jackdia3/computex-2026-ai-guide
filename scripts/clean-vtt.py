#!/usr/bin/env python3
"""清洗 YouTube auto-sub VTT → 乾淨逐字稿（保留分鐘級時間戳）。

用法: python3 clean-vtt.py <input.vtt> [output.txt]
      python3 clean-vtt.py --dir <vtt目錄> <輸出目錄>   # 批量
"""
import re
import sys
from pathlib import Path


def clean_vtt(vtt_path: Path) -> str:
    """VTT → 純文字逐字稿，每分鐘插一個 [MM:SS] 時間戳。"""
    text = vtt_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()

    out_segments = []  # (秒數, 文字)
    cur_time = 0.0
    seen = set()

    ts_re = re.compile(r"^(\d{2}):(\d{2}):(\d{2})\.(\d{3}) --> ")
    tag_re = re.compile(r"<[^>]+>")

    for line in lines:
        m = ts_re.match(line)
        if m:
            h, mnt, s = int(m.group(1)), int(m.group(2)), int(m.group(3))
            cur_time = h * 3600 + mnt * 60 + s
            continue
        if (
            not line.strip()
            or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE"))
            or "align:" in line
            or "-->" in line
        ):
            continue
        # 去 inline word-level timestamp tag
        clean = tag_re.sub("", line).strip()
        if not clean or clean in seen:
            continue
        seen.add(clean)
        out_segments.append((cur_time, clean))

    # 組裝：每 60 秒插一個時間戳
    result = []
    last_marker = -60
    for t, txt in out_segments:
        if t - last_marker >= 60:
            mm, ss = divmod(int(t), 60)
            hh, mm = divmod(mm, 60)
            stamp = f"[{hh}:{mm:02d}:{ss:02d}]" if hh else f"[{mm}:{ss:02d}]"
            result.append(f"\n{stamp}")
            last_marker = t
        result.append(txt)
    return " ".join(result).strip()


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    if args[0] == "--dir":
        src_dir, dst_dir = Path(args[1]), Path(args[2])
        dst_dir.mkdir(parents=True, exist_ok=True)
        count = 0
        for vtt in sorted(src_dir.glob("*.vtt")):
            # 檔名格式 <video_id>.<lang>.vtt → 輸出 <video_id>.txt
            vid = vtt.name.split(".")[0]
            out = dst_dir / f"{vid}.txt"
            cleaned = clean_vtt(vtt)
            if cleaned:
                out.write_text(cleaned, encoding="utf-8")
                count += 1
        print(f"cleaned {count} transcripts -> {dst_dir}")
    else:
        vtt_path = Path(args[0])
        cleaned = clean_vtt(vtt_path)
        if len(args) > 1:
            Path(args[1]).write_text(cleaned, encoding="utf-8")
            print(f"-> {args[1]}")
        else:
            print(cleaned)


if __name__ == "__main__":
    main()
