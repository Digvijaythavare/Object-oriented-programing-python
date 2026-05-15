# Encapsulation
# Restrict access to certain attribute or methodes 
# to protect data and enforce controlled access
class Student:
    def __init__(self,name,grade,per):
        self.name = name
        self.grade = grade
        self.__precentage = per

    def get_percentage(self):
        if self.__precentage < 60:
            return self.__precentage    
        else:
            print("Sorry!!")

    def show_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.__precentage}%")

student1 = Student("Digvijay",12,98)

student1.show_details()  

print(student1.get_percentage())


