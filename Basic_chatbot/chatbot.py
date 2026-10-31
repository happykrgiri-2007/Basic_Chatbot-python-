

# Basic Chatbot Using Python

def chatbot_response(user_input):

    # Convert input into lowercase
    user_input = user_input.lower().strip()

    # Predefined chatbot responses
    if user_input in ["hello", "hi", "hey"]:
        return "Hi! Welcome. How can I help you?"

    elif "how are you" in user_input:
        return "I'm fine, thanks! How are you?"

    elif "your name" in user_input:
        return "I am a Python Basic Chatbot."

    elif "what can you do" in user_input:
        return "I can answer basic questions and chat with you."

    elif "thank" in user_input:
        return "You're welcome!"

    elif "help" in user_input:
        return "Sure! Tell me what you need help with."

    elif "your creator" in user_input:
        return "I was created using Python programming."

    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Please try another message."


# Main chatbot function
def start_chatbot():

    print("\n====================================")
    print("       WELCOME TO PYTHON CHATBOT")
    print("====================================")

    print("Chatbot: Hello! I am your chatbot.")
    print("Chatbot: Type 'bye' to exit the chat.")

    # Continuous conversation loop
    while True:

        user_input = input("\nYou: ")

        if not user_input.strip():
            print("Chatbot: Please enter a message.")
            continue

        response = chatbot_response(user_input)

        print("Chatbot:", response)

        # Stop chatbot when user exits
        if user_input.lower().strip() in ["bye", "exit", "quit", "goodbye"]:
            break


# Run the chatbot
if __name__ == "__main__":
    start_chatbot()
