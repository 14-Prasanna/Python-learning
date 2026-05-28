class Create:

    def __init__(self, *args):

        if len(args) == 0:
            self._radius = 0
            self._color = "red"

        elif len(args) == 1:
            self._radius = args[0]
            self._color = "red"

        elif len(args) == 2:
            self._radius = args[0]
            self._color = args[1]

        else:
            raise ValueError("Too many arguments")

    
    def setRadius(self, radius):
        self._radius = radius

    def setColor(self, color):
        self._color = color

    
    def getRadius(self):
        return self._radius

    def getColor(self):
        return self._color


    def getArea(self):
        return 3.14 * self._radius * self._radius

    
    def display(self):
        print("Radius :", self._radius)
        print("Color  :", self._color)



obj1 = Create()

print("Object 1 Default Values")
obj1.display()

print()


obj1.setRadius(10)
obj1.setColor("blue")

print("Object 1 Updated Values")
obj1.display()

print("Radius :", obj1.getRadius())
print("Color  :", obj1.getColor())
print("Area   :", obj1.getArea())

print()

obj2 = Create(5)

print("Object 2 Values")
obj2.display()

print("Area :", obj2.getArea())

print()


obj3 = Create(7, "green")

print("Object 3 Values")
obj3.display()

print("Area :", obj3.getArea())