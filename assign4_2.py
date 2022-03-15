#Write a Python program to calculate the length of a string 

a=input("enter your string : ")
# using built-in func
print("length of string is :",len(a))

# through iteration
b=0
for i in a:
    b+=1
    
print("length of string is :",b)