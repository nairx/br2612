from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

    def company(self):
        print("ABC Ltd")

class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")

class GooglePay(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using GooglePay")

p1 = CreditCard()
p1.pay(1000)
p1.company()

p2 = UPI()
p2.pay(500)
p2.company()
