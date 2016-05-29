import matplotlib.pyplot as plt
import numpy as np
import random
fig = plt.figure()
ax = plt.gca()
ax.cla() # clear things for fresh plot

ax.set_xlim((0,10))
ax.set_ylim((0,10))
a = range(1,10)
b = range(1,10)
c = str(int(np.pi*10**100))
i = 0
for dy in a :
    for dx in b:
        print(dx, dy,int(c[i]))
        fig.gca().add_artist(plt.Circle((dx,dy),int(c[i]),color='b',fill=False,linewidth=1))
        i += 1
plt.show()
