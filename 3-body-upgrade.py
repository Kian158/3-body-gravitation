import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



m1 = 6e24
m2 = 2e30 ## two bodies, comparable to planet and star
m3 = 6e24

x1_0 = np.array([1.5e11, 0, 0])
x2_0 = np.array([0 , 0, 0 ]) ## define starting positions
x3_0 = np.array([0 , 1.5e11, 0])

v1_mag = np.sqrt(G * m2 / np.linalg.norm(x1_0))  # around 29780 m/s
v3_mag = np.sqrt(G * m2 / np.linalg.norm(x3_0))  # smaller, since further out

v1_0 = np.array([0, v1_mag, 0])
v2_0 = np.array([0 , 0, 0 ]) ## initial velocities
v3_0 = np.array([-v3_mag, 0.4*v3_mag, 0])

G = 6.67e-11 ## gravitational constant
dt = 1e4 ## time step

x1 = x1_0.copy()
x2 = x2_0.copy()
x3 = x3_0.copy()

v1 = v1_0.copy()
v2 = v2_0.copy()
v3 = v3_0.copy()

## F = ma = GMm / r^2
time = 10000
x1_vals = np.zeros((time, 3))
x2_vals = np.zeros((time, 3))
x3_vals = np.zeros((time, 3))

def compute_accelerations(x1, x2, x3):
    r12 = x1 - x2
    r13 = x1 - x3
    r23 = x2 - x3

    a1 = (-G * m2 * r12 / (np.dot(r12, r12) + epsilon**2)**(1.5) -
          G * m3 * r13 / (np.dot(r13, r13) + epsilon**2)**(1.5))
    a2 = (-G * m1 * -r12 / (np.dot(r12, r12) + epsilon**2)**(1.5) -
          G * m3 * r23 / (np.dot(r23, r23) + epsilon**2)**(1.5))
    a3 = (-G * m1 * -r13 / (np.dot(r13, r13) + epsilon**2)**(1.5) -
          G * m2 * -r23 / (np.dot(r23, r23) + epsilon**2)**(1.5))

    return a1, a2, a3

# Initial accelerations
a1, a2, a3 = compute_accelerations(x1, x2, x3)

for t in range(time):
    # Update positions
    x1 = x1 + v1 * dt + 0.5 * a1 * dt**2
    x2 = x2 + v2 * dt + 0.5 * a2 * dt**2
    x3 = x3 + v3 * dt + 0.5 * a3 * dt**2

    # Compute new accelerations
    a1_new, a2_new, a3_new = compute_accelerations(x1, x2, x3)

    # Update velocities
    v1 = v1 + 0.5 * (a1 + a1_new) * dt
    v2 = v2 + 0.5 * (a2 + a2_new) * dt
    v3 = v3 + 0.5 * (a3 + a3_new) * dt

    # Update accelerations for next step
    a1, a2, a3 = a1_new, a2_new, a3_new

    # Save positions
    x1_vals[t] = x1
    x2_vals[t] = x2
    x3_vals[t] = x3


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot3D(x1_vals[:, 0], x1_vals[:, 1], x1_vals[:, 2], color='blue')
ax.plot3D(x2_vals[:, 0], x2_vals[:, 1], x2_vals[:, 2], color='blue')
ax.plot3D(x3_vals[:, 0], x3_vals[:, 1], x3_vals[:, 2], color='blue')

