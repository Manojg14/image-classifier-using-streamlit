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
        model = "google/vit-base-patch16-224"
        )

classifier = load_classifier()

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        with st.spinner("Analyzing the image..."):
            predictions = classifier(image, top_k=3)

        st.subheader("Predictions:")

        for prediction in predictions:
            label = prediction["label"]
            confidence = prediction["score"] * 100

            st.write(f"**{label}**")
            st.progress(float(prediction["score"]))
            st.write(f"Confidence: {confidence:.2f}%")
            
    except Exception as error:
        st.error(f"This image cannot be processed. Please upload a valid image file.")
        st.exception(error)
else:
    st.info("Please upload an image to classify.")

