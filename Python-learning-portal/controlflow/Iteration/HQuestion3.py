prices = []
while True:
    price = int(input())
    if price == -1:
        break
    prices.append(price)

in_range = []
for p in prices:
    if p >= 5 and p <= 30:
        in_range.append(p)

print(max(prices), min(prices), int(sum(in_range)/len(in_range)))