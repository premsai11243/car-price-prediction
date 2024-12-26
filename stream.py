import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved models and encoders
column_label = joblib.load("D:/Desktop/car price prediction/structured files/encoders")  # LabelEncoders
model = joblib.load("D:/Desktop/car price prediction/structured files/predicted_price.sav")  # Trained model
scaler = joblib.load("D:/Desktop/car price prediction/structured files/MinMax.sav")  # MinMaxScaler

# Define columns expected by the model
columns = ['Fuel Type', 'bt', 'transmission', 'ownerNo', 'modelYear', 'Gear Box', 'Kms Driven', 'Mileage', 'city']


def encode_data(data):
    """
    Encode categorical features using the loaded LabelEncoders.
    Handles unseen labels by assigning a default value or skipping.
    """
    for col in column_label:  # Iterate over saved LabelEncoders
        if col in data.columns:
            try:
                # Transform data if label exists
                data[col] = column_label[col].transform(data[col])
            except ValueError as e:
                # Handle unseen labels
                st.warning(f"Unseen labels in column '{col}': {data[col].values}")
                #data[col] = -1  # Assign a default category for unseen labels
    return data



def preprocess_data(new_data):
    """
    Preprocess user input: Convert to DataFrame, encode, and scale.
    """
    # Create DataFrame with user input
    input_df = pd.DataFrame([new_data], columns=columns)

    # Encode categorical columns
    input_encoded = encode_data(input_df)

    # Scale numerical columns
    input_scaled = scaler.transform(input_encoded)
    return input_scaled


def predict_price(new_data):
    """
    Predict car price using the trained model.
    """
    try:
        processed_data = preprocess_data(new_data)
        prediction = model.predict(processed_data)
        return f"Predicted price: ₹{prediction[0]:,.2f}",processed_data # Format the prediction
    except Exception as e:
        return f"Error in prediction: {e}"


def main():
    st.title("Car Price Prediction")
    st.write("Fill in the car details to predict the price:")

    # Sidebar input widgets
    Fueltype = st.sidebar.selectbox("Fuel Type", ['Select', 'Petrol', 'Diesel', 'LPG', 'Electric']) 
    bodytype = st.sidebar.selectbox("Body Type", ['Select', 'Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 'Minivans', 'Pickup Trucks', 'Convertibles', 'Wagon'])
    transmission = st.sidebar.selectbox("Transmission", ['Select', 'Automatic', 'Manual'])
    owner = st.sidebar.number_input("Owner No", min_value=1, max_value=5, value=1, step=1)
    modelYear = st.sidebar.number_input("Model Year", min_value=1985, max_value=2023, value=2010, step=1)
    GearBox = st.sidebar.number_input("Gear Box", min_value=1, max_value=10, value=4, step=1)
    KmsDriven = st.sidebar.number_input("Kms Driven", min_value=1, max_value=975000, value=10000, step=500)
    Mileage = st.sidebar.number_input("Mileage", min_value=1, max_value=140, value=15, step=1)
    city = st.sidebar.selectbox("City", ['Select', 'Bangalore', 'chennai', 'delhi', 'hyderabad', 'jaipur', 'kolkata'])
    
    if st.button('Predict Price'):
        
        # Check for invalid selections
        if Fueltype == 'Select' or bodytype == 'Select' or transmission == 'Select' or city == 'Select':
            st.warning("Please select all fields correctly.")
        else:
            # Prepare input data
            new_data = [Fueltype, bodytype, transmission, owner, modelYear, GearBox, KmsDriven, Mileage, city]
            
            # Make prediction
            result , inp = predict_price(new_data)
            st.write(inp)
            st.success(result)


if __name__ == "__main__":
    main()
