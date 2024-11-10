from fastapi import FastAPI
from api.car.controller.car import router as car_router
from api.train.controller.train import router as train_router

app = FastAPI()

app.include_router(car_router)
app.include_router(train_router)
