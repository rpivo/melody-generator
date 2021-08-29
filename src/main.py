# musical notes
# A A# B C C# D D# E F F# G  G#
# 0 1  2 3 4  5 6  7 8 9  10 11
# this number system code be extended for octaves

from random import randint


def generate_melody():
    return [get_random_number_between_zero_and_eight() for n in range(0, 8)]


def get_random_number_between_zero_and_eight():
    return randint(0, 8)


def get_zero_or_eight():
    n = randint(0, 1)
    return n if n == 0 else 8
