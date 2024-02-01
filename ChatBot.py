import nltk
from nltk.tokenize import word_tokenize
import pandas as pd
import re
import os

# Download NLTK resources
nltk.download('punkt')

# Source files
breeds_information = pd.read_csv("dog_breeds/dog_breeds_info_prepared.csv")
registered_dogs = pd.read_csv("dog_breeds/dogs_database.csv")

# Define responses for different questions
responses = {
    "behavior": "The behavior of a {breed} includes {traits}.",
    "traits": "Typical traits of a {breed} are {traits}.",
    "color_of_eyes": "The common color of eyes for a {breed} is {color}.",
    "health_problems": "Common health problems for a {breed} include {problems}.",
    "origin": "{breed} originated from {origin}.",
    "height": "The height range of a {breed} is {height} inches.",
    "longevity": "The average longevity of a {breed} is {years} years."
}

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get information about a specific breed
def get_breed_info(breed):
    row = breeds_information[breeds_information['Breed'] == breed]
    if row.empty:
        return None
    return row.iloc[0]

# Function to generate responses based on user input
def generate_response(question, breed):
    info = get_breed_info(breed)
    if info is None:
        return "Sorry, I don't have information about that breed."
    
    traits = info['Character Traits'].split(', ')
    color_of_eyes = info['Color of Eyes']
    health_problems = info['Common Health Problems']
    origin = info['Country of Origin']
    height = info['Height (in)']
    longevity = info['Longevity (yrs)']
    
    response_template = responses.get(question)
    if not response_template:
        return "I'm not sure how to answer that question."
    
    response = response_template.format(
        breed=breed,
        traits=', '.join(traits),
        color=color_of_eyes,
        problems=health_problems,
        origin=origin,
        height=height,
        years=longevity
    )
    return response

def split_question(question):
    tokens = re.findall(r'\b\w+\b|\S', question)
    lowercase_tokens = [token.lower() for token in tokens]
    return lowercase_tokens


def find_key_question(lowercase_tokens):
    question = ""
    for token in lowercase_tokens:
        for response in responses:
            if token == response:
                question = response
    return question        

def find_breed(user_text):
    found_breed = ""
    
    dog_breeds = breeds_information.Breed.to_list()
    registered_dogs_names = registered_dogs.Name.tolist()

    for breed in dog_breeds:
        if breed.lower() in user_text.lower():
            found_breed = breed

    for name in registered_dogs_names:
        if name.lower() in user_text.lower():
            found_breed = get_breed(name.lower())
    
    if found_breed != "":
        return found_breed
    else:
        return "Breed or dog's name wasn't found"

def get_breed(name):
    row = registered_dogs[registered_dogs.Name == name]
    if not row.empty:
        return row['Breed'].values[0]
    else:
        return "Name not found"

# Main function to handle the conversation
def chatbot():
    clear_terminal()
    
    print("""
        ███████████████████████████████
        █───█────█────█────█─██─█──█──█
        █─███─██─█─██─█─██─█─█─███───██
        █───█────█────█────█──█████─███
        ███─█─████─██─█─█─██─█─████─███
        █───█─████─██─█─█─██─██─███─███
        ███████████████████████████─███
    """)
    print("Welcome to the Dog Breed Chatbot!")
    print("I can provide information about different dog breeds.")
    print("You can ask me about behavior, traits, color of eyes, health problems, origin, height, and longevity of a breed.")
    print("Type 'quit' to exit the chatbot.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        splitted_lowercase_tokens = word_tokenize(user_input)
        question = find_key_question(splitted_lowercase_tokens)
        breed = find_breed(user_input)

        if question:
            response = generate_response(question, breed)
            print("Chatbot:", response)
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase your question?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
