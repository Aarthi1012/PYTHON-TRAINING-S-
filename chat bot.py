while True:
    user = input("you: ")

    if user.lower() in ["hai"]:
        print("bot: heyy hai how can I help you")
    elif user.lower() in ["what date today"]:
        print("bot: jan 10")
    elif user.lower() in ["bye"]:
        print("bot: bye, have a nice day") 
    else:
        print("bot: I didn't understand your question")