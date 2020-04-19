import matplotlib.pyplot as plt
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Shape:

    def __init__(self, points, index=None, index_style="integers"):
        self.cons = []
        if index is None and isinstance(points, dict):
            self.data = points
        elif index is None:
            if index_style == "integers":
                self.data = dict(zip(range(len(points)), points))
            elif index_style == "letters":
                self.data = {(i//26 + 1) * letters[i % 26]: item for i, item in enumerate(points)}
            elif callable(index_style):
                self.data = dict(zip(index_style(points), points))
            else:
                raise ValueError("index_style has to be string or generator.")
        else:
            self.data = dict(zip(index, points))

    def connect(self, s, connector="-", delimiter=" ", **kwargs):
        for connection in s.upper().split(delimiter):
            self.cons.append(connection.split(connector))
            self.cons[-1].append(kwargs)

    def draw(self, ax=plt, mark_edges=False, label=False, line_kw={}, marker_kw={}, label_kw={}):
        for con in self.cons:
            x = [self.data[c][0] for c in con[:-1]]
            y = [self.data[c][1] for c in con[:-1]]
            line_kw.update(con[-1])
            ax.plot(x, y, **dict({"color": "blue"}, **line_kw))
            if mark_edges:
                ax.scatter(x, y, **dict({"color": "black"}, **marker_kw))
            if label:
                lblkw = {"textcoords": "offset points", "xytext": (3, -3)}
                lblkw.update(label_kw)
                for lbl in self.data:
                    ax.annotate(str(lbl), self.data[lbl], **lblkw)


# -------DARK LAYOUT-------
# plt.rcParams['axes.facecolor'] = '0.1'
# plt.rcParams['figure.facecolor'] = "0.1"
# ax = plt.axes()
# for spine in ax.spines.values():
#     spine.set_color("white")
# ax.tick_params(colors="white")
# ax.xaxis.label.set_color("white")
# ax.yaxis.label.set_color("white")

if __name__ == "__main__":
    pyramid = Shape([(0, 0), (-0.5, -1.5), (5, 0), (3, 5)], index_style="letters")
    pyramid.connect("A-B-C-A A-D B-D C-D")
    pyramid.draw(label=True)
    plt.show()
