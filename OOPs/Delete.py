class Student:
        def __init__(self):
          self.name = "Latur"
          self.Grade =  "A++"


# Object is instance of class
student1 = Student()                                                                                                                                                                                                                                                                                                                                                                      
print(student1.__dict__)


# Delete Attribute in class
del student1.name                                                                                                                                                                                                                                                                                                                                                                  
print(student1.__dict__)

# Delete an object in class
del student1                                                                                                                                                                                                                                                                                                                                                               
print(student1)