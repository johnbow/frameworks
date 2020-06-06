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
and animate them to visualize your research.

### animator.ContourAnimation
For animations using plt.contourf(). Make 2-dimensional graphs and visualize their behaviour when you change a variable. 
