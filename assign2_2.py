print("enter no of values in list")
n=int(input())

print("enter the values in the list: ")
l=[]
for i in range(n):
    l.append(int(input()))

l.sort()

print("sorted in ascending order: ",l)
l.sort(reverse=True)

print("sorted in descending order: ",l)