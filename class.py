class Person():
    def insert(self,name,age,idNum):
        self.name=name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("your name is " + self.name +" Your age is "+self.age+" your ID is " +self.idNum)
    
    # insert(self="yes",name="utsab",age=14,idNum=23)

#After Creating the class we can use that class by createin g an instance or an object
print("-------------------Creating An instance or an obejct to call the class------------------------")
j = Person()
j.insert('utsab','27','648759')
j.output()

print("-------------------Constructor init function------------------------")
#This is a built in function when , It should be called only during creating the object
class Vechicles():
    def __init__(self,name,rating,idNum):
        self.name=name
        self.rating = rating
        self.idNum = idNum

    def output(self):
        print("your name is " + self.name +" Your age is "+self.rating+" your ID is " +self.idNum)

john = Vechicles('Ferrari','27','598888888888')
john.output()

#Accessing Variables or fuction of an object
print("-------------------Accessing Variables or fuction of an object------------------------")

print(john.name)
print(john.rating)
print(john.idNum)

#Creating Multiple Instances of a class
print("------------------- Creating Multiple Instances of a class ------------------------")
hari = Vechicles('honda','29','59555555555')
sita = Vechicles('Ferrari','27','598883334356534')

hari.output()
sita.output()