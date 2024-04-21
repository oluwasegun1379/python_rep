#!/usr/bin/env python3
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, Animal_color):
        super().__init__(name, species)
        self.Animal_color = Animal_color

    def body_color(self):
        return f"The {self.name} which belong to {self.species} as a body color of {self.Animal_color}"
        
dog = Dog("Dog", "Mammal", "Sandy Brown")
print(dog.body_color())