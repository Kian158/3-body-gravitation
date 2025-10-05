import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



m1 = 6e24
m2 = 2e30 ## two bodies, comparable to planet and star

x1_0 = np.array([1.5e11, 0, 0])
x2_0 = np.array([0 , 0, 0 ]) ## define starting positions

v1_0 = np.array([0, 29780, 0])
v2_0 = np.array([0 , 0, 0 ]) ## initial velocities

G = 6.67e-11 ## gravitational constant
dt = 1e4 ## time step

x1 = x1_0.copy()
x2 = x2_0.copy()

v1 = v1_0.copy()
v2 = v2_0.copy()

## F = ma = GMm / r^2
time = 10000
x1_vals = np.zeros((time, 3))
x2_vals = np.zeros((time, 3))
for t in range(time):

    r = x1 - x2 ## displacement vector
    
    a1 = -G * m2 * r / np.dot(r,r)** (3 / 2)
    a2 = -G * m1 * r / np.dot(r,r)** (3 / 2) ## work out accelerations
    
    v1 = v1 + a1 * dt 
    v2 = v2 + a2 * dt ## velocities

    x1 = x1 + v1 * dt
    x2 = x2 + v2 * dt ## update positions

    x1_vals[t] = x1
    x2_vals[t] = x2 ## save pos data



fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot3D(x1_vals[:, 0], x1_vals[:, 1], x1_vals[:, 2], color='blue')
ax.plot3D(x2_vals[:, 0], x2_vals[:, 1], x2_vals[:, 2], color='blue')

x1_vals
