import streamlit as st

st.set_page_config(
    page_title="yandlestreamlitapp",
    page_icon="",
    layout="wide"
)

st.title("MiFood")


st.write("Welcome to our website! We are passionate about using computer vision and robotics to improve efficiency.")

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

st.title("About MiFood Solutions")

with st.expander("The Robotics Revolution", expanded=True):
    st.write("""
    We're living in a time of unprecedented transformation. The world is on the cusp of a new revolution, driven by the rapid advancement of robotics and automation technologies. This shift is fundamentally changing the way businesses operate, paving the way for a more efficient, sustainable, and prosperous future.
    """)
    st.write("""
    At MiFood, we're at the forefront of this robotics evolution. Our mission is to empower companies of all sizes to embrace this technological revolution and unlock its full potential. We firmly believe that access to cutting-edge automation solutions should not be limited to only the largest enterprises – every business deserves the opportunity to leverage the power of robotics to drive growth and stay ahead of the competition.
    """)

with st.expander("Our Expertise and Solutions"):
    st.write("""
    Born out of a deep understanding of the complexities and labor-intensive nature of various business operations, our team of passionate innovators has combined expertise in robotics, computer vision, and artificial intelligence to develop autonomous systems that dramatically improve efficiency and productivity. From precision manufacturing and logistics to data-driven decision-making and remote monitoring, our tailored solutions are designed to help our clients overcome their most pressing challenges and capitalize on emerging opportunities.
    """)

with st.expander("Our Vision and Commitment"):
    st.write("""
    We're living in a world that is rapidly evolving, and the pace of change is only accelerating. Businesses that fail to adapt and embrace the robotics revolution risk being left behind. That's why we're dedicated to empowering our clients with the tools and support they need to stay ahead of the curve.
    """)
    st.write("""
    Our vision is to create a future where robotics and automation are seamlessly integrated into every aspect of business operations, leading to increased efficiency, reduced waste, and a more sustainable tomorrow. We're committed to developing and deploying innovative solutions that address real-world challenges, helping our clients achieve their goals and pave the way for long-term success.
    """)

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