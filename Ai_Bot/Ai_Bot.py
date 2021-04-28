import os
import logging


is_data = {}
in_data = {}

for file in os.listdir(os.path.join(os.path.dirname(__file__), "data")):
    with open(os.path.join(os.path.dirname(__file__), "data", file)) as f:
        data = [item.rstrip().split(",") for item in f.readlines()]
    is_data.update({item[1]:item[2] for item in filter(lambda x: x[0] == "is", data)})
    in_data.update({item[1]:item[2] for item in filter(lambda x: x[0] == "in", data)})

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
            teach = input("Oh, im not so sure about that, would you like to teach me?\n(type yes/no)\n")
            if teach == "yes":
                category = input("""Ohh! Thank you so much for teaching me new things!
What category does this knowledge fall into?
    (a) General Conversation
    (b) Politics
    (c) Food
    (d) Science
    (e) Others\n""")


                if category == "a":
                    file_name = 'Coding/Ai_Bot/data/general.txt'
                if category == "b":
                    file_name = 'Coding/Ai_Bot/data/politics.txt'
                if category == "c":
                    file_name = 'Coding/Ai_Bot/data/food.txt'
                if category == "d":
                    file_name = 'Coding/Ai_Bot/data/science.txt'
                if category == "e":
                    file_name = 'Coding/Ai_Bot/data/others.txt'
                new_input = input("Great! So what would the correct answer to your statement be?\n")

                logger = logging.getLogger(__name__)
                logger.setLevel(logging.DEBUG)

                file_handler = logging.FileHandler(file_name)
                formatter = logging.Formatter('%(message)s')

                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
                
                logger.debug(f'in,{msg},{new_input}')
                print("Data has been updated! Re-run the program to use new data!")



            elif teach == "no":
                print("Ok, no problem")
            else:
                print("Hey thats an invalid input!")

while True: 
    message()

