import h5py
import numpy as np
import scipy
import pyqtgraph

f = h5py.File('../OEdata/2017-11-10_CHresponse/experiment_1.nwb', 'r')

data = f["acquisition"]["timeseries"]["continuous"]["processor100_100"]["recording1"]["data"]
time = f["acquisition"]["timeseries"]["continuous"]["processor100_100"]["recording1"]["timestamps"]

rec = data[:,0]
pyqtgraph.plot(time, rec)
