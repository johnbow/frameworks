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
