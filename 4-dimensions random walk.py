import numpy as np
import random 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#definig the costance of the simulation
random_walks_number = 1000
random_walk_steps = 1000
radius = 1

#defing the random walk function
def random_walk(n, r):
    #defining the coordinates and length of every step
    x = [0]
    y = [0]
    z = [0]
    t = [0]
    
    #simulating the steps
    for i in range(n):
        dx = np.sqrt(random.uniform(0, r))*random.choice([-1, 1])
        dy = np.sqrt(random.uniform(0, r - (dx)**2))*random.choice([-1, 1])
        dz = np.sqrt(random.uniform(0, r - (dx)**2 - (dy)**2))*random.choice([-1, 1])
        dt = np.sqrt( r - (dx)**2 - (dy)**2 - (dz)**2)*random.choice([-1, 1])
        x.append(x[i]+dx)
        y.append(y[i]+dy)
        z.append(z[i]+dz)
        t.append(t[i]+dt)
    return np.array(x), np.array(y), np.array(z), np.array(t)

#defining the arrays of final x positiona and final distance
final_x = []
final_distance = []

#appending on the vector each value
for i in range (random_walks_number):
    x, y, z, t = random_walk(random_walk_steps, radius)
    final_x.append(x[-1])
    final_distance.append(np.sqrt(x[-1]**2+y[-1]**2+z[-1]**2+t[-1]**2))
    print(round((i/random_walks_number)*100, 3),"%")
    
#plotting the distributions
plt.figure()
plt.title("Distribution of the final distance")
plt.hist(final_distance, bins = 70)
 
plt.figure()
plt.hist(final_x, bins = 70)
plt.title("Distribution of the final x coordinate")

#creating the figure for the last random walk
fig = plt.figure()

#adding a subplot to the figure
ax = fig.add_subplot(111, projection='3d')

#aesthetics
ax.set_title("Projection of the 4-dimensional random walk on xyz (1000 steps)")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.scatter(0, 0, 0, color='red', s=10, marker='o', label='O')

#set the margins of the plot
margin = 1
ax.set_xlim(min(x) - margin, max(x) + margin)
ax.set_ylim(min(y) - margin, max(y) + margin)
ax.set_zlim(min(z) - margin, max(z) + margin)

# Defing the line and the point 
line, = ax.plot([], [], [], lw=2, color='blue')
point, = ax.plot([], [], [], marker='o', color='red')

#inizilating 
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return line, point

# frame update function
def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    point.set_data([x[frame]], [y[frame]])
    point.set_3d_properties([z[frame]])
    return line, point

# create the animation
ani = FuncAnimation(
    fig, update, frames=len(x),
    init_func=init, interval=50, blit=True
)

plt.show()


