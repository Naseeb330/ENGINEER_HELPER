import streamlit as st
from google import genai
import os

# Page Config
st.set_page_config(page_title="Engineering Career Portal", layout="wide")

# State Management
if "page" not in st.session_state: st.session_state.page = "home"
if "selected_domain" not in st.session_state: st.session_state.selected_domain = None

# Gemini API Helper
def ask_gemini(query):
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    prompt = f"You are a Career Counselor for engineering students. Answer this: {query}. Keep it concise and professional."
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text

# --- PAGE 1: LANDING PAGE ---
if st.session_state.page == "home":
    st.title("🎓 Engineering Career Development Portal")
    st.subheader("Select a domain to explore career paths and syllabus:")
    
    domains = ["Electrical Engineering", "Software Engineering", "Civil Engineering", "Mechanical Engineering"]
    
    cols = st.columns(4)
    for i, domain in enumerate(domains):
        if cols[i].button(domain, use_container_width=True):
            st.session_state.selected_domain = domain
            st.session_state.page = "dashboard"
            st.rerun()

# --- PAGE 2: DOMAIN DASHBOARD ---
elif st.session_state.page == "dashboard":
    st.button("⬅️ Back to Home", on_click=lambda: st.session_state.update(page="home"))
    st.title(f"⚡ {st.session_state.selected_domain} Dashboard")
    
    tab1, tab2, tab3 = st.tabs(["Qualifications", "Syllabus", "Subjects"])
    
    with tab1:
        st.subheader("Qualification Requirements")
        if st.button("Get Qualification Info"):
            with st.spinner("Fetching from AI..."):
                st.write(ask_gemini(f"What are the qualification requirements for {st.session_state.selected_domain}?"))
                
    with tab2:
        st.subheader("Core Syllabus Outline")
        st.write(ask_gemini(f"Provide a brief semester-wise syllabus outline for {st.session_state.selected_domain}."))
        
    with tab3:
        st.subheader("Important Subjects")
        st.write(ask_gemini(f"List the 5 most important subjects in {st.session_state.selected_domain} and why they matter."))
