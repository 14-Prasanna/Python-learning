
'''
5. Implement a program that takes a user's birthdate as input and calculates their age.
Input format
The user is prompted to enter their birthdate as a string in the format "YYYY-MM-DD," where:
"YYYY" represents the year with four digits (e.g., 1990).
"MM" represents the month with two digits (e.g., 05 for May).
"DD" represents the day with two digits (e.g., 15).
Output format
The program displays the user's age as an integer in years.
Constraints
The program assumes that the user will provide a valid birthdate in the specified format.
The program calculates the age accurately based on the provided birthdate.
The age calculation takes into account leap years for accurate results.
The program does not handle future birthdates (birthdates beyond the current date) for age
calculation. It assumes that the birthdate is in the past.

'''

from datetime import datetime

input1 = input("Enter the DOB: ")

birthdate = datetime.strptime(input1, "%Y-%m-%d")

today = datetime.today()

age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print("Your age is: ", age)
