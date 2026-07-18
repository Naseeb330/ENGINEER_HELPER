import streamlit as st

# 1. Page Configuration
st.set_page_config(layout="wide")

# 2. Sidebar: User Account & Navigation
with st.sidebar:
    st.header("User Account")
    st.write("Welcome, User!")
    st.button("View Profile")
    st.divider()
    st.header("Filters")
    category = st.selectbox("Category", ["Coffee", "Equipment", "Merch"])

# 3. Main Area: Product Display
st.title("Available Products")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("coffee1.jpg")
    st.subheader("Product 1")
    st.button("Add to Cart", key="p1")

with col2:
    st.image("coffee2.jpg")
    st.subheader("Product 2")
    st.button("Add to Cart", key="p2")

with col3:
    st.image("coffee3.jpg")
    st.subheader("Product 3")
    st.button("Add to Cart", key="p3")
