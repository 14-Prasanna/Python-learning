total = 0

price = int(input("Enter the price of the first item: "))
quantity = int(input("Enter the quantity of the first item: "))

total = total + (price * quantity)

choice = input("Do you want to enter another item? (yes/no): ")

while choice.lower() == "yes":

    price = int(input("Enter the price of the next item: "))
    quantity = int(input("Enter the quantity of the next item: "))

    total = total + (price * quantity)

    choice = input("Do you want to enter another item? (yes/no): ")

print("Total Price:", total)