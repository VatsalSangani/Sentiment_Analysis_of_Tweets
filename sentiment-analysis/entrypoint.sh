#!/bin/bash
set -e

# 1. Start FastAPI (Backend) on PORT 8001 (Matches your app.py!)
# We use --port 8001 so Streamlit can find it.
echo "Starting FastAPI on port 8001..."
uvicorn app.main:app --host 0.0.0.0 --port 8001 > /var/log/fastapi.log 2>&1 &

# 2. Start Streamlit (Frontend)
# We use the flags to fix the browser security errors
echo "Starting Streamlit..."
exec streamlit run app/app.py \
    --server.port=8502 \
    --server.address=0.0.0.0 \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false
