from typing import Protocol
from abc import abstractmethod

class paymentMethod(Protocol):

    @abstractmethod
    def autherize_payment(self, amount: float) -> bool:
        pass

    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CrediCardPayment:
    def autherize_payment(self, amount: float) -> bool:
        print(f"Authorizing credit card payment of ${amount:.2f}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount:.2f}")
        return True
    

class PayPalPayment:
    def autherize_payment(self, amount: float) -> bool:
        print(f"Authorizing PayPal payment of ${amount:.2f}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount:.2f}")
        return True
    

def make_payment(payment_method: paymentMethod, amount: float):
    if payment_method.autherize_payment(amount):
        payment_method.process_payment(amount)
    else:
        print("Payment authorization failed.")

credit_card_payment = CrediCardPayment()
paypal_payment = PayPalPayment()
make_payment(credit_card_payment, 100.0)
make_payment(paypal_payment, 50.0)