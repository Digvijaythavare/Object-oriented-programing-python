print("Main area start :")
a = [10,20,30]
try:
    print("First element of list a is : ",a[0])
    print("Fourth element of list a is : ",a[4])
except IndexError:
    a.append(40)
    print("Fourth element of list a is : ",a[3])
    print("IndexError exception is handled successfully")
