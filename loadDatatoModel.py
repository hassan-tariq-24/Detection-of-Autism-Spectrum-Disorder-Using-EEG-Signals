import os
import pandas as pd

import numpy as np
import math

# mne imports
import mne
from mne import io
from mne.datasets import sample

# EEGNet-specific imports
from EEGModels import EEGNet
from tensorflow.keras import utils as np_utils
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras import backend as K

# PyRiemann imports
from pyriemann.estimation import XdawnCovariances
from pyriemann.tangentspace import TangentSpace
from pyriemann.utils.viz import plot_confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 

# tools for plotting confusion matrices
from matplotlib import pyplot as plt

#Checking Working Directory
os.getcwd()
import scipy.io

os.chdir("D:\\aaDataSet\\data")
current_dir = os.getcwd()
j=1

channelOne = pd.DataFrame()

for i in range(1,16):
    subject = "SBJ{j}".format(j= j)
    currentDir = os.chdir("D:\\aaDataSet\\data\\" + "{tmpSub}".format(tmpSub=subject))
    j = j+1 
    # In Folder of SUbject [SBJ]
    sessions = "S0"
    current_dir = os.getcwd()
    indexInfo = {'1':[], '2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[]}
    for l in range(1,8):
        currentSession = "S0{l}".format(l=l)
        # currentSession  will Alterate
        inSession = os.chdir(current_dir + "\\{currentSession}".format(currentSession=currentSession))
        os.chdir(current_dir + "\\{currentSession}".format(currentSession=currentSession))
        #print(os.getcwd())
        #FINALLY ILTERATING Sessions
        current_dir2 = os.getcwd()
        inTrainFolder = os.chdir(current_dir2 + "\\Train")
        current_dir3 = os.getcwd()
        #print(current_dir3)
        ## CODE FOR OPEN TRAIN GOES Here
        
        
        data = scipy.io.loadmat('trainData.mat')
        data = data['trainData']
        
        # Writing Function to Read Lines of TrainEvents.txt
        
        line = open(os.path.join(os.getcwd(), 'trainEvents.txt'), 'r').readlines()
        
        
        indexCounter = 0
        for i in line:
            indexCounter = indexCounter + 1
            if i == '1\n':
                indexInfo['1'].append(indexCounter)
            elif i == '2\n':
                indexInfo['2'].append(indexCounter)
            elif i == '3\n':
                indexInfo['3'].append(indexCounter)
            elif i == '4\n':
                indexInfo['4'].append(indexCounter)
            elif i == '5\n':
                indexInfo['5'].append(indexCounter)
            elif i == '6\n':
                indexInfo['6'].append(indexCounter)
            elif i == '7\n':
                indexInfo['7'].append(indexCounter)
            elif i == '8\n':
                indexInfo['8'].append(indexCounter)
            print(indexInfo)
        
        
        
        
        
        
        
        
        
        
        
        
