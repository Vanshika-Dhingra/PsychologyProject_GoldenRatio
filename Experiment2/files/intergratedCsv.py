import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('Experiment2Data.csv')

# Extract the name from the 'Path' column
df['Name'] = df['Path'].apply(lambda x: x.split('/')[1])

# Extract the category (3xShapes or 1xShapes) from the 'Path' column
df['Category'] = df['Path'].apply(lambda x: x.split('/')[2])

# Extract the shape name from the 'Path' column
df['Shape'] = df['Path'].apply(lambda x: x.split('/')[-1])

# Group by 'Name', 'Category', and 'Shape' and aggregate the data
aggregated_df = df.groupby(['Name', 'Category', 'Shape']).agg({
    'Ratio': 'mean'
}).reset_index()

# Pivot the DataFrame to have shape names as columns
pivoted_df = aggregated_df.pivot_table(index=['Name', 'Category'], columns='Shape', values='Ratio', fill_value=0)

# Flatten the MultiIndex columns
pivoted_df.columns = [f'{col}' for col in pivoted_df.columns]

# Reset the index
pivoted_df.reset_index(inplace=True)

# Save the result to a new CSV file
pivoted_df.to_csv('Experiment2DataChanged.csv', index=False)
