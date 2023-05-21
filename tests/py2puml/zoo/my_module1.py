class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__("Canine")
        self.name = name

    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__("Feline")
        self.name = name

    def make_sound(self):
        return "Meow."
