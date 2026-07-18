import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Coffee Shop", layout="wide")

# Persistent Cart
if "cart" not in st.session_state:
    st.session_state.cart = []

# Sidebar for User/Cart
with st.sidebar:
    st.header("Your Cart")
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"- {item}")
        if st.button("Clear Cart"):
            st.session_state.cart = []
    else:
        st.write("Cart is empty.")

# Main Dashboard
st.title("☕ Artisan Coffee Shop")
# Mock data display
menu = pd.DataFrame({"Item": ["Latte", "Espresso"], "Price": [4.50, 3.00]})

cols = st.columns(3)
for i, row in menu.iterrows():
    with cols[i]:
        st.write(f"**{row['Item']}**")
        if st.button(f"Add {row['Item']}", key=row['Item']):
            st.session_state.cart.append(row['Item'])
