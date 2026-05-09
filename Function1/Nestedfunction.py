def outer(num1):
    def ineer_increment(num1):
        return num1 + 1
    num2 = ineer_increment(num1)
    print(num1,num2)
outer(12) 