#Creare instance attribute of object or extermally modifying object's propertied
class Student:
    def __init__(self, S_name,S_grade): # method orn parameterized constructor
      self.name = S_name # attribute
      self.Grade =  S_grade # attribute

    def student_info(self):# method or default construct
       print(f"{self.name} is in class {self.Grade}")

#Student1 = Student("Digvijay",23)

#Student1.student_info()

class Student:
    def __init__(self): # method
      self.name ='Digvijay'# attribute
      self.Grade =  34 # attribute

    def student_info(self):# method
       print(f"{self.name} is in class {self.Grade}")

#Student1 = Student("Digvijay",23)

Student1 = Student()


Student1.student_info()
