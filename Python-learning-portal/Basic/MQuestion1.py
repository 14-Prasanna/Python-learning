'''

.Build a program that requests the user's weight (in kilograms) and height (in meters) to
calculate their body mass index (BMI)
Input format
The program takes two inputs from the user:
Weight in kilograms (a positive floating-point number).
Height in meters (a positive floating-point number).
Output format
The program calculates the Body Mass Index (BMI), which is a floating-point number representing the
BMI value.
Constraints
The weight input must be a positive floating-point number (greater than 0).
The height input must be a positive floating-point number (greater than 0).
The program does not handle extreme or unrealistic values (e.g., negative weight or height).
The program calculates the BMI accurately using the provided weight and height inputs.
'''

weight = (float)(input("Enter the weight: "))
height = (float)(input("Enter the height: "))


if(weight <= 0):
    print("Invalid weight input")
else:
     if(height <= 0):
        print("Invalid height input")

if(type(weight) == float):
    if(type(height) == float):
        bmi = weight / (height ** 2)
        print(f"Your BMI is: {bmi:.2f}")
    else:
        print("Invalid height input.")
else:
    print("Invalid weight input.")
