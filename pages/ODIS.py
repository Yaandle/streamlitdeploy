import streamlit as st
import os
from datetime import datetime
from ultralytics import YOLO
import shutil
import zipfile
import cv2
from pathlib import Path
import tempfile
import traceback

st.set_page_config(page_title="Object Detection Image Sorting", layout="wide")

st.title("Object Detection Image Sorting")
st.header("Instructions")
with st.expander("How to use this app"):
    st.write("1. Select a YOLOv model from the dropdown.")
    st.write("2. Upload a ZIP file containing the images you want to process.")
    st.write("3. Click the 'Run Image Prediction' button.")
    st.write("4. The images will be sorted into separate folders based on the detected classes.")
    st.write("5. A ZIP file containing all the class folders will be available for download.")

st.divider()

col1, col2 = st.columns(2)
model_paths = {
    'Apple': 'UltralyticsModels/Applev5.pt',
    'Strawberry': 'UltralyticsModels/StrawberryV9.pt',
    'Grapes': 'UltralyticsModels/GrapesV1.pt',
    'Rider NF7': 'UltralyticsModels/rnf7.pt',
    'YOLOv10': 'UltralyticsModels/yolov10m.pt',
}

with col1:
    option = st.selectbox('Select a YOLO model:', list(model_paths.keys()))
    st.write('You selected:', option, "Model")

uploaded_zip = st.file_uploader("Upload a ZIP file containing images (max 1GB)", type=["zip"])

@st.cache_resource
def load_model(model_path):
    return YOLO(model_path)

def get_image_files(directory):
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}
    return [f for f in Path(directory).rglob('*') if f.suffix.lower() in image_extensions]

def process_image_odis(image_path, model):
    try:
        opencv_image = cv2.imread(str(image_path))
        if opencv_image is None:
            return None, f"Failed to read image: {image_path}"

        results = model(opencv_image, conf=0.4)
        classes_detected = set()

        for result in results:
            for box in result.boxes:
                class_name = model.names[int(box.cls)]
                classes_detected.add(class_name)

        return list(classes_detected) if classes_detected else ["No_Detections"], None
    except Exception as e:
        return None, f"Error processing image {image_path}: {str(e)}\n{traceback.format_exc()}"

if uploaded_zip is not None:
    with tempfile.TemporaryDirectory() as temp_dir:
        with st.spinner("Extracting ZIP file..."):
            with zipfile.ZipFile(uploaded_zip, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
            image_files = get_image_files(temp_dir)
            if not image_files:
                st.error("No image files found in the extracted directory. Please check the ZIP file contents.")
                st.stop()
            st.success(f"ZIP file extracted successfully. Found {len(image_files)} image files.")

        if st.button("Run Image Prediction"):
            try:
                model_path = model_paths.get(option, '')
                if not model_path:
                    raise ValueError("Model path not found.")
                model = load_model(model_path)
            except Exception as e:
                st.error(f"Failed to load model. Error: {e}")
                st.stop()

            progress_bar = st.progress(0)
            status_text = st.empty()

            all_detected_classes = set()
            failed_files = []
            image_classifications = {}

            # Process images
            total_images = len(image_files)
            for i, image_path in enumerate(image_files):
                result, error_message = process_image_odis(image_path, model)

                if result:
                    all_detected_classes.update(result)
                    image_classifications[image_path] = result
                else:
                    failed_files.append((image_path, error_message))
                    image_classifications[image_path] = ["Failed_Processing"]
                    all_detected_classes.add("Failed_Processing")

                progress_bar.progress((i + 1) / total_images)
                status_text.text(f"Processing image {i+1} of {total_images}")

            # Create output ZIP file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_zip:
                with zipfile.ZipFile(temp_zip.name, 'w') as zip_file:
                    for image_path, classes in image_classifications.items():
                        for class_name in classes:
                            zip_path = f"{class_name}/{image_path.name}"
                            zip_file.write(image_path, zip_path)

                st.success(f"Object detection completed. All {total_images} images have been processed and sorted into class folders.")

                st.write("Detected classes:", list(all_detected_classes))
                if failed_files:
                    st.warning(f"Failed to process {len(failed_files)} files:")
                    for failed_file, error_message in failed_files:
                        st.write(f"- {failed_file.name}: {error_message}")

                with open(temp_zip.name, "rb") as f:
                    st.download_button(
                        label="Download Filtered Images",
                        data=f.read(),
                        file_name="filtered_images.zip",
                        mime="application/zip"
                    )

            # Clean up the temporary zip file
            os.unlink(temp_zip.name)
