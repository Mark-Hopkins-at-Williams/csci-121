from threading import Timer

def write(s):
    """
    This function allows us to print to the screen WITHOUT adding
    a newline!!!

    """
    from sys import stdout
    stdout.write(s)
    stdout.flush()


def correct_answer(num):
    """
    This function got us through the first round of interviews
    at Kate Club Incorporated!!!!

    """
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


def listen_for_keypress(f):
    """
    This creates a listener that calls f(key) whenever a key
    is pressed!!!!!

    """
    import asyncio
    import contextlib
    import sys
    import termios
    @contextlib.contextmanager
    def raw_mode(file):
        old_attrs = termios.tcgetattr(file.fileno())
        new_attrs = old_attrs[:]
        new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
        try:
            termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
            yield
        finally:
            termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)
    async def start_listener(f):
        with raw_mode(sys.stdin):
            reader = asyncio.StreamReader()
            loop = asyncio.get_event_loop()
            await loop.connect_read_pipe(lambda: asyncio.StreamReaderProtocol(reader),
                                         sys.stdin)
            while not reader.at_eof():
                ch = await reader.read(1)
                ch = ch.decode()
                continue_signal = f(ch)
                if not continue_signal:
                    break
    asyncio.run(start_listener(f))



class Fizzbuzz:
    """
    This is our alpha version!!!!!!!!!

    """
    def __init__(self,
                 keypresses = {'f': 'fizz', 'b': 'buzz'}):
        self.n = 1
        self.should_end_game = False
        self.increment = 1
        self.keypresses = keypresses
        self.recent_keypresses = []
        self.display_welcome_message()
        Timer(1, self.take_turn).start()
        listen_for_keypress(self.react_to_keypress)

    def display_welcome_message(self):
        print("***   WELCOME TO FIZZBUZZ   ***")
        print("***  (f to FIZZ, b to BUZZ  ***")
        write("***      and q to QUIT)     ***\n> ")

    def take_turn(self):
        if not self.should_end_game:
            self.process_user_input()
            self.n += self.increment
            self.recent_keypresses = []
            Timer(1, self.take_turn).start()

    def react_to_keypress(self, key):
        if key == "q":
            print("quitting...")
            self.should_end_game = True
        elif key in self.keypresses:
            self.recent_keypresses += [key.lower()]
            write(self.keypresses[key.lower()])
        return not self.should_end_game

    def reconstruct_answer(self):
        answer = ""
        for key in self.recent_keypresses:
            answer += self.keypresses[key]
        return answer

    def process_user_input(self):
        if self.reconstruct_answer() == "" and correct_answer(self.n) == str(self.n):
            write(str(self.n) + "\n> ")
        elif correct_answer(self.n) == self.reconstruct_answer():
            write("\n> ")
        else:
            self.should_end_game = True
            msg = "  <-- WRONG! should have been: " + correct_answer(self.n)
            msg += "\nGAME OVER! Press any key to quit.\n"
            write(msg)


class Fizzbuzzjazz(Fizzbuzz):
    """ Feedback from Kate: extend this class to make the alpha version jazzier. """

    def __init__(self):
        super().__init__({'f': 'fizz', 'b': 'buzz'})


fbj = Fizzbuzzjazz()









