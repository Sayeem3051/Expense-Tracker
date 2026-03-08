# Personal Expense Tracker

A simple Streamlit application to track and analyze your personal daily expenses.

## Features
- **Add Expenses**: Easily record expenses with an amount, category, date, and description.
- **Categorization**: Group your spending by predefined categories (Food, Travel, Shopping, Bills, Entertainment, Other).
- **Dashboard insights**: View your total spending, top spending category, and interactive charts visualizing your expenses by category and date.
- **Data Persistence**: Automatically stores your expenses locally in a CSV file (`expenses.csv`).

## Requirements
- Python 3.9+ 
- Streamlit
- Pandas
- Plotly

## Installation and Execution

1. Navigate to the project directory:
   ```bash
   cd c:\Users\SHIFA\Documents\projects\expense_tracker
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. Open the provided `Local URL` in your web browser to use the tracker!

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Web application framework for the UI.
- **Pandas**: Used for data manipulation, aggregation, and reading/writing the CSV.
- **Plotly Express**: Used for generating interactive pie and bar charts.
