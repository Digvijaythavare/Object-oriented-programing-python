# Arbitry Argument(Length of argument)
# 1:  Positional Argument

def count_length(*var_arg):
    print("length of : ",var_arg.__len__())
    for getvalue in var_arg:
        print(getvalue)
    count_length("vijay","Thavare","shital")  

def add_number(*add):
    print(type(add))
    return sum(add)
    result = add_number(1,2,3,4,5) #variable number of argument
    print("Total sum of : ",result)      

def greeting(*names):
    for name in names:
        print(f"hello , {name}!")
    greeting("vijay","jay","Digvijay")



# 2: Keyword Argument
def print_detial(**future):
    print(type(future))
    for key,value in future.items():
        print(f"{key} : {value}")
print_detial(name = "Vijay",age = 20,city = "Latur")                   