from graphics import Rectangle, Circle, BulletinBoard, Poster, TextBox
import random

class BrickWall(Poster):

    def __init__(self, width, height, color_matrix, color_map, outline_bricks):
        super().__init__()
        self.bricks_left = 0
        n_rows = len(color_matrix)
        n_cols = len(color_matrix[0])
        self.brick_width = width // n_cols
        self.brick_height = height // n_rows
        self.outline_bricks = outline_bricks
        for row in range(n_rows):
            for column in range(n_cols):
                brick = self.create_brick(color_map[color_matrix[row][column]])
                if brick != None:
                    self.bricks_left += 1
                    self.pin(brick,
                             column * self.brick_width,
                             row * self.brick_height)

    def create_brick(self, color):
        if color == None:
            return None
        else:
            return Rectangle(self.brick_width, self.brick_height,
                             color, filled=True, outlined=self.outline_bricks)

    def all_shattered(self):
        return self.bricks_left <= 0

    def shatter(self, x, y):
        brick = self.getElementAt(x, y)
        if brick != None:
            self.unpin(brick)
            self.bricks_left -= 1
            return True
        return False




class BreakoutGame:

    def __init__(self, config):
        self.board = BulletinBoard(config.get_board_width(),
                                   config.get_board_height())
        self.wall = BrickWall(self.board.get_width(),
                              self.board.get_height()*0.3,
                              config.get_color_matrix(),
                              config.get_color_map(),
                              config.outline_bricks())
        paddle_width = self.board.get_width() // 8
        paddle_height = self.board.get_height() // 40
        self.paddle = Rectangle(paddle_width, paddle_height, "black", filled=True)
        self.board.pin(self.wall, 0, 0.1 * self.board.get_height())
        self.board.pin(self.paddle,
                       self.board.get_width()/2,
                       0.9 * self.board.get_height())
        self.reset_ball()
        self.message_box = TextBox("", "Helvetica Neue", 20, "#0000FF")
        self.dy = config.get_initial_y_velocity()
        self.dx = random.uniform(config.get_min_x_velocity(),
                                 config.get_max_x_velocity())
        self.dx = random.choice([-1, 1]) * self.dx
        self.lives_left = config.get_num_balls()
        self.time_step = config.get_time_step()
        self.game_in_progress = False
        self.game_over = False

    def start(self):
        self.board.listen_for("mousemove", self.mousemove_action)
        self.timer = self.board.call_every(self.step, self.time_step)
        self.board.listen_for("click", self.click_action)

    def mousemove_action(self, x, y):
        paddle_x = min(self.board.get_width() - self.paddle.get_width(), x)
        self.board.unpin(self.paddle)
        self.board.pin(self.paddle, paddle_x, 0.9 * self.board.get_height())

    def display_message(self, msg):
        self.board.unpin(self.message_box)
        self.message_box = TextBox(msg, "Helvetica Neue", 20, "#0000FF")
        self.board.pin(self.message_box,
                       self.board.get_width() // 2,
                       10)


    def reset_ball(self):
        ball_size = self.board.get_width() // 25
        self.ball = Circle(ball_size, "black", filled=True)
        self.board.pin(self.ball,
                       self.board.get_width() / 2,
                       self.board.get_height() / 2)

    def click_action(self, x, y):
        if not self.game_over:
            self.game_in_progress = True

    def check_for_bounce(self):
        (x, y) = self.ball.get_center()
        radius = self.ball.get_radius()
        if x - radius <= 0 or x + radius >= self.board.get_width():
            self.dx = -self.dx
        if y - radius <= 0:
            self.dy = -self.dy

    def element_at(self, x, y):
        result = self.wall.shatter(x, y - (0.1 * self.board.get_height()))
        if not result:
            return self.board.element_at(x, y)
        else:
            return self.wall

    def check_for_collision(self):
        def get_colliding_objects():
            (x, y) = self.ball.get_center()
            radius = self.ball.get_radius()
            corners = [(x - radius, y - radius), (x + radius, y - radius),
                       (x - radius, y + radius), (x + radius, y + radius)]
            colliders = set()
            for (corner_x, corner_y) in corners:
                element = self.element_at(corner_x, corner_y)
                if element != None:
                    colliders.add(element)
            return colliders
        for collider in get_colliding_objects():
            if collider == self.paddle:
                self.dy = -abs(self.dy)
            elif collider == self.wall:
                self.dy = -self.dy

    def check_for_game_end(self):
        if self.wall.all_shattered():
            self.game_in_progress = False
            self.game_over = True
            self.display_message("YOU WIN!")
        else:
            (x, y) = self.ball.get_center()
            radius = self.ball.get_radius()
            if y - radius >= self.board.get_height():
                self.board.unpin(self.ball)
                self.lives_left -= 1
                self.game_in_progress = False
                if self.lives_left <= 0:
                    self.game_over = True
                    self.display_message("GAME OVER")
                else:
                    self.reset_ball()

    def step(self):
        if self.game_in_progress and not self.game_over:
            self.ball.move(self.dx, self.dy)
            self.check_for_bounce()
            self.check_for_collision()
            self.check_for_game_end()
