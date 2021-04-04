"""A module to work with Multiples and Factors."""

def get_factors(number):
    """Returns all the factors of a number."""
    factors = []
    for number_to_divide in range(1, number+1):
        if number % number_to_divide == 0:
            factors.append(number_to_divide)

    return factors