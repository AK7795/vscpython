a=input("enter string : ")
a= a.split()
z=len(a[0])
x= 0

for i in a:
    j=len(i)
    if j>x:
        x=j

for i in a:
    j=len(i)
    if j==x:
        print("largest word is ", i)


for i in a:
    j = len(i)
    if j<z:
        z = j

for i in a:
    j = len(i)
    if j==z:
        w=i
print("smallest word is :",w)