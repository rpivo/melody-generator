# musical notes
# A A# B C C# D D# E F F# G  G#
# 0 1  2 3 4  5 6  7 8 9  10 11
# this number system code be extended for octaves

from random import randint


def generate_melody():
    l = []
    for i in range(0, 8):
        if i == 0 or i == 7:
            l.append(get_zero_or_seven())
        else:
            l.append(get_random_number_between_zero_and_seven())
    return l


def get_random_number_between_zero_and_seven():
    return randint(0, 7)


def get_zero_or_seven():
    n = randint(0, 1)
    return n if n == 0 else 7
