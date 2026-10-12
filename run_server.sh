#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

preview_port="${PREVIEW_PORT:-8000}"
exec python3 scripts/preview.py --port "$preview_port"
