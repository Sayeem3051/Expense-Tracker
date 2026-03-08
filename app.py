import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import data_manager as dm

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")

st.title("💰 Personal Expense Tracker")
st.markdown("Track and analyze your daily spending easily.")

# Sidebar - Add Expense Form
st.sidebar.header("Add New Expense")
with st.sidebar.form("expense_form", clear_on_submit=True):
    date = st.date_input("Date", value=datetime.today())
    category = st.selectbox("Category", dm.CATEGORIES)
    amount = st.number_input("Amount", min_value=0.01, step=1.0, format="%.2f")
    description = st.text_input("Description (Optional)")
    
    submitted = st.form_submit_button("Add Expense")
    
    if submitted:
        dm.save_expense(date.strftime("%Y-%m-%d"), category, amount, description)
        st.success("Expense added successfully!")

# Load Data
df = dm.load_expenses()

if df.empty:
    st.info("No expenses recorded yet. Add some from the sidebar!")
else:
    # Top Row - Summary Metrics
    total_spending = dm.get_total_spending(df)
    
    st.markdown("### 📊 Dashboard Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Spending", f"${total_spending:,.2f}")
    col2.metric("Total Transactions", f"{len(df)}")
    if not df.empty:
        top_cat = df.groupby("Category")["Amount"].sum().idxmax()
        col3.metric("Top Category", top_cat)
    
    st.markdown("---")
    
    # Middle Row - Charts
    st.markdown("### 📈 Spending Insights")
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Category Pie Chart
        cat_summary = dm.get_expenses_by_category(df)
        if not cat_summary.empty:
            fig_pie = px.pie(cat_summary, values="Amount", names="Category", 
                             title="Expenses by Category",
                             color_discrete_sequence=px.colors.sequential.Teal)
            st.plotly_chart(fig_pie, use_container_width=True)
            
    with chart_col2:
        # Spending over time (Bar Chart)
        date_summary = dm.get_expenses_by_date(df)
        if not date_summary.empty:
            fig_bar = px.bar(date_summary, x="Date", y="Amount", 
                             title="Daily Spending",
                             text_auto='.2s',
                             color_discrete_sequence=["#1f77b4"])
            st.plotly_chart(fig_bar, use_container_width=True)
            
    st.markdown("---")

    # Bottom Row - Data Table
    st.markdown("### 📋 Recent Expenses")
    # Show most recent first
    st.dataframe(df.sort_values(by="Date", ascending=False).reset_index(drop=True), use_container_width=True)
