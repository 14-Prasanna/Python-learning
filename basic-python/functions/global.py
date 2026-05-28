num = 2

# def fun():
#     num = num * 2  # UnboundLocalError - num
#     print("In Function num = ", num)


def fun():
    global num
    num = num * 2
    print("In Function num = ", num)


fun()

