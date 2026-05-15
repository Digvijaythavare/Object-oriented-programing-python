class Employee:
    company = "Apple"
    
    def show(self):
        print("company is ", self.company)

    @classmethod
    def newcompany(cls, ncompany):
        cls.company = ncompany    

e1 = Employee()
e1.show()

e1.newcompany("Microsoft")
e1.show()

print(Employee.company)

# class Employee:
#     company = "Apple"
#     numwmp = 0
#     def __init__(self,name):
#         self.name = name
#         Employee.numwmp +=  1

#     def show(self):
#         print(f"Hi my name is {self.name} and i work at {self.company} and size od emp {self.numwmp}")

#     @classmethod
#     def newcompany(cls, ncompany):
#         cls.company = ncompany    


# el = Employee("Viajy")
# el.company = "Google"
# el.show()


# e2 = Employee("jay")
# e2.company = "Microsoft"
# e2.show()


# e3 = Employee("digvijay")
# e3.show()
