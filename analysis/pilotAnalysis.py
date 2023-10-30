import csv
import re

# Define a regular expression pattern to match IDs starting with '#'
pattern = r'#\w+\d'

# Initialize a dictionary to store counts for each ID (question ID) and figure
id_figure_counts = {}

# Open the CSV file
with open('Aesthetics Of Simple Shapes.csv', 'r') as csvfile:
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

#print the counts
for id in id_figure_counts:
    print(id, id_figure_counts[id])
