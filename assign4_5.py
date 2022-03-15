#Write a Python program to square and cube every number in a given list of integers using Lambda


def fun(a):
    return lambda n : n**a


square=fun(2)
cube=fun(3)
l=[1,2,5,8,9,6,3]
for b in l:
    print(b,":",square(b),",",cube(b))

