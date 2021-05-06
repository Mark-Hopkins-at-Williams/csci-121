from pgl import GWindow, GOval, GRect, GCompound, GLabel, GPolygon


class Rectangle(GRect):
    def __init__(self, width, height, color, filled=True, outlined=False):
        super().__init__(width, height)
        self.setFillColor(color)
        if outlined:
            self.setColor("black")
        else:
            self.setColor(color)
        self.setFilled(filled)

    def set_color(self, color):
        self.setFillColor(color)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width


class RegularPolygon(GPolygon):
    def __init__(self, side_length, num_sides, color,
                 rotation=0, filled=True, outlined=False):
        super().__init__()
        self.addVertex(-side_length, 0)
        angle = 360/num_sides + rotation
        for i in range(num_sides):
            self.addPolarEdge(side_length, angle)
            angle += 360/num_sides
        self.setFillColor(color)
        self.setFilled(filled)
        if outlined:
            self.setColor("black")
        else:
            self.setColor(color)


class Triangle(RegularPolygon):
    def __init__(self, side_length, color, rotation=0):
        super().__init__(side_length, 3, color, rotation)


class Hexagon(RegularPolygon):
    def __init__(self, side_length, color, rotation=0):
        super().__init__(side_length, 6, color, rotation)


class Circle(GCompound):
    def __init__(self, diameter, color, filled=True):
        super().__init__()
        self.oval = GOval(-diameter//2, -diameter//2, diameter, diameter)
        self.oval.setFillColor(color)
        self.oval.setColor(color)
        self.oval.setFilled(filled)
        self.diameter = diameter
        self.add(self.oval)

    def set_color(self, color):
        self.oval.setColor(color)
        self.oval.setFillColor(color)

    def get_radius(self):
        return self.diameter / 2

    def get_center(self):
        return (self.getX(), self.getY())


class TextBox(GCompound):
    def __init__(self, msg, font="Helvetica", font_size=12, font_color="#000000"):
        super().__init__()
        self.label = GLabel(msg)
        self.label.setFont("{}px '{}'".format(font_size, font))
        self.label.setColor(font_color)
        self.add(self.label, -self.get_width()//2, (self.label.getAscent() - self.label.getDescent())//2)

    def get_height(self):
        return self.label.getAscent() + self.label.getDescent()

    def get_width(self):
        return self.label.getBounds().getWidth()


class Poster(GCompound):
    def __init__(self):
        super().__init__()

    def pin(self, shape, x, y):
        self.add(shape, x, y)

    def unpin(self, shape):
        self.remove(shape)

    def element_at(self, x, y):
        return self.getElementAt(x, y)


class BulletinBoard(GWindow):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.w = w
        self.h = h

    def get_width(self):
        return self.w

    def get_height(self):
        return self.h

    def pin(self, obj, x, y):
        self.add(obj, x, y)

    def unpin(self, obj):
        self.remove(obj)

    def element_at(self, x, y):
        return self.getElementAt(x, y)

    def listen_for(self, event, handler):
        self.addEventListener(event, lambda e: handler(e.getX(), e.getY()))

    def call_every(self, function, interval):
        timer = self.createTimer(function, interval)
        timer.setRepeats(True)
        timer.start()
        return timer

    def call_later(self, function, interval):
        timer = self.createTimer(function, interval)
        timer.setRepeats(False)
        timer.start()
        return timer

