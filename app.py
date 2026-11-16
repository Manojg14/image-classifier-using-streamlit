import streamlit as st

st.set_page_config(page_title="Image Classifier", 
                   page_icon=":camera:", 
                   layout="centered")

st.title("Image Classifier")
st.write("Upload an image and the model will predict its class.")

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

