l = [1,2,3,4,5,6,7,8]

def filter_function(a):
    return a > 2
elem = list(filter(filter_function,l))
print(elem)

list2= [22,43,54,68,79,98,684]

lst_get = list(filter(lambda x : x % 2 ==0,list2))
print(lst_get)
