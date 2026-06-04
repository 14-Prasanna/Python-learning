import re

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software including versions of Lorem Ipsum."

res = re.findall(r"^Lorem", text)
print("1. ^Lorem :", res)
print("-" * 70)

res1 = re.findall(r"\btook", text)
print("2. \\btook :", res1)
print("-" * 70)

res2 = re.findall(r"St\b", text)
print("3. St\\b :", res2)
print("-" * 70)

res3 = re.findall(r"\BIpsum", text)
print("4. \\BIpsum :", res3)
print("-" * 70)

res4 = re.findall(r"\d", text)
print("5. \\d :", res4)
print("-" * 70)

res5 = re.findall(r"\D", text)
print("6. \\D :", res5)
print("-" * 70)

res6 = re.findall(r"\s", text)
print("7. \\s :", res6)
print("-" * 70)

res7 = re.findall(r"\S", text)
print("8. \\S :", res7)
print("-" * 70)

res8 = re.findall(r"\W", text)
print("9. \\W :", res8)
print("-" * 70)

res9 = re.findall(r"\w", text)
print("10. \\w :", res9)
print("-" * 70)

# Match at the absolute end of the string
res10 = re.findall(r"Ipsum\.\Z", text)
print("11. \\Z :", res10)
print("-" * 70)