#!/usr/bin/env python
"""
The SpanSelector is a mouse widget to select a xmin/xmax range and plot the
detail view of the selected region in the lower axes
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np
from sys import stdout
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

import csv
import matplotlib.pyplot as plt
### Extract data from CSV ###
with open('temperatures.csv', 'rb') as n:
    reader = csv.reader(n)
    reader.next()
    dates = []
    freq = []
    freq1 = []
    for row in reader:
        if row==[]:
         break        
        values = row
        dates.append(values[0])
        freq.append(values[1])
        freq1.append(values[2])
### Do plot ###
false_x = [x for x in range(len(dates))]
#plt.plot(false_x,freq, 'o-')
#plt.plot(false_x,freq1, 'o-')
plt.xticks(range(len(dates)), (dates), rotation=45)
# plt.axis([xmin, xmax, ymin, ymax]) - sets axes limits on graph
plt.axis([0, 50, 0, 100])



def hzfunc(label):
    hzdict = {'Mark Steady': highlight ,'Mark Unsteady':dehighlight}   
    global func
    func=hzdict[label]
    #hzdict = {'Demark':dehighlight(xmin , xmin ) }
    #ydata = hzdict[label]
    #line2.set_ydata(ydata)
    #plt.draw()
    #exec(hzdict[label])
    #return hzfunc[label]

def in_take(xmin[],xmax[]):
    global func
    func(xmin[],xmax[])


def onselect(xmin[], xmax[]):
    indmin, indmax = np.searchsorted(x, (xmin[], xmax[]))
    indmax = min(len(x)-1, indmax)

    thisx = x[indmin:indmax]
    thisy = y[indmin:indmax]
    line2.set_data(thisx, thisy)
    line3.set_data(thisx, thisy)
    ax2.set_xlim(thisx[0], thisx[-1])
    ax2.set_ylim(thisy.min(), thisy.max())    
    #ax.axvspan(thisx[0], thisx[-1], color='black', alpha=0.5)    
    fig.canvas.draw()
    
def highlight(xmin[], xmax[]):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x)-1, indmax)

    thisx = x[indmin:indmax]
    #thisy = y[indmin:indmax]
    #line2.set_data(thisx, thisy)
    #ax2.set_xlim(thisx[0], thisx[-1])
    #ax2.set_ylim(thisy.min(), thisy.max())
    ax2.axvspan(thisx[0], thisx[-1], color='yellow', alpha=1)    
    #ax2 = fig.add_subplot(212, axisbg='#FFFFCC')
    #line3, = ax2.plot(x, y ,'-')
    steadyxmin = thisx[0]
    steadyxmax = thisx[-1]
    print steadyxmax
    print steadyxmin        
    fig.canvas.draw()
            
    
def dehighlight(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x)-1, indmax)

    thisx = x[indmin:indmax]
    print 'dfd'
    #thisy = y[indmin:indmax]
    #line2.set_data(thisx, thisy)
    #ax2.set_xlim(thisx[0], thisx[-1])
    #ax2.set_ylim(thisy.min(), thisy.max())
    #ax2.axvspan(thisx[0], thisx[-1], color='blue', alpha=0.5)
    #ax2.axvspan(thisx[0], thisx[-1], color='red', alpha=0.5)
    #ax2.axvspan(thisx[0], thisx[-1], color='lime', alpha=0.5)
    ax2.axvspan(thisx[0], thisx[-1], color='white', alpha=1)    
    #ax2 = fig.add_subplot(212, axisbg='#FFFFCC')
    #line4, = ax2.plot(x, y , '-')
    steadyxmin = thisx[0]
    steadyxmax = thisx[-1]
    print steadyxmax
    print steadyxmin        
    fig.canvas.draw()
        
# set useblit True on gtkagg for enhanced performance

if __name__=='__main__':
    fig = plt.figure(figsize=(15,10))
    ax = fig.add_subplot(211, axisbg='white')
#######################################################################################################################################################    
    #x = np.arange(0.0, 5.0, 0.01)
    #y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))
    x = false_x
    y = freq
    ax.plot(false_x,freq, 'o-')
    ax.plot(false_x,freq1, 'o-')
#######################################################################################################################################################    
    #ax.plot(x, y, '-')
    ax.set_ylim(0,100)
    ax.set_title('Press left mouse button and drag to test')
    
    ax2 = fig.add_subplot(212, axisbg='white')
    line2[], =ax2.plot(x, freq, '-')
    #line3,=ax2.plot(x, freq1, '-')
#################RADIO BUTTON CODE #######################################    
    axcolor = 'white'
    rax = plt.axes([0.92, 0.01, 0.1, 0.1], axisbg=axcolor)
    radio = RadioButtons(rax, ('Mark Steady', 'Mark Unsteady'))  
    radio.on_clicked(hzfunc)   
##########################################################################

#########################SPANNER CODE ####################################    
    span = SpanSelector(ax, onselect, 'horizontal', useblit=True,rectprops=dict(alpha=0.5, facecolor='red') )
    print span
    print dir(span)
    func=highlight
    span1 = SpanSelector(ax2, in_take, 'horizontal', useblit=True,rectprops=dict(alpha=0.5) )
    #exec(span1)
    #span2 = SpanSelector(ax2, dehighlight, 'horizontal', useblit=False,rectprops=dict(alpha=0.5, facecolor='yellow') )
    #exec(span2)

###########################################################################
    plt.show()
    

