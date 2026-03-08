import pandas as pd
import os
from datetime import datetime

# Path to the CSV file where expenses will be stored
DATA_FILE = "expenses.csv"

# Predefined categories for expenses
CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Other"]

def initialize_data_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(DATA_FILE, index=False)

def load_expenses() -> pd.DataFrame:
    """Load expenses from the CSV file into a Pandas DataFrame."""
    initialize_data_file()
    df = pd.read_csv(DATA_FILE)
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"]).dt.date
    return df

def save_expense(date, category: str, amount: float, description: str):
    """Save a single new expense to the CSV file."""
    initialize_data_file()
    
    # Create a DataFrame for the new record
    new_expense = pd.DataFrame([{
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Description": description
    }])
    
    # Append to existing data
    new_expense.to_csv(DATA_FILE, mode='a', header=False, index=False)

def get_total_spending(df: pd.DataFrame) -> float:
    """Calculate the sum of all expenses."""
    if df.empty:
        return 0.0
    return df["Amount"].sum()

def get_expenses_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Group expenses by category and calculate total for each."""
    if df.empty:
        return pd.DataFrame(columns=["Category", "Amount"])
    
    summary = df.groupby("Category")["Amount"].sum().reset_index()
    # Sort backwards or forwards, depending on preference
    summary = summary.sort_values(by="Amount", ascending=False)
    return summary

def get_expenses_by_date(df: pd.DataFrame) -> pd.DataFrame:
    """Group expenses by date and calculate total for each."""
    if df.empty:
        return pd.DataFrame(columns=["Date", "Amount"])
        
    summary = df.groupby("Date")["Amount"].sum().reset_index()
    summary = summary.sort_values(by="Date")
    return summary
