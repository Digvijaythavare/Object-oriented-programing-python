# using 'self' parameter it helps  giving refrence to the class variable ---fix
# build connnection between class and object
# __init__() helps to initilize of vaue of constructor--fix
class Student:
    def __init__(self, S_name,S_grade): # method
     self.name = S_name # attribute
     self.Grade =  S_grade # attribute

    def show_details(self):
        print(f"{self.name} is in class {self.Grade}")


# passing value  in class
student1 = Student('Digvijay',23)                                                                                                                                                                                                                                                                                                                                                                      
student1.show_details()

student2 = Student('Vijay',20)                                                                                                                                                                                                                                                                                                                                                                      
student2.show_details()

student3 = Student('Dnyaneshwer',22)                                                                                                                                                                                                                                                                                                                                                                      
student3.show_details()