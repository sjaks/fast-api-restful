from fastapi import APIRouter
from api.car.model.car import Car
from api.car.service.car import CarService

router = APIRouter()

cars = []

car_service = CarService()

@router.post("/car/", response_model=Car)
async def create_car(car: Car):
    processed_car = car_service.processNewCar(car)
    cars.append(processed_car)
    return processed_car
