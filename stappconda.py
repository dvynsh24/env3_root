import streamlit as st

# Get user's name
name = st.text_input("Enter your name")

# Get user's email
email = st.text_input("Enter your email")

# Display the entered name and email
st.write("Name:", name)
st.write("Email:", email)

