n = int(input())
factor = 2
while n > 1:
    while n % factor == 0:
        print(factor, end=" ")
        n = n // factor
    factor = factor + 1