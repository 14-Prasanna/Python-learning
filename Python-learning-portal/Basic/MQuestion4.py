'''
4. List of Products
You are building an e-commerce application. Ask the user to enter a list of product names as a string,
and then convert it to a list of strings to display the products.
Input format
The user is prompted to enter a list of product names as a string.
Product names are separated by commas (,).
Output format
The program displays the list of products, each on a separate line.
Constraints
The input should be a string of product names separated by commas.
There are no specific constraints on the length of the input string.
The program assumes that the input format adheres to the comma-separated list of product names.

'''

print("Enter a list of product names separated by commas: ")

a = input()
product_list = a.split(",")
print("The list of products is: ")
for product in product_list:
    print(product.strip())

