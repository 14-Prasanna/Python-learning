def SumofOdd(n, n1):

    total = 0

    if n1 % 2 == 0:
        n1 += 1

    for i in range(n1, n + 1, 2):
        total += i

    return total


def SumofEven(n, n1):

    total = 0

    if n1 % 2 != 0:
        n1 += 1

    for i in range(n1, n + 1, 2):
        total += i

    return total


n = int(input("Enter upper limit: "))

n1 = int(input("Enter lower limit: "))

even_sum = SumofEven(n, n1)

odd_sum = SumofOdd(n, n1)

print("The sum of even numbers from",n1,"to",n,"is:",even_sum)

print("The sum of odd numbers from",n1,"to",n,"is:",odd_sum)

print("The absolute value is:",abs(even_sum - odd_sum))