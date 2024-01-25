def is_triangle(sides):

    return 2 * max(sides) < sum(sides)


def equilateral(sides):
    a, b, c = sides

    return is_triangle(sides) and (a == b == c)


def isosceles(sides):
    a, b, c = sides

    return is_triangle(sides) and (a == b or b == c or c == a)


def scalene(sides):
    a, b, c = sides

    return is_triangle(sides) and (a != b and b != c and c != a)