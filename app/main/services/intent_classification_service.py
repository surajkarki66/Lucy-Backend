import json
import pickle
import numpy as np
import tensorflow as tf

from pathlib import Path
from app.main.utility.voc import voc


class IntentClassificationService(object):

    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        MODELS_DIR = BASE_DIR.joinpath('lucy_models')
        LUCY_MODEL = MODELS_DIR.joinpath('lucy_simple_ann.h5')

        LABELS_DIR = BASE_DIR.joinpath('datasets')
        LABELS = LABELS_DIR.joinpath('labels.pickle')

        self.classifier = tf.keras.models.load_model(LUCY_MODEL)

        with open(LABELS, "rb") as f:
            self.data = pickle.load(f)


    def predict(self, query):
        ques = self.data.getQuestionInNum(query)

        ques = np.array(ques)
        ques = np.expand_dims(ques, axis = 0)
    
        y_pred = self.classifier.predict(ques)
        res = np.argmax(y_pred, axis=1)
        return res
        

    def get_response(self, results):
        intent = self.data.index2intents[int(results)]
        response = self.data.response[intent]
        return response


        

    

        

        
