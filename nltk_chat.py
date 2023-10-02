import nltk
from nltk.chat.util import Chat, reflections

from dataset.data import pairs


def nltk_chat(user_input):
    chatbot = Chat(pairs, reflections)        
    response = chatbot.respond(user_input)
    return response
        
