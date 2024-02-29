'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''

def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    # numbers = input_list.split()
    result = []

    for num in input_list:
        if int(num) >= min_val and int(num) <= max_val:
            result.append(num)
    print(','.join(result), end = ',')


if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = user_input.split()

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = map(int, user_input.split())

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)
   
