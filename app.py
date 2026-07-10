import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Engineering Career Portal", layout="wide")

# API Configuration using Streamlit Secrets
# Make sure you have GEMINI_API_KEY in your Streamlit Cloud Secrets settings
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("API Key configure nahi ho saki. Check your Secrets.")

# Gemini function
def ask_gemini(query):
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# State Management
if "page" not in st.session_state: st.session_state.page = "home"
if "selected_domain" not in st.session_state: st.session_state.selected_domain = None

# --- UI ---
if st.session_state.page == "home":
    st.title("🎓 Engineering Career Development Portal")
    st.subheader("Select a domain:")
    
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
    
    tab1, tab2, tab3 = st.tabs(["Qualifications", "Syllabus", "Subjects"])
    
    with tab1:
        if st.button("Get Qualification Info"):
            with st.spinner("Loading..."):
                st.write(ask_gemini(f"What are the qualification requirements for {st.session_state.selected_domain} in Pakistan?"))
    with tab2:
        if st.button("Get Syllabus"):
            with st.spinner("Loading..."):
                st.write(ask_gemini(f"Provide a brief semester-wise syllabus outline for {st.session_state.selected_domain}."))
    with tab3:
        if st.button("Get Important Subjects"):
            with st.spinner("Loading..."):
                st.write(ask_gemini(f"List the 5 most important subjects in {st.session_state.selected_domain} and why they matter."))
