from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self, sound):
        print(sound)


class rat(Animal):

    def make_sound(self):
        return super().make_sound("rat")
    

class cat(Animal, rat): 

    def make_sound(self, sound):
        return super().make_sound("I am going to eat rat") 


oj1 = cat()
oj1.make_sound()