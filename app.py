import streamlit as st
import pandas as pd

# Expanded Menu Data
data = {
    "Item": ["Espresso", "Latte", "Cappuccino", "Mocha", "Muffin", "Croissant", "Bagel", "Cookie"],
    "Type": ["Drink", "Drink", "Drink", "Drink", "Food", "Food", "Food", "Food"],
    "Location": ["Downtown", "Uptown", "Downtown", "Uptown", "Downtown", "Uptown", "Downtown", "Uptown"],
    "Price": [3.50, 4.50, 4.75, 5.00, 3.00, 3.50, 4.00, 2.50]
}
df = pd.DataFrame(data)

st.set_page_config(page_title="Coffee Shop Ordering", layout="wide")
st.title("☕ Artisan Coffee Ordering")

# Sidebar Filters
with st.sidebar:
    st.header("Menu Filters")
    selected_location = st.selectbox("Select Location", df["Location"].unique())
    selected_types = st.multiselect("Select Item Types", df["Type"].unique(), default=df["Type"].unique())

# Filtered View
filtered_df = df[(df["Location"] == selected_location) & (df["Type"].isin(selected_types))]

# Display Items with Quantity Selectors
st.subheader(f"Available Items in {selected_location}")
cart = {}

# Create grid for items
cols = st.columns(3)
for idx, row in enumerate(filtered_df.itertuples()):
    with cols[idx % 3]:
        st.write(f"**{row.Item}** - ${row.Price:.2f}")
        # Add a quantity selector for each item
        qty = st.number_input(f"Qty for {row.Item}", min_value=0, max_value=10, value=0, key=row.Item)
        if qty > 0:
            cart[row.Item] = {"qty": qty, "price": row.Price}

# Checkout Section
if cart:
    st.divider()
    st.header("Checkout")
    total = sum(item["qty"] * item["price"] for item in cart.values())
    st.write(f"### Total Amount: ${total:.2f}")
    
    with st.form("checkout_form"):
        name = st.text_input("Customer Name")
        address = st.text_input("Delivery Address")
        if st.form_submit_button("Place Order"):
            st.success(f"Order confirmed for {name}! Total: ${total:.2f}")
