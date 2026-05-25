'''
3.Average Rating
You are developing a program for a movie rating system. Request the user to enter an average rating
as a floating-point number, and then convert it to an integer to display the rounded rating.
Input format
The program prompts the user to enter the average movie rating as a floating-point number.
Output format
The program calculates and displays the rounded movie rating as an integer.
Constraints
The input should be a valid floating-point number representing the average movie rating.
The program converts the input to an integer using rounding (nearest integer) without any additional
conditions.
The program does not handle out-of-range ratings or non-numeric inputs.
'''

input1 = float(input("Average Rating: "))
print("Rounded Rating: ", (int)(input1))