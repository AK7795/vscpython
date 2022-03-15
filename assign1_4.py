st= input("enter str: ")
s=st.casefold()
p=0
q=0
r=0
z=0
t=0

b=len(s)
print(b)
for i in range(0,b):
     if s[i]=='a':
         p+=1

for i in range(0,b):
     if s[i]=='e':
         q+=1

for i in range(0,b):
     if s[i]=='i':
         r+=1

for i in range(0,b):
     if s[i]=='o':
         z+=1

for i in range(0,b):
     if s[i]=='u':
         t+=1

print("no of a's: ",p)
print("no of e's: ",q)
print("no of i's: ",r)
print("no of o's: ",z)
print("no of u's: ",t)