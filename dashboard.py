import streamlit as st
from app import BugAnalyzer
from dotenv import load_dotenv
import os

# Page Configuration
st.set_page_config(
    page_title="Bug Summary AI Tool",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextArea textarea {
        background-color: #161b22;
        color: #e6edf3;
        border: 1px solid #30363d;
        border-radius: 8px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #238636, #2ea043);
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        opacity: 0.8;
        box-shadow: 0 0 15px rgba(46, 160, 67, 0.4);
    }
    .report-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
    }
    h1, h2, h3 {
        color: #58a6ff !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.title("🧠 Bug Summary AI Tool")
    st.markdown("---")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📥 Input Bug Report / Logs")
        bug_input = st.text_area(
            "Paste your error logs or Jira ticket description here...",
            height=400,
            placeholder="e.g., NullReferenceException in UserService.cs:line 52..."
        )
        
        analyze_button = st.button("Analyze with AI")

    with col2:
        st.subheader("💡 Analysis Results")
        if analyze_button:
            if not bug_input:
                st.warning("Please provide a bug report before analyzing.")
            else:
                try:
                    with st.spinner("AI is crunching the logs..."):
                        analyzer = BugAnalyzer()
                        result = analyzer.analyze(bug_input)
                    
                    st.markdown(f'<div class="report-card">{result}</div>', unsafe_allow_html=True)
                    
                    # Download button
                    st.download_button(
                        label="📄 Export Report",
                        data=result,
                        file_name="bug_analysis_report.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.info("Results will appear here once analysis is complete.")

    # Sidebar for API Status
    with st.sidebar:
        st.title("Settings")
        st.markdown("---")
        if os.getenv("OPENAI_API_KEY"):
            st.success("✅ API Key Loaded")
        else:
            st.error("❌ API Key Missing")
            st.info("Please set `OPENAI_API_KEY` in your `.env` file.")

if __name__ == "__main__":
    main()
