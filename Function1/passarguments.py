def check_odd_even(num):
    if num % 2 == 0:
        print(num,"is even")
    else:
        print(num,"is odd")
        print("main function ends") 


def operation(a,b):
     
     print("Add is",(a+b))
     print("Sub is",(a-b))
     print("Mul is",(a*b))
     print("Div is",(a/b))
     print("Rem is",(a%b)) 
     operation(a=14,b=29)          


def show_list_element(a):
    print("List Contains")
    i = 0
    while i<a.__len__():
        print("At index ",i," element is ", a[i])
        i +=1 
    lst1 = [10,20,30,40]
    lst2 = [5,15,25,35,45]
    print("Passing lst1 as parameters")    
    show_list_element(lst1)
    print("Passing lst2 as parameters")  
    show_list_element(lst2 )


def sample_function(value):
     print("Recived",value,"as parameters and it's type is",type(value))
     sample_function(True)
     sample_function(15) 
     sample_function(34.36)
     sample_function("Vijay")
     sample_function((1,2,3,4,5,6))
     sample_function([1,2,3,4,5])
     sample_function({1,2,"jay",True})
     sample_function({"a":1,"b":2,"c":3})


def sequence_operation(a):
    print("sequence of element",a)
    print("It's type is",type(a))
    print("Max element is",max(a))
    print("Min element is",min(a))
    print("Sum of element is",sum(a))
list1=[1,23,46,38,49]
tuple1=(33,54,2,58,47)
set1={33,44,6,3,87,57,38}    
print("---when passed list1----")
sequence_operation(list1)    
print("---when passed tupl1----")
sequence_operation(tuple1)    
print("---when passed set1----")
sequence_operation(set1)    




