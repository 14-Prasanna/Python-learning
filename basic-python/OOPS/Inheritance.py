class Student:

    def getStudent(self):
        self.__rollno = input("Enter the Roll Number: ")
        self.__name = input("Enter Name: ")

    def printStudent(self):
        print("Roll Number :", self.__rollno)
        print("Name        :", self.__name)


class Mark(Student):

    def getMark(self):
        self.getStudent()

        self.__mark1 = float(input("Enter Mark 1: "))
        self.__mark2 = float(input("Enter Mark 2: "))
        self.__mark3 = float(input("Enter Mark 3: "))

    def printMark(self):
        self.printStudent()

        print("Mark 1 :", self.__mark1)
        print("Mark 2 :", self.__mark2)
        print("Mark 3 :", self.__mark3)

    def calcTotalMark(self):
        return self.__mark1 + self.__mark2 + self.__mark3


class Result(Mark):

    def getResult(self):
        self.getMark()
        self.__total = self.calcTotalMark()

    def putResult(self):
        self.printMark()

        print("Total Marks out of 300 :", self.__total)


# Object Creation
obj = Result()

obj.getResult()

print()

obj.putResult()