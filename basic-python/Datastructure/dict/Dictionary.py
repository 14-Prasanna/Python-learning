my_dic = {}
my_dic = {1:"apple", 2:"banana"}
my_dic = {1:"cse", 'name':"RAM", 'list':[1,2,3], "tuple":(4,5,6)}

print(my_dic)
print(my_dic[1])
print(type(my_dic[1]))


numbers = dict(x=5, y=0)
print(numbers)

numbers1 = dict({'x':4, 'y':5})
print(numbers1)

number2 = dict([('x',5),('y',6)])
print(number2)


Ethuku = {"child1":{"newEthuku": "RAMA", "email" : "@gmail.com"}, "child2":{"newEthuku" : "Mutila"}}
print(Ethuku)
print(Ethuku["child1"])

Ethuku["child3"] = {"Eva_vera" : "Summa"}

print(Ethuku)
value = Ethuku.keys()

print(value)


dict = {"brand":"frod", "model": "Mustang", "years":2090}
for x in dict:
    print(x, dict[x])

print(dict.values())
print(dict.keys())

print(dict.popitem())
print(dict)

print(dict.get("brand","Not Found"))


d= {}
d = dict.copy()
print(d)


d = {1: "one", 2 : "three"}
d1 = {2:"two"}
d.update(d1)
print(d)


dict = {x:x*x for x in range(5)}
print(dict)