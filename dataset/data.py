pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['what is your name', ['You can call me ChatBot.', 'I am a chatbot.']],
    ['how are you', ['I am doing well, thank you!', 'I am good, how about you?']],
    ['.*your name.*', ['You can call me ChatBot.', 'I am a chatbot.']],
    ['.*fine.*', ['Great!', 'Thats good to hear.']],
    ['bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!']],
    # Add more patterns and responses as needed.
]

intents = {
    "greeting": ["hello", "hi", "hey", "howdy"],
    "weather": ["what's the weather like?", "tell me the weather forecast", "is it going to rain?"],
    "farewell": ["goodbye", "bye", "see you later"]
}

responses = {
    "greeting": "Hello! How can I assist you today?",
    "weather": "Sure, I can check the weather for you.",
    "farewell": "Goodbye! Have a great day!"
}