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
