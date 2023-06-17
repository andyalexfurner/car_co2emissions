# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import pickle 
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('/Users/aniketmare/Work/Car_CO2_emissions/trained_model.sav', 'rb'))

# prediction functions

def prediction(input_data):

    # changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    
    #print(prediction)
    return "Co2 Emission:", int(prediction)
    
def main():
    
    #title
    st.title('Co2 Emissions Prediction')
    
    #taking input 
    Enginesize = st.number_input('Engine Size')
    Cylinders = st.number_input('Cylinders')
    Fuelconsumption = st.number_input('Fuel Consumption')
    
    #prediction
    emission = ''
    
    #button 
    if st.button("CO2 Emissions"):
        emission = prediction([Enginesize, Cylinders, Fuelconsumption])
    
    st.success(emission)
    
    
if __name__ == '__main__':
    main()