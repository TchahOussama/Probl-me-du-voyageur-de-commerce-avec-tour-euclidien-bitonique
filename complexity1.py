from bitonique import bitonique
from bitonique_iterative import bitonique_iter
import numpy as np
import matplotlib.pyplot as plt
height = []
bar = []
colors = []
k = 0
# Make a fake dataset:
for i in range (3,15):
    height.append(bitonique(i))
    height.append(bitonique_iter(i))
    bar.append(i)
    bar.append(i)
    colors.append('blue')
    colors.append('cyan')
bars = tuple(bar)
y_pos = np.arange(len(bars))
# Create bars
plt.bar(y_pos, height, color = colors)
 
# Create names on the x-axis
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()
