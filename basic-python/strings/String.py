Greet = "Naa enga apdi iruka vadiyava..."  
# Creating a string variable named Greet

print(Greet)  
# Prints the complete string

print(len(Greet))  
# Prints the length of the string


for i in Greet:  
    # Looping through each character in the string

    print(i)  
    # Prints one character at a time


print(Greet[2:])  
# Prints characters from index 2 to end



print(Greet[-6: ])  
# Starts from negative index -6 up to end



print(Greet[2:2])  
# Start and end index are same



print(Greet[6:2])  
# Default step is positive
# Start > End so output is empty



print(Greet[-3:-1])  
# Prints from negative index -3 to -1 (excluding -1)



print(Greet[-1:-3])  
# Start > End with positive step



print(Greet[:-1])  
# Prints from beginning to last character excluding last



print(Greet[0:6:2])  
# Prints characters from index 0 to 5 with step 2



print(Greet[-1:-7:-2])  
# Reverse traversal with step -2
# Output: eoe


print(Greet[0:4:-2])  
# Invalid because step is negative but start < end
# Output: Empty string

print(Greet[::-2])

str1 = 'Hello'
str2 = 'World'

print(str1 + str2)

print(str2 * 3)

txt = "I am a Devil in my world"

if 'Devil' in txt:
    print("Yes you are devil")
else:
    print("Sorry, unfortunately you are human")

print()


# Greet[1] = 'P'
print(Greet)


String = " Ivan vera ettu kattaiyila Kaadhukulla kaththuran Ketta kovam varudhunga"

# new_str = 'A' + String[1:]
# print(new_str)

# new_str1 = 'B' + String[-8:]
# print(new_str1)

print(String)

print(String.find("ettu"))
print(String.find('I'))


Sstr = "hello World!"
new_str3 = 'J' + Sstr[-6:-1]
new_str4 = 'J' + Sstr[6:11]
print(new_str3 , new_str4)

print()


String1 = "sobaa... mutila"
print(String1.find('.'))
print(String1.find("aa"))
print(String1.find("ti", 2))

print(String1.replace("sobaa", "rama"))

print(String1.count('a'))
print(String1.capitalize())


print(String1.endswith("..."))
print(String1.startswith("soba"))


if(String1 == String1[::-1]):
    print(String1 , "is an palindrome string")
else:
    print(String1, "is not a palindrome string")   

if(String1.__eq__(String1)):
    print(String1 , "is an palindrome string")
else:
    print(String1, "is not a palindrome string")   



del Greet  
# Deletes the variable Greet from memory


print(Greet)  
# Error because variable was deleted
# NameError: name 'Greet' is not defined
