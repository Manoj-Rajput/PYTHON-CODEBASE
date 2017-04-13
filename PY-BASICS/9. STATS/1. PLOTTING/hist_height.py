import matplotlib.pyplot as plt
import numpy as np

data_height = np.array([65.78, 71.52, 69.4, 68.22, 67.79, 68.7, 69.8, 70.01, 67.9, 66.78,
 66.49, 67.62, 68.3, 67.12, 68.28, 71.09, 66.46, 68.65, 71.23, 67.13, 67.83, 
68.88, 63.48, 68.42, 67.63, 67.21, 70.84, 67.49, 66.53, 65.44, 69.52, 65.81, 
67.82, 70.6, 71.8, 69.21, 66.8, 67.66, 67.81, 64.05, 68.57, 65.18, 69.66, 67.97, 
65.98, 68.67, 66.88, 67.7, 69.82, 69.09])

plt.hist(data_height)
plt.title("Height of People In Group 'X' ( Unit: Inches)")
plt.xlabel("Cumulative Groups")
plt.ylabel("Frequency")

plt.show()