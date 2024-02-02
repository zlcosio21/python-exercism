import math


def score(x, y):
    distance = math.sqrt(x**2 + y**2)

    bands_score = [(1, 10), (5, 5), (10, 1)]

    for band, score in bands_score:
        if distance <= band:
            return score

    return 0
