


def message():
    msg = ""
    msg = input()

    # General Conversation
    if (msg == "hi" ) or (msg == "hello"):
        print("Heyyy how are you?")
    if msg == "im fine how are you":
        print("Thats great to hear!")
    
    # Political Questions

    # India
    if msg == "Who is the president of India?":
        print("Ram Nath Kovind is the Current President of India")
    if msg == "Who is the Prime Minister of India":
        print("Narendra Modi Is the current Prime Minister of India")

while True: 
    message()

