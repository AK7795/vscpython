t="hi, hello, hola, bonjour,{abc}"
s="           hi,hello,hola,bonjour        "
b= t.format(abc='namaste')
c=b.replace('h','c')
d=t.split(",")
e=s.strip()
f='.'.join(e)


print(b)
print(c)
print(d)
print(e)
print(f)

'''a=input() # always returns str
print(type(a))
if(type(a)==int):
    print("input is an integer")
else:
    print("invalid input because not an integer")'''