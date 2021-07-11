a=4
if a>0:
    print(True)
else:
    print(False) 
#Greater than or equal and less than or equal
# 15>=4, 16<=19 

#Compare Strings
print("-----------------------------------#Compare Strings---------------------------------------")

name="Python"
name2="Python"

if(name == name2):
    print("Two strings are equal")
else:
    print("Two strings are not equal")

#using not equal with if ,else statements
print("-----------------------------------#using not equal with if ,else statements---------------------------------------")

num= 10
num2=11

if(num != num2):
    print("num is not equal to num2")
else:
    print("num is qual to num2")

#using (and) with if else statement
print("-----------------------------------using (and) with if else statement---------------------------------------")
ten=10
five=5
if(ten>=five and five==ten):
    print("True")
else:
    print("False")

print("-----------------------------------using (or) with if else statement---------------------------------------")
ten=10
five=5
if(ten>=five or five==ten):
    print("True")
else:
    print("False")