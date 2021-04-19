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

    def __init__(self):
        self.n = 1

    def take_turn(self):
        print(correct_answer(self.n))
        self.n += 1
        timer = Timer(1, fb.take_turn)
        timer.start()

print("*** WELCOME TO FIZZBUZZ! ***")
fb = Fizzbuzz()
timer = Timer(1, fb.take_turn)
timer.start()
