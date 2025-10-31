#!/usr/bin/env bash
# run_report_pipeline.sh
# Usage: ./run_report_pipeline.sh <target-ip> <job-name-optional>
set -e
TGT="$1"
JOB="${2:-report_$(date +%Y%m%d%H%M%S)}"
WORKDIR="$HOME/cyber-security/day4"
OUTDIR="$HOME/cyber-security/reports/$JOB"
mkdir -p "$OUTDIR"
cd "$WORKDIR"

echo "[*] Running nmap (this may take a few minutes)..."
nmap -sS -sV -O --script=banner,vuln -p- -T4 -oX "$OUTDIR/${JOB}.xml" "$TGT"

echo "[*] Converting XML -> JSON..."
python3 xmljson.py "$OUTDIR/${JOB}.xml"
mv "${JOB}.json" "$OUTDIR/${JOB}.json" 2>/dev/null || mv scanfull.json "$OUTDIR/${JOB}.json" 2>/dev/null || true

echo "[*] Converting JSON -> HTML..."
python3 jsonhtml.py "$OUTDIR/${JOB}.json"
mv "${JOB}.html" "$OUTDIR/${JOB}.html" 2>/dev/null || mv scanfull.html "$OUTDIR/${JOB}.html" 2>/dev/null || true

echo "[*] Generating summary markdown..."
python3 generate_summary_from_json.py "$OUTDIR/${JOB}.json" "$OUTDIR/${JOB}_summary.md"

echo "[*] Converting HTML -> PDF..."
# try wkhtmltopdf; fallback to print instructions if not installed
if command -v wkhtmltopdf >/dev/null 2>&1; then
  wkhtmltopdf "$OUTDIR/${JOB}.html" "$OUTDIR/${JOB}.pdf"
  echo "[*] PDF saved to $OUTDIR/${JOB}.pdf"
else
  echo "WARNING: wkhtmltopdf not installed. Open the HTML and print to PDF manually: $OUTDIR/${JOB}.html"
fi

echo "[*] All done. Files in: $OUTDIR"
