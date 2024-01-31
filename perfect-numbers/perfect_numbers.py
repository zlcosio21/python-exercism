def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    total = sum(num_iterator for num_iterator in range(1, number) if number % num_iterator == 0)

    if total == number:
        return "perfect"

    if total > number:
        return "abundant"

    return "deficient"
