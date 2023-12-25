from pre_trained.generator import gpt2, blenderbot
from custom.generator import generator

def chat(prompt):
    responses = generator(prompt)
    # print(responses)
    return responses