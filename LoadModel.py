#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pickle


# In[4]:


# modelFilePath: a model object ending in 'pkl' format in the Models directory 
def loadModelFromFile(modelFilePath):

    model = pickle.load(open(modelFilePath, 'rb'))

    return model

