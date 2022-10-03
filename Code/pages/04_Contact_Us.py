import email
import streamlit as st


st.subheader(
    'Hello, *we are R2M solution* if you have any further question or discussion fill in this form :sunglasses:')

st.write("write your idea")

with st.container():
    with st.form("my_form"):
        Name = st.text_input("Name: ")
        Email = st.text_input("Email: ")
        Idea = st.text_area("Put your idea here")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(
                "Your suggestion has been inputted to our system, Thank you!")
