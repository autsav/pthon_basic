#Making a slicing list
OS=['Mac','Window','Linux','Android','iOS']
print(OS[0:3])#prints all the elements from row 1 to 3
print(OS[2:])#prints all element row 2
print(OS[-2:])#prints all the element Android and iOS

#using for loop for slicing list

print('Now You are using for loop with slicing list')
for OS in OS[0:5]:
    print(OS)

#Copying Lists Using Slicing Lists
print('-------------Copying Lists Using Slicing Lists--------------')
ProOS=['Mac','Window','Linux','Android','iOS']

cpy_ProLang = ProOS[:]

print('Printing Programming Language List Here')
print(ProOS)
print('print copy one')
# print(cpy_ProLang)

cpy_ProLang.append('Java')
cpy_ProLang.append('C++')

print(cpy_ProLang)
