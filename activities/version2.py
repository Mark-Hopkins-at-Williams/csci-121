from graphics import BulletinBoard, Poster
from graphics import Circle, Rectangle, TextBox

board = BulletinBoard(200, 350)

# Code for creating the "counter display"
poster = Poster()
rect = Rectangle(80, 50, "#7BA4DB")
poster.pin(rect, -40, -25)
textbox = TextBox("000", "Courier", "40")
poster.pin(textbox, 0, 0)
board.pin(poster, 100, 50)

# TODO: Code for creating a "fizz button"
# fill me in!