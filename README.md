Fracture Detection Using YOLO
![Fracture Detection - Google Chrome 27-05-2024 15_26_34](https://github.com/pramothkumarm/Fracture-Detection/assets/93421622/3d0cfc26-e5c1-437b-a10e-11404ae0937f)

# Bone Fracture Detection Using YOLO

## Overview
Welcome to the Bone Fracture Detection project! This project utilizes the YOLO (You Only Look Once) object detection algorithm to identify and localize fractures in medical images. The primary aim is to assist radiologists and medical professionals in accurately and efficiently detecting fractures, enhancing diagnosis and treatment.

---

## Features
- **Fracture Detection:** Identifies and localizes fractures in X-ray images using the YOLO algorithm.
- **User-Friendly Interface:** Integrated UI design allows users to upload images and view detection results.
- **Real-Time Processing:** Provides quick and accurate fracture detection, making it suitable for clinical use.
- **Model Accuracy:** Trained on a comprehensive dataset to ensure high detection accuracy.

---

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Machine Learning:** YOLOv5, OpenCV
- **Database:** SQL/NoSQL (e.g., MySQL, MongoDB)
- **Visualization:** Matplotlib, Seaborn

---

## Prerequisites
### Hardware
- A computer capable of running Python applications.

### Software
- Python (3.7 or above)
- Required libraries (specified in `requirements.txt`):
  - `Flask`
  - `torch`
  - `opencv-python`
  - `numpy`
  - `Pillow`

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/bone-fracture-detection.git
   cd bone-fracture-detection
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the `data.yaml` file with your dataset paths.
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Access the application in your browser at `http://127.0.0.1:5000`.

---

## Dataset
- The project uses annotated X-ray images stored in the dataset specified in the `data.yaml` file.
- Ensure the dataset is properly labeled and preprocessed for YOLO training and inference.

---

## How It Works
1. **Upload X-ray Images:**
   - Users upload X-ray images through the web interface.
2. **YOLO Inference:**
   - The uploaded image is processed using the YOLOv5 model to detect fractures.
3. **Visualization:**
   - Detected fractures are highlighted with bounding boxes in the output image.
4. **Results Display:**
   - The system displays the processed image along with detection details.

---

## Directory Structure
```
.
├── app.py                  # Flask application entry point
├── data.yaml               # YOLO dataset configuration file
├── Fracture Detection Using YOLO # Documentation
├── requirements.txt        # Dependencies
├── templates/              # HTML templates for the web interface
├── static/                 # Static files (CSS, JS, images)
├── README.md               # Project documentation
└── dataset/                # X-ray images and annotations
```

---

## Future Enhancements
- Integration with advanced deep learning models for improved accuracy.
- Deployment on cloud platforms for scalable real-time detection.
- Support for multiple types of medical imaging (e.g., CT, MRI).
- Adding a database for storing user-uploaded images and results.

---

## Contributors
- [PRAMOTH KUMAR](https://github.com/pramothkumarm)

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

