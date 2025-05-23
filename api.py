import streamlit as st
import requests 

st.title("live currency converter")

amount = st.number_input("enter the input in INR",min_value=1)

target_currency = st.selectbox("convert to: ", ['USD','EUR','GBP','JYP'])

if st.button("convert"):
    url = 'https://api.exchangerate-api.com/v4/latest/INR'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted = rate * amount
        st.success(f'{amount} INR = {converted} {target_currency}')
    else:
        st.error("failed to fetch conversion rate")
         