import streamlit as st
from PIL import Image 
from transformers import pipeline

st.set_page_config(page_title="Image Classifier", 
                   page_icon=":camera:", 
                   layout="centered")

st.title("Image Classifier")
st.write("Upload an image and the model will predict its class.")

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

@st.cache_resource
def load_classifier():
    return pipeline(
        task = "image-classification",
        model = "domai-tb/OpenPlants-Identification-ViT-Base-Patch16-224"
        )

# model = "google/vit-base-patch16-224"

classifier = load_classifier()

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )



