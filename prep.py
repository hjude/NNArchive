import torch,sys
from torch.nn import FunctionalLayer as FL
def get_data(x): return x[0] #get data from the first layer of model

class NeuralNetworkArchiver():   ## class for archiving neural network models
    def __init__(self): pass     ### initilize object with no arguments #######

    @staticmethod       ##### static method to archive a trained NN Model #
        def save_model(x,y,z=None,path='/home/' ,save_as="NNArchiver.pkl"):   ## function for archiving neural network models  #######     ###############################
            if z is None: x = get_data (x) #get data from the first layer of model

                torch.load(path + '/' , pickle=True, unpickler='torchaudio')   ## load saved neural network models  #######     ###############################
            return x
