'''write a function to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
example: input is

"New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."


Then, the output should be:


2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1 '''


def fun(input):
    f = {}
    for i in input.split():
        f[i] = f.get(i, 0) + 1

    w = list(f.keys())
    w.sort()

    for j in w:
        print(f'{j}:{f[j]}')


fun("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3")