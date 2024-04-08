import streamlit as st

st.set_page_config(
    page_title="yandlestreamlitapp",
    page_icon="",
    layout="wide"
)

st.title("YK Solutions")
st.write("Welcome to our website! We are passionate about using computer vision and robotics to improve efficiency.")

st.divider()

container1, container2 = st.columns(2)

with container1:
    st.subheader("Robots as a Service")
    st.write("Use our robots to automate your workflow.")
    st.page_link("pages/Service.py", label="Service", icon="🤖")

    st.subheader("ODIS Function")
    st.write("A tool for sorting images based on detected objects.")
    st.page_link("pages/ODIS.py", label="ODIS", icon="🔁")

with container2:
    st.subheader("MFIT Inference")
    st.write("MFIT is a feature for model testing.")
    st.page_link("pages/MFIT.py", label="MFIT", icon="📸")

    st.subheader("Technology")
    st.write("Explore the technology used in our service and operations.")
    st.page_link("pages/Technology.py", label="Technology", icon="🔧")

st.divider()
