#Write a Python function that checks whether a passed string is palindrome or not.

print("enter your string : ")

def myfun(s):
    if s[::-1]==s:
        print("it is a palindrome.")
    else :
        print("not a palindrome.")

myfun(input())