Face Detection Web Application
The Face Detection Web Application is a web-based application built using FastAPI and OpenCV. It allows users to detect faces and smiles in real-time using the device camera.

Table of Contents
Introduction
Installation
Usage
API Endpoints
ML Module
Templates
Dependencies
Contributing
License
Introduction
The Face Detection Web Application leverages FastAPI, a modern, fast (high-performance), web framework for building APIs with Python. It uses OpenCV, a popular computer vision library, to perform real-time face and smile detection. The application provides a user-friendly interface for capturing images using the device camera and detecting faces and smiles.

Installation
To install and run the Face Detection Web Application, follow these steps:

Clone the repository:

bash
Copy code
git clone <repository-url>
Navigate to the project directory:

bash
Copy code
cd FaceDetectionWebApp
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate  # On Windows
Install the required dependencies:

Copy code
pip install -r requirements.txt
Start the application:

css
Copy code
uvicorn main:app --reload
Open a web browser and visit http://localhost:8000 to access the Face Detection Web Application.

Usage
Once the application is running, you can use the following steps to detect faces and smiles:

Open the web browser and access the application at http://localhost:8000.

The home page will be displayed, showing a "Camera" link. Click on the link to access the camera view.

The camera view will open, and the application will start detecting faces and smiles in real-time. If a smile is detected, the text "Beautiful" will be displayed; otherwise, the text "Smile:)" will be shown.

You can click on the "Go Back" link to return to the home page and restart the process.

API Endpoints
The Face Detection Web Application provides the following API endpoints:

GET /: Renders the home page of the application.
GET /camera: Starts the face detection process using the device camera.
GET /favicon.ico: Endpoint for serving the favicon (excluded from API documentation).
ML Module
The ML module used in the Face Detection Web Application is responsible for performing the face and smile detection. It utilizes the following components from the OpenCV library:

cv2.VideoCapture: This class is used to capture video frames from the device camera.
cv2.CascadeClassifier: This class implements the Haar cascade-based face and smile detection algorithms.
The FaceDetect class within the ML module provides the start_detect method, which initiates the face detection process using the device camera.

Templates
The Face Detection Web Application uses two HTML templates to render the user interface:

index.html: This template is displayed as the home page and provides a link to access the camera view.
smile-detected.html: This template is shown when a smile is detected, displaying a message indicating a beautiful smile.
Dependencies
The Face Detection Web Application relies on the following external dependencies:

FastAPI: A modern,
