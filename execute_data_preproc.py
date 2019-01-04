from Libraries import configuration
from Libraries import data_import as dataImport
from Libraries import data_preprocessing as dataPreproc
from Libraries import prepare_csv as csv
import pickle

from Libraries import log_setup as logSetup



projectName = 'Window10s_pad'
callDataset = '1051'
config = configuration.getConfig(projectName, callDataset)

# Setup Logger
logSetup.configureLogfile(config.logPath, config.logName)
logSetup.writeLogfileHeader(config)

# Import verified Time Series Data with Nadines Libraries
X_ts, labels = dataImport.loadVerifiedBrakeData(config.eedPath, config.eecPath, config.datasetNumber)
balance = 50
# X_ts, labels = dataPreproc.balanceDataDaniel(X_ts, labels, balance)
X_ts = dataPreproc.smoothingEedData(X_ts)
eec = csv.eec_csv_to_eecData(config.eecPath, callDataset)

labels = dataPreproc.getTimeDistributedLabels(eec, X_ts)

# data preproc with differentiatedTruncation
#target_list = [(5, 5)]
#part = ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center']
#Data = dataPreproc.truncate_differentiated(X_ts, labels, part, target_list)

# data preproc with sliding window
#w_size = 10 # [s]
#hop = 1# [s]
#Data = dataPreproc.windowData_all(X_ts, labels, w_size, hop, discard=False)

# data preproc with one window
part = 'center'
duration = 10
Data = dataPreproc.truncate_all(X_ts, labels, duration, part, discard=False)

pickle.dump(Data, open(config.savePath + projectName + '/' + projectName + '.p', "wb"))
