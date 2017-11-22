"""written by Chinmayee.

Code to analyse Open-ephys recording data stored in hdf5 file format
"""

import h5py
import numpy as np
import scipy
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from scipy.signal import butter, filtfilt


f = h5py.File('../OEdata/2017-11-10_CHresponse/experiment_1.nwb', 'r')

data = f["acquisition"]["timeseries"]["continuous"]["processor100_100"]["recording1"]["data"]
time = f["acquisition"]["timeseries"]["continuous"]["processor100_100"]["recording1"]["timestamps"]


rec = data[:, 0]

order = 5
fs = 30000.0
nyq = 0.5 * fs
lowcut = 150.0/nyq
highcut = 1000.0/nyq

b, a = butter(
    order, [lowcut, highcut], btype='bandpass', analog=False, output='ba')
filtered_data = filtfilt(b, a, rec)

# filtered_data = butter_bandpass_filter(rec, lowcut, highcut, fs, order=6)

app = QtGui.QApplication([])
# win = pg.GraphicsWindow(title="Response to tactile stimulus on cephalic hair")
# win.resize(1000, 600)
# win.setWindowTitle('Suction electrode recording from VNC')
pg.setConfigOptions(antialias=True)
# p1 = win.addPlot(time, filtered_data, title="Suction electrode recording from VNC")
p1 = pg.plot(time, filtered_data,
             title="Suction electrode recording from VNC(filtered)")
p1.setLabel('left', "Y Axis", units='uV')
p1.setLabel('bottom', "X Axis", units='time')

p2 = pg.plot(time, rec, title="Suction electrode recording from VNC")
p2.setLabel('left', "Y Axis", units='uV')
p2.setLabel('bottom', "X Axis", units='time')


QtGui.QApplication.instance().exec_()
