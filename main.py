import computer_vision_model as cvm
import pandas as pd
import os 

def get_dog_info():
    name = input("What is your dog's name?\n").lower()
    #age
    while True:
        age = input("How old is your dog?\n")

        try:
        # Attempt to convert the input to a float
            age_float = float(age)

        # Check if it's a float and not bigger than 30
            if isinstance(age_float, float) and age_float <= 30:
                break
            else:
                print("Please enter a valid age (a number not bigger than 30).")

        except ValueError:
            print("Please enter a valid number as the age")

    sex = input("Is your dog Male or Female?\n").lower()

    while sex != "male" or sex != "female":
        if sex == "male" or sex == "female":
            break
        sex = input("Please write one of two options: Male or Female.\n").lower()
    return name, age, sex

picture = input("Please enter the name of your dog's picture in the \"images\" folder.\n")
picture_path = os.path.join("dog_breeds", "images", picture)

breed = cvm.get_predicted_breed(f"dog_breeds/images/{picture}")
name, age, sex = get_dog_info()

print(name, breed, age, sex)

# Write result to csv
data = {"Name" : [name], 
        "Breed" : [breed],
        "Age" : [age], 
        "Sex" : [sex]
        }
# capitalized_data = {key: value.capitalize() if isinstance(value, str) else value for key, value in data.items()} # capitalizing value of every key in dict

# for key in data:
#     key = key.capitalize()
#     print(key, data[key])

df = pd.DataFrame(data)
df.to_csv("dog_breeds/dogs_database.csv", index=False)
