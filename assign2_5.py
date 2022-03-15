print("enter no of values in list")
n=int(input())

print("enter the values in the list: ")
l=[]
for i in range(n):
    l.append(int(input()))

print("the values in list are",l)

print("list after removing duplicate items from it : ")
print(list(set(l)))
