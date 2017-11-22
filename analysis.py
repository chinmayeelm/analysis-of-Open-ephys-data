"""written by Chinmayee.

Code to analyse Open-ephys recording data stored in hdf5 file format
"""

import h5py
import numpy as np
import scipy.signal
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
# from scipy.signal import butter, lfilter

'''
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
'''

f = h5py.File('../OEdata/2017-11-10_CHresponse/experiment_1.nwb', 'r')

data = f["acquisition"]["timeseries"]["continuous"]["processor100_100"]["recording1"]["data"]
time = f["acquisition"]["timeseries"]["continuous"]["processor100_100"]["recording1"]["timestamps"]


rec = data[:, 0]

order = 6
fs = 30000.0
nyq = 0.5 * fs
lowcut = 150.0 * 2 * np.pi / nyq
highcut = 1000.0 * 2 * np.pi / nyq

b, a = scipy.signal.butter(
    order, [lowcut, highcut], btype='bandpass', analog=False, output='ba')
filtered_data = scipy.signal.lfilter(b, a, rec, zi=None)

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
