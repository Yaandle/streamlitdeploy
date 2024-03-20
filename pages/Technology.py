import streamlit as st

st.set_page_config(page_title="Technology", layout="wide")

# CSS styles
css = """
<style>
h1 {
    font-size: 36px;
    font-weight: bold;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

h2 {
    font-size: 24px;
    font-weight: bold;
    color: #2c3e50;
    margin-top: 40px;
    margin-bottom: 20px;
}

p {
    font-size: 16px;
    line-height: 1.6;
    color: white;
    margin-bottom: 20px;
}

ul {
    list-style-type: disc;
    margin-left: 30px;
    margin-bottom: 20px;
}

li {
    font-size: 16px;
    line-height: 1.6;
    color: #34495e;
}

.model-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 30px;
}

.model-card {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    padding: 20px;
    margin: 10px;
    width: 300px;
    text-align: center;
}

.model-card img {
    max-width: 100%;
    height: auto;
    margin-bottom: 10px;
}

.model-card h3 {
    font-size: 18px;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 10px;
}

.model-card p {
    font-size: 14px;
    color: #34495e;
    margin-bottom: 10px;
}

.model-card a {
    display: inline-block;
    background-color: #2c3e50;
    color: #fff;
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.model-card a:hover {
    background-color: #34495e;
}
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
st.subheader("Robot Operating System (ROS)")
st.write("""
    ROS is a flexible and robust framework for building robotic applications. It provides a set of tools and libraries for developing
    robot software, enabling seamless communication and collaboration between various components and devices.
""")

st.divider()
st.subheader("Computer Vision with Ultralytics")
st.write("""
    We utilize Ultralytics, a powerful computer vision framework, for tasks such as object detection, segmentation, and tracking.
    Ultralytics provides state-of-the-art models, including YOLOv8, which offers high accuracy and real-time performance.
""")
st.header("Pre-trained Models")
st.write("""
    We have developed and trained various models for specific applications. You can download the pre-trained models and leverage them
    in your projects or applications.
""")

models = [
    {
        "name": "Strawberry Detection",
        "description": "A model trained to detect strawberries in images and videos.",
        "image": "static/strawberry.jpg",
        "download_url": "https://example.com/models/strawberry_detection.pt"
    },
    {
        "name": "Grape Segmentation",
        "description": "A model trained to segment different grape varieties in images.",
        "image": "static/grapes.jpg",
        "download_url": "https://example.com/models/grape_segmentation.pt"
    },
    {
        "name": "Tomato Detection and Counting",
        "description": "A model trained to detect and count tomatoes in images and videos.",
        "image": "static/tomato.jpg",
        "download_url": "https://example.com/models/tomato_detection_counting.pt"
    }
]

st.header("Available Models")
model_list = st.container()
with model_list:
    cols = st.columns(len(models))
    for idx, model in enumerate(models):
        with cols[idx]:
            st.markdown(f"""
                <div class="model-card">
                    <img src="{model['image']}" alt="{model['name']}">
                    <h3>{model['name']}</h3>
                    <p>{model['description']}</p>
                    <a href="{model['download_url']}" download>Download Model</a>
                </div>
            """, unsafe_allow_html=True)

st.divider()
st.subheader("Roboflow")
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
        "description": "Research and Development dataset.",
        "image": "static/rnd.jpg",
        "download_url": "https://example.com/datasets/rnd_dataset.zip"
    }
]

st.header("Available Datasets")
dataset_list = st.container()
with dataset_list:
    cols = st.columns(len(datasets))
    for idx, dataset in enumerate(datasets):
        with cols[idx]:
            st.markdown(f"""
                <div class="dataset-card">
                    <img src="{dataset['image']}" alt="{dataset['name']}">
                    <h3>{dataset['name']}</h3>
                    <p>{dataset['description']}</p>
                    <a href="{dataset['download_url']}" download>Download Dataset</a>
                </div>
            """, unsafe_allow_html=True)
