class ModOfTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):

        if self.n <= self.max:

            result = self.n % 2

            output = f"{result} #{self.n} % 2"

            self.n += 1

            return output

        else:
            raise StopIteration


num = ModOfTwo(3)

for value in num:
    print(value)