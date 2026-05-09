class Test:
    x = 10
    y = 20
    def method1(self):
        pass
    def method2(self):
        pass
print("Class 'Test' has attribute 'x' : ",hasattr(Test,'x'))    
print("Class 'Test' has attribute 'y' : ",hasattr(Test,'y'))    
print("Class 'Test' has attribute 'z' : ",hasattr(Test,'z'))  
print()
print("Class 'Test' has attribute 'method1' : ",hasattr(Test,'method1'))
print("Class 'Test' has attribute 'method2' : ",hasattr(Test,'method2'))
print("Class 'Test' has attribute 'method3' : ",hasattr(Test,'method3'))

    