import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Engineering Portal", layout="wide")

# API Configuration
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Yeh line search karein aur replace karein
   model = genai.GenerativeModel('gemini-1.5-flash')

# UI Logic
if "page" not in st.session_state: st.session_state.page = "home"

if st.session_state.page == "home":
    st.title("🎓 Engineering Career Portal")
    if st.button("Electrical Engineering"):
        st.session_state.selected_domain = "Electrical Engineering"
        st.session_state.page = "dashboard"
        st.rerun()

elif st.session_state.page == "dashboard":
    if st.button("⬅️ Back"):
        st.session_state.page = "home"
        st.rerun()
    st.title(f"⚡ {st.session_state.selected_domain}")
    
    if st.button("Get Info"):
        with st.spinner("Fetching..."):
            st.write(ask_gemini(f"Qualification requirements for {st.session_state.selected_domain}"))
