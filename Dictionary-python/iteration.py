Student = {
    "Name" : "Vijay",
    "Age" : 21,
    "City" : "Latur",
    "Per" : 50.13,
 }

# 1: Access keys

for key in Student:
   print(key)

# 2:  Access Values

for value in Student:
    print(Student[value])

# Access values using value() method 

for value in Student.values():
    print(value)

# 3: Access keys and values

for key, value in Student.items():
      print(key,value)   

# 4:  Access empty value key
for key, value in Student.items():
     if not value:
      print(key)   