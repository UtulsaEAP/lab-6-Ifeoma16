'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''

def process_user_contacts(user_input):
    user_contacts = {}

    tokens = user_input.split() or user_input.split(',')

    # Put word pairs into a dictionary
    for i in range(0, len(tokens), 2):
        if i + 1 < len(tokens):
            name = tokens[i].strip()
            phone_num = tokens[i + 1].strip()
            user_contacts[name] = phone_num
    
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")

    if contact_name in user_contacts:
        print(user_contacts[contact_name])
    else:
        print("Contact not found.")
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
