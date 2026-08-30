class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello , I'm {self.name}")


class Employee(Person):
    def __init__(self ,name ,job):
        self.name = name
        self.job = job

    def work(self):
        print(f"{self.name} is working as a {self.job}")


employee = Employee("Digvijay", "Software Engineer")

employee.greet()
employee.work()