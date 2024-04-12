import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1
    z = np.zeros(len(__data_columns))
    z[0] = sqft
    z[1] = bath
    z[2] = bhk
    if loc_index >= 0:
        z[loc_index] = 1
    return round(__model.predict([z])[0],2)


def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json", "rb") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    if __model is None:
        with open("./artifacts/Bangalore_house_prediction.pickle", "rb") as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_all_locations():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_all_locations())
    # print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    # #print(get_estimated_price('5th Block Hbr Layout',1000,2,2))
    # print(get_estimated_price('Yelahanka New Town',1000,2,2))
    # print(get_estimated_price('Whitefield',1000,2,2))
    #
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('kalahalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))

