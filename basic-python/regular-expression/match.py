import re

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software including versions of Lorem Ipsum."

res = re.search("Ipsum",text)
print("match object = {}".format(res))
print("-"*70)

print("group method output = ",res.group())
print("-"*70)

print("start method output = ", res.start())
print("-"*70)

print("end method output",res.start())
print("-"*70)

print("span method output", res.span())
print("-"*70)

print("re attribute output = ",res.re)
print("-"*70)

print("String attribute output = ",res.string)
print("-"*70)


