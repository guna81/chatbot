from .models import gpt2, blenderbot

def generate_response(prompt):
    responses = blenderbot([prompt])
    return responses
