class Car:
    carType="vehicle"
    def __init__(self,carColor,carMileage,carModel):
        self.carColor=carColor
        self.carMileage=carMileage
        self.carModel=carModel
    def move(self):
        return f"Hello your carColor is {self.carColor},your carMileage is {self.carMileage},your carModel is {self.carModel}"


       