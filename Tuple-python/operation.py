# concatination
tuple1 = (1,2,3,4,5,6)
tuple2 = (7,8,9,10)
tuple3 = tuple1 + tuple2
print(tuple3)

 #Repetitive
tuple4 = ("hello jay ") * 2
print(tuple4)

#Checking a element in a tuple

number = (1,2,3,4,5,6,7,8,9,10)
x = 4
if x in number:
    print(f"The Number is in {x} tuple")
else:
    print("invalid number")