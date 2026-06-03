#!/bin/bash
# 批量抓 COMPUTEX 2026 影片字幕（YouTube auto-sub，零轉錄成本）
# 用法: ./fetch-subs.sh <影片清單檔> [輸出目錄]
# 清單格式: 標題|||時長|||video_id（yt-dlp flat-playlist 輸出）
# 增量安全：已存在的 .vtt 跳過，可重複跑

set -u
LIST="${1:?需要影片清單檔}"
OUTDIR="${2:-transcripts/raw}"
mkdir -p "$OUTDIR"

total=0; ok=0; skip=0; fail=0; failed_ids=""

while IFS= read -r line; do
  [ -z "$line" ] && continue
  id=$(echo "$line" | awk -F'\\|\\|\\|' '{print $3}')
  dur=$(echo "$line" | awk -F'\\|\\|\\|' '{print $2}')
  [ -z "$id" ] && continue
  # NA 時長 = premiere/live 未結束，跳過
  if [ "$dur" = "NA" ]; then skip=$((skip+1)); continue; fi
  total=$((total+1))
  # 增量：已抓過就跳過
  if ls "$OUTDIR/${id}".*.vtt >/dev/null 2>&1; then ok=$((ok+1)); continue; fi

  if timeout 60 yt-dlp --write-auto-sub --sub-lang "en,zh-TW,zh" --skip-download \
       --sub-format vtt -o "$OUTDIR/%(id)s" "https://www.youtube.com/watch?v=$id" >/dev/null 2>&1 \
     && ls "$OUTDIR/${id}".*.vtt >/dev/null 2>&1; then
    ok=$((ok+1))
  else
    fail=$((fail+1)); failed_ids="$failed_ids $id"
  fi
  sleep 1.5  # YouTube rate limit 禮貌間隔
done < "$LIST"

echo "=== fetch-subs 完成 ==="
echo "可處理: $total / 成功: $ok / 跳過(NA): $skip / 失敗: $fail"
[ -n "$failed_ids" ] && echo "失敗 ID:$failed_ids"
