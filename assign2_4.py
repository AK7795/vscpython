dic={"name" : "bruce wayne","occupation" : "batman", "sidekick":"robin"}

print("enter the key to be checked")
a= input()
if a in dic:
    print("yes key exists in the dictionary")
else:
    print("key does not exist")