import sklearn
import pycaret
import streamlit as st
import pandas as pd
from pycaret.regression import load_model,predict_model

# Made by Jhon Vincent Gupo
# jhonvincentgupo@gmail.com

pipeline = load_model('rfr_model')

def classification(vlue):
    if vlue <= 2.99999:
        classifier = "Clean"
    elif vlue >= 3.0 and vlue <= 5.99999:
        classifier = "Moderately Clean"
    elif vlue >= 6.0 and vlue <= 9.99999:
        classifier = "Somewhat Polluted"
    elif vlue >= 10.0:
        classifier = "Very Polluted"
    return classifier

with st.sidebar:
    st.image("https://snipboard.io/8R3vZa.jpg")
    st.title("Biochemical Oxygen Demand Prediction")
    st.info("Web application for BOD prediction using Decision Tree Regressor",icon="ℹ️")

with st.form(key="myform", clear_on_submit=True):
    temp = st.number_input("Temperature")
    do = st.number_input("Dissolved Oxygen (mg/l)")
    ph = st.number_input("PH", key="ph")
    conductivity = st.number_input("Conductivity (µmhos/cm)")
    nt = st.number_input("Nitrate+ (mg/l)")
    fc = st.number_input("Fecal Coliform (MPN/100ml)")
    tc = st.number_input("Total Coliform (MPN/100ml) Mean")
    submit_button = st.form_submit_button("Predict")

if submit_button:
    test = pd.DataFrame(columns=
                 ['Temp','D.O. (mg/l)', 'PH', 'CONDUCTIVITY (µmhos/cm)',
                  'NITRATENAN N+ NITRITENANN (mg/l)', 'FECAL COLIFORM (MPN/100ml)',
                  'TOTAL COLIFORM (MPN/100ml)Mean'])

   
    test.loc[0] = [temp,do,ph,conductivity,nt,fc,tc]
    st.text("Inputs")
    st.dataframe(test)
    df_result = predict_model(pipeline , data = test)
    rs = df_result.iloc[0]['Label']
    cf_rs = classification(float(rs))
    st.text(f"Predicted Biochemical Oxygen Demand (mg/l) \n{rs} : {cf_rs}")
    del df_result