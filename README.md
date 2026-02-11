# 🧠 Bug Summary AI Tool

An AI-powered utility that automatically analyzes bug reports, error logs, or Jira ticket descriptions and generates clear, concise summaries along with potential root causes and suggested fixes.

This tool is designed to improve developer productivity by reducing the time spent understanding complex bug reports and log files. It leverages OpenAI's GPT-4o to provide high-quality summaries and actionable insights instantly.

## 🚀 Features

- **📄 Automatic Bug Summaries**: Converts long or unclear bug descriptions into short, clear summaries.
- **🛠 Root Cause Analysis**: AI suggests the most probable root cause based on error logs.
- **🧪 Fix Recommendations**: Provides logical solutions and debugging steps.
- **� Dual Interface**:
  - **CLI**: Fast terminal-based analysis.
  - **Dashboard**: Premium web interface built with Streamlit.

## 📦 Tech Stack

- **Python 3.10+**
- **OpenAI API** (GPT-4o)
- **FastAPI / CLI** (Click, Rich)
- **Streamlit** (Web UI)

## 🔧 Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone <repo-url>
   cd AI-Project
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Copy `.env.example` to `.env` and add your OpenAI API Key:
   ```bash
   OPENAI_API_KEY=your_key_here
   ```

## 🎮 How to Use

### 📟 Command Line Interface (CLI)

Analyze a file directly from your terminal:

```bash
python app.py analyze examples/sample_bug.txt
```

### 🌐 Web Dashboard

Launch the interactive dashboard:

```bash
streamlit run dashboard.py
```

## 📝 Example Output

**Input**: `NullReferenceException in UserService.cs at line 52...`

**AI Output**:

- **Summary**: The system crashes due to a null object reference in UserService.
- **Root Cause**: Missing null validation on user profile data.
- **Fix**: Add null checks before accessing user attributes.

## 🎯 Purpose of This Project

- Independent development using AI
- High token usage & effective prompt design
- Practical improvement for engineering teams
- Fast delivery using AI-assisted coding workflows

## 📚 Future Enhancements

- Integrate with Jira/GitHub API
- Generate fix PR templates
- Export reports to PDF
