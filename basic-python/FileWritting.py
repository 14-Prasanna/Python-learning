# myObject = open("newFile.txt", 'r')
# d = myObject.readlines()

# for line in d:
#     words = line.splitlines()
#     print(words)


# MyObject = open("newFile.txt", 'r')

# for str in MyObject:
#     print(str)


# fobject = open()

myObject = open("Advantage.txt", "w")

char = input("Type Character : ")

count = 0

for i in range(len(char)):

    myObject.write(char[i])

    count += 1

    if count == 50:

        myObject.write("\n")

        count = 0

        print("Next Line Started")

myObject.close()





myObject = open("Advantage.txt", "r+")

content = myObject.read()

print(content)

offset = int(input("Enter the offset position: "))

myObject.seek(offset)

text = input("Enter the text to write: ")

myObject.write(text)

myObject.seek(0)

print("\nUpdated File Content:\n")

print(myObject.read())

myObject.close()