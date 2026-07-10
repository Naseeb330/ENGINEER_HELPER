import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Engineering Portal", layout="wide")

# API Configuration
try:
    # Secrets se API Key lein
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Model define karein
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Config Error: {e}")

def ask_gemini(query):
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"

# UI Logic
if "page" not in st.session_state: st.session_state.page = "home"

if st.session_state.page == "home":
    st.title("🎓 Engineering Career Development Portal")
    domains = ["Electrical Engineering", "Software Engineering", "Civil Engineering", "Mechanical Engineering"]
    cols = st.columns(4)
    for i, domain in enumerate(domains):
        if cols[i].button(domain):
            st.session_state.selected_domain = domain
            st.session_state.page = "dashboard"
            st.rerun()

elif st.session_state.page == "dashboard":
    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()
    st.title(f"⚡ {st.session_state.selected_domain} Dashboard")
    
    if st.button("Get Qualification Info"):
        with st.spinner("Fetching..."):
            st.write(ask_gemini(f"Explain qualification requirements for {st.session_state.selected_domain}."))
