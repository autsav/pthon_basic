dic = {'son':'sam','daughter':'aruna'}
        #key and value pair
print(dic['daughter'])

#Addking new Key value in disctionary

print('-----------------------------#Adding new Key value in disctionary------------------')
dic['color']= 'red'
print(dic)
print('-----------------------------# Filling empty dictionary------------------')

List = {}
List['car']='Tesla'
List['motorcycle']='Hayabusa'
List['house']='Modern House'

print(List)
print('-----------------------------#Changing the value in dictionary------------------')
List['motorcycle']='Suzuki'
print(List)

print('-----------------------------#Delete the value in dictionary------------------')
del List['house']
print(List)

