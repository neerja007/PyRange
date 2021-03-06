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
import findfiles
### Extract data from CSV ###
the_choosen_one = findfiles.Window.openFileOfItem
print the_choosen_one
with open('temperatures.csv', 'rb') as n:
	reader = csv.reader(n)
	reader.next()
    
	dates = []
	c=0
	dim=0
	for row in reader:
		if row==[]:
			break
		
		c+=1		
		values = row

		dim=len(row)-1
       
		
		dates.append(values[0])
		
freq = [[ 0 for y in xrange(dim)] for x in xrange(c)]		       
    	

with open('temperatures.csv', 'rb') as n1:
	reader1 = csv.reader(n1)
	reader1.next()
    
	
	
	k=0
	for row1 in reader1:
		if row1==[]:
			break
		values = row1
		for num1 in range(1,dim+1):
			freq[k][num1-1] = values[num1]
		k+=1	
				

 

### Do plot ###
false_x = [x for x in range(len(dates))]
for ch1 in range(0,dim):	
	temp = []
	for ch in range(0,c):
		temp.append(freq[ch][ch1])
	plt.plot(false_x,temp, 'o-')
	plt.xticks(range(len(dates)), (dates), rotation=80)
#plt.yticks(range(len(temp)), (temp), rotation=0)
# plt.axis([xmin, xmax, ymin, ymax]) - sets axes limits on graph
	
	print temp
	temp1 = temp
	temp1.sort()
	ymin = int(temp[0])
	ymax = int(temp[c-1])
	plt.axis([0, 50, ymin, ymax])



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

def in_take(xmin,xmax):
    global func
    func(xmin,xmax)


def onselect(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x)-1, indmax)

    thisx = x[indmin:indmax]
    thisy = y[indmin:indmax]
    line.set_data(thisx, thisy)
    #line3.set_data(thisx, thisy)
    ax2.set_xlim(thisx[0], thisx[-1])
    #ax2.set_ylim(thisy.min(), thisy.max())    
    #ax.axvspan(thisx[0], thisx[-1], color='black', alpha=0.5)    
    fig.canvas.draw()
    
def highlight(xmin, xmax):
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
    fig = plt.figure(figsize=(25,15))
    ax = fig.add_subplot(211, axisbg='white')
#######################################################################################################################################################    
    #x = np.arange(0.0, 5.0, 0.01)
    #y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))
    x = false_x
    ax2 = fig.add_subplot(212, axisbg='white')   
    for ch1 in range(0,dim):	
	temp = []
	for ch in range(0,c):
		temp.append(freq[ch][ch1])
	#ax.xticks(range(len(dates)), (dates), rotation=80)
    	ax.plot(false_x,temp, 'o-')
        y = temp
        ax.set_ylim(0,100)
        ax.set_title('Press left mouse button and drag to test')
    

        line, =ax2.plot(x, y, 'o-')
	   
#################RADIO BUTTON CODE #######################################    
    axcolor = 'white'
    rax = plt.axes([0.92, 0.01, 0.1, 0.1], axisbg=axcolor)
    radio = RadioButtons(rax, ('Mark Steady', 'Mark Unsteady'))  
    radio.on_clicked(hzfunc)   
##########################################################################

#########################SPANNER CODE ####################################    
    span = SpanSelector(ax, onselect, 'horizontal', useblit=True,rectprops=dict(alpha=0.5, facecolor='red') )
  
    func=highlight
    span1 = SpanSelector(ax2, in_take, 'horizontal', useblit=True,rectprops=dict(alpha=0.5) )
    

###########################################################################

plt.show()
    

