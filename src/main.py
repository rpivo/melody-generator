# musical notes
# A A# B C C# D D# E F F# G  G#
# 0 1  2 3 4  5 6  7 8 9  10 11
# this number system code be extended for octaves

from random import randint


def generate_melody():
    melody = [0, 0, 0, 0, 0, 0, 0, 0]
    return melody


def get_random_number_between_one_and_eight():
    return randint(1, 8)
