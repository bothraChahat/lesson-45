class parrot:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sing(self,song):
        return "{0} sings {1}".format(self.name,song)
    
    def dance(self):
        return "{} likes to dance".format(self.name)
    
p1=parrot("blu",10)
p2=parrot("rio",12)

print(p1.sing("'happy'"))
print(p1.dance())
