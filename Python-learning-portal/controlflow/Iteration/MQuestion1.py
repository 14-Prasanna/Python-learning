n = int(input())
odd_sum = 0
even_sum = 0
for i in range(1, n+1):
    if i % 2 != 0:
        odd_sum = odd_sum + i
    else:
        even_sum = even_sum + i
print(odd_sum, even_sum)