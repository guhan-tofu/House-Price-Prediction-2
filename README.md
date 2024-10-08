# House-Price-Prediction-2
![ScreenRecording2024-10-10175337-ezgif com-video-to-gif-converter (2)](https://github.com/user-attachments/assets/29b61be7-b946-4a3c-82c6-407d7b4c7217)

![image](https://github.com/user-attachments/assets/4629de41-edf5-4c1e-99d4-b66b45b43a2d)


https://github.com/guhan-tofu/House-Price-Prediction-2/blob/main/Screen%20Recording%202024-10-10%20175337.mp4

## Overview

This project combines a machine learning model with a simple web app interface. It allows users to input details of a property, such as the number of bedrooms, bathrooms, square footage, and location, and provides a predicted house price using the pre-trained model.

### Key Features:
- **Data Preprocessing:** Data is cleaned and transformed before feeding into the model.
- **Model Training:** The model is trained on a dataset of house prices in Bengaluru.
- **Web Application:** A frontend interface where users can input house features and get predictions in real-time.

## How It Works

1. **Frontend (Client):** 
   - The `client/` folder contains the HTML, CSS, and JavaScript files that make up the user interface. Users can input house features such as the area, number of bedrooms, and bathrooms.
   
2. **Backend (Server):**
   - The `server/` folder contains the Python Flask server that loads the machine learning model and handles prediction requests. 
   - It uses `columns.json` to map input fields to the correct format and `pipeline.pickle` to preprocess input data and `model.pickle` to load the pre-trained machine learning model.

3. **Machine Learning:**
   - The Jupyter notebook `Bengaluru_House.ipynb` contains the steps for data exploration, model training, and evaluation. The trained model is then serialized into `model.pickle`.

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
- Scikit-learn
- Pandas
- Numpy

You can install the required dependencies using:

```bash
pip install -r requirements.txt




