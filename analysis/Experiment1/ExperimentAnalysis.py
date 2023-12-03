import csv
import re
import copy 
# Define a regular expression pattern to match IDs starting with '#'
pattern = r'#\w+\d'

# Initialize a dictionary to store counts for each ID (question ID) and figure
id_figure_counts = {}
user =[]
# Open the CSV file
with open('Experiment1Data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read the header row

    # Find and extract unique IDs from the header
    ids = re.findall(pattern, ','.join(header))

    # Create an empty dictionary for each unique ID
    for id in ids:
        id_figure_counts[id] = {}

    # Iterate through the columns (questions) and update the counts
    for row in reader:
        for i,id in enumerate(ids):
            if row[6+i] not in id_figure_counts[id]:
                id_figure_counts[id][row[6+i]]=1
            else:
                id_figure_counts[id][row[6+i]]+=1
            user.append(copy.deepcopy(id_figure_counts[id]))

count=[0,0,0,0,0,0,0]
for id in ids:
    for i in range(1,7):
        if 'Figure - '+str(i)+'' not in id_figure_counts[id]:
            count[i]=count[i]
        else:
            count[i]+=id_figure_counts[id]['Figure - '+str(i)+'']

#plot a bar graph for count
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,7)
y = count[1:7]
plt.bar(x, y, color='green')
plt.xlabel('Figure Number')
plt.ylabel('Count')
plt.title('Count of Figure Number')
plt.show()