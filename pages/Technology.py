import streamlit as st
import base64
import os

css = """
<style>
    /* ... (existing CSS styles) ... */
</style>
"""
st.markdown(css, unsafe_allow_html=True)

st.title("Technology")

st.write("""
    At our company, we leverage cutting-edge technologies to develop advanced solutions for various applications.
    Our core technologies include Robot Operating System (ROS), Computer Vision with Ultralytics, and Roboflow for data management and model training.
""")

st.divider()

with st.expander("Robot Operating System (ROS)"):
    st.write("""
        ROS is a flexible and robust framework for building robotic applications. It provides a set of tools and libraries for developing
        robot software, enabling seamless communication and collaboration between various components and devices.
    """)

with st.expander("Computer Vision with Ultralytics"):
    st.write("""
        We utilize Ultralytics, a powerful computer vision framework, for tasks such as object detection, segmentation, and tracking.
        Ultralytics provides state-of-the-art models, including YOLOv8, which offers high accuracy and real-time performance.
        To learn more about Ultralytics visit the docs https://docs.ultralytics.com/.
    """)
st.subheader("MFIT")
multi = '''The MFIT app supports Dectection and Segmentation,
These 2 tasks have different use cases and results.

Detection is the primary task supported by YOLOv8. It involves detecting objects in an image or video frame and drawing bounding boxes around them.

Segmentation is a task that involves segmenting an image into different regions based on the content of the image. Each region is assigned a label based on its content.
'''

st.markdown(multi)
st.page_link("pages/MFIT.py", label="MFIT", icon="📸")
st.divider()

st.header("Datasets")
st.write("""
Roboflow is our platform for dataset management. It simplifies the process of annotating and labelling, data for computer vision tasks. Roboflow also supports seamless integration with popular model training frameworks like Ultralytics.
""")

datasets = [
    {
        "name": "Strawberry",
        "description": "Dataset containing images of strawberries.",
        "image": "static/strawberry.jpg",
        "download_url": "https://example.com/datasets/strawberry_dataset.zip"
    },
    {
        "name": "Grapes",
        "description": "Dataset containing images of different grape varieties.",
        "image": "static/grapes.jpg",
        "download_url": "https://universe.roboflow.com/mifood/grapes-mitcn"
    },
    {
        "name": "Tomato",
        "description": "Dataset containing images of tomatoes.",
        "image": "static/tomato.jpg",
        "download_url": "https://universe.roboflow.com/mifood/grapes-mitcn"
    },
    {
        "name": "Apple",
        "description": "Rider Number Detector, Dataset of riders.",
        "image": "static/apple.jpg",
        "download_url": "https://universe.roboflow.com/mifood/apple-uzehd"
    }
]

dataset_list = st.container()
with dataset_list:
    cols = st.columns(len(datasets))
    for idx, dataset in enumerate(datasets):
        with cols[idx]:
            with st.expander(dataset["name"]):
                st.image(dataset["image"], caption=dataset["name"], use_column_width=True)
                if "roboflow.com" in dataset["download_url"]:
                    link = f"[View on Roboflow]({dataset['download_url']})"
                    if st.button(link, key=f"roboflow_button_{idx}"):
                        js = f"window.open('{dataset['download_url']}')"
                        st.markdown(f"<script>{js}</script>", unsafe_allow_html=True)
                else:
                    st.download_button(
                        label="View on Roboflow",
                        data=dataset["download_url"],
                        file_name=dataset["download_url"].split("/")[-1],
                        mime="application/octet-stream",
                    )
st.divider()

model_paths = {
    'Strawberry': 'UltralyticsModels/Strawberry V8.pt',
    'AppleV1': 'UltralyticsModels/AppleV1.pt',
    'Grapes': 'UltralyticsModels/GrapesV1.pt',
    'Tomato': 'UltralyticsModels/TomatoV3.pt',
    'Apple': 'UltralyticsModels/AppleV1.pt',
    'Weeding': 'UltralyticsModels/WeedingV3.pt',
    'Rider NF2': 'UltralyticsModels/rnd_detect4.0.pt',
    'Rider NF4': 'UltralyticsModels/RiderNF4.pt',
}

st.header("Models")
st.subheader("Don't have a Model?, Download One of ours:")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("AppleV1")
    with open(model_paths['AppleV1'], "rb") as file:
        st.download_button(
            label="Download AppleV1",
            data=file,
            file_name="AppleV1.pt",
            mime="application/octet-stream"
        )

with col2:
    st.header("Strawberry")
    with open(model_paths['Strawberry'], "rb") as file:
        st.download_button(
            label="Download Strawberry",
            data=file,
            file_name="StrawberryV8.pt",
            mime="application/octet-stream"
        )

with col3:
    st.header("Grapes")
    with open(model_paths['Grapes'], "rb") as file:
        st.download_button(
            label="Download Grapes",
            data=file,
            file_name="GrapesV1.pt",
            mime="application/octet-stream"
        )

col4, col5 = st.columns(2)

with col4:
    st.header("Rider NF2")
    with open(model_paths['Rider NF2'], "rb") as file:
        st.download_button(
            label="Download Rider NF2",
            data=file,
            file_name="rnd_detect4.0.pt",  
            mime="application/octet-stream"
        )

with col5:
    st.header("Rider NF4")
    with open(model_paths['Rider NF4'], "rb") as file:
        st.download_button(
            label="Download Rider NF4",
            data=file,
            file_name="RiderNF4.pt",
            mime="application/octet-stream"
        )

st.divider()
