# Multilevel inheritance means when a dervied class decomes base class of another class
class A:
    attr_1 = 10
    def method1(self):
        print("Hello from method-1 of class A")

class B(A):
    attr_2 = 20
    def method2(self):
        print("Hello from method-2 of class B")

class C(B):
    attr_3 = 20
    print("This is Class : C")
    def method3(self):
        print("Hello from method-3 of class C")


obj = C()
obj.method1()
obj.method2()
obj.method3()