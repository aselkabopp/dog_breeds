import computer_vision_model as cvm
import pandas as pd
def get_dog_info():
    name = input("What is your dog's name?\n").lower()
    age = float(input("How old is your dog?\n"))

    sex = input("Is your dog Male or Female?\n").lower()

    while sex != "male" or sex != "female":
        if sex == "male" or sex == "female":
            break
        sex = input("Please write one of two options: Male or Female.\n").lower()
    return name, age, sex

picture = input("Please enter the name of your dog's picture in the \"images\" folder.\n")

breed = cvm.get_predicted_breed(f"dog_breeds/images/{picture}")
name, age, sex = get_dog_info()

print(name, breed, age, sex)

# Write result to csv
data = {"Name" : [name], 
        "Breed" : [breed],
        "Age" : [age], 
        "Sex" : [sex]
        }
df = pd.DataFrame(data)
df.to_csv("dog_breeds/dogs_database.csv", index=False)
