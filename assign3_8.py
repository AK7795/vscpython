'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
 Ask user to enter marks and print the corresponding grade.      '''


n=int(input("enter your marks out of 100 : "))

print("ypur grade is : ")

if n<25:
    print("F")

if n>=25 :
    if n<=45:
        print("E")

if n<=50:
    if n>=45:
        print("")

if n>=50:
    if n<=60:
        print("C")

if n>=60:
    if n<=80:
        print("B")


if n>80:
    print("A")