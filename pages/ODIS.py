import streamlit as st
import os
from datetime import datetime
from ultralytics import YOLO
import shutil
import base64
from PIL import Image
import numpy as np


st.title("Object Detection Image Sorting")

destination_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'filtered_images')

st.divider()
option = st.selectbox('Select a YOLOv8 model.', ('Detect4.0', '200cc'))
st.write('You selected:', option, "Model")

model_paths = {
    'Detect4.0': 'UltralyticsModels/rnd_detect4.0.pt',
    '0-999': 'UltralyticsModels/GrapesModel.pt',
}

folder_path = st.text_input("Enter the folder path for image prediction:")
number = st.text_input("Enter a number corresponding to the class for detection:")

try:
    model_path = model_paths.get(option, '')
    if not model_path:
        raise ValueError("Model path not found.")
    model = YOLO(model_path)
except Exception as e:
    st.error(f"Failed to load model. Error: {e}")
    st.stop()

if st.button("Run Image Prediction") and folder_path:
    num_list = ['1', '10', '100', '103', '104', '105', '106', '11', '111', '112', '113', '114', '115', '117', '118', '12', '121', '123', '126', '128', '13', '132', '133', '137', '14', '145', '147', '148', '15', '150', '151', '153', '159', '16', '160', '162', '164', '165', '166', '17', '171', '172', '174', '177', '178', '18', '180', '182', '184', '188', '189', '19', '191', '199', '2', '20', '202', '204', '209', '21', '210', '211', '215', '217', '22', '222', '225', '226', '227', '23', '231', '235', '237', '238', '24', '241', '243', '247', '25', '252', '257', '26', '266', '267', '27', '270', '272', '273', '275', '277', '28', '286', '287', '29', '290', '291', '295', '298', '299', '3', '30', '309', '31', '310', '311', '313', '315', '317', '318', '32', '323', '325', '33', '332', '338', '340', '341', '346', '348', '35', '355', '36', '37', '376', '378', '38', '39', '392', '394', '4', '40', '404', '41', '410', '411', '414', '42', '421', '427', '428', '43', '44', '445', '45', '46', '47', '474', '48', '480', '49', '5', '50', '504', '51', '514', '518', '521', '523', '53', '532', '547', '549', '55', '555', '557', '56', '57', '58', '585', '59', '599', '6', '609', '61', '612', '613', '616', '62', '622', '627', '65', '650', '66', '666', '673', '687', '69', '690', '7', '71', '710', '711', '72', '724', '725', '731', '74', '742', '768', '77', '775', '782', '789', '79', '8', '80', '81', '818', '82', '823', '826', '829', '83', '84', '85', '852', '86', '869', '875', '876', '877', '88', '89', '893', '9', '914', '915', '916', '94', '95', '952', '96', '97', '972', '99', '997', '999']
    if os.path.exists(folder_path) and os.path.isdir(folder_path) and number in num_list:
        class_name = num_list.index(number)
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
                results = model(image_path, conf=0.01)
                boxes = results[0].boxes
                for box in boxes:
                    if int(box.cls) == class_name:
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
        st.error("Invalid input. Please enter a valid folder path and number.")
else:
    st.warning("Please enter a folder path and a valid number.")

st.header("About the Service")
st.write("""
    Our Object Detection Service is powered by YOLOv8 computer vision models
    to provide accurate detection and classification of objects within images.
    Simply upload your images, and let the app filter the class you need.
""")

st.write("© 2023 Object Detection Image Sorting. All rights reserved.")
