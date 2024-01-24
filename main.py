from transformers import AutoImageProcessor, AutoModelForImageClassification
import PIL
import requests
import pandas as pd

url = "https://upload.wikimedia.org/wikipedia/commons/5/55/Beagle_600.jpg"
image = PIL.Image.open(requests.get(url, stream=True).raw)

#example2 = "images.jfif"
#image = PIL.Image.open("images.jfif")

image_processor = AutoImageProcessor.from_pretrained("wesleyacheng/dog-breeds-multiclass-image-classification-with-vit")
model = AutoModelForImageClassification.from_pretrained("wesleyacheng/dog-breeds-multiclass-image-classification-with-vit")

inputs = image_processor(images=image, return_tensors="pt")

outputs = model(**inputs)
logits = outputs.logits

# model predicts one of the 120 Stanford dog breeds classes
predicted_class_idx = logits.argmax(-1).item()

breed = model.config.id2label[predicted_class_idx]
print("Predicted class:", breed)

# Write result to csv
data = {"Breed" : [breed]}
df = pd.DataFrame(data)
df.to_csv("breeds.csv", index=False)


