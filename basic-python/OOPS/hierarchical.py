class Num:

    def __init__(self):
        self.x = 2
        self.y = 10


class Add(Num):

    def findSum(self):
        self.z = self.x + self.y
        print("The Addition is :", self.z)


class Sub(Num):

    def findSub(self):
        self.z = self.y - self.x
        print("The Subtraction is :", self.z)


class Mul(Num):

    def findMul(self):
        self.z = self.x * self.y
        print("The Multiplication is :", self.z)


class Div(Num):

    def findDiv(self):
        self.z = self.y / self.x
        print("The Division is :", self.z)


# Object Creation
obj1 = Add()
obj1.findSum()

print()

obj2 = Sub()
obj2.findSub()

print()

obj3 = Mul()
obj3.findMul()

print()

obj4 = Div()
obj4.findDiv()