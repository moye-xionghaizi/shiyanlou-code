#! /usr/bin/env python3
def palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    s = input("Please enter a string:")
    if palindrome(s):
        print("This string is a palindrome ")
    else:
        print("This string is not palindrome")
