import numpy as np
import matplotlib.pyplot as plt
import animator as ani


@np.vectorize
def mandelbrot(x, y, z=0j, iterations=50):
    c = complex(x, y)
    n = -1
    for i in range(iterations):
        if abs(z) > 2:
            n = i
            break
        z = z**2 + c
    return n


xmin, xmax, ymin, ymax = -2, 1, -1, 1
precision = 300
frames = 60
levels = [-1, 0, 10, 15, 20, 25, 30, 35, 40, 45, 50]

values = np.linspace(-2, 2, frames)
x = np.linspace(xmin, xmax, precision)
y = np.linspace(ymin, ymax, precision)
x, y = np.meshgrid(x, y)
z = [mandelbrot(x, y, c) for c in values]

plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
animation = ani.ContourAnimation(x, y, z, levels=levels)
animation.save("contour_animation.gif")
animation.start()
