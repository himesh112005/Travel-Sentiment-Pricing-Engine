# 🌍 AI-Powered Travel Sentiment & Pricing Engine

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

A full-stack AI and Data Engineering project that helps users find the best travel destinations by blending real-time flight/hotel costs with NLP-based sentiment analysis of travel reviews.

## 🚀 Features
- **Data Engineering:** Automated generation and SQL-blending of pricing and review data.
- **AI Brain:** Utilizes NLTK VADER for rapid, lightweight sentiment analysis of thousands of reviews.
- **Interactive UI:** A Streamlit dashboard with Plotly visualisations to find the "High Sentiment, Low Cost" sweet spot.
- **MLOps Ready:** Fully containerised with Docker for seamless deployment.

## 🧠 Architecture Flow
`Raw CSVs` ➡️ `AI Sentiment Pipeline` ➡️ `SQLite Database` ➡️ `Streamlit Dashboard`

## 🛠️ How to Run Locally

### Option 1: Standard Python
```bash
pip install -r requirements.txt
python src/data_gen.py
python src/sentiment.py
python src/sql_blend.py
streamlit run app/app.py

<img width="1359" height="644" alt="image" src="https://github.com/user-attachments/assets/ab07f802-1aa4-4586-a5af-1885603cda4c" />
