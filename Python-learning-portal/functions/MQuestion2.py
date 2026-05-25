def primeRange(n, n1):
    for i in range(n, n1+1):
        if isPrime(i):
            print(i)


def isPrime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True


n = int(input())
n1 = int(input())
primeRange(n, n1)