class Dog:
    species = "Canis Familiaris"

    def __init__(self,name,age):
     self.name = name
     self.age = age

    def description(self):
      return f"{self.name} is {self.age} years old" 

    def speak(self,sound):
      return f"{self.name} says {sound}"

my_dog = Dog("Sheru" , 4) 

print(my_dog.name)
print(my_dog.age)

print(my_dog.description())

print(my_dog.speak("Woof"))