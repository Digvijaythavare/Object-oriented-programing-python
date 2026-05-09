# res = lambda num : num + num
# print(res(5))
list1 = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda items: items % 2 == 0,list1))
print("Even numbers is ",even)




city = ["Latur","pune","Goa","mumbai"]

sort = sorted(city,key=lambda x : len(x),reverse=True)
print(sort)


