import numpy as np
import matplotlib.pyplot as plt
import animator as ani

xmin, xmax, ymin, ymax = -3*np.pi, 3*np.pi, -1, 1
precision = 200
frames = 120

values = np.linspace(0, 2*np.pi, frames)
x = np.linspace(xmin, xmax, precision)
y = [np.sin(k+x) for k in values]

plt.xlim(xmin, xmax)
plt.ylim(xmin, ymax)
animation = ani.PlotAnimation(x, y, frames=frames, duration=4)
animation.save("plot_animation.gif")
animation.start()
