#Using while loop and an if statement write a function named name_adder which
#appends all the elements in a list to a new list unless the element is an empty string: "".

l=["tom","shelby","johnny","arthur","","thomas","chris"]
nl=[]

def name_adder(list):
    j=0
    while j < len(list):
        if list[j] != "":
            nl.append(list[j])
        j+=1
    return nl

print(name_adder(l))