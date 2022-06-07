import json
import numpy as np
import tensorflow as tf

from pathlib import Path
from app.main.utility.voc import Voc


class IntentClassificationService(object):

    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        MODELS_DIR = BASE_DIR.joinpath('lucy_models')
        LUCY_MODEL = MODELS_DIR.joinpath('lucy_simple_ann')

       

        self.classifier = tf.keras.models.load_model(LUCY_MODEL)
        self.voc = Voc()

    def preprocess_input_text(self,input_text):
        sequences = self.voc.tokenize([input_text])
        padded_sequences = self.voc.add_padding(sequences)
        return padded_sequences

    def classify_intent(self, query: str) -> str:
        padded_sequences = self.preprocess_input_text(query)
        y_pred = self.classifier.predict(np.expand_dims(padded_sequences[0], axis=0))[0]
        intent = self.voc.index2intents(int(np.argmax(y_pred)))
        return intent

    def get_response(self, query):
        intent = self.classify_intent(query)
        res = self.voc.intent2response(intent)
        return res


   

    

    
