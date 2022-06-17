import random
from django import template

register = template.Library()


def shuffle(arg):
    first = random.choice(arg[:])
    second = random.choice(arg[:])
    third = random.choice(arg[:])
    if first != second != third:
        return [first, second, third]
    else:
        shuffle(arg)


register.filter('shuffle', shuffle)
