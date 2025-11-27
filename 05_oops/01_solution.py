class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

my_Car =  Car("Toyota", "Corolla")
print(my_Car.brand)
print(my_Car.fullname())