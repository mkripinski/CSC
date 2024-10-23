import streamlit as st, datetime
import streamlit_authenticator as sta
import yaml
from yaml.loader import SafeLoader
with open('CSC/pass.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

watering_days = {
    "Monday" : [True,"8:00","9:00"],
    "Tuesday":[False,0,0],
    "Wednesday":[True,"8:00","9:00"],
    "Thursday":[False,0,0],
    "Friday":[True,"8:00","9:00"],
    "Saturday":[False,0,0],
    "Sunday":[False,0,0]
}

watering_days_text = ""
authenticator = sta.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    
)
for day in watering_days:
    if watering_days[day][0]:
        watering_days_text+=day
        watering_days_text+=" "
        watering_days_text+=watering_days[day][1]
        watering_days_text+=" - "
        watering_days_text+=watering_days[day][2]
        watering_days_text+="\n"

def flip(day):
    if(watering_days[day][0]):
        watering_days[day][0] = False
    else:
        watering_days[day][0] = True 


st.title("Student Center Hydroponics System")
col1,col2,col3 = st.columns(3)
with col1:
    st.image("CSC/images.jpg")
    st.header("Watering Days:")
    st.text(watering_days_text)
with col2:
    st.header("Current Conditions")
    st.text("Sunny")
    st.text("Humidity: 30%")
    st.text("Temperature: 80°F")
    st.text("Water Level: 50%")
with col3:
    authenticator.login("main",1,1,)
    if st.session_state["authentication_status"]:
        day = st.radio("Day:",watering_days.keys())
        st.checkbox("Water",watering_days[day][0],on_change=flip(day))

