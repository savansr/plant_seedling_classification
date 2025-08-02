# 🌱 Plant Seedlings Classification

This project focuses on classifying plant seedlings into 12 species using deep learning. It includes two pipelines:

* A **Custom CNN** model.
* A **ResNet50 Transfer Learning** model.

Dataset: [Kaggle - Plant Seedlings Classification](https://www.kaggle.com/c/plant-seedlings-classification)

---

## 📂 Dataset

* Contains 4,750+ labeled images
* Each image belongs to one of 12 plant species:

  * Black-grass
  * Charlock
  * Cleavers
  * Common Chickweed
  * Common wheat
  * Fat Hen
  * Loose Silky-bent
  * Maize
  * Scentless Mayweed
  * Shepherd’s Purse
  * Small-flowered Cranesbill
  * Sugar beet

---


## 🔍 Features

### ✅ Preprocessing

* HSV color segmentation to isolate plants
* Morphological closing and Gaussian sharpening
* Image resizing (256x256)

### 🧠 Models

* **Custom CNN** with 3 Conv blocks and GlobalMaxPooling
* **ResNet50** with frozen base and fine-tuning on last layers

### 🌿 Data Augmentation

* Rotation
* Zoom
* Width/Height Shift

### 💼 Class Handling

* One-hot encoding using `LabelBinarizer`
* Class imbalance handled with `class_weight`

---

## 📊 Evaluation

* Loss and accuracy plots
* Confusion matrix
* Classification report (precision, recall, F1-score)
* ROC curves (AUC) for all classes

### Example Results:

| Model    | Test Accuracy |
| -------- | ------------- |
| CNN      | \~79%         |
| ResNet50 | \~92%+        |

---

## 🚀 Future Work

* Real-time inference with a web UI
* Model ensembling
* ONNX/TFLite model export

---

## 🙏 Acknowledgments

* [Kaggle - Plant Seedlings Classification Competition](https://www.kaggle.com/c/plant-seedlings-classification)




## 📚 License

This project is licensed under the MIT License. See `LICENSE` for more details.
