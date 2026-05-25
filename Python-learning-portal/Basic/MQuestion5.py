'''
 Write a program that asks the user to enter a string. The program should then print the
following:
a. The total number of characters in the string
b. The string repeated 2 times
c. The first character of the string (remember that string indices start at 0)
d. The first three characters of the string
Input format
The first line of each test case consists of String.
Output format
Print the following
a. The total number of characters in the string
b. The string repeated 2 times
c. The first character of the string (remember that string indices start at 0)
d. The first three characters of the string

'''

str = input()

print("Total words count: ", len(str))
print("The string repeated 2 times:", str*2)
print("The firts character in the string: ", str[0])
print("The first three characters of the string, ", str[0:3])