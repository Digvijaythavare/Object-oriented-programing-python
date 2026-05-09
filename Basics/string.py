#1 # type: ignore
#Concatenation string can be concatenated using the + operaton .
#mean's adding two variabls in the python this is concatenation.


greeting  = "Hello"
name = "Vjay"
  
message = greeting + "" + name
print(message)
#o/p= Hello Vijay

#2 Repetition
#  Repetition string can be repeted using the  *  operator
# mean's one variable printing 3,4 times using this operator.

Repeat = "Wlcome to python program"*2
print(Repeat) 
#o/p = Wlcome to python program==Wlcome to python program== Wlcome to python program

#3  indexing 
#indexing  Access character in a string using squre bracket[]
 
first_char = greeting[0]
print(first_char)
#o/p = H


#4
# slicing extract parts of a string using slice nonation[start:end]

substring = name[0:5]
print(substring)

#==============================================================================================================================

# String  Changing Case
#1 Upper():
text = "Python Programming"
print(text.upper())

#2 Lower():
print(text.lower())

#3 Capitalize():
print(text.capitalize())

#4 Title():
print(text.title())

#==========================================================================================================================

# finding substring
# 1 fing():
text = "Hello, welcome to python programming"
position = text.find("e")
print(position)

# 2 Index():
text = "Hello, welcome to python programming"
position = text.index("python")
print(position)


# 3 Replace():
text = "Hello, welcome to python programming"
new_text = text.replace("python","java")
print(new_text)

#==================================================================================================================

#  Splitting and Joining String

# spilt():
Split = "apple,banana,mango"
Split = Split.split(",")
print(Split)


# join(): fv
jion = "apple,banana,mango"
jion = "-".join(jion)
print(jion)

#===================================================================================================================================================

# String Formatting
# using format()

name = "Digvijay"
age = 20
message = "My name is {} and i am {} years old".format(name,age)
print(message)

# using f-string()
message = "My name is {name} and i am {age} years old"
print(message)

#==========================================================================================================================

#Trimming and Stripping Strings

msg1 = "                        hello world!               "
clean_text = msg1.strip()
print(f"{clean_text}")

msg2 = "Ajay34435464356436345643563e645435637333Hello world!"
clean_text = msg2.lstrip("Ajaye23456789103")
print(clean_text)

msg3 = "hello world !!!22334455667788"
clean_text = msg3.rstrip("!2345678")
print(clean_text)

#=================================================================================================================================


# List:::
list1 = [12,23,2.333,"Vijay"]
list2 = [145,"Digvijay"]
print(list1)
print(list1[0])
print(list1[1:3])
print(list2 * 2)
print(list1 + list2)

#=================================================================================================================================

# Tuple:::
Tup1 = [12,23,2.333,"Vijay","Yeash","yogesh","kunal"]
Tup2 = [145,42354,435345,"Digvijay"]
print(Tup1)
print(Tup1[0])
print(Tup1[1:3])
print(Tup2 * 2)
print(Tup1 + Tup2)

#=================================================================================================================================

# Dictionary:::

Dict1 = {"Ravi":"22/04/1985","Vijay":"16/05/1989","Yeash":"11/03/2009"}
print(Dict1)
print(Dict1.keys())
print(Dict1.values())
