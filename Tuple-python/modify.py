tuple1 = (1,2,3,4,6)
print(tuple1)

list1 = list(tuple1)
list1 [4] = 5
tuple1 = tuple(list1)
print(tuple1)

list1.append(10)
tuple1 = tuple(list1)
print(tuple1)