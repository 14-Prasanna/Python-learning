age = int(input())
if age < 0:
    print("Invalid Age")
elif age >= 20:
    print("Not Allowed")
elif age < 13:
    print("Cartoon Club")
else:
    print("Teens Club")