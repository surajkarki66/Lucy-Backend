import json
from pathlib import Path

from app.main.services.process_dataset_service import ProcessDatasetService
from app.main.infrastructure.lucy.SimpleANN import SimpleANN

with open("datasets/data.json") as file:
    raw_data = json.load(file)


p = ProcessDatasetService(raw_data)

x_train,y_train = p.split_dataset()
batch_size = 10
epochs = 100

model = SimpleANN(len(x_train[0]))
model.compile()
model.train(x_train,y_train,batch_size, epochs)

p.removeQuestions()
