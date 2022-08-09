from showroom.celery import app
from orders.services import process_dealer_order, process_customer_order


@app.task
def buy_car_from_dealer():
    return True if process_customer_order() else False


@app.task
def buy_car_from_vendor():
    return True if process_dealer_order() else False
