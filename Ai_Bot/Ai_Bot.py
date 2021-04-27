with open("data.txt") as f:
    data = [item.split(",") for item in f.readlines()]
data = {item[0]:item[1:] for item in data]

def message2():
    msg = input()
    tokens = msg.lower().split()
    words = [e.lower() for e in tokens]
    if len(words[0]) == 1:
        msg = ''.join(words)
    if len(words[0]) >= 2:
        msg = ' '.join(words)

def message():
    msg = ""
    msg = input()
    tokens = msg.lower().split()
    words = [e.lower() for e in tokens]
    if len(words[0]) == 1:
        msg = ''.join(words)
    if len(words[0]) >= 2:
        msg = ' '.join(words)

    # General Conversation
    if (msg == "hi" ) or (msg == "hello"):
        print("Heyyy how are you?")
    if msg == "im fine how are you":
        print("Thats great to hear! Im fine as well!")
    
    # Political Questions

    # India
    if "president of india" in msg:
        print("Ram Nath Kovind is the Current President of India")
    if "prime minister of india" in msg:
        print("Narendra Modi Is the current Prime Minister of India")
    if msg == "Who is the P":
        print('nothing')

while True: 
    message()

