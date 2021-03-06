"""Specifies model architecture"""

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import TimeDistributed
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Lambda
from keras.layers import Dropout
from keras.layers import Bidirectional
from keras.optimizers import SGD
from keras import backend as K


def distributed_label(input_shape):
    #model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape))
    m.add(LSTM(16, return_sequences=True))
    m.add(LSTM(8, return_sequences=True))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    # m.add(TimeDistributed(Flatten()))
    # m.add(Flatten())
    #m.add(Dense(1, activation='sigmoid'))
    #specifies optimizer and lossfunctions
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def distributed_label2(input_shape):
    #model architecture
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(50, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def distributed_label3(input_shape):
    #model architecture
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def distributed_label4(input_shape):
    #model architecture
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def distributed_label5(input_shape):
    #model architecture
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def distributed_label6(input_shape):
    #model architecture
    m = Sequential()
    m.add(LSTM(20, return_sequences=True, input_shape=input_shape))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def distributed_label7(input_shape):
    #model architecture
    m = Sequential()
    m.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def distributed_into_one(input_shape):
    # model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape))
    m.add(LSTM(16, return_sequences=True))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.add(Lambda(lambda x: K.max(x, keepdims=True)))
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def singleLabel_1(input_shape):
    # model architecture
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    # specifies optimizer and lossfunctions
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def singleLabel_2(input_shape):
    # model architecture
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape))
    m.add(LSTM(16, return_sequences=True))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    # specifies optimizer and lossfunctions
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def singleLabel_3(input_shape):
    # model architecture
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape))
    m.add(LSTM(16, return_sequences=True))
    m.add(LSTM(8, return_sequences=True))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    # specifies optimizer and lossfunctions
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def singleLabel_HighNumber(input_shape):
    # model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(50, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def singleLabel_HighNumber2(input_shape):
    # model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.4))
    m.add(LSTM(50, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.4))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.4))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def singleLabel_HighNumber3(input_shape):
    # model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(50, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def Model6(input_shape):
    # model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(50, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def Model6a(input_shape):
    # model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(50, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def Model6b(input_shape):
    # model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(50, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def singleLabel_HighNumber4(input_shape):
    # model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(50, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def singleLabel_HighNumber5(input_shape):
    # model architecture
    m = Sequential()
    # m.add(Masking(mask_value=0., input_shape=(InputDataSet.shape[1], InputDataSet.shape[2])))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_8(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_16(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_32(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_64(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_128(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_256(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_8(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_16(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_32(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_64(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_128(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_256(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_8(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_16(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_32(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_64(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_128(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_256(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m



def Model4L_8(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_16(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_32(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_64(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_128(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_256(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_8(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_16(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_32(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_64(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_128(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_256(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m



def Model6L_8(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_16(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_32(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_64(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_128(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_256(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_8td(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_16td(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_32td(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_64td(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_128td(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_256td(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_8td(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_16td(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))

    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_32td(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_64td(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_128td(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_256td(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m



def Model3L_8td(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_16td(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_32td(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_64td(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_128td(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_256td(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m



def Model4L_8td(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_16td(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_32td(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_64td(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_128td(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_256td(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m



def Model5L_8td(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_16td(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_32td(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_64td(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_128td(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_256td(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_8td(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_16td(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_32td(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_64td(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_128td(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_256td(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model_bulb_td(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model_bulb(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model_hour_td(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model_hour(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def Model_pyr_td(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model_pyr(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model_ivpyr_td(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model_ivpyr(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def m2L_kRegu(input_shape, reg):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, kernel_regularizer=reg))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, kernel_regularizer=reg))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def m2L_bRegu(input_shape, reg):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, bias_regularizer=reg))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, bias_regularizer=reg))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def m2L_rRegu(input_shape, reg):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=reg))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=reg))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def m2L_rRegu16(input_shape, reg):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=reg))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=reg))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def m2L_allRegu(input_shape, rreg, breg, kreg):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=rreg, bias_regularizer=breg, kernel_regularizer=kreg))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=rreg, bias_regularizer=breg, kernel_regularizer=kreg))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def m2l_rRegu_nTD(input_shape, rreg):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=rreg))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=rreg))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(1, activation='sigmoid')))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def m2l_16_UpDown(input_shape, rreg=None, breg=None, kreg=None):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=rreg, bias_regularizer=breg, kernel_regularizer=kreg))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2, recurrent_regularizer=rreg, bias_regularizer=breg, kernel_regularizer=kreg))
    m.add(Dropout(0.2))
    m.add(TimeDistributed(Dense(3, activation='sigmoid')))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m



def m5l_64_Rate1(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    sgd = SGD(lr=0.0, momentum=0.9, decay=0.0, nesterov=False)
    m.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['accuracy'])
    return m

def adam(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def rmsprop(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def sgd(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def sgd2(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m



def Model1L_8sgd(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_16sgd(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_32sgd(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_64sgd(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_128sgd(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_256sgd(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_8sgd(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_16sgd(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_32sgd(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_64sgd(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_128sgd(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_256sgd(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_8sgd(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_16sgd(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_32sgd(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_64sgd(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_128sgd(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_256sgd(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m



def Model4L_8sgd(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_16sgd(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_32sgd(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_64sgd(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_128sgd(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_256sgd(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_8sgd(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_16sgd(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_32sgd(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_64sgd(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_128sgd(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_256sgd(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m



def Model6L_8sgd(input_shape):
    m = Sequential()
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_16sgd(input_shape):
    m = Sequential()
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_32sgd(input_shape):
    m = Sequential()
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_64sgd(input_shape):
    m = Sequential()
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_128sgd(input_shape):
    m = Sequential()
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_256sgd(input_shape):
    m = Sequential()
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
    return m

## bidirectional

def Model1L_8bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_16bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_32bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_64bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_128bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model1L_256bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_8bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_16bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_32bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_64bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_128bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model2L_256bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

def Model3L_8bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_16bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_32bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_64bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_128bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model3L_256bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_8bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_16bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_32bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_64bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_128bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model4L_256bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_8bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_16bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_32bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_64bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_128bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model5L_256bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_8bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(8, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_16bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(16, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_32bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(32, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_64bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(64, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_128bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(128, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m


def Model6L_256bi(input_shape):
    m = Sequential()
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Bidirectional(LSTM(256, return_sequences=True, input_shape=input_shape, recurrent_dropout=0.2)))
    m.add(Dropout(0.2))
    m.add(Flatten())
    m.add(Dense(1, activation='sigmoid'))
    m.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return m

modelDict = {
    'singleLabel_1': singleLabel_1,
    'singleLabel_2': singleLabel_2,
    'singleLabel_3': singleLabel_3,
    'singleLabel_HighNumber': singleLabel_HighNumber,
    'singleLabel_HighNumber2': singleLabel_HighNumber2,
    'singleLabel_HighNumber3': singleLabel_HighNumber3,
    'singleLabel_HighNumber4': singleLabel_HighNumber4,
    'singleLabel_HighNumber5': singleLabel_HighNumber5,
    'distributed_label4' : distributed_label4,
    'distributed_label3' : distributed_label3,
    'distributed_label2' : distributed_label2,
    'distributed_label' : distributed_label,
    'distributed_label5' : distributed_label5,
    'distributed_label6' : distributed_label6,
    'distributed_label7' : distributed_label7,
    'Model6a' : Model6a,
    'Model6b': Model6b,
    'Model6': Model6,
    ### wide deep
    'Model1L_8' : Model1L_8,
    'Model2L_8': Model2L_8,
    'Model3L_8': Model3L_8,
    'Model1L_16': Model1L_16,
    'Model2L_16': Model2L_16,
    'Model3L_16': Model3L_16,
    'Model1L_32': Model1L_32,
    'Model2L_32': Model2L_32,
    'Model3L_32': Model3L_32,
    'Model1L_64': Model1L_64,
    'Model2L_64': Model2L_64,
    'Model3L_64': Model3L_64,
    'Model1L_128': Model1L_128,
    'Model2L_128': Model2L_128,
    'Model3L_128': Model3L_128,
    'Model1L_256': Model1L_256,
    'Model2L_256': Model2L_256,
    'Model3L_256': Model3L_256,
    'Model4L_8': Model4L_8,
    'Model5L_8': Model5L_8,
    'Model6L_8': Model6L_8,
    'Model4L_16': Model4L_16,
    'Model5L_16': Model5L_16,
    'Model6L_16': Model6L_16,
    'Model4L_32': Model4L_32,
    'Model5L_32': Model5L_32,
    'Model6L_32': Model6L_32,
    'Model4L_64': Model4L_64,
    'Model5L_64': Model5L_64,
    'Model6L_64': Model6L_64,
    'Model4L_128': Model4L_128,
    'Model5L_128': Model5L_128,
    'Model6L_128': Model6L_128,
    'Model4L_256': Model4L_256,
    'Model5L_256': Model5L_256,
    'Model6L_256': Model6L_256,
    #### time distributed
    'Model1L_8td' : Model1L_8td,
    'Model2L_8td': Model2L_8td,
    'Model3L_8td': Model3L_8td,
    'Model1L_16td': Model1L_16td,
    'Model2L_16td': Model2L_16td,
    'Model3L_16td': Model3L_16td,
    'Model1L_32td': Model1L_32td,
    'Model2L_32td': Model2L_32td,
    'Model3L_32td': Model3L_32td,
    'Model1L_64td': Model1L_64td,
    'Model2L_64td': Model2L_64td,
    'Model3L_64td': Model3L_64td,
    'Model1L_128td': Model1L_128td,
    'Model2L_128td': Model2L_128td,
    'Model3L_128td': Model3L_128td,
    'Model1L_256td': Model1L_256td,
    'Model2L_256td': Model2L_256td,
    'Model3L_256td': Model3L_256td,
    'Model4L_8td': Model4L_8td,
    'Model5L_8td': Model5L_8td,
    'Model6L_8td': Model6L_8td,
    'Model4L_16td': Model4L_16td,
    'Model5L_16td': Model5L_16td,
    'Model6L_16td': Model6L_16td,
    'Model4L_32td': Model4L_32td,
    'Model5L_32td': Model5L_32td,
    'Model6L_32td': Model6L_32td,
    'Model4L_64td': Model4L_64td,
    'Model5L_64td': Model5L_64td,
    'Model6L_64td': Model6L_64td,
    'Model4L_128td': Model4L_128td,
    'Model5L_128td': Model5L_128td,
    'Model6L_128td': Model6L_128td,
    'Model4L_256td': Model4L_256td,
    'Model5L_256td': Model5L_256td,
    'Model6L_256td': Model6L_256td,
    #### hour bulb etc
    'Model_ivpyr': Model_ivpyr,
    'Model_ivpyr_td': Model_ivpyr_td,
    'Model_pyr': Model_pyr,
    'Model_pyr_td': Model_pyr_td,
    'Model_hour': Model_hour,
    'Model_hour_td': Model_hour_td,
    'Model_bulb': Model_bulb,
    'Model_bulb_td': Model_bulb_td,
    #### regularization models
    'm2l_bRegu' : m2L_bRegu,
    'm2l_kRegu' : m2L_kRegu,
    'm2l_rRegu' : m2L_rRegu,
    'm2l_allRegu' : m2L_allRegu,
    'm2l_rRegu_nTD' : m2l_rRegu_nTD,
    'm2L_rRegu16' : m2L_rRegu16,
    #### UpDownLabel Models
    'm2l_16_UpDown' : m2l_16_UpDown,

    ### Model for Learning rates
    'm5l_64_Rate1' : m5l_64_Rate1,
    'adam' : adam,
    'rmsprop' : rmsprop,
    'sgd' : sgd,
    'sgd2' : sgd2,

    ### sgd
    'Model1L_8sgd' : Model1L_8sgd,
    'Model2L_8sgd': Model2L_8sgd,
    'Model3L_8sgd': Model3L_8sgd,
    'Model1L_16sgd': Model1L_16sgd,
    'Model2L_16sgd': Model2L_16sgd,
    'Model3L_16sgd': Model3L_16sgd,
    'Model1L_32sgd': Model1L_32sgd,
    'Model2L_32sgd': Model2L_32sgd,
    'Model3L_32sgd': Model3L_32sgd,
    'Model1L_64sgd': Model1L_64sgd,
    'Model2L_64sgd': Model2L_64sgd,
    'Model3L_64sgd': Model3L_64sgd,
    'Model1L_128sgd': Model1L_128sgd,
    'Model2L_128sgd': Model2L_128sgd,
    'Model3L_128sgd': Model3L_128sgd,
    'Model1L_256sgd': Model1L_256sgd,
    'Model2L_256sgd': Model2L_256sgd,
    'Model3L_256sgd': Model3L_256sgd,
    'Model4L_8sgd': Model4L_8sgd,
    'Model5L_8sgd': Model5L_8sgd,
    'Model6L_8sgd': Model6L_8sgd,
    'Model4L_16sgd': Model4L_16sgd,
    'Model5L_16sgd': Model5L_16sgd,
    'Model6L_16sgd': Model6L_16sgd,
    'Model4L_32sgd': Model4L_32sgd,
    'Model5L_32sgd': Model5L_32sgd,
    'Model6L_32sgd': Model6L_32sgd,
    'Model4L_64sgd': Model4L_64sgd,
    'Model5L_64sgd': Model5L_64sgd,
    'Model6L_64sgd': Model6L_64sgd,
    'Model4L_128sgd': Model4L_128sgd,
    'Model5L_128sgd': Model5L_128sgd,
    'Model6L_128sgd': Model6L_128sgd,
    'Model4L_256sgd': Model4L_256sgd,
    'Model5L_256sgd': Model5L_256sgd,
    'Model6L_256sgd': Model6L_256sgd,


    ## bi
    'Model1L_8bi': Model1L_8bi,
    'Model2L_8bi': Model2L_8bi,
    'Model3L_8bi': Model3L_8bi,
    'Model4L_8bi': Model4L_8bi,
    'Model5L_8bi': Model5L_8bi,
    'Model6L_8bi': Model6L_8bi,

    'Model1L_16bi': Model1L_16bi,
    'Model2L_16bi': Model2L_16bi,
    'Model3L_16bi': Model3L_16bi,
    'Model4L_16bi': Model4L_16bi,
    'Model5L_16bi': Model5L_16bi,
    'Model6L_16bi': Model6L_16bi,

    'Model1L_32bi': Model1L_32bi,
    'Model2L_32bi': Model2L_32bi,
    'Model3L_32bi': Model3L_32bi,
    'Model4L_32bi': Model4L_32bi,
    'Model5L_32bi': Model5L_32bi,
    'Model6L_32bi': Model6L_32bi,

    'Model1L_64bi': Model1L_64bi,
    'Model2L_64bi': Model2L_64bi,
    'Model3L_64bi': Model3L_64bi,
    'Model4L_64bi': Model4L_64bi,
    'Model5L_64bi': Model5L_64bi,
    'Model6L_64bi': Model6L_64bi,

    'Model1L_128bi': Model1L_128bi,
    'Model2L_128bi': Model2L_128bi,
    'Model3L_128bi': Model3L_128bi,
    'Model4L_128bi': Model4L_128bi,
    'Model5L_128bi': Model5L_128bi,
    'Model6L_128bi': Model6L_128bi,

    'Model1L_256bi': Model1L_256bi,
    'Model2L_256bi': Model2L_256bi,
    'Model3L_256bi': Model3L_256bi,
    'Model4L_256bi': Model4L_256bi,
    'Model5L_256bi': Model5L_256bi,
    'Model6L_256bi': Model6L_256bi

}