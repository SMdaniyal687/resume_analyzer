# 🚀 Smart Resume Analyzer & Job Recommender

A premium, AI-powered web application that analyzes PDF resumes, extracts skills, provides a brutally honest "roast," prepares you for interviews, and suggests level-appropriate job matches.

![UI Design](https://raw.githubusercontent.com/SMdaniyal687/resume_analyzer/main/static/screenshot.png) *(Note: Add a real screenshot later)*

## ✨ Key Features

- **🔥 Resume Roaster:** Get brutally honest, constructive feedback on your resume's weaknesses and strengths.
- **💼 Smart Job Matching:** Real-time job listings from Adzuna, Remotive, and RemoteOK, scored and ranked specifically for your experience level.
- **🎯 Interview Prep Coach:** Generates behavioral and technical questions tailored to your background, with an interactive answer evaluator.
- **📊 Skill Extraction:** Automatically identifies technical and soft skills using NLP.
- **✍️ AI Rebuilder:** Rewrites weak bullet points and generates a tailored cover letter.
- **🎨 Premium UI:** Modern, animated "Aurora" dark theme with glassmorphic elements.

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** Vanilla HTML/CSS/JS (with marked.js)
- **AI Engine:** Groq (Llama 3.3 70B)
- **NLP/Parsing:** spaCy, pdfplumber
- **APIs:** Adzuna, Remotive, RemoteOK

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9+
- A Groq API Key (Get it at [console.groq.com](https://console.groq.com))

### 2. Installation
```bash
git clone https://github.com/SMdaniyal687/resume_analyzer.git
cd resume_analyzer
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here

# Optional (for better job search results)
ADZUNA_APP_ID=your_id
ADZUNA_APP_KEY=your_key
```

### 4. Run the App
```bash
python -m uvicorn main:app --reload
```
Visit `http://localhost:8000` in your browser.

## 📁 Project Structure
- `main.py`: FastAPI entry point and routes.
- `utils/`: Core logic modules (LLM client, parsing, fetching, etc.).
- `static/`: Frontend assets (HTML, CSS, JS).
- `requirements.txt`: Project dependencies.

## 📝 License
This project is for educational purposes. Feel free to use and modify it!
