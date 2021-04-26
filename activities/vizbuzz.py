from graphics import BulletinBoard, Poster
from graphics import Circle, Rectangle, TextBox


def make_counter(msg, color):
    poster = Poster()
    rect = Rectangle(80, 50, color)
    poster.pin(rect, -40, -25)
    textbox = TextBox(msg, "Courier", "40")
    poster.pin(textbox, 0, 0)
    return poster

def make_button(msg, color):
    poster = Poster()
    circle = Circle(100, color, filled=True)
    poster.pin(circle, 0, 0)
    textbox = TextBox(msg, "Helvetica", "40")
    poster.pin(textbox, 0, 0)
    return poster


class Vizbuzz:

    def __init__(self):
        self.count = 1
        self.board = BulletinBoard(200, 350)
        self.counter = None
        self.fizzbutton = None
        self.buzzbutton = None
        self.fizz_on = False
        self.buzz_on = False
        self.game_over = False
        self.counter_color = "#7BA4DB"
        self.draw_counter()
        self.draw_fizz_button()
        self.draw_buzz_button()
        self.board.call_every(self.step, 1000)
        self.board.listen_for("click", self.respond_to_click)

    def draw_counter(self):
        self.board.unpin(self.counter)
        self.counter = make_counter(str(self.count), self.counter_color)
        self.board.pin(self.counter, 100, 50)

    def draw_fizz_button(self):
        self.board.unpin(self.fizzbutton)
        if self.fizz_on:
            color = "#E56DB1"
        else:
            color = "gray"
        self.fizzbutton = make_button("fizz", color)
        self.board.pin(self.fizzbutton, 100, 150)

    def draw_buzz_button(self):
        self.board.unpin(self.buzzbutton)
        if self.buzz_on:
            color = "#E56DB1"
        else:
            color = "gray"
        self.buzzbutton = make_button("buzz", color)
        self.board.pin(self.buzzbutton, 100, 275)

    def respond_to_click(self, x, y):
        element = self.board.element_at(x, y)
        if element == self.fizzbutton:
            self.fizz_on = not self.fizz_on
            self.draw_fizz_button()
        elif element == self.buzzbutton:
            self.buzz_on = not self.buzz_on
            self.draw_buzz_button()

    def check_for_loss(self):
        """ Fill this in!!! """
        pass

    def step(self):
        self.check_for_loss()
        if not self.game_over:
            self.count += 1
            self.board.unpin(self.counter)
            self.draw_counter()
            self.board.pin(self.counter, 100, 50)

Vizbuzz()