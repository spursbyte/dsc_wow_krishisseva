import pickle
import streamlit as st
import pandas as pd
import numpy as np

model=open("fertilizer_model.pkl","rb")
cal=pickle.load(model)
def welcome():
    return " welcome"
def predict(Temparature,Humidity,Moisture,Soil_Type,Crop_Type,Nitrogen,Potassium,Phosphorous):
    predict=cal.predict([[Temparature,Humidity,Moisture,Soil_Type,Crop_Type,Nitrogen,Potassium,Phosphorous]])
    print(predict)
    return predict

def main():
    st.title("Fertilizer Suggestions")
    html_temp="""
    <div style="background-color: tomato; padding:10px">
    <h2 style="color:white;text-align:center;"> Fertilizer Suggestions </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Temparature= st.text_input("Temparature","Type Here")
    Humidity=st.text_input("Humidity","Type Here")
    Moisture = st.text_input("Moisture", "Type Here")
    Soil_Type= st.text_input("Soil_Type", "Type Here")
    Crop_Type = st.text_input("Crop_Type", "Type Here")
    Nitrogen = st.text_input("Nitrogen", "Type Here")
    Potassium= st.text_input("Potassium", "Type Here")
    Phosphorous = st.text_input("Phosphorous", "Type Here")
    result=""
    if st.button("predict"):
        result=predict(Temparature,Humidity,Moisture,Soil_Type,Crop_Type,Nitrogen,Potassium,Phosphorous)
    st.success("you should use {} fertilizer".format(result))













if __name__ == "__main__":
    main()