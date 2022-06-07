import pickle
import numpy as np

from pathlib import Path

from app.main.utility.voc import voc

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATASET_DIR = BASE_DIR.joinpath('datasets')
LABEL_DIR = DATASET_DIR.joinpath('labels.pickle')

class ProcessDatasetService:
    def __init__(self,raw_data):
        self.data = voc()
        self.raw_data = raw_data

        for intent in self.raw_data["intents"]:
            intent_tag=intent["intent"]
            self.data.addIntents(intent_tag)

            for question in intent["questions"]: 
                ques=question.lower()
                self.data.addQuestion(ques,intent_tag)

    def split_dataset(self):
        x_train=[self.data.getQuestionInNum(x) for x in self.data.questions]
        y_train=[self.data.getIntent(self.data.questions[x]) for x in self.data.questions]
        x_train = np.array(x_train)
        y_train = np.array(y_train)
        return x_train,y_train


    def removeQuestions(self):
        self.data.questions = {}
        for intent in self.raw_data["intents"]:
            intent_tag = intent["intent"]
            response=[]
            for resp in intent["responses"]: 
                response.append(resp)
       
            self.data.addResponse(intent,response)
                
        with open(LABEL_DIR, 'wb') as handle:
            pickle.dump(self.data, handle)
