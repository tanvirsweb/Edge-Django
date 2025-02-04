# Django Object Detection Web App

## Overview
This is a Django-based web application for object detection using a pre-trained deep learning model. Users can upload an image, and the system will process it to detect objects using OpenCV and TensorFlow.
<br>
Coder: [Tanvir Anjom Siddique](https://www.linkedin.com/in/tanvir-anjom-siddique-50028a205/)
## Features
- Upload images for object detection
- Process images using a pre-trained model (SSD MobileNet v3)
- Can detect 80 types of objects
- Display detected objects with number of occurance and processed images with bounding boxes
- Bootstrap-based UI for a responsive experience

## Live Demo: Running YOLO v3 in a Django Web App
<iframe width="560" height="315" src="https://www.youtube.com/embed/PAmmYIlerAg?si=mISFB0-PKwrjWLZ9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[![Watch the video](https://img.youtube.com/vi/PAmmYIlerAg/maxresdefault.jpg)](https://www.youtube.com/watch?v=PAmmYIlerAg)

## Project Structure
```
ObjectDetection/                # Django Project Root
│── detection/                  # Django App
│   ├── migrations/             # Django Database Migrations
│   ├── static/                 # Static Files (CSS, JS)
│   ├── templates/              # HTML Templates
│   │   ├── detection/          # App-specific templates
│   │   │   ├── index.html      # Main UI Template
│   ├── __init__.py             # App Init File
│   ├── admin.py                # Django Admin Config (Optional)
│   ├── apps.py                 # App Configuration
│   ├── models.py               # Database Models (Not Needed Here)
│   ├── tests.py                # Unit Tests (Optional)
│   ├── urls.py                 # App URLs
│   ├── utils.py                # Object Detection Logic (cv2 model)
│   ├── views.py                # App Views
│── staticfiles/                # Stores Static Files
│   ├── img/                    # Stores Uploaded and Processed Images
│   │   ├── img.jpeg            # Uploaded Image
│   │   ├── img_out.jpeg        # Processed Image with Bounding Boxes
│   ├── css/                    # Stores Static Assets (CSS, JS)
│   │   ├── bootstrap.min.css   # Bootstrap CSS (Optional)
│── ObjectDetection/            # Main Django Project Folder
│   ├── __init__.py             # Project Init File
│   ├── asgi.py                 # ASGI Config (For Deployments)
│   ├── settings.py             # Project Settings
│   ├── urls.py                 # Root URLs
│   ├── wsgi.py                 # WSGI Config (For Deployments)
│── manage.py                   # Django Management Script
│── coconames.txt               # COCO Class Labels
│── frozen_inference_graph.pb   # Pretrained Model Weights
│── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt  # Model Config
│── requirements.txt            # Dependencies (Optional)

```

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/tanvirsweb/Object-Detection-Website-using-Django-YoloV3.git
cd ObjectDetectionWebsite
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Run the Server
```sh
python manage.py runserver
```
Open your browser and go to `http://127.0.0.1:8000/`

## Usage
1. Upload an image via the web interface.
2. The image will be processed using the SSD MobileNet model.
3. Detected objects and the processed image will be displayed.

## Model Details
- **Model:** SSD MobileNet V3
- **Configuration File:** `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`
- **Weights:** `frozen_inference_graph.pb`
- **Labels:** `coconames.txt`

## Troubleshooting
- If static files are not loading, run:
  ```sh
  python manage.py collectstatic
  ```
- Ensure `media/` and `uploads/` folders have write permissions.
- If `NoReverseMatch` error occurs, check `urls.py` for correct view names.

## License
This project is licensed under the MIT License.

