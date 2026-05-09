# Convert a normal member-function into a static member-function
class Test:
    def sayhello():
        print("hello")
Test.sayhello = staticmethod(Test.sayhello)    
Test.sayhello()