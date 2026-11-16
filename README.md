# 🖼️ Image Classifier using Hugging Face & Streamlit

An AI-powered image classification application built using **Python, Streamlit, Hugging Face Transformers, and Vision Transformer (ViT)**.

Upload an image and get the top 3 predicted classes with confidence scores.

## 🚀 Features

- Upload JPG, JPEG and PNG images.
- AI-based image classification.
- Pretrained Vision Transformer (ViT) model.
- Top 3 prediction results.
- Confidence score visualization.
- Interactive Streamlit interface.

## 🛠️ Technologies

- Python
- Streamlit
- PyTorch
- Pillow (PIL)
- Vision Transformer (ViT)

## 🧠 Model

**Model:** `google/vit-base-patch16-224`

**Task:** Image Classification

**Architecture:** Vision Transformer (ViT)

[View Hugging Face Model](https://huggingface.co/google/vit-base-patch16-224)

## 📂 Project Structure

```text
image-classifier-using-streamlit/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation & Execution

**1. Clone the repository**

```bash
git clone https://github.com/Manojg14/image-classifier-using-streamlit.git
cd image-classifier-using-streamlit
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the application**

```bash
streamlit run app.py
```

## 📦 Requirements

```text
streamlit
transformers
torch
pillow
```

## 🔄 Workflow

1. Upload an image.
2. Process the image using Pillow.
3. Analyze it using the pretrained ViT model.
4. Generate the top 3 predictions.
5. Display labels and confidence scores.

## 🔮 Future Enhancements

- Plant and animal identification.
- Automatic image category detection.
- Scientific name and species identification.
- Biological information integration.
- Streamlit Cloud deployment.
