List = []

print("Welcome to the World of List Operations : Vaanga Vaanga")

while True:

    print("1. Create an List")
    print("2. Append an element")
    print("3. Insert an element")
    print("4. Append a list to the given list")
    print("5. Modify an existing element")
    print("6. Delete an existing element from its position")
    print("7. Delete an existing element with a given value")
    print("8. Sort the list in ascending order")
    print("9. Sort the list in descending order")
    print("10. Display the list")
    print("0. Varataa Mamey...")

    print("Enter the correct option: ")

    option = int(input())

    if(option == 1):

        print("1 click pannathu ku nandri")

        print("Enter the range of the list")

        ran = int(input())

        List.clear()

        for i in range(ran):

            print("Enter the value {}".format(i + 1))

            value = int(input())

            List.append(value)

    elif(option == 2):

        print("2 click pannathuku nandri")

        print("Enter the append value")

        value = int(input())

        List.append(value)

    elif(option == 3):

        print("3 click pannathuku nandri")

        print("Enter the index")

        index = int(input())

        print("Enter the value")

        value = int(input())

        if(0 <= index <= len(List)):

            List.insert(index, value)

        else:

            print("Invalid Index")

    elif(option == 4):

        print("4 click pannathuku nandri")

        print("Enter the range of the list")

        ran = int(input())

        list2 = []

        for i in range(ran):

            print("Enter the value {}".format(i + 1))

            value = int(input())

            list2.append(value)

        List.extend(list2)

    elif(option == 5):

        print("5 click pannathuku nandri")

        print("Enter the index")

        index = int(input())

        print("Enter the modified value")

        value = int(input())

        if(0 <= index < len(List)):

            List[index] = value

        else:

            print("Invalid Index")

    elif(option == 6):

        print("6 click pannathuku nandri")

        print("Enter the index to be deleted")

        index = int(input())

        if(0 <= index < len(List)):

            del List[index]

        else:

            print("Invalid Index")

    elif(option == 7):

        print("7 click pannathuku nandri")

        print("Enter the value to be deleted")

        value = int(input())

        if(value in List):

            List.remove(value)

        else:

            print("Value not found")

    elif(option == 8):

        print("8 click pannathuku nandri")

        List.sort()

    elif(option == 9):

        print("9 click pannathuku nandri")

        List.sort(reverse=True)

    elif(option == 10):

        print("10 click pannathuku nandri")

        print(List)

    elif(option == 0):
        print("kalabu kalabu kathu varatum....")
        break

    else:
        print("Pariay Tester nu nenaipu... incorrect input thara mooditu oluga kudu da...")