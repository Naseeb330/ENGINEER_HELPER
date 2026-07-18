import streamlit as st
import pandas as pd

# 1. Setup Configuration
st.set_page_config(page_title="Coffee Shop Ordering", layout="wide")

# 2. Data Initialization
if "menu" not in st.session_state:
    st.session_state.menu = pd.DataFrame({
        "Item": ["Espresso", "Latte", "Cappuccino", "Mocha", "Croissant"],
        "Type": ["Drink", "Drink", "Drink", "Drink", "Food"],
        "Price": [3.50, 4.50, 4.75, 5.00, 3.50]
    })

# 3. Robust Cart Initialization (Fixes the TypeError)
# This clears the cart if it contains the old 'string' format instead of 'dictionary'
if "cart" not in st.session_state or (len(st.session_state.cart) > 0 and not isinstance(st.session_state.cart[0], dict)):
    st.session_state.cart = []

# 4. Sidebar: User Cart
with st.sidebar:
    st.header("🛒 Your Order")
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"- {item['Item']} (${item['Price']:.2f})")
        
        st.divider()
        total = sum(item['Price'] for item in st.session_state.cart)
        st.subheader(f"Total: ${total:.2f}")
        
        if st.button("Clear Cart"):
            st.session_state.cart = []
            st.rerun()
    else:
        st.write("Your cart is empty.")

# 5. Main Dashboard: Menu Display
st.title("☕ Artisan Coffee Shop")

cols = st.columns(3)
for idx, row in st.session_state.menu.iterrows():
    with cols[idx % 3]:
        with st.container(border=True):
            st.write(f"### {row['Item']}")
            st.write(f"Price: ${row['Price']:.2f}")
            # Ensure we append a dictionary to the cart
            if st.button(f"Add to Cart", key=f"add_{row['Item']}"):
                st.session_state.cart.append({"Item": row['Item'], "Price": row['Price']})
                st.toast(f"Added {row['Item']} to cart!")

# 6. Order Processing
# 5. Order Processing
st.divider()
st.header("Checkout")

# Check if cart has items before showing checkout
if st.session_state.cart:
    # Calculate Total
    total_amount = sum(item['Price'] for item in st.session_state.cart)
    st.write(f"### Total Amount to Pay: ${total_amount:.2f}")

    with st.form("order_form"):
        name = st.text_input("Customer Name")
        address = st.text_input("Delivery Address")
        
        # Display note about payment
        st.info("Note: Payment will be collected in person upon delivery.")
        
        if st.form_submit_button("Place Order"):
            if name and address:
                # Success message as requested
                st.success(f"Thank you, {name}! Your order will be delivered to: {address}.")
                st.write("Please have your payment ready when the delivery arrives.")
                
                # Reset cart
                st.session_state.cart = []
            else:
                st.error("Please provide both your name and delivery address.")
else:
    st.write("Add items to your cart to proceed to checkout.")
