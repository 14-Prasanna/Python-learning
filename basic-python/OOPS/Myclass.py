class Myclass:
    x = 5

    def __init__(self):
        pass

    def display(self, b):
        print("Welcome")
        print(b)

    def display(self):
        print("HII")
        


object = Myclass()

print("The value inside the class", object.x)

object.display(10)
object.display()