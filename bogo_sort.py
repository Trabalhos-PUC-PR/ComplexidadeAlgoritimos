import random

from gerador import agora


def is_sorted(x):
    for i in range(1, len(x)):
        if x[i] < x[i - 1]:
            return False
    return True


def bogo_sort(x, timeout=2_000):
    random.shuffle(x)
    start = agora()
    while not is_sorted(x):
        random.shuffle(x)
        if agora() - start >= timeout:
            # print('BOGO SORT DEU TIMEOUT!')
            return None
    return x
