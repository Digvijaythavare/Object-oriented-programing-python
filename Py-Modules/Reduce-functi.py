from functools import reduce
list3 = [23,34,23,64,75,24]

get_num = reduce(lambda x ,y : x+y,list3)
print(list3)