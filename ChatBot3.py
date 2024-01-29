import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

# Load data from CSV into a dictionary
data = {}
with open('dog_breeds/dog_breeds_info.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        breed = row['Breed']
        data[breed] = row

# NLTK setup
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def get_breed_info(breed_name):
    if breed_name in data:
        return data[breed_name]
    else:
        return None

def respond_to_query(query):
    tokens = preprocess_text(query)
    print("Tokens:", tokens)
    
    breed_name = None
    for token in tokens:
        if token in data:
            breed_name = token
            break

    if breed_name:
        breed_info = get_breed_info(breed_name)
        if breed_info:
            response = f"Here is some information about {breed_name}:"
            response += f"\nCountry of Origin: {breed_info['Country of Origin']}"
            response += f"\nFur Color: {breed_info['Fur Color']}"
            response += f"\nHeight (in): {breed_info['Height (in)']}"
            response += f"\nColor of Eyes: {breed_info['Color of Eyes']}"
            response += f"\nLongevity (yrs): {breed_info['Longevity (yrs)']}"
            response += f"\nCharacter Traits: {breed_info['Character Traits']}"
            response += f"\nCommon Health Problems: {breed_info['Common Health Problems']}"
        else:
            response = "I'm sorry, I don't have information about that breed."
    else:
        response = "I'm sorry, I couldn't understand your question."

    return response

# Test the chatbot
while True:
    query = input("Ask me about a dog breed (e.g., 'What do you know about Labrador Retriever?') or type 'exit' to quit: ")
    if query.lower() == 'exit':
        break
    response = respond_to_query(query)
    print(response)
