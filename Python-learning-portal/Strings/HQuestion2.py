s1 = input()

s2 = input()

s3 = ""

i = 0
j = len(s2) - 1

while i < len(s1) and j >= 0:

    s3 += s1[i]

    s3 += s2[j]

    i += 1

    j -= 1

print(s3)