def value(colors):
    RESISTANCE_VALUES = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    result = ""

    for color in colors[:2]:
        result += f"{RESISTANCE_VALUES[color]}"

    return int(result)
