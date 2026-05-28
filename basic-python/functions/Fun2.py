def circle(rad):
    print("Area of the circle" , 3.14 * rad*rad)

def rectangle(len, bd):
    print("Area of the rectangle ", len*bd)

def square(side):
    print("Area ", side*side)


while True:
    print("menu driven program")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Square")
    print("4. Exit")

    choice = int(input("Enter your choice"))

    if choice == 1:
        r = int(input("Enter the radius of the circle"))
        circle(r)
    elif choice == 2:
        l = int(input("Enter the length of the rectangle"))
        b = int(input("Enter the breadth of the rectangle"))
        rectangle(l, b)
    elif choice == 3:
        s = int(input("Enter the side of the square"))
        square(s)
    elif choice == 4:
        print("Exiting the program")
        break
    else:
        print("Wrong Choice")

    
