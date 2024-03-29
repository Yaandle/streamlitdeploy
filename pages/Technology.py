import streamlit as st
import base64
import os

# CSS styles
css = """
<style>
    /* ... (existing CSS styles) ... */
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Content
st.title("Technology")

st.write("""
    At our company, we leverage cutting-edge technologies to develop advanced solutions for various applications.
    Our core technologies include Robot Operating System (ROS), Computer Vision with Ultralytics, and Roboflow for data management and model training.
""")

st.divider()

# ROS section
with st.expander("Robot Operating System (ROS)"):
    st.write("""
        ROS is a flexible and robust framework for building robotic applications. It provides a set of tools and libraries for developing
        robot software, enabling seamless communication and collaboration between various components and devices.
    """)

# Ultralytics section
with st.expander("Computer Vision with Ultralytics"):
    st.write("""
        We utilize Ultralytics, a powerful computer vision framework, for tasks such as object detection, segmentation, and tracking.
        Ultralytics provides state-of-the-art models, including YOLOv8, which offers high accuracy and real-time performance.
    """)

# Models section
st.header("Models")
st.write("""
    We have developed and trained various models for specific applications. You can download the pre-trained models and leverage them
    in your projects or applications.
""")

# Search and filter functionality
search_query = st.text_input("Search models...", placeholder="Enter a search query")
model_type_filter = st.multiselect("Filter by model type", ["Object Detection", "Segmentation",])
models = [
    {
        "name": "Strawberry Detection",
        "description": "A model trained to detect strawberries in images and videos.",
        "image": "static/strawberry.png",
        "download_url": os.path.join("UltralyticsModels", "StrawberryV6.pt"),  
        "type": "Segmentation, Object Detection"
    },
    {
        "name": "Grape Segmentation",
        "description": "A model trained to segment different grape varieties in images.",
        "image": "static/grapes.jpg",
        "download_url": os.path.join("UltralyticsModels", "GrapesV1.pt"),  
        "type": "Detection, Segmentation"
    },
    {
        "name": "Tomato Detection",
        "description": "A model trained to detect and count tomatoes in images and videos.",
        "image": "static/tomato.jpg",
        "download_url": os.path.join("UltralyticsModels", "TomatoV3.pt"),  
        "type": "Object Detection, Segmentation"
    },
    {
        "name": "Rider Number Detector",
        "description": "A model trained to detect numbers in images and videos.",
        "image": "static/555RIDER.jpg",
        "download_url": os.path.join("UltralyticsModels", "rnd_detect4.0.pt"),  
        "type": "Object Detection"
    }
]

filtered_models = models
if search_query:
    filtered_models = [m for m in models if search_query.lower() in m["name"].lower() or search_query.lower() in m["description"].lower()]
if model_type_filter:
    filtered_models = [m for m in filtered_models if any(t in m["type"] for t in model_type_filter)]

model_list = st.container()
with model_list:
    if filtered_models:
        cols = st.columns(len(filtered_models))
        for idx, model in enumerate(filtered_models):
            with cols[idx]:
                with st.expander(model["name"]):
                    st.image(model["image"], caption=model["name"], use_column_width=True)
                    st.write(f"**Description:** {model['description']}")
                    st.write(f"**Model Type:** {model['type']}")
                    
                    # Download button with actual data or URL
                    with open(model["download_url"], "rb") as f:
                        data = f.read()
                    file_data = base64.b64encode(data).decode("utf-8")
                    st.download_button(
                        label="Download Model",
                        data=file_data,
                        file_name=model["download_url"].split("/")[-1],
                        mime="application/octet-stream",
                    )
    else:
        st.warning("No models found.")

st.divider()

# Datasets section
st.header("Datasets")
st.write("""
    Roboflow is our go-to platform for data management and model training. It simplifies the process of annotating, organizing, and preprocessing
    data for computer vision tasks. Roboflow also supports seamless integration with popular model training frameworks like Ultralytics.
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
        "download_url": "https://example.com/datasets/grapes_dataset.zip"
    },
    {
        "name": "Tomato",
        "description": "Dataset containing images of tomatoes.",
        "image": "static/tomato.jpg",
        "download_url": "https://example.com/datasets/tomato_dataset.zip"
    },
    {
        "name": "RnD",
        "description": "Rider Number Detector, Dataset of riders.",
        "image": "static/555RIDER.jpg",
        "download_url": "https://example.com/datasets/rnd_dataset.zip"
    }
]

dataset_list = st.container()
with dataset_list:
    cols = st.columns(len(datasets))
    for idx, dataset in enumerate(datasets):
        with cols[idx]:
            with st.expander(dataset["name"]):
                st.image(dataset["image"], caption=dataset["name"], use_column_width=True)
                st.write(f"**Description:** {dataset['description']}")
                st.download_button(
                    label="Download Dataset",
                    data=dataset["download_url"],
                    file_name=dataset["download_url"].split("/")[-1],
                    mime="application/octet-stream",
                )