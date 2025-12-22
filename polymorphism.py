class Animal:
    def sound(self):
        print("Animal sounds.")
class Dog(Animal):
    def sound(self):
        print("Dog barks.")
d=Dog()
d.sound()