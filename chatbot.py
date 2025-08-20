print(" Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()

    if user_input in ["bye", "exit", "quit"]:
        print(" Chatbot: Goodbye! Have a great day! 👋")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello there! How can I help you today?")

    elif "your name" in user_input:
        print("Chatbot: I'm a simple chatbot built in Python!")

    elif "weather" in user_input:
        print("Chatbot: I can't check the weather right now, but it's always sunny in my world! 🌞")

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Chatbot: The current time is {current_time}")

    elif "how are you" in user_input:
        print("Chatbot: I'm just a program, but I'm feeling great! How about you?")

    else:
        print("Chatbot: I'm not sure how to respond to that. Can you rephrase?")
