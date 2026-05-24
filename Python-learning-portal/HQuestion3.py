price = float(input("Enter the price of the item: "))
qua = int(input("Enter the quantity of the item: "))
bud = float(input("Enter the budget: "))

total = price * qua
rbudget = bud - total

print("Total Cost: ${:.2f}".format(total))
print("Remaining budget: ${:.2f}".format(rbudget))