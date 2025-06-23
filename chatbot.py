def simple_chatbot():
    print("Chatbot: Hi! I'm a chatbot")
   
    while True:
        user_input = input("You: ")
       
       
        # Check for exit command first
        if 'bye' in user_input:
            print("Chatbot: Goodbye!")
            break
           
        # Response rules
        elif any(greeting in user_input for greeting in ['hello', 'hi', 'hey']):
            print("Chatbot: Hello")
           
        elif 'how are you' in user_input:
            print("Chatbot: I'm fine,how about you?")
           
        elif 'name' in user_input:
            print("Chatbot: I'm a simple  chatbot!")
           
           
       

# Start the chatbot
if __name__ == "__main__":
    simple_chatbot()
