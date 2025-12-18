# 🧠 Sentiment Analysis of Tweets

This project is an end-to-end application that analyzes the sentiment of tweets using a fine-tuned DistilBERT transformer model. It includes a FastAPI backend for inference and a Streamlit frontend for user interaction, deployed seamlessly via a CI/CD pipeline on an AWS EC2 instance..

---

## 🚀 Live App

👉 [Click to Open the Deployed App](http://18.171.75.241:8502)

---

## 🛠️ Tech Stack

- **NLP Model**: DistilBERT (fine-tuned for sentiment classification)
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Deployment**: Docker, GitHub Actions, AWS EC2
- **Model Hosting**: Hugging Face Hub

---

## ✨ Features

- Analyze sentiment (`positive`, `neutral`, `negative`) of any tweet or sentence.
- Live confidence score using a fine-tuned transformer.
- Real-time interactive frontend using Streamlit.
- Auto-deploys to EC2 via GitHub Actions on every `main` branch push.

---

## 📊 Model

- **Base**: `distilbert-base-uncased`
- **Trained On**: Custom Twitter sentiment dataset.
- **Hosted At**: [Hugging Face Hub](https://huggingface.co/brendvat/distilbert-ft)

---

## ⚙️ CI/CD Pipeline – EC2 Auto Deployment

This project uses **GitHub Actions** to automatically build and deploy the app to an AWS EC2 instance whenever changes are pushed to the `main` branch.

### 🔁 How It Works:

1. **Code pushed to GitHub** → triggers GitHub Actions
2. **SSH into EC2** via `EC2_SSH_KEY` (GitHub secret)
3. **Pull latest code**, stop old container, remove old image
4. **Build new Docker image** and run fresh container on EC2

### ✅ Workflow File: `.github/workflows/deploy.yml`

```yaml
on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: ⬇️ Checkout code
      uses: actions/checkout@v3

    - name: 🔐 Set up SSH
      uses: webfactory/ssh-agent@v0.8.0
      with:
        ssh-private-key: ${{ secrets.EC2_SSH_KEY }}

    - name: 🚀 Deploy Sentiment App to EC2
      run: |
        ssh -tt -o StrictHostKeyChecking=no deploy@<YOUR_EC2_PUBLIC_IP> << 'EOF'
          set -e
          cd ~/Sentiment_Analysis_of_Tweets/sentiment-analysis
          git pull origin main
          docker stop sentiment-app || true
          docker rm sentiment-app || true
          docker rmi -f sentiment-ui:latest || true
          docker build --no-cache -t sentiment-ui:latest .
          docker run -d -p 8001:8001 -p 8502:8502 --name sentiment-app sentiment-ui:latest
          exit 0
        EOF
```
---

## 🐳 Docker Commands (For Local Testing)
```
# Build Docker Image
docker build -t sentiment-ui:latest .

# Run Container
docker run -d -p 8001:8001 -p 8502:8502 --name sentiment-app sentiment-ui:latest
```


## 📥 Installation (Run Locally)
```
git clone https://github.com/VatsalSangani/Sentiment_Analysis_of_Tweets.git
cd Sentiment_Analysis_of_Tweets/sentiment-analysis
pip install -r requirements.txt
streamlit run app/app.py
```
