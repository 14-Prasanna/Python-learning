def SumOfNumber(a):
    even = 0
    odd = 0

    for i in range(a):
        if(i % 2 == 0):
            even = i+  even
        else:
            odd = i+odd

    print("Sum of even:",even)
    print("Sum od odd: ", odd)


SumOfNumber(10)
