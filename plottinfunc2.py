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
plt.plot(false_x,freq, 'o-')
plt.plot(false_x,freq1, 'o-')
plt.xticks(range(len(dates)), (dates), rotation=45)

plt.axis([0, 50, 0, 100])
plt.show()
