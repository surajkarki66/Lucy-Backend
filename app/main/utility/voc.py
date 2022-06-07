from spacy.lang.en import English

nlp = English()
tokenizer = nlp.Defaults.create_tokenizer(nlp)

class voc:
    def __init__(self):
        self.num_words= 1  # 0 is reserved for padding 
        self.num_intents=0
        self.intents={}
        self.index2intents={}
        self.questions={}
        self.word2index={}
        self.response={}
  
    def addWord(self,word):
        if word not in self.word2index:
            self.word2index[word] = self.num_words
            self.num_words += 1

    def addIntents(self,intent):
        if intent not in self.intents:
            self.intents[intent]=self.num_intents
            self.index2intents[self.num_intents]=intent
            self.num_intents+=1

    def addQuestion(self, question, answer):
        self.questions[question]=answer
        words=self.tokenization(question)
        for  wrd in words:
            self.addWord(wrd)
                 
    def tokenization(self,ques):
        tokens = tokenizer(ques)
        token_list = []
        for token in tokens:
            token_list.append(token.lemma_)
        return token_list
    
    def getIndexOfWord(self,word):
        return self.word2index[word]
    
    def getQuestionInNum(self, ques):
        words=self.tokenization(ques)
        tmp=[ 0 for i in range(self.num_words)]
        for wrds in words:
            tmp[self.getIndexOfWord(wrds)]=1
        return tmp
    
 
    def getIntent(self, intent):
        tmp=[0.0 for i in range(self.num_intents)]
        tmp[self.intents[intent]]=1.0
        return tmp
    
    def getVocabSize(self):
        return self.num_words
    
    def getIntentSize(self):
        return self.num_intents

    def addResponse(self, intent, responses):
        intent = intent["intent"]
        self.response[intent]=responses
        
      