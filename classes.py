class owner:
    def __init__(self,owname):
        self.owname = owname
        
    def OW(self):
        print("my owners name is : {}".format(self.owname))


class Dog:
    def __init__(self,name):
        self.name=name
        print("Object with name : {} created" .format(name))

    def talk(self):
        print("Woof woof!! i am : {}".format(self.name))

    def owner(self):
        print("my owner is : {} ".format(self.name))


d1= Dog("charlie")
d2= Dog("bruno")
o1= owner("tony")
o2=owner("ezequel")
d1.talk()
d2.talk()
o1.OW()
o2.OW() 
