


'''for outter_loop in range(3):
    for inner_loop in range(3):
     print(inner_loop)'''




'''i = 1 
while i < 4:
    for j in range(1,4):
        print(j)
    print("===")
    i += 1   '''




'''for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print() 




B1 = int(input("Entre num: "))
A1 = int(input("Entre num: "))
for num in range(A1,B1):

    for i in range(2,num):
        if num % i == 0:
            break
    else:   
        print(A1)'''



list = [5,1,1,5,1,1,1]
for i in list:
    for j in range(1,i+1):
        print("*",end ="")
    print()