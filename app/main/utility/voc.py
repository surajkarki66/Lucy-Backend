import json
import tensorflow as tf

from pathlib import Path


class Voc:
    def __init__(self):
        self.VOCAB_SIZE = 1000
        self.OOV_TOKEN = "<OOV>"
        self.MAX_LEN = 20
      
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        DATA_DIR = BASE_DIR.joinpath('datasets')
        DATA = DATA_DIR.joinpath('data.json')

        LABELS_DIR = BASE_DIR.joinpath('datasets')
        LABELS = LABELS_DIR.joinpath('labels.json')

        with open(LABELS) as file:
            data = json.load(file)
            self.labels = data["intent_labels"]

        with open(DATA) as file:
            data = json.load(file)
            self.intents = data["intents"]
    
    def tokenize(self, input_text):
        tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=self.VOCAB_SIZE, oov_token=self.OOV_TOKEN)
        tokenizer.fit_on_texts(input_text)
        word_index = tokenizer.word_index
        sequences = tokenizer.texts_to_sequences(input_text)
        return sequences

    def add_padding(self, sequences):
        padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, truncating='post', maxlen=self.MAX_LEN)
        return padded_sequences


    def index2intents(self, index):
        intent = self.labels[index]
        return intent

    def intent2response(self, intent_label):
        for intent in self.intents:
            if(intent["intent"] == intent_label):
                return intent["responses"]




