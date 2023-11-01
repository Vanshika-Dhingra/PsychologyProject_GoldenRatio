import csv
import re
import copy 
# Define a regular expression pattern to match IDs starting with '#'

# Initialize a dictionary to store counts for each ID (question ID) and figure
user =[{"figure1":0,"figure2":0,"figure3":0,"figure4":0,"figure5":0,"figure6":0},
       {"figure1":0,"figure2":0,"figure3":0,"figure4":0,"figure5":0,"figure6":0},
       {"figure1":0,"figure2":0,"figure3":0,"figure4":0,"figure5":0,"figure6":0},
       {"figure1":0,"figure2":0,"figure3":0,"figure4":0,"figure5":0,"figure6":0},
       {"figure1":0,"figure2":0,"figure3":0,"figure4":0,"figure5":0,"figure6":0}]
# Open the CSV file
with open('Aesthetics Of Simple Shapes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  

    j=0
    for row in reader:  
        for i in range(6,len(row)):
            if(row[i]=='Figure - 1'):
                user[j]['figure1']+=1
            elif(row[i]=='Figure - 2'):
                user[j]['figure2']+=1
            elif(row[i]=='Figure - 3'):
                user[j]['figure3']+=1
            elif(row[i]=='Figure - 4'):
                user[j]['figure4']+=1
            elif(row[i]=='Figure - 5'):
                user[j]['figure5']+=1
            elif(row[i]=='Figure - 6'):
                user[j]['figure6']+=1
        j+=1
        if(j==5):
            break

# plot each of the user as a line graph
import matplotlib.pyplot as plt
import numpy as np
x = ['1','1.268','1.618','2.098','2.791','3.885']
for i in range(5):
    plt.plot(x, user[i].values())
plt.xlabel('Ratio the figure was divided into')
plt.ylabel('Count')
plt.title('Count of Figures with particular ratio')
plt.show()
