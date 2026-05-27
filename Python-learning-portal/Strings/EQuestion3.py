def replace(text):

    result = ""

    for i in range(len(text)):

        if ('a' <= text[i] <= 'z') or ('A' <= text[i] <= 'Z'):
            result += text[i]
        else:
            result += '#'

    return result


str1 = input()

print(replace(str1))