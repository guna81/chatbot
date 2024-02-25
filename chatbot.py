from huggingface.inference import generate_response
# from mymodel.inference import generate_response

def chatbot(prompt):
    responses = generate_response(prompt)
    print(responses)
    return responses