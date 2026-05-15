# this is multiple inheritance -- derived class derives properties of multiple base classes
# To inherit multiple classes
class A:
    attr_1 = 10
    def method1(self):
        print("Hello from method-1 of class A")

class B:
    attr_2 = 20
    def method2(self):
        print("Hello from method-2 of class B")

class C(A,B):
    attr_3 = 20
    def method3(self):
        print("Hello from method-3 of class C")


obj = C()
obj.method1()
obj.method2()
obj.method3()