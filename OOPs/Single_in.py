# this is single inheritance -- when a derived class derives one base class 
class A:
    attr_1 = 10
    def method1(self):
        print("Hello from method-1 of class A")

class B(A):
    attr_2 = 20
    def method2(self):
        print("Hello from method-2 of class B")

# obj = B()
# obj.method1()
# obj.method2()


# this example of parameterzied constructor in base class and derived class 

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


detail = Employee("Digvijay",3422, 45000, "Manager")

detail.show_detials_emp()
