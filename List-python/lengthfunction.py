has_list =[10,20,30,40,50,60,70]
length_of_list = has_list.__len__()
print("length of list: ",length_of_list)

from math import factorial
list1 = [ 1,2,3,4,5,6,7,8,9 ]
i = 0
while i<list1.__len__():
    a = factorial(list1[i])
    print(list1[i],"-",[a])
    i+=1