from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")

obj = CreditCard()
obj.pay()