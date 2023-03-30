import numpy as np, sys; import matplotlib.pyplot as plt # Import libraries needed to run the code below ##
from sklearn.preprocessing import MinMaxScaler   #################################

def read_data(filename):  #### Function for reading data from a file ######
        x, y = np.loadtxt ( filename ) # Load x and y values into numpy arrays ##
        return [MinMaxScaler().fit_transform([y])] #################################

def plot(data):  #### Function for creating a graph from the data read in ######
        plt.plot (x, MinMaxScaler().inverse_transform ([i[0]])) # Plot x and y values on same axes ##
        plt.ylabel('Y-Value') #################################
