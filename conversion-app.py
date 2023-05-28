import streamlit as st

def convert_currency(amount, currency):
    conversion_rates = {
        "PKR": 285.00,
        "SGD": 1.35,
        "INR": 82.56,
        "EUR": 0.93,
        "CHF": 7.06,
        "GBP": 0.81
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
