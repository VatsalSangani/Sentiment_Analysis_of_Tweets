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

# Copy the entrypoint script and make it executable
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Expose Streamlit and FastAPI ports
EXPOSE 8001
EXPOSE 8502

# Use the script as the entry point
ENTRYPOINT ["./entrypoint.sh"]
