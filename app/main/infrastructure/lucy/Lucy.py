import torch
import torch.nn as nn

class Lucy(nn.Module):
  def __init__(self, pretrained_model):      
       super(Lucy, self).__init__()    
       self.len_labels = 38   
       self.pretrained_model = pretrained_model 
      
       # dropout layer
       self.dropout = nn.Dropout(0.2)
      
       # relu activation function
       self.relu =  nn.ReLU()     

       # dense layer       
       self.fc1 = nn.Linear(768,512)       
       self.fc2 = nn.Linear(512,256)       
       self.fc3 = nn.Linear(256,self.len_labels)    

       #softmax activation function
       self.softmax = nn.LogSoftmax(dim=1)      
      
  #define the forward pass
  def forward(self, sent_id, mask):      
      #pass the inputs to the model  
      cls_hs = self.pretrained_model(sent_id, attention_mask=mask)[0][:,0]
      
      x = self.fc1(cls_hs)
      x = self.relu(x)
      x = self.dropout(x)
      
      x = self.fc2(x)
      x = self.relu(x)
      x = self.dropout(x)      

      # output layer
      x = self.fc3(x)
   
      # apply softmax activation
      x = self.softmax(x)     
      return x