import tensorflow as tf

from pathlib import Path
from tensorflow.keras import layers, models

from app.main.utility.voc import voc

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
MODELS_DIR = BASE_DIR.joinpath('lucy_models')
LUCY_MODEL = MODELS_DIR.joinpath('lucy_simple_ann.h5')


class SimpleANN:
    def __init__(self, input_dim):

        self.model = models.Sequential()

        # adding first layer
        self.model.add(layers.Dense(units = 12, input_dim = input_dim))
        self.model.add(layers.Activation('relu'))

        #adding 2nd hidden layer
        self.model.add(layers.Dense(units = 8))
        self.model.add(layers.Activation('relu'))

        #adding output layer
        self.model.add(layers.Dense(units = 37))
        self.model.add(layers.Activation('softmax'))
        
        self.model.summary()

    def compile(self):
        # Compiling the ANN
        self.model.compile(optimizer = 'adam', loss ='categorical_crossentropy', metrics = ['accuracy'])

    def train(self, x_train, y_train, batch_size, epochs):
        # Fitting the ANN model to training set
        self.model.fit(x_train, y_train, batch_size = batch_size, epochs = epochs)
        self.model.save(LUCY_MODEL)

      
       



