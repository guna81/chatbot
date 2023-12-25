from joblib import load
from .train_model import cleaner

loaded_model = load('custom/models/chat_model.joblib')


def generator(prompt):
    print(prompt)
    responses = loaded_model.predict([prompt])
    print(responses)
    return responses