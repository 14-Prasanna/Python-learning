n = input()
digits = len(n)
total = 0
for d in n:
    total = total + int(d) ** digits
if total == int(n):
    print("true")
else:
    print("false")