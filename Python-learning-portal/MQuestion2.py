'''2. Score Message
You are creating a program to display a message for a game score. Ask the user for their score as an
integer and then convert it to a string to display a message like "Your score is [score]."
Input format
The program prompts the user to enter their game score as an integer.
Output format
The program converts the integer score to a string and displays a message in the format: "Your score
is [score]."
Constraints
The input should be a valid integer representing the game score.
The program converts the input integer to a string and displays it in the specified format.
The program does not handle out-of-range scores or non-integer inputs.

'''

input1 = (int)(input("Game Score: "))

intput2 = (str)(input1)

print("Your score is ", intput2, ".")
