from typing import Protocol


class Animal(Protocol):

    def sound(self):
        pass


class Dog:

    def sound(self):
        print("Bark")


obj = Dog()
obj.sound()