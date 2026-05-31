from typing import Protocol

class PaymentProtocol(Protocol):
    def authorize_payment(self, amount: float) -> bool:
        pass

    def process_payment(self, amount: float) -> bool:
        pass


class CreditCardPayment:
    def authorize_payment(self, amount: float) -> bool:
        print(f"Authorizing credit card payment of ${amount:.2f}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount:.2f}")
        return True
    

class PayPalPayment:
    def authorize_payment(self, amount: float) -> bool:
        print(f"Authorizing PayPal payment of ${amount:.2f}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount:.2f}")
        return True


def process_order(payment: PaymentProtocol, amount:float):
    if payment.authorize_payment(amount):
        payment.process_payment(amount)
    else:
        print("Payment authorization failed.")

    
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

process_order(credit_card_payment, 100.0)
process_order(paypal_payment, 50.0)