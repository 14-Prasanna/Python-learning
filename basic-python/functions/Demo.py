'''Demo for basic python and its syntax and Data types'''

# This is a Integer
a = 10
print(type(a))

# This is a Float
b = 10.5
print(type(b))

# This is a String
c = "Hello, World!"
print(type(c))

# This is a Boolean
d = True
print(type(d))

# This is complex number
e = 2 + 3j
print(type(e))

# This is a List
f = [1, 2, 3, 4, 5]
print(type(f))
print(type(f[1]))

# This is a tuple
h = (1, 2, 4, "apple")
print(type(h[3]))

# This is a set
f = {10,20, 3.14, "New"}
print(f)


# This is an None
myVar = None
print(type(myVar))

#This is a dictionary
set = {"name" : "Prasanna"}
print(type(set))

# This is an dictionary travel
dict1= {"Climate" : "Summer"}
print(dict["Climate"])


x=(1== True)
print(x)

a = True+1
print(a)


# Identifiers
c1 = a
print(c1 is not a)
print(c1 is a)

# Membership 

a = [1, '2',3]
print(2 in a)

print(True not in a)


num1 = 10
num2 = 20

num3 = num1+num2
print(num3)
print(type(num3))
num4 = float(num1+num2)
print(num4)
print(type(num4))


fname = input("Enter your first Name:")
print(fname)

age = int(input("Enter you age:"))
print(age)

print(f"My name and age is {fname} {age}")

print("apple","orange","banana",sep=",",end=".\n")