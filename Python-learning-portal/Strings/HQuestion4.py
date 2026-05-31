inputString = input("Enter the String:").split(" ")
length = float('inf') #Positive infinity
minString = ""
for i in inputString:
    if(len(i) < length):
        length = len(i)
        maxString = i

print(maxString)