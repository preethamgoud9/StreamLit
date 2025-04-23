import streamlit as st
import pandas as pd

st.title("hello palmer lucky")
st.subheader("i build military technology")
st.text("letsss goooo")
st.write("chose ur type of drone")

code = st.selectbox("your favorite programming language: ", ["python","javascript","c++","c","java",'Go',"rust","assemble"])

st.write(f"you choose {code}, Great choice")
st.success("you have finally chosen a language, now Do dsa")


if st.button("Dsa"):
    st.success('You got to learn man everyday')

result = st.checkbox('do AI/ml')

if result:
    st.success("go learn python and math")

programming_type = st.radio('pick your base: ', ['object oriented programming','functional programming'])
st.write(f"you chose, {programming_type} " )

st.slider("difficulty: ",0,5)

days = st.number_input("how many days can u complete in",min_value=0,max_value=100)
st.write(f"You got {days} to go" )

user = st.text_input("Enter your prompt")

if st.button("submit"):
    st.write(user)

dob = st.date_input("select your date of birth")

if dob:
    st.write(dob)
 
oops,fp = st.columns(2)
st.image('https://www.rockawave.com/wp-content/uploads/2021/01/142656955_263865468428216_420125125091627384_n.jpg',caption="dustin poirer",use_container_width=True)

file = st.file_uploader("upload ur image ",type=["csv"])

if file:
    df = pd.read_csv(file)
    st.dataframe(df)