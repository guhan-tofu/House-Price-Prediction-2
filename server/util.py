import pandas as pd
import numpy as np
import json
import pickle

__model = None
__locations = None
__data_columns = None
__pipeline = None




def load_saved_artifacts():
    print('load saved artifacts....start')
    global __data_columns
    global __locations
    global __pipeline
    global __model

    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]

    with open('./artifacts/banglore_home_prices_model.pickle','rb') as f:
        __model = pickle.load(f)
    
    with open('./artifacts/pipeline.pickle','rb') as f:
        __pipeline = pickle.load(f)
    print('load saved artifacts....end')



def get_estimated_price(location,sqft,bath,bhk,balcony):
    input_data = {
    'location': location,
    'total_sqft': sqft,
    'bath': bath,
    'balcony': balcony,
    'bhk': bhk}

    df_input = pd.DataFrame([input_data], columns=['location', 'total_sqft', 'bath', 'balcony', 'bhk'])

    preprocessed_data = __pipeline.transform(df_input)
    prediction = __model.predict(preprocessed_data)
    prediction = np.exp(prediction)

    return round(prediction[0], 2)

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns



if __name__ == '__main__':
    load_saved_artifacts()
    print(get_estimated_price('Bellandur',1500,2.0,2.0,1.0))