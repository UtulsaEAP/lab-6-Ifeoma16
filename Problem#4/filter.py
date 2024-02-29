'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''

def process_and_print(input_string):
    # Split into separate strings
    numbers = input_string.split()

    # Convert strings to integers and filter out negative values
    input_data = [int(num) for num in numbers if int(num) < 0]

    # Sort integers in reverse order
    input_data.sort(reverse = True)
  
    # Print sorted integers
    for num in input_data:
        print(num, end = ' ')
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
