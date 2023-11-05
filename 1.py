import random

# Your list of figures (assuming it's a list of numbers)
figures = list(range(1, 57))  # Assuming figures are numbered from 1 to 56

# Number of figures you want to select
num_to_select = 40

# Randomly select 40 figures
selected_figures = random.sample(figures, num_to_select)

# Shuffle the order of the selected figures
random.shuffle(selected_figures)

print("Selected and Shuffled Figures:", selected_figures)
