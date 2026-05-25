def appraisal(oldsal, percentage):
    return (int) (oldsal + (oldsal * percentage / 100))


oldsal = float(input("Enter the salary: "))
app = float(input("Enter the appraisal rating: "))

if app >1 and app<=4:
    print("The new salary is: ", appraisal(oldsal, 10))

elif app >4.1 and app<=7:
    print("The new salary is: ", appraisal(oldsal, 25))

elif app >7.1 and app<=10:
    print("The new salary is: ", appraisal(oldsal, 30))

else:
    print("Invalid Input")
