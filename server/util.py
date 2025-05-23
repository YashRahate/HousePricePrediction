
import json
import pickle
import numpy as np

#global variables
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
        
    x = np.zeros(len(__data_columns))
    
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >=0:
        x[loc_index] = 1
        
    return round(__model.predict([x])[0],2)

    
def get_location_names():
    load_saves_artifacts()
    return __locations

def load_saves_artifacts():
    print("Loading the saved artifacts...")
    global __data_columns
    global __locations
    global __model
    with open("./artifacts/columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    with open("./artifacts/HousePredictionModel.pickle","rb") as f :
        __model = pickle.load(f)
    print("Loading Completed !!!")
    
if __name__ == '__main__':
    load_saves_artifacts()
    # print(get_location_names())
    # print(get_estimated_price('8th phase jp nagar',1000,2,2))
    # print(get_estimated_price('thane',1222,2,2))
    # print(get_estimated_price('mulund',1222,2,2))