import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="Coffee Shop Agent", page_icon="☕")

# Setup Gemini API (Add your key in Streamlit secrets for security)
# In your local environment, use: st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("☕ Artisan Coffee Bot")
st.write("Welcome! I'm here to help you with orders, menu info, and delivery status.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you with your order today?"}
    ]

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to order?"):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # System instructions to keep the bot focused
        system_instruction = """
        You are a helpful coffee shop assistant. 
        1. Keep responses concise and friendly.
        2. If the user asks for an order, confirm the items, size, and milk preference.
        3. If you don't know the answer, politely ask them to speak to a human.
        """
        
        chat = model.start_chat(history=[])
        response = chat.send_message(system_instruction + prompt)
        
        full_response = response.text
        message_placeholder.markdown(full_response)
    
    # Add assistant response to state
    st.session_state.messages.append({"role": "assistant", "content": full_response})
