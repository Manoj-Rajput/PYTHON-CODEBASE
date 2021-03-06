import matplotlib.pyplot as plt
import numpy as np

data_weight = np.array([112.99, 136.49, 153.03, 142.34, 144.3, 123.3, 141.49, 136.46, 
112.37, 120.67, 127.45, 114.14, 125.61, 122.46, 116.09, 140.0, 129.5, 142.97, 
137.9, 124.04, 141.28, 143.54, 97.9, 129.5, 141.85, 129.72, 142.42, 131.55, 
108.33, 113.89, 103.3, 120.75, 125.79, 136.22, 140.1, 128.75, 141.8, 121.23, 
131.35, 106.71, 124.36, 124.86, 139.67, 137.37, 106.45, 128.76, 145.68, 116.82, 
143.62, 134.93])

plt.hist(data_weight)
plt.title("Weight of People In Group 'X' ( Unit: Lbs)")
plt.xlabel("Cumulative Groups")
plt.ylabel("Frequency")

plt.show()