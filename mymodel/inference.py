from joblib import load
from .model import cleaner

loaded_model = load('mymodel/models/chat_model.joblib')

def generate_response(prompt):
    print(prompt)
    responses = loaded_model.predict([prompt])
    print(responses)
    return responses
