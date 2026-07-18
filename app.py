import streamlit as st
import pandas as pd

# 1. Setup Configuration
st.set_page_config(page_title="Coffee Shop Ordering", layout="wide")

# 2. Data Initialization
# In a professional app, you would load this from a CSV or Database
if "menu" not in st.session_state:
    st.session_state.menu = pd.DataFrame({
        "Item": ["Espresso", "Latte", "Cappuccino", "Mocha", "Croissant"],
        "Type": ["Drink", "Drink", "Drink", "Drink", "Food"],
        "Price": [3.50, 4.50, 4.75, 5.00, 3.50]
    })

# Initialize Cart in Session State
if "cart" not in st.session_state:
    st.session_state.cart = []

# 3. Sidebar: User Cart & Controls
with st.sidebar:
    st.header("🛒 Your Order")
    if st.session_state.cart:
        for i, item in enumerate(st.session_state.cart):
            st.write(f"{item['Item']} (${item['Price']:.2f})")
        
        st.divider()
        total = sum(item['Price'] for item in st.session_state.cart)
        st.subheader(f"Total: ${total:.2f}")
        
        if st.button("Clear Cart"):
            st.session_state.cart = []
            st.rerun()
    else:
        st.write("Your cart is empty.")

# 4. Main Dashboard: Menu Display
st.title("☕ Artisan Coffee Shop")
st.subheader("Explore our menu")

# Simple Filtering
menu_df = st.session_state.menu
item_type = st.radio("Filter by:", ["All", "Drink", "Food"], horizontal=True)

if item_type != "All":
    menu_df = menu_df[menu_df["Type"] == item_type]

# Product Grid
cols = st.columns(3)
for idx, row in enumerate(menu_df.itertuples()):
    with cols[idx % 3]:
        with st.container(border=True):
            st.write(f"### {row.Item}")
            st.write(f"Price: ${row.Price:.2f}")
            if st.button(f"Add to Cart", key=f"add_{row.Item}"):
                st.session_state.cart.append({"Item": row.Item, "Price": row.Price})
                st.toast(f"Added {row.Item} to cart!")

# 5. Order Processing
st.divider()
st.header("Checkout")
with st.form("order_form"):
    name = st.text_input("Name")
    address = st.text_input("Delivery Address")
    payment = st.selectbox("Payment Method", ["Credit Card", "Cash", "Digital Wallet"])
    
    if st.form_submit_button("Place Order"):
        if name and address and st.session_state.cart:
            st.success(f"Thank you, {name}! Your order is being prepared for delivery to {address}.")
            st.session_state.cart = [] # Reset cart after order
        else:
            st.error("Please ensure your cart is not empty and you've provided your details.")
