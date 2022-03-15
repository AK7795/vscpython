#Write a program to Take input of age of 3 people by user and determine oldest and youngest among them
print("enter age of 3 people :")
l=[]
for i in range(3):
    l.append(int(input()))
print(l)

print("oldest members age is : ",max(l))
print("youngest members age is : ",min(l))