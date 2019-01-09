import pickle
from keras.models import load_model
from Libraries import configuration
from Libraries import log_setup as logSetup
from Libraries import model_setup
from Libraries import data_import as dataImport
from Libraries import data_preprocessing as pp
from Libraries import prepare_csv as csv_read
from Libraries import data_evaluation as d_eval
import pandas as pd
from keras.regularizers import L1L2
import numpy as np
import csv

projectName = 'TestAufschwingen'
callDataset = '1051'
stopId = '1399.1051'
path = '/media/computations/DATA/ExperimentalData/'

config = configuration.getConfig(projectName, callDataset)

# Setup Logger
#logSetup.configureLogfile(config.logPath, config.logName)
##logSetup.writeLogfileHeader(config)

Model_name = 'Diff10Sec_trainedmodel.h5'
model = load_model(Model_name)

dataSetName = 'SmallWindowData.p'
Data = pickle.load(open(dataSetName, 'rb'))
X_ts = Data[0]
labels_td = Data[1]

dropChannels = ['time', 'stopId', 'trg1', 'n1', 'trot1', 'tlin1', 'tlin2', 'tamb1']

COLUMN_ID = 'sliceId'