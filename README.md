![GitHub language count](https://img.shields.io/github/languages/count/amarjin6/CarShowRoom?logo=python&logoColor=green)
![GitHub repo size](https://img.shields.io/github/repo-size/amarjin6/CarShowRoom?color=blueviolet&logo=GitBook&logoColor=critical)
![GitHub django version](https://img.shields.io/badge/django-4.0.6-critical?logo=django&logoColor=lightgreen)
![GitHub django version](https://img.shields.io/badge/redis-4.3.4-yellow?logo=redis&logoColor=9cf)
![GitHub watchers](https://img.shields.io/github/watchers/amarjin6/CarShowRoom?logo=wechat)

# 🚔 **Car ShowRoom simulator** 🚔

## 🎈 **Main Purpose** 🎈
Write a backend to simulate the work of car dealerships with their customers and vendors.

### **Dealership** 🚖

When creating a car dealership, its name, location, characteristics of those cars that the car dealership prefers to sell in the future are indicated, after creation, according to these characteristics, those car models that are most suitable for the car dealership are found. The dealership should also have a list of cars and the quantity of each individual car model. The purchase of cars takes place from suppliers who will be matched to those models that are most suitable (after the process that was described above).

As a result, the car dealership should store:
* Its characteristics (name, location, etc.)
* Characteristics of the cars that will be sold
* Balance
* History of car sales
* Unique buyers
* A system of promotions

The percentage of discounts is individual for each car dealership and may differ accordingly.

### **Customer** 🙆‍♂️

The customer must have a balance showing how much money he has at the moment. Also, customer must have a history of his car purchases. Buying a car is as follows: the customer creates an Offer, indicating the maximum price of the car and indicating the car he is interested in. Celery then launches a script that, based on Offer users in all car dealerships, searches for suitable cars at the best prices. Deal requirements: the car must be the one that was specified by the user when creating the Offer. The car price must be less than or equal to the price specified in the Offer by the user. The car must really be available in the dealership (the number of these cars in the dealership must be greater than 0 - indicated in the “Car dealerships” section). The user must have enough money on the balance to make a purchase (Must be checked at the stage of creating an Offer).

As a result, the customer should store:
* A profile in which there will be some information about the user
* Some information the user must enter himself
* Some type of purchase history will be generated automatically by the script.

### **Vendor** 👨‍💼

The vendor must store: information about himself (name, year of foundation, number of buyers and location), as well as a list of cars that this supplier sells and the corresponding prices for them. Similar to a car dealership, suppliers should implement systems of promotions and discounts for regular customers. The vendor must have a history of selling cars to car dealerships.

As a result, the vendor should store:
* Information about himself
* A list of cars
* A system of promotions and discounts

### **Celery** 🥦

Celery runs a script once every 10 minutes, which buys cars from vendors based on the characteristics that were indicated above and are individual for each car dealership. Of course, the balance of the car dealership should also be checked. The cars for which there is the greatest demand should be bought first (the demand is calculated based on the history of car sales). At the same time, when the script is launched, it must check for the presence of any shares from vendors for cars that are purchased by any car dealership, if, taking into account the share, the price of the car will be less than that of a regular supplier, taking into account the discount of a regular customer (who has a car dealership at standard buys a car), then you need to purchase this car model from the vendor from whom this promotion takes place.

Celery runs a script once an hour, which checks the profitability of cooperation with vendors. Since the price of cars from vendors may constantly change or new vendors may appear, it is necessary to periodically check the feasibility of cooperation with a particular vendor. The script should check the prices of cars that the dealership buys from all vendors (taking into account discounts for regular customers) and update the list of suppliers stored in the dealership model when it finds a better price than the previous vendor. The script should also take into account the percentages and the required number of purchases for discounts for regular customers and choose the most profitable ones (it may be that at the moment the price is more favorable from one supplier, but the discounts are better from another and in the future it is better to choose another vendor and this is the situation should be checked, you also need to take into account the number of purchases in order to achieve a favorable percentage of discounts.

### **Technologies** 🛡

* Databases: PostgreSQL, Redis
* Authorization: JWT
* Location: django_countries
* Endpoints testing: Swagger
* Model filters: django_filters
* Scheduler: Celery, celery-beat, Flower
* Deployment: ngnix, gunicorn
* Testing: PyTest
  
## 🛠 **How to Use** 🛠
* **Clone project to your folder** 
  
        git clone https://github.com/amarjin6/chat-room.git
* **Check for updates and install all necessary requirements**
  
        pipenv shell
        pipenv install -r requirements.txt
* **Create env folder in project root & declare all env variables**

        mkdir env
        cd env
        touch db.env redis.env celery.env
* **Build docker services** 
        
         docker-compose up django --build
         docker-compose run django
         docker-compose up
         docker-compose down
* **Open project in your browser & check its functionality**

        google-chrome --no-sandbox


## 📌 **Active endpoints** 📌

    admin
    __debug__
    api/swagger
    api/v1/login
    api/v1/login/refresh
    api/v1/login/verify
    api/v1/users
    api/v1/customer/orders
    api/v1/dealer/orders
    api/v1/balances
    api/v1/promotions
    api/v1/dealers
    api/v1/cars

## 🥽 **Preview** 🥽

![flower](https://user-images.githubusercontent.com/86531927/187090651-cc226ccd-062c-4874-891f-5fc0d30ad73b.png)

![drf](https://user-images.githubusercontent.com/86531927/187090657-d6d1f5a9-c036-4d0e-ab80-366f53f96c02.png)

![swagger](https://user-images.githubusercontent.com/86531927/187090668-0a0f7e0d-4027-41ec-b642-d756a99816d8.png)
