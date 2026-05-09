#Add set{} value
numbers = {1,2,3,4,5}
numbers.add(6)
print(numbers)

Fruit = {'Apple','Banana','Orange'}
print(Fruit)
 
#Removing elements
# 1: Remove

Fruits = {'Apple','Banana','Orange'}
Fruits.remove('Orange')
print(Fruits)


# 2: Discard
    
Fruits.discard('Cherry')
print(Fruits)

# 3: Update
 
Fruits.update(['mango,','watermelon']) 
print(Fruits)