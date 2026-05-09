a = 10   # Is  Global variable
def sample_function():
    b = 20 # Is local variable
    print("Global variable is a",a)
    print("Local variable is b",b)
def sample_function1():
    c = 30 # Is local variable
    return
    print("Global variable is a",a)
    print("Local variable is c",c)    
    print("main area start")    
    print("---Sample_function call----")
    sample_function()
    print("---Sample_function-1 call----")
    sample_function1()
    print("main area ends") 



# Update Global Value using keyword == "globle"  

 
a = 10
def change_a():
    global a # access global variable for change value
    a = 20 # changes globle value

print(a)  # before change variable

change_a()    
print(a)  # After change variable