class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self):
       return f"{self.name} car"

    def __repr__(self):
        return f"Car(name='{self.name}', speed={self.speed})"

c = Car("BMW", 240)

print(c)        # __str__
print(repr(c))  # __repr__