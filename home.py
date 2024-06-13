import streamlit as st
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.set_page_config(
    page_title="YKSolutions",
    page_icon="",
    layout="wide"
)

st.title("YK")


st.write("Welcome to our website! We are passionate about using computer vision and robotics to improve efficiency in businesses.")

st.divider()

container1, container2 = st.columns(2)

with container1:
    st.subheader("ODIS Function")
    st.write("A tool for sorting images based on detected objects.")
    st.page_link("pages/ODIS.py", label="ODIS", icon="🔁")
    st.subheader("Technology")
    st.write("Explore the technology used in our services and operations.")
    st.page_link("pages/Technology.py", label="Technology", icon="🔧")

with container2:
    st.subheader("MFIT Inference")
    st.write("MFIT is a feature for pretrained model testing.")
    st.page_link("pages/MFIT.py", label="MFIT", icon="📸")



st.divider()




styles = """
<style>
  form {
    background-color: #212121;
    padding: 20px;
    border-radius: 5px;
    color: white;
    font-family: Arial, sans-serif;
  }

  input[type=text], input[type=email], textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: none;
    border-radius: 5px;
    background-color: #333333;
    color: white;
    font-size: 14px;
  }

  button[type=submit] {
    background-color: #800080;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    float: right;
    font-size: 14px;
  }

  button[type=submit]:hover {
    background-color: #45a049;
  }
</style>
"""

# Render the contact form
contact_form = f"""
{styles}
<form action="https://formsubmit.co/8d19c4dff7c14ae7aa2f638d3dbe15f0" method="POST">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="name" placeholder="Your name" required>
  <input type="email" name="email" placeholder="Your email" required>
  <textarea name="message" placeholder="Your message here"></textarea>
  <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)