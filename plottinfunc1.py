import csv
import matplotlib.pyplot as plt
### Extract data from CSV ###
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
# plt.axis([xmin, xmax, ymin, ymax]) - sets axes limits on graph
plt.axis([0, 50, 0, 100])
plt.show()

