class Person():
    def __init__(self,name,age,idNum):
        self.name=name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("your name is " + self.name +" Your age is "+self.age+" your ID is " +self.idNum)

class Man():
    def strong(self):
        print("Men are strong")
#Class Inheritance

class Child(Person,Man):
    pass

kid = Child('John','6','7655')
kid.output()
kid.strong()
#Add kid object to inherit Man class feature