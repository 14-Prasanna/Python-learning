class Student:
    def __init__(self):
        self.name = "Shon"
        self.__age = 39

obj = Student()
print(obj.name)
print(obj.__age)