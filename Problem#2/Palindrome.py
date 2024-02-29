'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''

def check_palindrome(user_input):
 #type your code here
    if user_input[::-1] == user_input:
        print("palindrome:", user_input)
    else:
        print("not a palindrome:", user_input)

if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
