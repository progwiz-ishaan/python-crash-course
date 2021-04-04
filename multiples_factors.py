"""A module to work with Multiples and Factors."""

def get_factors(number):
    """Returns all the factors of a number."""
    factors = []
    for number_to_divide in range(1, number+1):
        if number % number_to_divide == 0:
            factors.append(number_to_divide)

    return factors

def get_multiples(number, till):
    """Returns all the multiples of a given number till a given number."""
    multiples = []
    for number1 in range(1, till+1):
        multiple = number1 * number
        multiples.append(multiple)

    return multiples

def check_factor(number, factor_to_check):
    """Gives true if the given number is a factor of another given number."""
    is_factor = number % factor_to_check == 0
    return is_factor

def check_multiple(number, multiple_to_check):
    """Gives true if the given number is a multiple of another given number."""
    is_multiple = multiple_to_check % number == 0
    return is_multiple

def is_prime(number):
    """Returns true if the number given is prime."""
    return len(get_factors(number)) == 2

def get_common_factors(number1, number2):
    number1_factors = get_factors(number1)
    number2_factors = get_factors(number2)
    all_factors = number1_factors[:] + number2_factors[:]
    index = 0
    for e in range(min(all_factors), max(all_factors)+1):
        if number1_factors[index]