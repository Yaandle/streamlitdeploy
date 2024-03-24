import streamlit as st
from datetime import datetime
from ultralytics import YOLO
from PIL import Image
import numpy as np
from zipfile import ZipFile
import tempfile
import cv2
import PIL.Image
import time
import torch 

#UI Header, Text paragraph and 2 Images
st.title("Object Detection Image/Video Inference", )
server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Server time: {server_time}")
col1, col2 = st.columns(2)
with col1:
    st.image('static/strawberryrobotlarge.jpg', caption="", width=250)
with col2:
    st.image('static/strawberryrobot3.jpg', caption="", width=250)

multi = '''The MFIT app supports Dectection and Segmentation,
These 2 tasks have different use cases and results.

Detection is the primary task supported by YOLOv8. It involves detecting objects in an image or video frame and drawing bounding boxes around them.

Segmentation is a task that involves segmenting an image into different regions based on the content of the image. Each region is assigned a label based on its content.
'''
st.markdown(multi)

# Model and mode selection
st.subheader("Select a model, or upload a custom model.")
option = st.selectbox('Select a YOLOv8 model.', ('Strawberry', 'Grapes', 'Tomato', 'RND', 'Custom'))
st.write('You selected:', option, "Model")
st.subheader("Select a task.")
option2 = st.selectbox('Select a mode.', ('Detection', 'Segmentation'))
st.write('You selected:', option2, "mode")
st.divider()
model_paths = {
    'Strawberry': 'UltralyticsModels/StrawberryV6.pt',
    'Apple': 'UltralyticsModels/AppleV1.pt',
    'Grapes': 'UltralyticsModels/GrapesV1.pt',
    'Tomato': 'UltralyticsModels/TomatoV3.pt',
    'RND': 'UltralyticsModels/rnd_detect4.0.pt',
}

seg_model_paths = {
    'StrawberrySeg': 'UltralyticsModels/StrawberryV6.pt',
    'AppleSeg': 'UltralyticsModels/AppleV1.pt',
    'GrapesSeg': 'UltralyticsModels/GrapesV1.pt',
    'TomatoSeg': 'UltralyticsModels/TomatoV3.pt',
    'RND': 'UltralyticsModels/rnd_detect4.0.pt',
}


try:
    model_path = ''
    if option2 == 'Detection':
        model_path = model_paths.get(option, '')
    elif option2 == 'Segmentation':
        model_path = seg_model_paths.get(option + 'Seg', '')

    if option == 'Custom':
        uploaded_file = st.file_uploader("Upload your pretrained model", type=['pt'])
        if uploaded_file:
            model_path = uploaded_file.name
            with open(model_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            st.success("Custom model uploaded successfully.")
            try:
                model = YOLO(model_path)
            except Exception as e:
                st.error(f"Failed to load the custom model. Error: {e}")
    else:
        if model_path:
            model = YOLO(model_path)
        else:
            raise ValueError("Model path not found.")
except ValueError as e:
    st.warning(str(e))

# Single-Image upload and display
source_img = st.file_uploader("Choose an image file", type=['png', 'jpeg', 'jpg'])
if source_img:
    uploaded_image = Image.open(source_img).convert('RGB')
    np_image = np.array(uploaded_image)
    col1, col2 = st.columns(2)
    with col1:
        st.image(source_img, caption="Uploaded Image", use_column_width=True)

    if st.button('Detect Objects'):
        if option2 == 'Segmentation':
            results = model(np_image, conf=0.3, show_boxes=False)
            for result in results:
                annotated_image = result.plot(masks=True, labels=False)
                annotated_image = Image.fromarray(annotated_image[..., ::-1])
                with col2:
                    st.image(annotated_image, caption='Detected Image with Segmentation', use_column_width=True)
        else:
            results = model.predict(np_image, conf=0.3, show_conf=True)
            annotated_image = results[0].plot()
            annotated_image = Image.fromarray(annotated_image[..., ::-1])
            with col2:
                st.image(annotated_image, caption='Detected Image', use_column_width=True)

# Multi-image process and download
uploaded_files = st.file_uploader("Or upload multiple image files", accept_multiple_files=True, type=['png', 'jpeg', 'jpg'])
if uploaded_files and len(uploaded_files) > 1:
    if st.button('Process Multiple Images'):
        with tempfile.TemporaryDirectory() as temp_dir:
            zip_path = f"{temp_dir}/processed_images.zip"
            with ZipFile(zip_path, 'w') as zipf:
                for uploaded_file in uploaded_files:
                    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                    opencv_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                    results = model(opencv_image, conf=0.2)
                    for result in results:
                        if option2 == 'Detection':
                            annotated_image = result.plot(masks=False, labels=True, boxes=True)
                        elif option2 == 'Segmentation':
                            annotated_image = result.plot(masks=True, labels=False, boxes=False)
                        annotated_image = np.array(annotated_image)
                        annotated_image_bgr = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
                        temp_file_path = f"{temp_dir}/{uploaded_file.name}"
                        cv2.imwrite(temp_file_path, annotated_image_bgr)
                        zipf.write(temp_file_path, arcname=uploaded_file.name)
            with open(zip_path, "rb") as f:
                st.download_button(label="Download Processed Images", data=f, file_name="processed_images.zip")

# Video process and download
uploaded_video = st.file_uploader("Upload a video file", type=['mp4', 'avi'])
if uploaded_video is not None:
    if st.button('Process Video'):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
            temp_video_file.write(uploaded_video.read())
            video_path = temp_video_file.name
        _, output_video_path = tempfile.mkstemp(suffix=".mp4")
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))
        progress_bar = st.progress(0)
        for i in range(frame_count):
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame, device=1)
            for result in results:
                annotated_frame = result.plot()
                out.write(annotated_frame)
            progress_bar.progress((i + 1) / frame_count)
            time.sleep(0.5)  
        cap.release()
        out.release()
        with open(output_video_path, "rb") as file:
            st.download_button(label="Download Processed Video", data=file, mime="video/mp4")


st.subheader("Models")
st.write('Ultralytics is a framework that allows different computer vision tasks. We train our models with custom data on the YOLOv8 models.')
st.write('To see a full list of our avaiable models visit the Technology page.')
st.page_link("pages/Technology.py", label="Models",)
st.write('To learn more about Ultralytics visit the docs https://docs.ultralytics.com/.')


tab1, tab2, tab3 = st.tabs(["Strawberry", "Grapes", "Tomato"])

with tab1:
   st.caption("The Strawberry model is trained on 600 images for 100 epochs.")
   st.image("static/strawberry.jpg", width=400)

with tab2:
   st.caption("The Grapes model can detect Chardonnay, PinotGris and PinotNoir.")
   st.image("static/grapes.jpg", width=400)

with tab3:
   st.caption("Tomato model is trained on 300 images for 100 epochs. ")
   st.image("static/tomato.jpg", width=400)
