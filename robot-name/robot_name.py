from string import ascii_uppercase as uppers
from random import choice, randint


class Robot:
    NAMES = []

    def __init__(self):
        self.name = Robot.get_unique_random_name()

    def reset(self):
        self.name = Robot.get_unique_random_name()

    @staticmethod
    def get_unique_random_name():
        name = Robot.get_random_name()
        while name in Robot.NAMES:
            name = Robot.get_random_name()
        Robot.NAMES.append(name)
        return name

    @staticmethod
    def get_random_name():
        return choice(uppers) + choice(uppers) + str(randint(100, 999))
