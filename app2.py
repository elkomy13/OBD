import numpy as np
import pandas as pd
from joblib import load
import streamlit as st

# Load the model and scaler
try:
    model = load('test_model.joblib')
    scaler_test = load('C:/Users/adham.hany/Desktop/OBD/scaler_test.joblib')
except Exception as e:
    st.error(f"Error loading model or scaler: {e}")

# st.write(scaler_test)

# Define the feature columns
columns_to_exclude = ['VEHICLE_ID', 'TIME',"x","y","z"]

columns_to_scale = [
  'AIR_INTAKE_TEMP', 'ALTITUDE', 'AMBIENT_AIR_TEMP',
       'BAROMETRIC_PRESSURE', 'DTC_NUMBER', 'ENGINE_COOLANT_TEMP',
       'ENGINE_LOAD', 'ENGINE_RPM', 'EQUIV_RATIO', 'FUEL_LEVEL',
       'INTAKE_MANIFOLD_PRESSURE', 'MAF', 'MIN', 'SPEED',
       'Short Term Fuel Trim Bank 1', 'THROTTLE_POS', 'TIMING_ADVANCE',
       'TROUBLE_CODES', 'Total_Engine_Seconds'
]

columns_to = [
'TIME', 'ALTITUDE', 'VEHICLE_ID', 'BAROMETRIC_PRESSURE',
       'ENGINE_COOLANT_TEMP', 'FUEL_LEVEL', 'ENGINE_LOAD', 'AMBIENT_AIR_TEMP',
       'ENGINE_RPM', 'INTAKE_MANIFOLD_PRESSURE', 'MAF', 'AIR_INTAKE_TEMP',
       'SPEED', 'Short Term Fuel Trim Bank 1', 'THROTTLE_POS', 'DTC_NUMBER',
       'TROUBLE_CODES', 'TIMING_ADVANCE', 'EQUIV_RATIO',
       'Total_Engine_Seconds', 'MIN', 'x', 'y', 'z'
]

# Title for the Streamlit app
st.title("Feature Input Form")

# Create input fields for each feature
input_data = {}
for feature in columns_to:
    input_data[feature] = st.number_input(feature, format="%.6f")

# Add a button to make predictions
if st.button('Predict'):
    try:
        # Create DataFrame from input data
        input_df = pd.DataFrame([input_data])
        
        # Check that the columns are in the same order as the scaler expects
        input_df = input_df[columns_to]
        
        # Separate non-scaled and scaled columns
        input_df_non_scaled = input_df[columns_to_exclude]
        input_df_scaled = input_df[columns_to_scale]
        
        # Display DataFrames
        st.write("DataFrame with Non-Scaled and Scaled Columns Separately:")
        st.write("Non-Scaled DataFrame:")
        st.write(input_df_non_scaled)
        
        st.write("Scaled DataFrame:")
        st.write(input_df_scaled)
        
        # Scale the input data
        input_df_scaled = scaler_test.transform(input_df_scaled)
        
        # Replace scaled columns in the original DataFrame
        input_df[columns_to_scale] = input_df_scaled

        
        # Print the combined DataFrame
        st.write("Combined DataFrame (Ordered and Scaled):")
        st.write(input_df)
    
        
        
        # Make prediction
        prediction = model.predict(input_df)
        probabilities = model.predict_proba(input_df)

        label={0:"BAD",1:"NEED CARE",2:"GOOD"}
        
        # Convert probabilities to percentages
        probabilities_percent = probabilities * 100
        
        # Show prediction

        if(prediction==0):
            st.write(f'Prediction: {label[0]}')
        elif(prediction==1):
            st.write(f'Prediction: {label[1]}')
        else:
            st.write(f'Prediction: {label[2]}')
         

        # Display probabilities in percentage format
        st.write("Probabilities (%):")
        for i, prob in enumerate(probabilities_percent[0]):
            st.write(f'Class {i}: {prob:.6f}%')

    except Exception as e:
        st.error(f"Error during prediction: {e}")
