#!/bin/bash
set -e

# 1. Start FastAPI (Backend)
# We log to a file for debugging, just like you did in Credit Risk
echo "Starting FastAPI..."
uvicorn app.main:app --host 0.0.0.0 --port 8001 > /var/log/fastapi.log 2>&1 &

# 2. Start Streamlit (Frontend)
# We ADD the flags to stop the "Failed to fetch" errors.
echo "Starting Streamlit..."
exec streamlit run app/app.py \
    --server.port=8502 \
    --server.address=0.0.0.0 \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false
