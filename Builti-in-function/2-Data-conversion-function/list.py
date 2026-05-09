# This function converts specified data-structure into 'list' and returns 
tuple1 = (10,20,30)
set1 = {20,30,40,50}
dict1 = {1:"One",2:"Two",3:"Three"}
str1 = "Ravi"
a = list(tuple1)
b = list(set1)
c = list(dict1)
d = list(str1)
print("List conversion of tuple1 is ",a," and its types is : ",type(a))
print("List conversion of set1 is ",b," and its types is : ",type(b))
print("List conversion of dict1 is ",c," and its types is : ",type(c))
print("List conversion of str1 is ",d," and its types is : ",type(d))