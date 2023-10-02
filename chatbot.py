from joblib import load
from train_model import cleaner

loaded_model = load('models/chat_model.joblib')

def chat(user_input):
    response = loaded_model.predict([user_input])
    return response[0]

def bot():
    print("ChatBot: Hi, how can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = chat(user_input)

        if not response:
            response = "Sorry, I don't understand."

        print("ChatBot:", response)
