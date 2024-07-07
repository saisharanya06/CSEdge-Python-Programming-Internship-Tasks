import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey there', ['Hello!', 'Hey!', 'Hi!']),
    (r'how are you', ["I'm good, thank you!", "Doing well, thanks."]),
    (r'what is your name', ["I'm a chatbot.", "I don't have a name."]),
    (r'(.*) your name(.*)', ["I'm a chatbot.", "I don't have a name."]),
    (r'what can you do', ["I can answer your questions.", "I'm here to help."]),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
]

# Create a Chat instance
chatbot = Chat(patterns, reflections)

def main():
    print("Welcome! Ask me a question or say hi.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        response = chatbot.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    nltk.download('punkt')  # Ensure NLTK data is downloaded
    main()
