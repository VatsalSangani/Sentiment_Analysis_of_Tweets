# ─────────────────────────────────────────────────────────────
# Dockerfile – Twitter-Sentiment (UI + API same container)
# ─────────────────────────────────────────────────────────────
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application and model files
COPY app ./app

# Expose Streamlit and FastAPI ports
EXPOSE 8001
EXPOSE 8502

# Start both servers
CMD ["bash", "-c", "\
  uvicorn app.main:app --host 0.0.0.0 --port 8001 & \
  streamlit run app/app.py --server.port 8502 --server.address 0.0.0.0 & \
  wait"]

