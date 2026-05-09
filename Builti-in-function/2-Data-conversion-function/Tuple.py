# This function converts specified data-structure into 'Tuple' and returns 
List1 = [10,20,30]
set1 = {20,30,40,50}
dict1 = {1:"One",2:"Two",3:"Three"}
str1 = "Ravi"
a = tuple(List1)
b = tuple(set1)
c = tuple(dict1)
d = tuple(str1)
print("tuple conversion of List1 is ",a," and its types is : ",type(a))
print("tuple conversion of set1 is ",b," and its types is : ",type(b))
print("tuple conversion of dict1 is ",c," and its types is : ",type(c))
print("tuple conversion of str1 is ",d," and its types is : ",type(d))