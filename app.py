import streamlit as st
st.title("my firt time trying")
name=st.text_inport("Enter your name")

if st.button("Submit"):

  st.write(f"Hello,{name}")
