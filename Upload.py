import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

freqs = np.arange(2, 20, 3)

ax = plt.subplot(111)
plt.subplots_adjust(bottom=0.2)



class Index:
    ind = 0
    def next(self, event):
        os.system(' > temp.csv')
    def prev(self, event):
        os.system ('python findfiles.py')

callback = Index()
axprev = plt.axes([0.10, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Save')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Upload')
bprev.on_clicked(callback.prev)

plt.show()

