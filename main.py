import random


class Car():

    def __init__(model=None):
        print('vrum vrum')
        self.model = model


car_list = {}
for f in range(34):
    new_car = Car(model="honda")
    car_list[new_car:f]
print(f"\n{car_list}")
