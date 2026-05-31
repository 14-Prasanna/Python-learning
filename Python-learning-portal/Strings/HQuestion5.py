def first(String):
    return String[0]

def last(String):
    return String[-1]

def middle(String):
    mid = len(String)//2
    return String[mid]

String1 = input("Enter the input1:")
String2 = input("Enter the input2:")

print(first(String1)+first(String2)+middle(String1)+middle(String2)+last(String1)+last(String2))