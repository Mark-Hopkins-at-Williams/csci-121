from graphics import BulletinBoard, Poster
from graphics import Circle, Rectangle, TextBox, Triangle


def make_button(msg, color):
    poster = Poster()
    circle = Circle(100, color, filled=True)
    poster.pin(circle, 0, 0)
    textbox = TextBox(msg, "Helvetica", "40")
    poster.pin(textbox, 0, 0)
    return poster


class Counter(Poster):

    def __init__(self, msg, bg_color):
        super().__init__()
        self.rect = Rectangle(120, 50, bg_color)
        self.pin(self.rect, -60, -25)
        self.textbox = None
        self.update_count(msg)
        self.triangle = None
        self.triangle_rotation = 0
        self.triangle_color = "#ABC2FF"
        self.draw_triangle()

    def update_count(self, count):
        self.unpin(self.textbox)
        self.textbox = TextBox(str(count), "Courier", "40", font_color="black")
        self.pin(self.textbox, -30, 0)

    def update_color(self, color):
        self.rect.set_color(color)

    def draw_triangle(self):
        self.unpin(self.triangle)
        self.triangle = Triangle(20, self.triangle_color,
                                 rotation=self.triangle_rotation)
        self.pin(self.triangle, 50, 0)

    def notify(self, x, y, board):
        def animate_triangle(num_frames):
            if num_frames > 0:
                self.triangle_rotation += 4
                self.draw_triangle()
                board.call_later(lambda: animate_triangle(num_frames - 1), 1)
        if self.element_at(x, y) == self.triangle:
            board.call_later(lambda: animate_triangle(45), 1)
            return True
        else:
            return False


class Vizbuzz:

    def __init__(self):
        self.count = 1
        self.board = BulletinBoard(200, 350)
        self.increment = 1
        self.counter = None
        self.fizzbutton = None
        self.buzzbutton = None
        self.fizz_on = False
        self.buzz_on = False
        self.game_over = False
        self.counter_color = "#7BA4DB"
        self.counter = Counter(str(self.count), self.counter_color)
        self.board.pin(self.counter, 100, 50)
        self.draw_fizz_button()
        self.draw_buzz_button()
        self.board.call_every(self.step, 1000)
        self.board.listen_for("click", self.respond_to_click)

    def draw_counter(self):
        self.counter.update_count(self.count)
        self.counter.update_color(self.counter_color)

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
        elif element == self.counter:
            if self.counter.notify(x - 100, y - 50, self.board):
                self.increment *= -1

    def check_for_loss(self):
        if self.count % 3 == 0 and self.count % 5 == 0:
            correct = self.fizz_on and self.buzz_on
        elif self.count % 3 == 0:
            correct = self.fizz_on and not self.buzz_on
        elif self.count % 5 == 0:
            correct = self.buzz_on and not self.fizz_on
        else:
            correct = not self.fizz_on and not self.buzz_on
        if not correct:
            self.counter_color = "red"
            self.draw_counter()
            self.game_over = True

    def step(self):
        self.check_for_loss()
        if not self.game_over:
            self.count += self.increment
            self.draw_counter()
            self.fizz_on = False
            self.buzz_on = False
            self.draw_fizz_button()
            self.draw_buzz_button()

Vizbuzz()