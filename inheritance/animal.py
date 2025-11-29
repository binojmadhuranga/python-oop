"""Simple Inheritance Example"""

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"


# Child class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# Child class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Demo
if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    print(dog.speak())
    print(cat.speak())
