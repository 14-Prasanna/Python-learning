n = int(input())
if len(str(n)) != 5:
    print("Not a valid number")
else:
    reversed_num = int(str(n)[::-1])
    print(reversed_num)