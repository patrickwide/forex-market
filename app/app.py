import math
import random
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas_datareader as data_reader
from tensorflow import sigmoid
import multiprocessing

from tqdm import tqdm_notebook, tqdm
from collections import deque
from tensorflow.python.keras.models import  Sequential
from rl.memory import SequentialMemory
from tensorflow.python.keras.layers import  Dense, Activation, Flatten
from tensorflow.python.keras.layers import  Dense
from tensorflow.python.keras.layers import  LSTM
from tensorflow.python.keras.layers import  Dropout
from tensorflow.python.keras.layers import  *
from tensorflow.python.keras.callbacks import  EarlyStopping
from tensorflow import train
from tensorflow.keras.optimizers import Adam


def Ai_Trader():
    def __init__(self, state_size, action_space=3, model_name="AITrader"):
        self.state_size = state_size
        self.action_space = action_space
        self.memory = deque(maxlen=2000)
        self.inventory = []
        self.model_name = model_name
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_final = 0.01
        self.epsilon_decay = 0.995
        self.model = self.model_builder()


    def model_builder(self):
        model = Sequential()
        model.add(Flatten(input_shape=(0, 0)))
        model.add(Dense(units=32, activation='relu', input_dim=self.state_size))
        model.add(Dense(units=64, activation='relu'))
        model.add(Dense(units=126, activation='relu'))
        model.add(Dense(units=self.action_space, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(learning_rate=0.001))

        return model

    def trade(self, state):
        if random.random() <= self.epsilon:
            return random.randrange(self.action_space)

        else:
            actions = self.model.predict(state)
            return np.argmax(actions[0])

    def batch_train(self, batch_size):

        batch = []
        for i in range(len(self.memory) - batch_size + 1, len(self.memmory)):
            batch.append(self.memory[i])

        for state, action,reward,next_state,done in batch:
            reward = reward

            if not done:
                reward = reward + self.gamma * np.amax(self.model.predict(next_state)[0])

            target = self.model.predict(state)
            target[0][action] = reward

            self.model.fit(state, target, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_final:
            self.epsilon *= self.epsilon_decay


#Stock Market Data Preprocessing
def sigmoid(x):
  return 1, (1 + math.exp(-x))


def stocks_price_format(n):
    if n < 0:
        return "- # {0:2f}".format(abs(n))
    else:
        return "$ {0:2f}".format(abs(n))


def dataset_loader(stock_name):
    dataset = data_reader.DataReader(stock_name, data_source="yahoo")

    start_date = str(dataset.index[0]).split()[0]
    end_date = str(dataset.index[1]).split()[0]

    close = dataset['Close']

    return close


def state_creater(date,timestamp,window_size):
    starting_id = timestamp - window_size + 1


    #When the starting_id is positive we create a state
    if starting_id <= 0:
        print("go on")


    # if it is negative we append the info until we get to the window_size
    else:
        print()



























































