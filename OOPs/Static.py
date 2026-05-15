class Math:
    def __init__(self,num):
        self.num = num

    def addnum(self,n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a + b



a = Math(16)
print(a.num)
print(a.add(3, 4))