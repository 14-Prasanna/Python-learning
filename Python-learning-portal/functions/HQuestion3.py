def maximum(arr):
    max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i

    return max_value

limit = int(input("Enter limit: ")) 

arr = []
for i in range(limit):
    arr.append(int(input()))

print("Maximum value is:", maximum(arr))