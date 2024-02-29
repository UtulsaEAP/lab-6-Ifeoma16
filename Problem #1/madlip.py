'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''

def food_input():
    #type you while  loop here
    while True:
        user_input = input()
        tokens = user_input.split()

        if len(tokens) == 2 and tokens[0].lower() == 'quit' and int(tokens[1]) == 0:
            break
        if len(tokens) == 2:
            item = tokens[0]
            quantity = int(tokens[1])

            print("Eating", quantity, item, "a day keeps you happy and healthy.")
    

    

if __name__ == "__main__":
    food_input()
