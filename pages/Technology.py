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
st.subheader("MFIT"
          )
multi = '''The MFIT app supports Dectection and Segmentation,
These 2 tasks have different use cases and results.

Detection is the primary task supported by YOLOv8. It involves detecting objects in an image or video frame and drawing bounding boxes around them.

Segmentation is a task that involves segmenting an image into different regions based on the content of the image. Each region is assigned a label based on its content.
'''

st.markdown(multi)
st.page_link("pages/MFIT.py", label="MFIT", icon="📸")
st.divider()
st.header("Models")
st.write("""
We have developed and trained various models for specific applications. You can download our pre-trained models and use them in your projects or applications.
""")

search_query = st.text_input("Search models...", placeholder="Enter a search query")
model_type_filter = st.multiselect("Filter by model type", ["Object Detection", "Segmentation", "Weeding", "Cherry", "Full Model"])

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
    },
    {
        "name": "Weeding Model",
        "description": "A model trained to detect and classify weeds in agricultural fields.",
        "image": "static/weeding.jpg",
        "download_url": os.path.join("UltralyticsModels", "WeedingV3.pt"),
        "type": "Weeding, Object Detection"
    },
    {
        "name": "Cherry Detection",
        "description": "A model trained to detect and classify cherry varieties.",
        "image": "static/cherry.jpg",
        "download_url": os.path.join("UltralyticsModels", "CherryV1.pt"),
        "type": "Cherry, Object Detection"
    },
    {
        "name": "Full Model",
        "description": "A comprehensive model trained for multiple agricultural tasks.",
        "image": "static/full_model.jpg",
        "download_url": os.path.join("UltralyticsModels", "FullModelV1.pt"),
        "type": "Full Model, Object Detection, Segmentation"
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


st.header("Datasets")
st.write("""
Roboflow is our platform for dataset management. It simplifies the process of annotating and labelling, data for computer vision tasks. Roboflow also supports seamless integration with popular model training frameworks like Ultralytics.
""")

datasets = [
    {
        "name": "Strawberry",
        "": "Dataset containing images of strawberries.",
        "image": "static/strawberry.jpg",
        "download_url": "https://example.com/datasets/strawberry_dataset.zip"
    },
    {
        "name": "Grapes",
        "": "Dataset containing images of different grape varieties.",
        "image": "static/grapes.jpg",
        "download_url": "https://universe.roboflow.com/mifood/grapes-mitcn"
    },
    {
        "name": "Tomato",
        "": "Dataset containing images of tomatoes.",
        "image": "static/tomato.jpg",
        "download_url": "https://universe.roboflow.com/mifood/grapes-mitcn"
    },
    {
        "name": "Apple",
        "": "Rider Number Detector, Dataset of riders.",
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

                if dataset["download_url"].startswith("https://universe.roboflow.com"):
                    st.markdown(f"[View on Roboflow]({dataset['download_url']})")
                else:
                    st.download_button(
                        label="Download Dataset",
                        data=dataset["download_url"],
                        file_name=dataset["download_url"].split("/")[-1],
                        mime="application/octet-stream",
                    )