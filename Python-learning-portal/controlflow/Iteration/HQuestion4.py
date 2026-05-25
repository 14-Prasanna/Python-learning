income = int(input())
if income <= 250000:
    print("You are exempted from tax")
elif income <= 500000:
    tax = (income - 250000) * 0.10
    print("Tax amount is", int(tax))
elif income <= 1200000:
    tax = (250000 * 0.10) + ((income - 500000) * 0.20)
    print(int(tax))
else:
    tax = (250000 * 0.10) + (700000 * 0.20) + ((income - 1200000) * 0.30)
    print(int(tax))