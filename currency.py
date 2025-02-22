import streamlit as st

# Function to convert the currency
def convert_currency(amount, from_currency, to_currency):
    # Exchange rates (for simplicity, you can replace these with real-time API data)
    exchange_rates = {
        'USD': {'EUR': 0.92, 'GBP': 0.75, 'INR': 75.0, 'JPY': 110.0, 'PKR': 285.0, 'USD': 1.0},
        'EUR': {'USD': 1.09, 'GBP': 0.82, 'INR': 81.0, 'JPY': 119.0, 'PKR': 310.0, 'EUR': 1.0},
        'GBP': {'USD': 1.33, 'EUR': 1.22, 'INR': 98.5, 'JPY': 144.0, 'PKR': 370.0, 'GBP': 1.0},
        'INR': {'USD': 0.013, 'EUR': 0.012, 'GBP': 0.010, 'JPY': 1.46, 'PKR': 3.8, 'INR': 1.0},
        'JPY': {'USD': 0.0091, 'EUR': 0.0084, 'GBP': 0.0069, 'INR': 0.68, 'PKR': 2.6, 'JPY': 1.0},
        'PKR': {'USD': 0.0035, 'EUR': 0.0032, 'GBP': 0.0027, 'INR': 0.26, 'JPY': 0.38, 'PKR': 1.0}
    }
    
    # Convert the amount
    return amount * exchange_rates[from_currency][to_currency]

# Streamlit UI
st.title("💰 Currency Converter")
st.write("Convert between six popular currencies.")

# Input for amount
amount = st.number_input("Enter Amount", min_value=0.01, format="%.2f")

# Dropdowns for selecting the currencies
currencies = ['USD', 'EUR', 'GBP', 'INR', 'JPY', 'PKR']

from_currency = st.selectbox("From Currency", currencies)
to_currency = st.selectbox("To Currency", currencies)

# Button to perform the conversion
if st.button("Convert"):
    if from_currency == to_currency:
        st.error("Please choose different currencies to convert.")
    else:
        # Perform the conversion
        converted_amount = convert_currency(amount, from_currency, to_currency)
        st.success(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
