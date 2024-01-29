def is_armstrong_number(number):
    num_string = str(number)
    total = 0

    for num in num_string:
        total += int(num) ** len(num_string)

    return total == number