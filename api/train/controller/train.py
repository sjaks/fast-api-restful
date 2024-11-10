from fastapi import APIRouter
from api.train.model.train import Train
from api.train.service.train import TrainService

router = APIRouter()

trains = []

train_service = TrainService()

@router.post("/train/", response_model=Train)
async def create_train(train: Train):
    processed_train = train_service.processNewTrain(train)
    trains.append(processed_train)
    return processed_train
