def sayhello():
    print("Main function start")
def operation():
    print("Enter two vlues ")
    a = int(input())
    b = int(input())
    
    print("Add is",a+b)
    print("Sub is",a-b)
    print("Mul is",a*b)
    print("Div is",a/b)
    print("Rem is",a%b)
def check_odd_even():
    print("Enter a value")
    num = int(input())
    if (num % 2 == 0):
        print(num,"is even")
    else:
        print(num,"is odd")
sayhello()
operation()
check_odd_even()
print("main function ends")                