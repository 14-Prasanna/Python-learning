string1 = input()

words = string1.split()

print("Print String in default order:")
print("{} {} {}".format(words[0], words[1], words[2]))

print("Print String in Positional order:")
print("{1} {0} {2}".format(words[0], words[1], words[2]))

print("Print String in order of Keywords:")
print("{c} {b} {a}".format(a=words[0], b=words[1], c=words[2]))