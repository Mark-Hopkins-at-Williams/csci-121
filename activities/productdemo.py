from threading import Timer

def correct_answer(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)

class Fizzbuzz:

    def __init__(self, maximum):
        self.n = 1
        self.maximum = maximum

    def take_turn(self):
        print(correct_answer(self.n))
        self.n += 1
        if self.n <= self.maximum:
            timer = Timer(1, self.take_turn)
            timer.start()

print("*** WELCOME TO FIZZBUZZ! ***")
fb = Fizzbuzz(15)
timer = Timer(1, fb.take_turn)
timer.start()
