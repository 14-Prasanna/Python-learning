prices = []

# Read all prices until -1
while True:
    try:
        price = int(input().strip())
        if price == -1:
            break
        prices.append(price)
    except:
        break

if not prices:
    print("0 0 0")
    exit()

in_range = [p for p in prices if 5 <= p <= 30]

print(max(prices), min(prices), int(sum(in_range)/len(in_range)) if in_range else 0)
