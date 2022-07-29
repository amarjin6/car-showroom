from orders.models import CustomerOrder
from dealer.models import DealerCar, Dealer
from trades.models import Balance
from cars.models import Car


def create_order_customer_to_dealer(order: CustomerOrder):
    dealers = find_dealers_by_customer_order(order)
    best_dealer = min(dealers, key=dealers.get)
    customer_data = order.sender.objects.all()
    customer_balance = Balance(customer_data.model.id)
    customer_balance.amount = dealers[best_dealer]
    dealer_cars = DealerCar(Dealer(best_dealer).id, Car(order.car.id))
    dealer_cars.amount -= order.amount

    # Save data


def find_dealers_by_customer_order(order: CustomerOrder) -> dict:
    available_dealers = {Dealer: int}
    customer = order.sender
    desired_car = order.car
    desired_price = order.price
    amount = order.amount
    customer_balance = Balance.user.objects.filter(id=customer.id)
    if customer_balance >= desired_price:
        data = DealerCar.objects.all()
        for car in data.model.car:
            if car.model == desired_car.model:
                if amount <= data.model.amount:
                    price = data.model.price * amount
                    if desired_price >= price:
                        available_dealers[data.model.dealer] = price

    return available_dealers
