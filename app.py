import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Engineering Portal", layout="wide")

# API Configuration
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # DYNAMIC MODEL CHECKING
    # Is block se hum wo model uthayenge jo aapke account par active hai
    def get_valid_model():
        models = genai.list_models()
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                # Agar 'gemini-1.5-flash' mil jaye toh best hai
                if 'gemini-1.5-flash' in m.name:
                    return genai.GenerativeModel(m.name)
                # Agar nahi, toh 'gemini-pro' (1.0) use karein
                if 'gemini-pro' in m.name:
                    return genai.GenerativeModel(m.name)
        return None

    model = get_valid_model()
except Exception as e:
    st.error(f"Config Error: {e}")

def ask_gemini(query):
    if not model:
        return "Model not found. Please check your API permissions."
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"

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
