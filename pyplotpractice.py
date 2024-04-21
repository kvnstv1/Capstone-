import matplotlib.pyplot as plt
import numpy as np

#Practicing Git using this file
x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]

fig, ax = plt.subplots()
ax.plot(x,y)

ax.set(xlabel = 'x', ylabel = 'y', title = 'Simple plot')
ax.grid()

plt.show()

