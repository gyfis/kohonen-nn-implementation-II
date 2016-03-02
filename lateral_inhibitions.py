import math
from operator import sub

def __id_man_dist(id1, id2):
    return sum(map(abs, map(sub, id1, id2)))


def __id_euc_dist(id1, id2):
    return math.sqrt(sum(map(lambda x, y: (x - y)**2, id1, id2)))


def hex_loc(id):
    return id[0] * math.sqrt(3/4), id[1] if id[0] % 2 == 0 else id[1] + 0.5
    # return id[0] if id[1] % 2 == 0 else id[0] + 0.5, id[1] * math.sqrt(3/4)


def gauss(id1, id2, diameter):
    return math.e**-(__id_euc_dist(id1, id2) / diameter)**2


def gauss_hex(id1, id2, diameter):
    return math.e**-(__id_euc_dist(hex_loc(id1), hex_loc(id2)) / diameter)**2