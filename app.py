import streamlit as st
import pandas as pd
import pydeck as pdk

# Set Streamlit page configuration
st.set_page_config(page_title="Financial Assistant", layout="centered")

# Load and display the logo in the sidebar
logo = "logo.jpg"
st.sidebar.image(logo, use_column_width=True)

# Password authentication
st.sidebar.title("Configuration")
input_password = st.sidebar.text_input("Enter Password (password is team's name without capital)", type="password")
correct_password = "openmachine"
if input_password != correct_password:
    st.sidebar.error("Incorrect password. Access denied.")
    st.stop()

# Financial analysis inputs
st.title("Financial Diagnostic Tool")
st.subheader("Enter Your Financial Details")

# Input for current balance and expenses
balance = st.number_input("Current Balance (Rp)", min_value=0, value=3000000)
pln_bill = st.number_input("PLN Bill (Rp)", min_value=0, value=600000)
comm_bill = st.number_input("Communication Bill (Rp)", min_value=0, value=200000)

# Calculate total expenses and determine cash flow status
total_expenses = pln_bill + comm_bill
cashflow_status = "Surplus" if balance > total_expenses else "Deficit"
remaining_balance = balance - total_expenses

# Display cash flow analysis
st.write(f"Total Expenses: Rp{total_expenses}")
st.write(f"Remaining Balance: Rp{remaining_balance}")
st.write(f"Cash Flow Status: {cashflow_status}")

# Investment and financial planning suggestions
st.subheader("Investment and Financial Planning Suggestions")

if cashflow_status == "Surplus":
    st.write("With a surplus cash flow, here are some suggestions:")
    st.write("- **Emergency Fund**: Allocate at least 3-6 months of expenses to an emergency fund for unexpected events.")
    st.write("- **Investment Options**: Consider low-risk investments such as mutual funds or fixed deposits for stable returns.")
    st.write("- **Retirement Planning**: Start a retirement plan by setting aside a small amount each month in a pension fund or retirement savings account.")
    st.write("- **Education Fund**: If you have dependents, consider saving for their education.")
else:
    st.write("With a deficit cash flow, here are some suggestions:")
    st.write("- **Budget Review**: Review and adjust your budget to reduce unnecessary expenses.")
    st.write("- **Debt Management**: Prioritize paying off high-interest debts to improve cash flow.")
    st.write("- **Increase Income**: Explore additional income opportunities, such as freelancing or part-time work.")
    st.write("- **Financial Goals**: Set realistic financial goals and track your spending to stay within budget.")

# Additional question-answer model for finance FAQ
st.subheader("Ask a Financial Question")
question = st.text_input("Ask a question about finance:")
if question:
    # Here would be the integration to an API for response generation (omitted for offline demonstration)
    answer = "This is a placeholder response for financial queries."
    st.write(f"**Q:** {question}\n**A:** {answer}")
    st.write("---")
