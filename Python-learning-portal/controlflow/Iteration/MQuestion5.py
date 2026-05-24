n = input()
even_sum = 0
odd_sum = 0
for digit in n:
    d = int(digit)
    if d % 2 == 0:
        even_sum = even_sum + d
    else:
        odd_sum = odd_sum + d
print(even_sum, odd_sum)