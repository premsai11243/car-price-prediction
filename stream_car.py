import streamlit as st
import pandas as pd
import numpy as np
import joblib

load_saved = joblib.load('D:/Desktop/car price prediction/structured files/predicted_price.sav')

def encode_data(data):
    
    data_encoded = pd.get_dummies(data, drop_first=True)
    return data_encoded

def prediting(new_data):
    
    new_data_df = pd.DataFrame([new_data], columns=[
        'Fueltype', 'bodytype', 'transmission', 'owner', 'modelYear', 
        'GearBox', 'KmsDriven', 'Mileage', 'cityname'
    ])
    
    
    new_data_encoded = encode_data(new_data_df)
    
   
    missing_cols = set(load_saved.feature_names_in_) - set(new_data_encoded.columns)
    for col in missing_cols:
        new_data_encoded[col] = 0
    new_data_encoded = new_data_encoded[load_saved.feature_names_in_]
    
    
    predd = load_saved.predict(new_data_encoded)
    return f"Predicted price: {predd[0]}"


def main():
    st.title("Car Price Prediction")
    
    
    Fueltype = st.sidebar.selectbox("Fueltype", ['Select', 'petrol', 'Diesel', 'LPG', 'Electric']) 
    bodytype = st.sidebar.selectbox("Body Type", ['Select', 'Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 'Minivans', 'Pickup Trucks', 'Convertibles', 'Wagon'])
    transmission = st.sidebar.selectbox("Transmission", ['Select', 'Automatic', 'Manual'])
    owner_numbers = [1, 2, 3, 4, 5]
    owner = st.sidebar.selectbox("Owner Number", owner_numbers)
    years = [i for i in range(1985, 2024)]
    modelYear = st.sidebar.selectbox("Model Year", years)
    GearBox = st.sidebar.number_input("Gearbox", min_value=1, max_value=10, value=1, step=1)
    KmsDriven = st.sidebar.number_input("Kilometers Driven", min_value=1, max_value=975000, value=100, step=500)
    Mileage = st.sidebar.number_input("Mileage", min_value=1, max_value=140, value=5, step=5)
    cityname = st.sidebar.selectbox("Select a City", ['Select', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Jaipur', 'Kolkata'])
    
    if st.button('Evaluate the price'):
       
        if Fueltype == 'Select' or bodytype == 'Select' or transmission == 'Select' or cityname == 'Select':
            st.warning("Please select all the necessary fields.")
        else:
            
            new_data = [
                Fueltype, bodytype, transmission, owner, modelYear,
                GearBox, KmsDriven, Mileage, cityname
            ]
            
            # Get prediction
            pred = prediting(new_data)
            
            # Show the predicted price
            st.success(pred)

if __name__ == "__main__":
    main()
