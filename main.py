"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st #streamlit is an open-source app framework that lets you create web apps from data scripts in pure Python, without front-end experience.

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise

# Configure the app
st.set_page_config(
    page_title = 'Stress Detection Degree',
    page_icon = 'bg_img\stress_bg.jpg',
    layout = 'centered',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise   
}
with open('wave.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
# Create a sidebar
# Add title to sidear
# st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.radio("*Welcome to Health Assistance System!!*",list(Tabs.keys()))
# page = st.radio("Welcome to Health Assistance System!!", [f"<b>{key}</b>" for key in Tabs.keys()], format_func=lambda x: x, unsafe_allow_html=False)

# st.write('<style>div.row-widget.stRadio>div{flex-direction:row;layout:center;background-color:Black;padding:20px;margin-bottom:10px;margin-top:40px;}</style>',unsafe_allow_html=True)
# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
