def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("🤖 Chatbot: Hi there!")
        elif user_input == "hi":
            print("🤖 Chatbot: Hello!")
        elif user_input == "good morning":
            print("🤖 Chatbot: Good morning! Have a great day!")
        elif user_input == "good evening":
            print("🤖 Chatbot: Good evening!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "what is your name":
            print("🤖 Chatbot: My name is ChatBot.")
        elif user_input == "who made you":
            print("🤖 Chatbot: I was created using Python.")
        elif user_input == "what can you do":
            print("🤖 Chatbot: I can chat with you and answer simple questions.")
        elif user_input == "tell me a joke":
            print("🤖 Chatbot: Why did the computer go to school? To improve its bytes!")
        elif user_input == "favorite color":
            print("🤖 Chatbot: I like blue because it looks cool on screens!")
        elif user_input == "thank you":
            print("🤖 Chatbot: You're welcome!")
        elif user_input == "time":
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print("🤖 Chatbot: Current time is", current_time)
        elif user_input == "date":
            from datetime import date
            today = date.today()
            print("🤖 Chatbot: Today's date is", today)
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")
chatbot()
