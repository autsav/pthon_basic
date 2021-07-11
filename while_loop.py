i=1
while(i <= 6):
    print(i)
    i +=1

#using flag t stop looping
i = ""
name = "Write any name. \n"

while(i != 'q'):
    i = input(name)

#infinite loop
#the loop that doesnot stop,

j=1
while(j <= 6):
    user = input("What is your name?")
    print("You inserted " + user)

    if(user == "John"):
        break
    elif( user == "Mic"):
        continue
    j+= 1

