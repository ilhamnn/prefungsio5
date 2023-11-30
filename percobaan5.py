import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate random data
sample = np.random.normal(loc=50, scale=5, size=1000)

# Create a figure and axis
plt.figure(figsize=(5, 4))

# Plot histogram using Seaborn's distplot
sns.histplot(sample, bins=10, kde=True, color="pink")

# Show the plot
plt.show()
