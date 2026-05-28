t = list()

c ="Prasanna"

t = list(c)

print(t)



# t = [10, 20.4, "Ram"]
# del t[2]
# print(t)

# del t
# print(t)


list1 = ['Red', "Green", "Blue", "234", "789"]

for i in range(len(list1)):
    print(list1[i])



list2 = [267,89,809,123,90,567]

list1.sort()
print(list1)

list2.sort(reverse=True)
print(list2)


t = [1, 2, 456, 6]

t1 = t.copy()

print(t)
print(t1)

print(id(t))
print(id(t1))