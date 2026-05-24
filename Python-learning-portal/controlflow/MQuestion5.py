name = input()
items = int(input())
if items < 10:
    total = items * 12
elif items <= 99:
    total = items * 10
else:
    total = items * 7
print(name, total)