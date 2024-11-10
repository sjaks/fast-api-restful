from util.common import get_id

class CarService():
    def processNewCar(self, car):
        print("Processing new car...")
        car.id = get_id()
        return car
