class Circle:

    _radius = 0
    _color = "blue"

    def __init__(self, radius = 1.0, color = "blue"):
        Circle._radius = radius
        Circle._color = color

    @classmethod
    def setRadius(cls, radius):
        cls._radius = radius

    @classmethod
    def setColor(cls, color):
        cls._color = color

    @classmethod
    def getRadius(cls):
        return cls._radius

    @classmethod
    def getColor(cls):
        return cls._color

    @classmethod
    def getArea(cls):
        return 3.14 * cls._radius * cls._radius

    @classmethod
    def display(cls):
        print("Radius :", cls._radius)
        print("Color  :", cls._color)


# Object Creation
obj1 = Circle()

print("Default Values")
Circle.display()

print()

# Updating values
Circle.setRadius(10)
Circle.setColor("blue")

print("Updated Values")
Circle.display()

print()

radius = Circle.getRadius()
color = Circle.getColor()

print("Getter Radius :", radius)
print("Getter Color  :", color)

print("Area of Circle :", Circle.getArea())

print()

# Second Object
obj2 = Circle(5.5, "green")

print("Second Object Values")
Circle.display()