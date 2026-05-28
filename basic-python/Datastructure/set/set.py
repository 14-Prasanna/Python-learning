my_Set = {1, 2, 2, 4, 5, 6, 6}
print(my_Set)


my_Set = {1, 2, [3, 4]}
print(my_Set)

my_Set = {1, 2, 4, 5, (5, 6)}
print(my_Set)

my_Set.add(2)
print(my_Set)

my_Set.update([2,3,5])
print(my_Set)

my_Set = {1, 2, 4, 5, 6, 7}
print(my_Set)
my_Set.discard(4)
print(my_Set)
my_Set.remove(6)
print(my_Set)


my_Set.pop()
print(my_Set)

my_Set.clear()