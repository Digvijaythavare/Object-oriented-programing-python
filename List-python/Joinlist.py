list1 = [1, 2, 3,]
list2 = ['a','b']
list3 = list1 + list2

print(list3)


for x in list2:
    list1.append(x)
    print("second mtnod",list1)


list1.extend(list2)
print("third method=",list1)