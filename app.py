import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Churn_Model.pkl")

st.title("Netflix Churn Prediction")

age = st.number_input("Age",18,100)
watch_hours = st.number_input("Watch Hours",0.0)
country = st.selectbox("Country",["Brazil","Canada","France","Germany","India","Japan","Mexico","UK","USA"])
subscription = st.selectbox( "Subscription Type", ["Premium","Standard","Normal"])
genre = st.selectbox("Favorite Genre", ["Comedy","Documentary","Drama","Horror","Romance","Sci-Fi"])

countries = ["Brazil","Canada","France","Germany","India","Japan","Mexico","UK","USA"]
subscriptions = ["Premium","Standard"]
genres = ["Comedy","Documentary","Drama","Horror","Romance","Sci-Fi"]


data = {
    "Age": age,
    "Watch_Time_Hours": watch_hours
     }

for c in countries:
    data[f"Country_{c}"] = 1 if country == c else 0


for s in subscriptions:
    data[f"Subscription_Type_{s}"] = 1 if subscription == s else 0


for g in genres:
    data[f"Favorite_Genre_{g}"] = 1 if genre == g else 0
    

input_df = pd.DataFrame([data])

if st.button("Predict Churn"):

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("Customer will churn ")
    else:
        st.success("Customer will stay ")