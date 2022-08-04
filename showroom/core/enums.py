from enum import Enum


class Profile(Enum):
    NONE = 'none'
    CUSTOMER = 'customer'
    VENDOR = 'vendor'
    DEALER = 'dealer'

    @classmethod
    def choices(cls):
        return [(attr.value, attr.name) for attr in cls]

    def __str__(self):
        return self.value


class Acronym(Enum):
    USD = 'US Dollar'
    EUR = 'Euro'
    RUB = 'Ruble'
    PLN = 'Zloty'
    UAH = 'Hryvnia'
    JPY = 'Yen'
    CNY = 'Yuan'
    TRY = 'Turkish Lira'
    ITL = 'Lira'
    BTC = 'Bitcoin'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value
