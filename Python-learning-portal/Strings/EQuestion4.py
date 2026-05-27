words = []

String = input()

words = String.split(" ")

for i in range(len(words)):

    word = words[i]

    has_alpha = False
    has_digit = False

    for j in range(len(word)):

        if word[j].isalpha():
            has_alpha = True

        if word[j].isdigit():
            has_digit = True

    if has_alpha and has_digit:

        print(word)