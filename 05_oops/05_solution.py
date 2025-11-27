class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def fullname(self):
        return f"{self.__brand} {self.model}"
        


my_Car =  Car("Toyota", "Corolla")
print(my_Car.__brand)
print(my_Car.get_brand())
print(my_Car.fullname())

