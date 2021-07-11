print("----------------------------------------------------This is a function----------------------------------------------------")
def hello():
    print("hello this is a function")

hello()
print("---------------------------------------------Arguments and parameters in functions----------------------------------------------------")
#Parameters are the variable names within the function defination
#Arguments are the values that passws in the function that is called

def names(Fname,Lname):
    print("Your first name is "+Fname)
    print("Your last name is "+Lname)


#Now we are out of the function
names('Utsab','Adhikari')
names('nancy','karki')

print("---------------------------------------------Default values in functions----------------------------------------------------")

def carnames(sports='honda',classic='royal'):
    print("My fav sports car name is : "+sports)
    print("My fav classic car name is: "+classic)
    print("\n")

carnames()
carnames(sports='ducati',classic='porche')

print("---------------------------------------------Order matters in parameterss----------------------------------------------------")

carnames(classic='highness',sports='benelli')

print("---------------------------------------------Return values in functions----------------------------------------------------")
def sum(a,b):
    total=a+b
    return total

print(sum(6,5))