import csv
import matplotlib.pyplot as plt
### Extract data from CSV ###
with open('temperatures.csv', 'rb') as n:
    reader = csv.reader(n)
    reader.next()
    
    dates = []
    c=0
    k=0
    l=0
    num1=0
    
   
    for row in reader:
        if row==[]:
         break
     	else:
	 c+=1
	values = row
        dim=len(row)-1
       
        freq = [[0 for y in xrange(dim)] for x in xrange(c)]
        dates.append(values[0])        
      
        
	
print freq         


for k in range(0,c):
 for num2 in range(1,dim+1):
  freq[k][num2-1] = values[num2]
print freq
         
  

        
        
        

### Do plot ###
#false_x = [x for x in range(len(dates))]
#plt.plot(false_x,freq, 'o-')
#plt.plot(false_x,freq1, 'o-')
#plt.xticks(range(len(dates)), (dates), rotation=45)
#plt.axis([0, 50, 0, 100])
#plt.show()
