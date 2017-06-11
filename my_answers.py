import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
import re


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    # x input of window series
    X = [series[i:i + window_size] for i in range(0, len(series) - window_size)]
    # y output of window series, correponding to input x
    y = [series[i + window_size] for i in range(0, len(series) - window_size)]

    # reshape each
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    #sequentail model
    model = Sequential()

    # create LSTM layer input size window_size, step_size
    model.add(LSTM(5, input_shape=(window_size, step_size)))

    # add dense of 1
    model.add(Dense(1))

    #intialize optimizer
    optimizer = keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

    # compile the model
    model.compile(loss='mean_squared_error', optimizer=optimizer)


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text

    uniq_char = list(set(text))
    print(uniq_char)

    # remove as many non-english characters and character sequences as you can
    text = re.sub(r'[^a-zA-Z.,!?\']', ' ', text)

    # shorten any extra dead space created above
    text = text.replace('  ', ' ')
    print(text)




### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    # parse intput
    inputs = [text[i:i + window_size] for i in range(0, len(text) - window_size)]
    # parse output
    outputs = [text[i + window_size] for i in range(0, len(text) - window_size)]
    

    
    return inputs,outputs
