# 1 : creating dictionary
Student = {
    1 : "Class-A",
    "Name" : "Vijay",
    "Age" : 21,
    "City" : "Latur"
}
print(type(Student))
print(Student["Name"])

# 2 : Using Dict() constructor

person = dict(name='digvijay',age=20,city='renapur')
print(type(person))
print(person)

# 3 : Using list of tuple 
# each tuple only two values
state = dict([("MH","Maharastra"),("UP","Uater pradesh"),("Dl","Delhi")])
for dic in state:
  print(dic,state[dic])