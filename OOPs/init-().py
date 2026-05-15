# this is __init__() constructor to initillaze attribute
class Person:
    def __init__(self): 
        self.age = int(input("Enter your age : "))
        self.name= str(input("Enter your name : "))

student1 = Person()
print(student1.name,student1.age)       
print("--------------------------------------------------------------") 

# There are two types of constructor in python
# 1: Default Constructor
# The application of default constructor  is to  intialize default values to attribute

class Person1:
    def __init__(self):  # Default constructor to initilize default values to attribute
        self.age = 20
        self.name= 'Vijay'

student2 = Person1()
print(student2.name,student2.age)   
print("--------------------------------------------------------------") 

# 2: parameterized Constructor
# The parameterized constructor is to initilize/assign different values to different object.
# parameterized constructor, define __init__() function with parameters (next to 'self')  

class Person2:
    def __init__(self,sname,sage): # parameterized constructor with 3 additional paramerters
        self.age = sage
        self.name= sname


student1 = Person2("jay",21)
print(student1.name,student1.age)
print("--------------------------------------------------------------")    


# 3 : Constructor with Default Argument
class Person3:
    def __init__(self,sname ="Shital",sage=19): # parameterized constructor with 3 additional paramerters
        self.age = sage
        self.name= sname

    def show_value(self):
        print("Name is",self.name)
        print("Age is",self.age)

student1 = Person3()
student3 = Person3("latur",20)
student1.show_value()
student3.show_value()
print(student1.name,student1.age)
print("--------------------------------------------------------------")    

