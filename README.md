# frameworks
all of my little, helpful frameworks


## shaper.py
Lets you create shapes with __matplotlib__ and
display them. e.g.:
```python
    pyramid = Shape([(0, 0), (-0.5, -1.5), (5, 0), (3, 5)], index_style="letters")
    pyramid.connect("A-B-C-A A-D B-D C-D")
    pyramid.draw(label=True)
    plt.show()
```

## animator.py
Made for scientific purposes. Create simple yet meaningful animations with the __matplotlib.animations__ module.
There are 2 classes for different animation types.

### animator.PlotAnimation
For animations using plt.plot(). Make sine waves or parameter variations of different functions
and animate them to visualize your research. Minimal example:
```python
import numpy as np
from animator import PlotAnimation

x = np.linspace(-3*np.pi, 3*np.pi, 200)
y = [np.sin(x+k) for k in np.linspace(0, 4*np.pi, 60)]
animation = PlotAnimation(x, y)
animation.save("sine_wave_animation.gif")
animation.start()
```

### animator.ContourAnimation
For animations using plt.contourf(). Make 2-dimensional graphs and visualize their behaviour when you change a variable.
Minimal example:
```python
import numpy as np
from animator import ContourAnimation

x = np.linspace(-10, 10, 300)
y = np.linspace(-10, 10, 300)
x, y = np.meshgrid(x, y)
z = [np.sin(x**2 + y**2 + k) for k in np.linspace(0, 4*np.pi, 60)]
animation = ContourAnimation(x, y, z)
animation.save("hypnosis.gif")
animation.start()
```
