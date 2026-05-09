# pased single default value
def sayhello(name = "Everyone"):
    print("hello ",name)

    sayhello("Digvijay")    
    sayhello()    

# passed multiple default value

def sample_function(a="nothing",b="nothing",c="nothing"):
    print("For a",a,"is passed")
    print("For b",b,"is passed")
    print("For c",c,"is passed")
    print("Main area start")
    print("---When called first time---")
    sample_function(10,"jay",True)
    print("---When called second time---")
    sample_function(244)
    print("---When called third time---")
    sample_function("Digvijay",24)  
    print("---When called fourth time---")
    sample_function()
    print("Main area ends")


# passing keyword argument in python

def sample_function(para1,para2,para3):
    print("Parameter-1 recevied : ",para1)
    print("Parameter-2 recevied : ",para2)
    print("Parameter-3 recevied : ",para3)
    sample_function(15,25.34,"Jay")    

def sample_function(para1,para2,para3):
    print("Parameter-1 recevied : ",para1)
    print("Parameter-2 recevied : ",para2)
    print("Parameter-3 recevied : ",para3)
    sample_function(para3=15,para1=25.34,para2="Jay")

# print table passing parameters

def print_table(num=2,upto=10):
    i = 1
    while i <= upto:
        mul = num * i
        print(num,"x",i,"=",mul)
        i = i + 1    
print_table()        