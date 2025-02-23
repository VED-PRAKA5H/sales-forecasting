import streamlit as st
from src.utils import load_model, load_five_columns
import numpy as np

# Load model and data
model = load_model()
df = load_five_columns()

# Set page configuration
st.set_page_config(page_title="Sales Prediction App", page_icon="📈", layout="centered")

# Title and description
st.title("Sales Prediction App 🏷️")
st.markdown("Predict sales based on various parameters! 🎉")

# Sidebar for input descriptions
st.sidebar.header("Input Descriptions")
st.sidebar.markdown("### Input Parameters")
st.sidebar.markdown(f"**{df.columns[0].replace('_', " ")}**: Represents the number of products sold (e.g., 1.0).")
st.sidebar.markdown(f"**{df.columns[1].replace('_', " ")}**: Represents the advertising budget in thousands (e.g., 9.0).")
st.sidebar.markdown(f"**{df.columns[2].replace('_', " ")}**: Represents the number of sales representatives (e.g., 2.0).")
st.sidebar.markdown(f"**{df.columns[3].replace('_', " ")}**: Represents the total store area in square feet (e.g., 400.0).")
st.sidebar.markdown(f"**{df.columns[4].replace('_', " ")}**: Represents the average customer rating (e.g., 27.0).")

# Number input widgets for five numerical entries
num1 = st.number_input(df.columns[0].replace('_', " "), value=1.0)
num2 = st.number_input(df.columns[1].replace('_', " "), value=9.0)
num3 = st.number_input(df.columns[2].replace('_', " "), value=2.0)
num4 = st.number_input(df.columns[3].replace('_', " "), value=400.0)
num5 = st.number_input(df.columns[4].replace('_', " "), value=27.0)

# Create a numpy array from the input values
row = np.array([[num1, num2, num3, num4, num5]])

# Predict button
if st.button("Predict"):
    try:
        prediction = int(model.predict(row)[0])
        # Display the output
        st.header(f"The Predicted Sales is: {prediction}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
