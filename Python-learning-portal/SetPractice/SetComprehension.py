def set_comprehension(n):
    return {i * i for i in range(1, n + 1)}

print(set_comprehension(5))