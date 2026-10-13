#!/bin/bash

LOG_FILE="${1:-logs/ecommerce-app.log}"

if [ ! -f "$LOG_FILE" ]; then
    echo "ERROR: Log file not found: $LOG_FILE"
    exit 1
fi

echo "===== E-Commerce Log Analysis ====="
echo "Log file: $LOG_FILE"
echo "Total log lines: $(wc -l < "$LOG_FILE")"
echo "Successful HTTP requests (200): $(grep -Ec '" 200 ' "$LOG_FILE" || true)"
echo "Client/Server errors (4xx/5xx): $(grep -Ec '" [45][0-9][0-9] ' "$LOG_FILE" || true)"
echo "==================================="
