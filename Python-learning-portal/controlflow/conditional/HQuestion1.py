n = input().strip()
digits = len(n)
total = 0
for d in n:
    total += int(d) ** digits

print("true" if total == int(n) else "false")
