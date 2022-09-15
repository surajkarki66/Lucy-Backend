import re
import json
import random
import torch
import pickle
import numpy as np

from pathlib import Path
from transformers import DistilBertTokenizer, DistilBertModel, RobertaTokenizer, RobertaModel, AutoModel, BertTokenizerFast

from app.main.config import settings
from app.main.infrastructure.lucy.Lucy import Lucy


class IntentClassificationService(object):

    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        MODELS_DIR = BASE_DIR.joinpath('lucy_models')
        LUCY_MODEL = None
        PRETRAINED_MODEL = None
       
        if settings.MODEL_NAME == "bert":
            LUCY_MODEL = MODELS_DIR.joinpath('lucy_bert.pth')
            PRETRAINED_MODEL = AutoModel.from_pretrained("bert-base-uncased")
            self.TOKENIZER = BertTokenizerFast.from_pretrained("bert-base-uncased")
        if settings.MODEL_NAME == "roberta":
            LUCY_MODEL = MODELS_DIR.joinpath('lucy_roberta.pth')
            PRETRAINED_MODEL = RobertaModel.from_pretrained("roberta-base")
            self.TOKENIZER = RobertaTokenizer.from_pretrained("roberta-base")
        if settings.MODEL_NAME == "distilbert":
            LUCY_MODEL = MODELS_DIR.joinpath('lucy_distilbert.pth')
            PRETRAINED_MODEL = DistilBertModel.from_pretrained("distilbert-base-uncased")
            self.TOKENIZER = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

        # TODO: Fetching below from database
        LABELS_DIR = BASE_DIR.joinpath('datasets')
        INTENTS_TO_RESPONSE = LABELS_DIR.joinpath('intents.json')
        LABELS = LABELS_DIR.joinpath('labels.json')

        self.model = Lucy(PRETRAINED_MODEL)
        self.model.load_state_dict(torch.load(LUCY_MODEL))

        with open(INTENTS_TO_RESPONSE, "r") as f:
            self.intents_to_response = json.load(f)

        with open(LABELS, "r") as f:
            self.labels = json.load(f)


    def predict(self, query):
        query = re.sub(r'[^a-zA-Z ]+', '', query)
        test_text = [query]

        self.model.eval()
        
        tokens_test_data = self.TOKENIZER(
                        test_text,
                        max_length = 9,
                        padding="max_length",
                        truncation=True,
                        return_token_type_ids=False
                        ) 
        test_seq = torch.tensor(tokens_test_data['input_ids'])
        test_mask = torch.tensor(tokens_test_data['attention_mask'])
        
        pred = None
        with torch.no_grad():
            pred = self.model(test_seq.to(settings.DEVICE), test_mask.to(settings.DEVICE))
        
        pred = pred.detach().cpu().numpy()
        pred = np.argmax(pred)
        
        intent = self.labels[pred]
    
        return intent

    def get_response(self, message): 
        intent = self.predict(message)
        result = None
        links = []
      
        for i in self.intents_to_response['intents']: 
            if i["tag"] == intent:
                result = random.choice(i["responses"])
                break
        return result, i["links"]


        

    

        

        
