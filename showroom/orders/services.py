from orders.models import CustomerOrder
from dealer.models import DealerCar


def process_customer_order(order: CustomerOrder):
    desired_car = order.objects.select_related('car').all()
    desired_price = order.objects.only('price')
    desired_amount = order.objects.only('amount')
    dealers = DealerCar.objects.select_related('dealer').filter(price__lte=desired_price,
                                                                amount__lte=desired_amount) & DealerCar.objects.select_related(
        'car').filter(car=desired_car)

    print(dealers)
