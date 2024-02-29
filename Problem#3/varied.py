'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''



def process_input(input_string):
    # Split into separate strings
    numbers = input_string.split()

    # Convert strings to floats
    floatnum = [float(num) for num in numbers]

    if all(float_num > 0 for float_num in floatnum):
      # Get max and average
      max_value = max(floatnum)
      average_value = sum(floatnum) / len(floatnum)
      return max_value, average_value
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
