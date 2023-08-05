import streamlit as st
from pages.home import MultiPage

# Load pages scripts
from pages.summary import page_summary_body
from pages.visualiser import page_visualiser_body
from pages.mildew_detection import page_mildew_detection_body
from pages.hypothesis import page_hypothesis_body
from pages.prediction import page_prediction
from pages.instructions import page_instructions_body

# Create an instance of the app
app = MultiPage(app_name="Powdery Mildew Detector")

# Add app pages here
app.add_page("Project Summary", page_summary_body)
app.add_page("Cherry Leaf Visualiser", page_visualiser_body)
app.add_page("Powdery Mildew Detection", page_powdery_mildew_detection_body)
app.add_page("Project Hypothesis", page_hypothesis_body)
app.add_page("ML Prediction Metrics", page_prediction)
app.add_page("Usage Guidelines", page_instructions_body)

app.run()
