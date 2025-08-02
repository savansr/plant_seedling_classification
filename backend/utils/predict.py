import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Replace this with your real class names from notebook
CLASS_NAMES = ['Black-grass', 'Charlock', 'Cleavers', 'Common Chickweed', 'Common wheat', 
               'Fat Hen', 'Loose Silky-bent', 'Maize', 'Scentless Mayweed', 
               'Shepherds Purse', 'Small-flowered Cranesbill', 'Sugar beet']

model = load_model("model/resnet50_model.h5")

def preprocess_image(image: Image.Image) -> np.ndarray:
    image = image.resize((224, 224))  # ResNet50 input size
    img_array = np.array(image) / 255.0  # Normalize if you used rescale=1./255
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_image(image: Image.Image) -> str:
    processed = preprocess_image(image)
    prediction = model.predict(processed)
    predicted_index = np.argmax(prediction, axis=1)[0]
    return CLASS_NAMES[predicted_index]
