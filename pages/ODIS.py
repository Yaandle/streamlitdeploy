import streamlit as st
import os
from datetime import datetime
from ultralytics import YOLO
import shutil
import base64
import zipfile

st.set_page_config(page_title="Object Detection Image Sorting", layout="wide")

st.title("Object Detection Image Sorting")
st.header("Instructions")
with st.expander("How to use this app"):
    st.write("1. Select a YOLOv model from the dropdown.")
    st.write("2. Enter the folder path containing the images you want to process.")
    st.write("3. Click the 'Run Image Prediction' button.")
    st.write("4. The images will be sorted into separate folders based on the detected classes.")
    st.write("5. A ZIP file containing all the class folders will be downloaded.")

destination_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'filtered_images')

st.divider()

col1, col2 = st.columns(2)
model_paths = {
    'AppleV1': 'UltralyticsModels/AppleV1.pt',
    'Strawberry': 'UltralyticsModels/Strawberry V8.pt',
    'Grapes': 'UltralyticsModels/GrapesV1.pt',
    'Rider NF2': 'UltralyticsModels/rnd_detect4.0.pt',
    'Rider NF4': 'UltralyticsModels/RiderNF4.pt',
}

with col1:
    option = st.selectbox('Select a YOLOv8 model:', list(model_paths.keys()))
    st.write('You selected:', option, "Model")

class_lists = {
    'AppleV1': ['appleRED', 'appleGreen', 'tree_stem'],
    'Strawberry': ['strawberryR', 'strawberryNR', 'stem'],
    'Grapes': ['PinotNoir', 'PinotGris', 'Chardonnay', 'Stem'],
    'Rider NF2': [
    '1', '10', '100', '103', '104', '105', '106', '11', '111', '112',
    '113', '114', '115', '117', '118', '12', '121', '123', '126', '128',
    '13', '132', '133', '137', '14', '145', '147', '148', '15', '150',
    '151', '153', '159', '16', '160', '162', '164', '165', '166', '17',
    '171', '172', '174', '177', '178', '18', '180', '182', '184', '188',
    '189', '19', '191', '199', '2', '20', '202', '204', '209', '21', '210',
    '211', '215', '217', '22', '222', '225', '226', '227', '23', '231',
    '235', '237', '238', '24', '241', '243', '247', '25', '252', '257',
    '26', '266', '267', '27', '270', '272', '273', '275', '277', '28',
    '286', '287', '29', '290', '291', '295', '298', '299', '3', '30',
    '309', '31', '310', '311', '313', '315', '317', '318', '32', '323',
    '325', '33', '332', '338', '340', '341', '346', '348', '35', '355',
    '36', '37', '376', '378', '38', '39', '392', '394', '4', '40', '404',
    '41', '410', '411', '414', '42', '421', '427', '428', '43', '44',
    '445', '45', '46', '47', '474', '48', '480', '49', '5', '50', '504',
    '51', '514', '518', '521', '523', '53', '532', '547', '549', '55',
    '555', '557', '56', '57', '58', '585', '59', '599', '6', '609', '61',
    '612', '613', '616', '62', '622', '627', '65', '650', '66', '666',
    '673', '687', '69', '690', '7', '71', '710', '711', '72', '724',
    '725', '731', '74', '742', '768', '77', '775', '782', '789', '79',
    '8', '80', '81', '818', '82', '823', '826', '829', '83', '84', '85',
    '852', '86', '869', '875', '876', '877', '88', '89', '893', '9', '914',
    '915', '916', '94', '95', '952', '96', '97', '972', '99', '997', '999'
    ],
    
    'Rider NF4': [
        '10', '100', '103', '105', '111', '112', '113', '117', '122', '126',
        '145', '15', '150', '151', '159', '162', '165', '17', '2', '20',
        '201', '202', '207', '210', '216', '22', '25', '28', '290', '31',
        '428', '43', '44', '46', '49', '5', '514', '700', '88', '883', '89',
        '99', '999'
    ],
}

with col2:
    class_list = class_lists[option]
    st.write("Class List:")
    st.write("\n".join(class_list))

folder_path = st.text_input("Enter the folder path for image prediction:")

try:
    model_path = model_paths.get(option, '')
    if not model_path:
        raise ValueError("Model path not found.")
    model = YOLO(model_path)
except Exception as e:
    st.error(f"Failed to load model. Error: {e}")
    st.stop()

if st.button("Run Image Prediction") and folder_path:
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        st.error("Invalid folder path. Please enter a valid folder path.")
    else:
        results_dir = os.path.join(os.path.dirname(folder_path), 'results')
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        zip_output_path = os.path.join(results_dir, 'filtered_images.zip')

        with zipfile.ZipFile(zip_output_path, 'w') as zip_file:
            for image_name in os.listdir(folder_path):
                image_path = os.path.join(folder_path, image_name)
                if os.path.isfile(image_path):
                    results = model(image_path, conf=0.8)
                    boxes = results[0].boxes
                    for box in boxes:
                        if 0 <= int(box.cls) < len(class_list):
                            class_name = class_list[int(box.cls)]
                            zip_file.write(image_path, os.path.join(class_name, image_name))
                        else:
                            st.warning(f"Detected class index {int(box.cls)} is out of range.")

        st.success(f"Object detection completed. Images have been sorted into class folders and a ZIP file has been created.")

        with open(zip_output_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            href = f'<a href="data:file/zip;base64,{b64}" download="{os.path.basename(zip_output_path)}">Download Sorted Images</a>'
            st.markdown(href, unsafe_allow_html=True)
else:
    st.warning("Please enter a folder path and click the 'Run Image Prediction' button.")

st.divider()