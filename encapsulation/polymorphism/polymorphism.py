

# Three animals with same method name but different behavior
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"


# One function works with all animals - that's polymorphism!
def make_sound(animal):
    print(animal.speak())


# Demo
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    cow = Cow()
    
    make_sound(dog)  # Woof!
    make_sound(cat)  # Meow!
    make_sound(cow)  # Moo!
