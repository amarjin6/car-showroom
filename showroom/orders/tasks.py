from showroom.celery import app
from orders.services import process_dealer_order, process_customer_order


@app.task
def buy_car():
    return True if process_customer_order() else False
