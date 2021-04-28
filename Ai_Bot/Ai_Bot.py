import os

is_data = {}
in_data = {}

for file in os.listdir(os.path.join(os.path.dirname(__file__), "data")):
    with open(os.path.join(os.path.dirname(__file__), "data", file)) as f:
        data = [item.rstrip().split(",") for item in f.readlines()]
    is_data.extend({item[1]:item[2] for item in filter(lambda x: x[0] == "is", data)})
    in_data.extend({item[1]:item[2] for item in filter(lambda x: x[0] == "in", data)})

def message():
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
        flag = False
        for key, item in in_data.items():
            if key in msg:
                print(in_data[key])
                flag = True
        if not flag:
            pass # Add code here

while True: 
    message()

