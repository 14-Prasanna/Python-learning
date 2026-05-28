my_tuple = ()
print(my_tuple)
my_tuple = (10, 20, 40, 50)
print(my_tuple)
my_tuple = (10, "ram", 89)
print(my_tuple)
my_tuple = 10, 30, 60, 70
print(type(my_tuple))
print(my_tuple)
my_tuple = (10, 3.14, "ram", True, [3,4])
print(my_tuple)
print(type(my_tuple[4]))
print(type(my_tuple))
print(id(my_tuple))

for i in range(len(my_tuple)):
    my_tuple[i] += i

print(my_tuple)
print(id(my_tuple))

# Memmbership operator available for  tuple also...


SUMMA = "prasanna@gmail.com"
print(type(SUMMA) , id(SUMMA))
user, domain = SUMMA.split("@")

print(user, domain)

my_tuple = (10,20,40)
q, r = divmod(10, 20)
print(q, r)