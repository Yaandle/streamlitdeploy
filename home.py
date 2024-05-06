import streamlit as st

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
    st.write("MFIT is a feature for model testing.")
    st.page_link("pages/MFIT.py", label="MFIT", icon="📸")



st.divider()


st.title("Contact Us")
st.write("Please fill out the form below to get in touch with us.")

with st.form(key="contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
    with col2:
        email = st.text_input("Email")
    company = st.text_input("Company")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.success("Thank you for contacting us! We'll be in touch soon.")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Company: {company}")
    st.write(f"Message: {message}")