import nltk
from nltk.chat.util import Chat, reflections
import pandas as pd

# Define pairs of patterns and responses
pairs = [
    [
        r"What is the behavior of a (.*)?",
        ["The behavior of a %1 varies depending on its breed. Can you specify the breed you're interested in?",]
    ],
    [
        r"The behavior of a (.*) is (.*)",
        ["The behavior of a %1 is %2.",]
    ],
    [
        r"What are common behaviors of a (.*)?",
        ["Common behaviors of a %1 include %2, %3, and %4.",]
    ],
    [
        r"What are typical characteristics of a (.*)?",
        ["Typical characteristics of a %1 include %2, %3, and %4.",]
    ],
    [
        r"(.*) created ?",
        ["I was created by OpenAI using Python's NLTK library.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!", "It was nice talking to you. Goodbye!"]
    ],
]

# Create a ChatBot with the defined pairs
chatbot = Chat(pairs, reflections)

# Start the conversation loop
def chatbot_terminal():
    print("""
            ╔══╗╔═══╗╔══╗╔═══╗╔╗╔══╗╔╗╔╗───╔══╗╔╗╔╗╔══╗╔════╗╔══╗─╔══╗╔════╗
            ║╔═╝║╔═╗║║╔╗║║╔═╗║║║║╔═╝║║║║───║╔═╝║║║║║╔╗║╚═╗╔═╝║╔╗║─║╔╗║╚═╗╔═╝
            ║╚═╗║╚═╝║║╚╝║║╚═╝║║╚╝║──║╚╝║───║║──║╚╝║║╚╝║──║║──║╚╝╚╗║║║║──║║──
            ╚═╗║║╔══╝║╔╗║║╔╗╔╝║╔╗║──╚═╗║───║║──║╔╗║║╔╗║──║║──║╔═╗║║║║║──║║──
            ╔═╝║║║───║║║║║║║║─║║║╚═╗─╔╝║───║╚═╗║║║║║║║║──║║──║╚═╝║║╚╝║──║║──
            ╚══╝╚╝───╚╝╚╝╚╝╚╝─╚╝╚══╝─╚═╝───╚══╝╚╝╚╝╚╝╚╝──╚╝──╚═══╝╚══╝──╚╝──
          """)
    print("""Hi, I'm Sparky! Haf-haf! I am not experienced ChatBot. 
          I can provide information about your dog. Feel free to ask!\n
          If you want to end our conversation please write me \"quit\".\n
          """)
    name = input("What is your dog's name?\n").lower()
    breed, age, sex = get_data(name)

    while True:
        user_input = input("> ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        print(response)

def get_data(name):
    df = pd.read_csv("dog-breeds/breeds.csv")
    breed = df.loc[df['Name'] == name, 'Breed']
    age = df.loc[df['Name'] == name, 'Age'].iloc[0]
    sex = df.loc[df['Name'] == name, 'Sex'].iloc[0]
    return breed, age, sex

# Run the chatbot in the terminal
if __name__ == "__main__":
    nltk.download('punkt')
    chatbot_terminal()