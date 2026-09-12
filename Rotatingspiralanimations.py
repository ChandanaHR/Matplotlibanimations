from IPython.display import HTML
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig,ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('blue')
theta = np.linspace(0,12*np.pi,1000)
r = theta
x = r*np.cos(theta)
y = r*np.sin(theta)
line, = ax.plot(x,y,color='cyan',linewidth=3)
ax.set_xlim(-40,40)
ax.set_ylim(-40,40)
ax.axis("off")
def rotate(frame):
    angle = np.radians(frame)
    x_rotated = x * np.cos(angle) - y * np.sin(angle)
    y_rotated = x * np.sin(angle) + y * np.cos(angle)
    line.set_data(x_rotated, y_rotated)
    return line,
animation = FuncAnimation(
    fig,
    rotate,
    frames=360,
    interval=20,
    blit=True
)
HTML(animation.to_jshtml())
