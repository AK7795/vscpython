#Write a python program to check given number is prime or not
print("enter the number : ")
n=int(input())

for i in range(2,n):
    if (n % i)==0 :
        print("it is not a prime number")
        break
    else:
        print("it is a prime")
        break



