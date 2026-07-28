def parse_positive_int(value):
    try:
        number = int(value)
    except ValueError:
        return None

    if number <= 0:
        return None

    return number


def parse_positive_float(value):
    try:
        number = float(value.replace(",", "."))
    except ValueError:
        return None

    if number <= 0:
        return None

    return number
