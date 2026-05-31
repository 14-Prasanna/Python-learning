class Example:
    def method(self, a, b=None, *args, **kwargs):
        print("Method in Example")


    def method(self, a, b=None):
        if b is None:
            print(f"Single argument: {a}")

        elif isinstance(a, int) and isinstance(b, int):
            print(f"Two integers: {a}, {b}")
        
        elif isinstance(a, str) and isinstance(b, str):
            print(f"Two String: {a}, {b}")

        else:
            print("Mixed")


        



obj1 = Example()
obj1.method(1)
obj1.method(1, 2)
obj1.method("Tr", "Ar")
obj1.method(67.9, 7898)
obj1.method(1, 2,"Python", 3.8)
