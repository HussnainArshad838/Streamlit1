import streamlit as st

def convert_currency(amount, currency):
    conversion_rates = {
        "PKR": 171.5,
        "SGD": 1.34,
        "INR": 74.81,
        "EUR": 0.91,
        "CHF": 0.98,
        "GBP": 0.71
    }

    converted_amount = amount * conversion_rates[currency]
    return converted_amount

def main():
    st.title("Currency Converter")

    amount = st.number_input("Enter the amount in USD:")
    currency = st.selectbox("Select the currency to convert to:",
                            ["PKR", "SGD", "INR", "EUR", "CHF", "GBP"])

    if st.button("Convert"):
        converted_amount = convert_currency(amount, currency)
        st.success(f"The converted amount is {converted_amount} {currency}")

if __name__ == "__main__":
    main()
