animals = ["lion","tiger","dog","parrot"]

print(animals)#list of animals in array
print(animals[0])#Name of fist animals from the array
print(animals[2].title())#Name of the animals in title
print(animals[-3].title())

#Combine an element from a list with string
print("I love my"+" "+ animals[1].title())

#change and Element from a list
animals[3]= "elephant"
animals[0]="snake"
print(animals)
# delete the element from the list
del animals[1]
print(animals)
#using sort and reverse
List=["books","pen","dog","telivision","computer"]
# List.sort()
# List.sort(reverse=True)
List.reverse()
print(List)
#length of the list
print(len(List))
#for loop
Lists=["shocks","pen","dog","telivision","computer"]

for List in Lists:
    print("I love my"+" "+List)
print("end of loop")

#using for loop with range
for value in range(1,5):
    print(value)

#using min max and sum with number
print("----")
ListNum=[1,2,3,4,5,6,7,8,9]
print(min(ListNum))
print(max(ListNum))
print(sum(ListNum))

