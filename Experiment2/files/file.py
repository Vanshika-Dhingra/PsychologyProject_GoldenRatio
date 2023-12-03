import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('Experiment2Data_1xShapes2.csv')
df3 = pd.read_csv('Experiment2Data_1xShapes.csv')
df4 = pd.read_csv('Experiment2Data_3xShapes.csv')
df5 = pd.read_csv('Experiment2Data_3xShapes2.csv')


# Read the second CSV file
df2 = pd.read_csv('Experiment2.csv')

# Merge the two DataFrames on the common columns ('Name' and 'Category')
merged_df1 = pd.merge(df1, df2, on=['Name'])
merged_df2 = pd.merge(df3, df2, on=['Name'])
merged_df3 = pd.merge(df4, df2, on=['Name'])
merged_df4 = pd.merge(df5, df2, on=['Name'])

# Save the result to a new CSV file
merged_df1.to_csv('Experiment2Data_1xShapes2_merged.csv', index=False)
merged_df2.to_csv('Experiment2Data_1xShapes_merged.csv', index=False)
merged_df3.to_csv('Experiment2Data_3xShapes_merged.csv', index=False)
merged_df4.to_csv('Experiment2Data_3xShapes2_merged.csv', index=False)
