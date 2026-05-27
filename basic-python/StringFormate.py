listA = []

n = int(input("Enter number of elements in the list: "))
for i in range(0, n):
    print("Enter element No-{}: ".format(i+1))
    elm = eval(input())
    print(type(elm))

    listA.append(elm)

print("The entered list is: \n", listA)
print(type(listA[1]))


    