
import re

def chatbot(user_input):

    user_input = user_input.lower()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I help you?"

    elif re.search(r"\b(your name|who are you)\b", user_input):
        return "I am a simple rule-based chatbot."

    elif re.search(r"\b(how are you)\b", user_input):
        return "I am fine. Thank you!"

    elif re.search(r"\b(your age|old are you)\b", user_input):
        return "I don't have an age. I am a chatbot."

    elif re.search(r"\b(time|date)\b", user_input):
        return "Sorry, I cannot provide real-time information."

    elif re.search(r"\b(bye|goodbye|exit)\b", user_input):
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand."


print("Chatbot: Hello! Start chatting (type 'bye' to exit)")

while True:
    user = input("You: ")

    response = chatbot(user)
    print("Chatbot:", response)

    if re.search(r"\b(bye|goodbye|exit)\b", user.lower()):
        break
