import computer_vision_model as cvm
import pandas as pd

def get_dog_info():
    name = input("What is your dog's name?\n")
    age = int(input("How old is your dog?\n"))

    sex = input("Is your dog Male or Female?\n").lower()

    while sex != "male" or sex != "female":
        if sex == "male" or sex == "female":
            break
        sex = input("Please write one of two options: Male or Female.\n").lower()
    return name, age, sex

# picture = input("Please enter the path to your picture.\n")

picture = "images.jfif"

breed = cvm.get_predicted_breed(picture)
name, age, sex = get_dog_info()

print(name, breed, age, sex)

# Write result to csv
data = {"Name" : [name], 
        "Breed" : [breed],
        "Age" : [age], 
        "Sex" : [sex]
        }
df = pd.DataFrame(data)
df.to_csv("breeds.csv", index=False)
