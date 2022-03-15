class person:
    def __init__(self,name):
        self.name=name
    
    def sayname(self):
        print("my name is {}".format(self.name))

class engineer(person):
    def __init__(self,name):
        super().__init__(name)
        self.prof="i am an engineer"

    def sayprof(self):
        print(self.prof)
    
class doctor(person):
    def __init__(self,name):
        super().__init__(name)
        self.prof="i am a doc"

    def sayprof(self):
        print(self.prof)


p1 =engineer("charlie")
p2=doctor("tony")
p1.sayname()
p1.sayprof()
p2.sayname()
p2.sayprof()