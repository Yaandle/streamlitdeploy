import streamlit as st

st.set_page_config(
    page_title="MiFood",
    page_icon="",
    layout="wide"
)

col1, col2 = st.columns([2, 3])
with col1:
    st.title("MiFood: Revolutionizing Horticulture with Robotics")
    st.write("Welcome to our website! We are passionate about using robotics to improve efficiency and sustainability in the horticultural industry.")


st.header("About MiFood")
with st.expander("Vision and Mission", expanded=True):
    st.write("""
        MiFood's vision is to create a future where robotics empowers the
        horticultural industry, leading to increased productivity, reduced
        waste, and a more sustainable food system. Our mission is to develop
        and deploy innovative robotic solutions that address real-world
        challenges faced by farmers and growers.
    """)

st.header("Our Programs")
st.write("Discover our innovative tools for object detection and analysis:")

with st.expander("ODIS Function"):
    st.write("""
        The Object Detection Image Sorting (ODIS) function is a tool designed for sorting images based on detected objects. Leveraging state-of-the-art object detection algorithms, ODIS can automatically organize your images, making it easier to manage and analyze large datasets.

        **Key Features:**

        * Automated image sorting based on object detection.
        * Support for various object detection models.
        * Efficient processing for large image datasets.
    """)
    st.markdown("[Go to ODIS Function](/ODIS)")


with st.expander("MFIT Inference"):
    st.write("""
        MFIT is our specialized feature for object recognition and analysis. Whether you're working with single images, multiple images, or videos, MFIT offers robust inference capabilities, including detection and segmentation, to provide data on the inference.

        **Key Features:**

        * Support for inference on images, multi-images, and videos.
        * Capabilities include both detection and segmentation.
        * Ideal for testing and model analysis.
    """)
    st.markdown("[Go to MFIT](/MFIT)")

st.write("MiFood, Australia | Contact: zac@mifood.es")

st.image("whitelogo.png", width=350)