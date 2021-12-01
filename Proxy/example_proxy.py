from abc import ABC, abstractmethod


class Payment(ABC):
    """
    Абстрактный класс оплаты
    """
    @abstractmethod
    def method_payment(self):
        pass


class PaymentCash(Payment):
    """
    Класс оплаты наличными
    """
    def method_payment(self):
        print('Оплата товара прошла успешно')


class PaymentCreditCard(Payment):
    """
        Класс оплаты кредитной картой
    """
    def __init__(self):
        self.payment = PaymentCash()

    def method_payment(self):
        print('Карта принята')
        self.payment.method_payment()


if __name__ == '__main__':
    payment = PaymentCash()
    payment.method_payment()
    print('-- // --')
    payment_credit_card = PaymentCreditCard()
    payment_credit_card.method_payment()

