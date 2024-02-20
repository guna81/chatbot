# from huggingface.inference import gpt2, blenderbot
from mymodel.inference import generate_response

def chatbot(prompt):
    responses = generate_response(prompt)
    # print(responses)
    return responses