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
steady = []
steadys = []
steadye = []
unsteady = []
unsteadye = []
unsteadys = []
arrs = 0
arre = 0
result = []
final = []
re = []
def hzfunc(label):
	hzdict = {'Mark Steady': highlight ,'Mark Unsteady':dehighlight}   
	global func
	func=hzdict[label]
def in_take(xmin,xmax):
	global func
	func(xmin,xmax)
	
	


#	arrs = result[::2]
#	arre = result[1::2]
#	if type == 0 :
#		arrs.append(xmin)
#		arre.append(xmax)
#	else :
#		arre.append(xmin)
#		arrs.append(xmax)
#		final = arrs + arre
#		final.sort()
#	idx = 0
#	scount = 0
#	
#	for i in (0,len(final)):
#		if (-1 != arrs.index(final[i])):
#			idx+=-1
#		else:
#			idx+=1
#		if (-1 == idx and scount == 0):
#			SS.append(final[i])
#			scount = 1
#		if (idx ==0 and scount == 1):
#			scount = 0
#			SS.append(final[i])
#	print SS
#


def onselect(xmin, xmax):
	indmin, indmax = np.searchsorted(x, (xmin, xmax))
	indmax = min(len(x)-1, indmax)

	thisx = x[indmin:indmax]
	thisy = y[indmin:indmax]
	line2.set_data(thisx, thisy)
	
	ax2.set_xlim(thisx[0], thisx[-1])
	ax2.set_ylim(thisy.min(), thisy.max())    
		
	fig.canvas.draw()
	
def highlight(xmin, xmax):
	indmin, indmax = np.searchsorted(x, (xmin, xmax))
	indmax = min(len(x)-1, indmax)
	thisx = x[indmin:indmax]
	ax.axvspan(thisx[0], thisx[-1], color='yellow', alpha=1)
	ax2.axvspan(thisx[0], thisx[-1], color='yellow', alpha=1)    
	steadyxmin = thisx[0]
	steadyxmax = thisx[-1]
	steady.append(steadyxmin)
	steadys.append(steadyxmin)
	steady.append(steadyxmax)
	steadye.append(steadyxmax)        
	fig.canvas.draw()
	type = 0        
	#fitdata(xmin,xmax,0)
def dehighlight(xmin, xmax):
	indmin, indmax = np.searchsorted(x, (xmin, xmax))
	indmax = min(len(x)-1, indmax)

	thisx = x[indmin:indmax]
	
	ax.axvspan(thisx[0], thisx[-1], color='white', alpha=1)  
	ax2.axvspan(thisx[0], thisx[-1], color='white', alpha=1)    
	steadyxmin = thisx[0]
	steadyxmax = thisx[-1]
	unsteadys.append(steadyxmin)
	unsteady.append(steadyxmin)
	unsteady.append(steadyxmax)
	unsteadye.append(steadyxmax)       
	fig.canvas.draw()
	type = 1    
	#fitdata(xmin,xmax,1)
# set useblit True on gtkagg for enhanced performance

if __name__=='__main__':
	fig = plt.figure(figsize=(15,10))
	ax = fig.add_subplot(211, axisbg='white')
	
	x = np.arange(0.0, 5.0, 0.01)
	y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))
	
	ax.plot(x, y, '-')
	ax.set_ylim(-2,2)
	ax.set_title('Press left mouse button and Drag to Magnify in the Zoom Window')
	
	ax2 = fig.add_subplot(212, axisbg='white')
	line2,=ax2.plot(x, y, '-')
	ax2.set_title('Zoom Window')
	axcolor = 'white'
	rax = plt.axes([0.905, 0.01, 0.1, 0.1], axisbg=axcolor)
	radio = RadioButtons(rax, ('Mark Steady', 'Mark Unsteady'))  
	radio.on_clicked(hzfunc)   
	
	span = SpanSelector(ax, onselect, 'horizontal', useblit=True,rectprops=dict(alpha=0.5, facecolor='red') )
	#print span
	#print dir(span)
	func=highlight
	span1 = SpanSelector(ax2, in_take, 'horizontal', useblit=True,rectprops=dict(alpha=0.5) )
	plt.show()
	

	c = 0
	k = 0
	steady.sort()
	for i in steady:
		if i in steadys:
			c-=1
		else:
			c+=1
		if ( c==-1 and k==0):
			temp = i
			result.append(temp)
			k+=1
		if c==0 :
			k=0
			result.append(i)

arrs = result [::2]
arre = result [1::2]
result1 = result
final = result1 + unsteady
final.sort()
c=0
k=0
for j in final:
	if j in unsteadys or j in arre:
		c+=1
	else:		
		c+=-1
	if (c==-1 and k==0):			
		temp = i
		re.append(i)
		k+=1
	if c==0:
		k=0	
		re.append(i)
print re
