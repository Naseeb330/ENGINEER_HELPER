import streamlit as st
import pandas as pd

# 1. Mock Data Setup (Replace this with your database or CSV file)
data = {
    "Item": ["Espresso", "Latte", "Cappuccino", "Muffin", "Croissant", "Bagel"],
    "Type": ["Drink", "Drink", "Drink", "Food", "Food", "Food"],
    "Location": ["Downtown", "Uptown", "Downtown", "Downtown", "Uptown", "Downtown"]
}
df = pd.DataFrame(data)

st.set_page_config(page_title="Coffee Shop Menu", layout="wide")
st.title("☕ Coffee Shop Availability Dashboard")

# 2. Sidebar Filters
with st.sidebar:
    st.header("Filter Options")
    
    # Get unique values for filters
    locations = df["Location"].unique()
    types = df["Type"].unique()
    
    selected_location = st.selectbox("Select Location", options=locations)
    selected_type = st.multiselect("Select Order Type", options=types, default=types)

# 3. Filtering Logic
filtered_df = df[
    (df["Location"] == selected_location) & 
    (df["Type"].isin(selected_type))
]

# 4. Display Results
st.subheader(f"Available Items in {selected_location}")

if not filtered_df.empty:
    # Use columns to display items in a grid-like view
    cols = st.columns(3)
    for i, row in enumerate(filtered_df.itertuples()):
        with cols[i % 3]:
            st.info(f"**{row.Item}**\n\nType: {row.Type}")
else:
    st.warning("No items match your selected criteria.")

# Optional: Show raw data in an expander
with st.expander("View all data"):
    st.dataframe(df)
