import operator
list1 =[10,20,30,40,50]
list2 = [5,10,15,20,25]

print("List-1 contains 20 ",operator.contains(list1,30))
list3 = operator.concat(list1,list2)
print("After Concationtion, result list contains : ",list3)