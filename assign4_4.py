#Write a Python program to copy the contents of a file to another file  


with open('a.txt','r') as f1, open('b.txt','a') as f2:
    for line in f1:
        f2.write(line)