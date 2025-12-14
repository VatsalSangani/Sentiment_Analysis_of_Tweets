#!/bin/bash
set -e

echo "Starting FastAPI on port 8001..."
/usr/local/bin/uvicorn app.main:app --host 0.0.0.0 --port 8001 &

echo "Starting Streamlit on port 8502..."
/usr/local/bin/streamlit run app/app.py --server.port 8502 --server.address 0.0.0.0 &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
