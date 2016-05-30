import matplotlib.pyplot as plt
import numpy as np
import random
fig = plt.figure()
ax = plt.gca()
ax.cla() # clear things for fresh plot

Lx = 3 #x
Ly = 4 #y
R = 2 #
c = str(11111)
#c = str(int(np.pi*10**100))

N = Lx * Ly
ax.set_xlim((0,R*(Lx+1)))
ax.set_ylim((0,R*(Ly+1)))
a = range(R, R*Lx+1, R)
b = range(R, R*Ly+1, R)
print a
print b
leng = len(c)
n = N -leng

if (n >0):
  c0 = str(10**(n+1))
  c += c0[1:]

i = 0
for dy in b :
    for dx in a:
        print(dx, dy,int(c[i]))
        fig.gca().add_artist(plt.Circle((dx,dy),int(c[i]) or 0,color='b',fill=False,linewidth=1))
        i += 1
plt.show()
#fig.savefig('draw.png')
