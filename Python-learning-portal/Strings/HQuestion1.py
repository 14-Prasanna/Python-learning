string = input()

lower = 0
upper = 0
non_letters = 0

for i in range(len(string)):

    if string[i].islower():

        lower += 1

    elif string[i].isupper():

        upper += 1

    else:

        non_letters += 1

print("Lower case letters", lower)

print("Upper case letters", upper)

print("Non - letters:", non_letters)