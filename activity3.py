class parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=parrot("blu",10)
p2=parrot("rio",12)

#to access the class variables
print("blu is {}".format(p1.species))
print("rio is{}".format(p2.species))

#to access the instance variables
print("{0} is {1} years old".format(p1.name,p1.age))
print("{0} is {1} years old".format(p2.name,p2.age))