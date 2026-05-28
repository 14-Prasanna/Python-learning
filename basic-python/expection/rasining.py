import traceback
import random


class Error(Exception):
    """Base class for other Exception"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


num = random.randint(1, 10)

while True:

    try:

        i_num = int(input("Enter a positive integer: "))

        if(i_num <= 0):

            raise ValueTooSmallError("Value should be greater than 0")

        elif i_num < num:

            raise ValueTooSmallError("Entered value is too small")

        elif i_num > num:

            raise ValueTooLargeError("Entered value is too large")

        break

    except ValueTooSmallError as e:

        print(str(e))

        traceback.print_exc()

    except ValueTooLargeError as e:

        print(str(e))

        traceback.print_exc()

    except Exception as e:

        print(str(e))

        traceback.print_exc()

print("Sabash da mapla sabash 🫡")