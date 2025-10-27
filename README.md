# personal-finance-ai-agent


# 💰 Personal Finance AI Agent (Gemini 2.5 Flash)

An AI-powered personal finance assistant that automates expense categorization, generates insights, and visualizes spending trends.

## 🚀 Features
- 📊 Upload and analyze CSV bank statements  
- 🧹 Automatic cleaning & normalization  
- 🧠 Gemini 2.5 Flash–powered AI insights  
- 💸 Category-wise and monthly expense charts  
- 📥 Export processed transactions  

## 🧩 Tech Stack
- Python 3.13
- Streamlit
- Pandas
- Google Gemini 2.5 Flash
- Regex for rule-based categorization

## ⚙️ Setup
```bash
git clone https://github.com/<your-username>/personal-finance-ai-agent.git
cd personal-finance-ai-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your GEMINI_API_KEY here
streamlit run src/ui/dashboard.py
