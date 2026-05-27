string = input()

result = ""

for i in range(len(string)):

    if string[i].islower():

        result += string[i].upper()

    elif string[i].isupper():

        result += string[i].lower()

    else:

        result += string[i]

print(result)