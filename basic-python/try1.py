try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print(c)

except NameError:
    print("this is value is not declared")

except Exception:
    print(Exception)

else:
    print("The value")

finally:
    print("Finllay")
    