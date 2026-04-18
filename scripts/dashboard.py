import streamlit as st
import pandas as pd

# PAGE CONFIG
st.set_page_config(page_title="Transport Dashboard", layout="wide")

st.title(" Public Transport Ticketing Dashboard")

# LOAD DATA (FROM CSV)
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/final_data.csv")
    return df

df = load_data()

# KPI SECTION
col1, col2, col3 = st.columns(3)

col1.metric("Total Tickets", len(df))
col2.metric("Total Revenue", f"₹ {df['price'].sum():,.0f}")
col3.metric("Avg Price", f"₹ {df['price'].mean():.2f}")

# FILTERS
st.sidebar.header("Filters")

city = st.sidebar.multiselect("Select City", df["city"].unique(), default=df["city"].unique())
vehicle = st.sidebar.multiselect("Vehicle Type", df["vehicle_type"].unique(), default=df["vehicle_type"].unique())

filtered_df = df[(df["city"].isin(city)) & (df["vehicle_type"].isin(vehicle))]

# CHARTS

st.subheader(" Revenue by Route")
st.bar_chart(filtered_df.groupby("route")["price"].sum())

st.subheader(" Revenue by City")
st.bar_chart(filtered_df.groupby("city")["price"].sum())

st.subheader(" Revenue by Vehicle Type")
st.bar_chart(filtered_df.groupby("vehicle_type")["price"].sum())

st.subheader(" Price Category Distribution")
st.bar_chart(filtered_df["price_category"].value_counts())

# DATA VIEW
st.subheader(" Sample Data")
st.dataframe(filtered_df.head(100))