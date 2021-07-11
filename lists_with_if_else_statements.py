print("-------------------------------- checking values in list with if else statements -----------------------------------------")
myList=['john','sam','mia']

if('john' in myList):
    print("Yes its in the list")
else:
    print("No its not in the list")

#using And
print("-------------------------------- using And-----------------------------------------")

if('john' and 'sam' in myList):
    print("Yes they are in the list")
else:
    print("No they are not in the list")

print("-------------------------------- checking values NOT in lists with if, else statements -----------------------------------------")
name ="mark"

if(name not in myList):
    print(name.lower() + " " + "is not in the list")
else:
    print(name.upper()+ " " +" is in the list") 

print("-------------------------------- If elif statements-----------------------------------------")
print("This program checks if you are eligible for a bank loan or not")

salary=int(input("How much is your salary \n"))
if(salary>1000):
    amount=200
    print("You are eligible to get a bank loan by paying $",amount,"monthly")
elif(salary == 1000):
    amount=500
    print("You are eligible to get bank loan with higher monthly price $",amount,"monthly")
else:
    print("Sory You are not eligible")

print("-------------------------------- Multiple If elif statements-----------------------------------------")

print("this program checks for the zoo discount")
print(",and entrance price is $120")

price = 120
times = int(input("How many times did you go the zoo before \n"))

if(times == 3):
    price = 120-30
    print("Your total included discount will be $",price)
elif(times == 4):
    price = 120-40
    print("Your total included discount will be $",price)
elif(times == 5):
    price = 120-50
    print("Your total included discount will be $",price)
elif(times == 6):
    price = 120-60
    print("Your total included discount will be $",price)
else:
        print("Your total price is $",price,"You are not eligible for discount in this time ")