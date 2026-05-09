#First class is a subclass of the second class then it returns True Otherwise False
class A():
    pass
class B(A):
    pass
class C(B):
    pass
class D(C):
    pass
print("Class A is subclass of class B : ",issubclass(A,B))
print("Class B is subclass of class A : ",issubclass(B,A))
print("Class C is subclass of class B : ",issubclass(C,B))
print("Class D is subclass of class C : ",issubclass(D,C))