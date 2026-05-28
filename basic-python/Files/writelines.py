myObject = open("newFile.txt", 'r')
# lines = ["hello everyone\n ", "Writing n lines of the code"]
# myObject.writelines(lines)

comtent = myObject.readlines()
print(comtent)
myObject.close()