import streamlit as st
import requests
import datetime 

st.title('Bikeshare Demand Prediction')


in_dteday = st.date_input("Date",format="YYYY-MM-DD",min_value=datetime.date(2011,1,1), max_value=datetime.date(2012,12,31))
in_season = st.radio(
    "Season",
    ["spring", "summer", "fall", "winter"],)
in_hr = st.text_input("Hr","6am")
in_holiday = st.radio(
    "Holiday",
    ["Yes", "No"],)
in_workingday = st.radio(
    "WorkingDay",
    ["Yes", "No"],)
in_weekday = st.radio(
    "Weekday",
    ["Sun", "Mon","Tue","Wed","Thu", "Fri", "Sat"],)
in_weathersit = st.radio(
    "Weathersit",
    ["Clear", "Light Rain", "Mist", "Light Rain"],)
in_temp = st.number_input("Temp", step=1.,format="%.3f", value=34.06)
in_atemp = st.number_input("Atemp",step=1.,format="%.3f", value=49.01)
in_hum = st.number_input("Humidity",step=1.,format="%.3f", value=10.02)
in_windspeed = st.number_input("Windspeed",step=1.,format="%.3f",value=19.006)
in_casual = st.number_input("Casual",step=1,value=119)
in_registered = st.number_input("Registered",step=1,value=100)

str_date = in_dteday.strftime('%Y-%m-%d')

input_data = {
            "inputs": [ {"dteday" : str_date, 
                         "season" : in_season,
                        "hr" : in_hr, 
                        "holiday" : in_holiday,
                        "workingday" : in_workingday,
                        "weekday" : in_weekday,
                        "weathersit" : in_weathersit,
                        "temp" : in_temp,
                        "atemp" : in_atemp,
                        "hum": in_hum,
                        "windspeed" : in_windspeed,
                        "casual" : in_casual,
                        "registered" : in_registered
                }   
              ]  
}
st.write(input_data)


if st.button("Predict"):
    try:
        response = requests.post('http://0.0.0.0:8001/api/v1/predict', json=input_data)
        st.write(response.json())
        prediction = response.json()
        st.write(f"Predicted bikeshare demand: {prediction}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error occurred while making the request: {e}")