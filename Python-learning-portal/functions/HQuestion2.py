def Add(a, b):

    print("Add:", a + b)


def Sub(a, b):

    print("Subtract:", a - b)


def Mul(a, b):

    print("Multiply:", a * b)


value = input("Enter operation sentence: ")

words = value.replace(".", "").split()


if words[0] == "Add":

    a = int(words[1])

    b = int(words[3])

    Add(a, b)


elif words[0] == "Subtract":

    a = int(words[3])

    b = int(words[1])

    Sub(a, b)


elif words[0] == "Multiply":

    a = int(words[1])

    b = int(words[3])

    Mul(a, b)


else:

    print("Invalid input")