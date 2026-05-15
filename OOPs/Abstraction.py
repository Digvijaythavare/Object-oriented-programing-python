# Abstraction
# hiding unnecesary data form users through class, methods
class Student:
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.precentage = percentage

    def show_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.precentage+3}%")

student1 = Student("Digvijay",12,95)
student2 = Student("Vijay",12,93)
student1.show_details()  
student2.show_details()  



