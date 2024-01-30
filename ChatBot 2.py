import nltk
import pandas as pd
import random
import re

# Download NLTK resources
nltk.download('punkt')

# Load the CSV file
df = pd.read_csv("dog_breeds/dog_breeds_info.csv")

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

# Function to get information about a specific breed
def get_breed_info(breed):
    row = df[df['Breed'] == breed]
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


def find_breed(lowercase_tokens):
    result_breed = ""
    breeds = df.Breed.tolist()
    for token in lowercase_tokens:
        for breed in breeds:
            if token == breed.lower():
                result_breed = breed
    return result_breed   

def get_breed(name):
    df = pd.read_csv("dog_breeds/breeds.csv")
    breed = df.loc[df['Name'] == name, 'Breed']
    return breed


# Main function to handle the conversation
def chatbot():
    print("Welcome to the Dog Breed Chatbot!")
    print("I can provide information about different dog breeds.")
    print("You can ask me about behavior, traits, color of eyes, health problems, origin, height, and longevity of a breed.")
    print("Type 'quit' to exit the chatbot.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        
        splitted_lowercase_tokens = split_question(user_input)
        question = find_key_question(splitted_lowercase_tokens)
        breed = find_breed(splitted_lowercase_tokens)
        # Check if the user input matches any question pattern
        
        # matched_question = None
        # for question in responses:
        #     if question in user_input:
        #         matched_question = question
        #         break
        
        if question:
            # breed = user_input.replace(matched_question, "").strip()

            response = generate_response(question, breed)
            print("Chatbot:", response)
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase your question?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
