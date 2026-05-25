def hike(oldsal, percentage):

    return oldsal + (oldsal * percentage / 100)


oldsal = float(input("Enter the old salary: "))

percentage = float(input("Enter the hike percentage: "))

print("The new salary is: ",hike(oldsal, percentage))