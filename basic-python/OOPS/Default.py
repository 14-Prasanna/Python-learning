class Circle:

    def __init__(self, radius=1.0, color="red"):
        self._radius = radius
        self._color = color

    
    def getRadius(self):
        return self._radius

    def getColor(self):
        return self._color

    
    def setRadius(self, radius):
        self._radius = radius

    def setColor(self, color):
        self._color = color

    
    def display(self):
        print("Radius :", self._radius)
        print("Color  :", self._color)



obj1 = Circle()
print("Default Values")
obj1.display()
print()


obj1.setRadius(10)
obj1.setColor("blue")
print("Updated Values")
obj1.display()
print()
print("Getter Radius :", obj1.getRadius())
print("Getter Color  :", obj1.getColor())
print()


obj2 = Circle(5.5, "green")
print("Second Object Values")
obj2.display()