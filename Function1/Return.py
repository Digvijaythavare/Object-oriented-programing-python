def add(x,y):
    return x + y
   
    print(add(33,54))




# with return statement for future use

def celsius_to_fahrenheit(clesius):
    fahrenheit = clesius * 9/5 + 32  

    return fahrenheit # after return statement function end

    temf = celsius_to_fahrenheit(25)    
    print(temf)
    print("With return statement ",type(temf))



# without return statemen

def celsius_to_fahrenheit(clesius):
    fahrenheit = clesius * 9/5 + 32    
    print(fahrenheit)
    temf1 = celsius_to_fahrenheit(35)    
    print("With-out return statement ",type(temf1))
      


#  Returing Multiple Values
def square_cube(num):
    sq = num * num 
    cu = num * num * num 
    return sq , cu 
    print("hello")
    print("Enter a number")
    a = 2
    s,c  = square_cube(a)
    print("Square is ",s)
    print("Cube is ",c)


# Return List Tuple and Set 


def str_conversion(s):
    ls = list(s)
    tup = tuple(s)
    set1 = set(s)
    return ls, tup, set1
print("Enter a String")
str = input()
a , b ,c = str_conversion(str)
print("Main String",str)
print("List Convertion",a)
print("Tuple Convertion",b)
print("Set Convertion",c)
