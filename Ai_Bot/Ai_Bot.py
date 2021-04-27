import os

is_data = {}
in_data = {}

for file in os.listdir("data"):
    with open(file) as f:
        data = [item.rstrip().split(",") for item in f.readlines()]
    is_data.extend({item[1]:item[2] for item in filter(lambda x: x[0] == "is", data)})
    in_data.extend({item[1]:item[2] for item in filter(lambda x: x[0] == "in", data)})

def message2():
    msg = input("> ")
    tokens = msg.lower().split()
    words = [e.lower() for e in tokens]
    if len(words[0]) == 1:
        msg = ''.join(words)
    if len(words[0]) >= 2:
        msg = ' '.join(words)
    
    if msg in is_data:
        print(is_data[msg])
    else:
        for key, item in in_data.items():
            if key in msg:
                print(in_data[key])

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
    message2()

