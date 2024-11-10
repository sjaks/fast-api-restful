from util.common import get_id

class TrainService():
    def processNewTrain(self, train):
        print("Processing new train...")
        train.id = get_id()
        return train
