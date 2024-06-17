import pandas as pd
# import yfinance as yf
import streamlit as st
import datetime
import pickle
import sklearn

# st.header('Car Prediction')
# df = pd.read_csv("C:/Users/91837/Desktop/Git&github/Github/rishav/cars24-car-price.csv")

st.dataframe(df)


Fuel_type = st.selectbox(
    "Select fuel type",
    ("Petrol", "Diesel", "CNG","LPG","Electric"))

col1, col2 = st.columns(2)

with col1:
   Trasmission  = st.selectbox(
    "Select Trasmission type",
    ("Automatic", "Manual"))

with col2:
   seat = st.selectbox(
    "Select seat no.",[1,2,3,4,5,6,7,8])
   

encode_dict={
   "Fuel_type":{"Petrol":2, "Diesel":1, "CNG":3,"LPG":4,"Electric":5},
   "Trasmission":{"Automatic":2, "Manual":1}
}




engine = st.slider("Engine range?", 500, 5000, 25)

def model_pred(fuel_encoded,Trasmission_encoded,seat,engine):
   with open("C:/Users/91837/Desktop/Git&github/Github/rishav/car_pred","rb") as file:
      input_features=[[2018.0,1,120000,fuel_encoded,Trasmission_encoded,19.7,engine,46.3,seat]]
      reg_model= pickle.load(file)
      return reg_model.predict(input_features)

if st.button("Predict"):
   fuel_encoded=encode_dict['Fuel_type'][Fuel_type]
   Trasmission_encoded=encode_dict['Trasmission'][Trasmission]

   price=model_pred(fuel_encoded,Trasmission_encoded,seat,engine)
   st.text("predicted price"+str(price))

   
