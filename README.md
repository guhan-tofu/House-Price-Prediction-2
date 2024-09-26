# House-Price-Prediction-2
![image](https://github.com/user-attachments/assets/401459c3-9dd4-48e7-a3a5-417263e61691)



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




