t1 = ()
t2 = ()
t3 = ()

for i in range(4):

    value = input()

    t1 = t1 + (value,)

    value1 = input()

    t2 = t2 + (value1,)

for i in range(4):

    t3 = t3 + (t1[i],)

    t3 = t3 + (t2[i],)

print("Tuple 1 :", t1)

print("Tuple 2 :", t2)

print("Tuple 3 :", t3)