#super keyword to make point towords member of base class.
class Person:
    def __init__(self,name,idnumber):
        self.name = name
        self.id = idnumber

class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        super().__init__(name, idnumber)        
        self.salary = salary
        self.post = post
  

    def show_detials_emp(self):
        print(f"Name of Employee {self.name} idnumber is {self.id} salary is {self.salary} post is {self.post}")    
        super().sayhello()

detail = Employee("Digvijay",3422, 45000, "Manager")

detail.show_detials_emp()

class A:
    def sayhello1(self):
        print("Class A")
        self.name = "vijay"
        print(self.name)
class B(A):
    def sayhello2(self):
        print("Class B")
class C(B):
    def sayhello3(self):
        print("Class C")
class D(C):
    def sayhello4(self):
        print("Class D")
        super().sayhello1()
obj = D()
#obj.sayhello4()    




        
        