string1 = input()

string2 = list(string1)

string2[2] = 'p'

updated_string = ""

for i in range(len(string2)):

    updated_string += string2[i]

print("Updating character at 2nd Index:")

print(updated_string)