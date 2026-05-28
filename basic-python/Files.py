# myObject = open("text.txt", 'r+')

# myObject.write("Hey I created an existing file and overwrite it")

# myObject.seek(0)

# content = myObject.read()

# print(len(content))

# print(content)

# myObject.close()



myObject =  open("newFile.txt", 'r+')
mark = 78
myObject.write((mark))
myObject.seek(0)

content = myObject.read()
print(type(content) ,  content)
myObject.close()


