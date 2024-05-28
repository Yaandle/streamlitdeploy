import streamlit as st
import os
from datetime import datetime
from ultralytics import YOLO
import shutil
import base64
from PIL import Image
import numpy as np

st.set_page_config(page_title="Object Detection Image Sorting", layout="wide")

st.title("Object Detection Image Sorting")
st.header("Instructions")
with st.expander("How to use this app"):
    st.write("1. Select a YOLOv model from the dropdown.")
    st.write("2. Enter the folder path containing the images you want to process.")
    st.write("3. Enter the class name you want to filter for.")
    st.write("4. Click the 'Run Image Prediction' button.")
    st.write("5. The filtered images will be downloaded as a ZIP file.")

destination_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'filtered_images')

st.divider()

col1, col2 = st.columns(2)

with col1:
    option = st.selectbox('Select a YOLOv8 model:', ('Detect4.0', 'Fruits', 'Rider NF4'))
    st.write('You selected:', option, "Model")

model_paths = {
    'Detect4.0': 'UltralyticsModels/rnd_detect4.0.pt',
    'Fruits': 'UltralyticsModels/rnd_detect4.0.pt',
    'Rider NF4': 'UltralyticsModels/RiderNF4.pt',
}

class_lists = {
    'Detect4.0': [
        'class_1', 
        'class_2', 
        'class_3'
    ],  
    'Fruits': [
        'apple', 'strawberry', 'grapes', 
    ],
    'Rider NF4': [
        '2', '5', '10', '15', '17', '20', '22', '25', '31', '43', '44', '46', '49',
        '88', '89', '99', '100', '103', '105', '111', '112', '113', '117', '122',
        '126', '145', '150', '151', '159', '162', '165', '201', '202', '207', '210',
        '216', '700', '883', '999'
],  
}


with col2:
    class_list = class_lists[option]
    st.write("Class List:")
    st.write("\n".join(class_list))

folder_path = st.text_input("Enter the folder path for image prediction:")
class_name = st.text_input("Enter the class name you want to find:")

try:
    model_path = model_paths.get(option, '')
    if not model_path:
        raise ValueError("Model path not found.")
    model = YOLO(model_path)
except Exception as e:
    st.error(f"Failed to load model. Error: {e}")
    st.stop()

if st.button("Run Image Prediction") and folder_path:
    if class_name not in class_list:
        st.error("Invalid class name. Please enter a valid class name from the class list.")
    elif not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        st.error("Invalid folder path. Please enter a valid folder path.")
    else:
        class_index = class_list.index(class_name)
        filtered_images = []
        results_dir = os.path.join(os.path.dirname(folder_path), 'results')
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        destination_dir = os.path.join(results_dir, 'filtered_images')
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        else:
            shutil.rmtree(destination_dir)
            os.makedirs(destination_dir)

        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            if os.path.exists(image_path):
                results = model(image_path, conf=0.6)
                boxes = results[0].boxes
                for box in boxes:
                    if int(box.cls) == class_index:
                        filtered_images.append(image_name)
                        shutil.move(image_path, os.path.join(destination_dir, image_name))
                        break

        if filtered_images:
            st.success(f"Object detection completed. {len(filtered_images)} images were filtered and saved to the output folder.")
            zip_output_path = os.path.join(results_dir, 'filtered_images')
            shutil.make_archive(zip_output_path, 'zip', destination_dir)

            with open(zip_output_path + '.zip', "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
                href = f'<a href="data:file/zip;base64,{b64}" download="{os.path.basename(zip_output_path)}.zip">Download Filtered Images</a>'
                st.markdown(href, unsafe_allow_html=True)
        else:
            st.error("No images matched the specified class.")
else:
    st.warning("Please enter a folder path and a valid class name.")

st.divider()

