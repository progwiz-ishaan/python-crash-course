"""A module to work with Multiples and Factors."""

def get_factors(number):
    """Returns all the factors of a number."""
    # Set up the variables.
    factors = []
    # Start the for loop.
    for number_to_divide in range(1, number+1):
        # Check if the number is divisible by the current number.
        if number % number_to_divide == 0:
            factors.append(number_to_divide)

    return factors

def get_multiples(number, till, from_=1):
    """Returns all the multiples of a given number till a given number."""
    # Set up the variables.
    multiples = []
     # Start the for loop.
    for number1 in range(from_, till+1):
         multiple = number1 * number
         multiples.append(multiple)

    return multiples

def check_factor(number, factor_to_check):
    """Gives true if the given number is a factor of another given number."""
    return number % factor_to_check == 0

def check_multiple(number, multiple_to_check):
    """Gives true if the given number is a multiple of another given number."""
    return multiple_to_check % number == 0

def is_prime(number):
    """Returns true if the number given is prime."""
    return len(get_factors(number)) == 2

def get_common_factors(number1, number2):
    """Returns the common factors of both the numbers."""
    # Set up the variables.
    common_factors = []
    # Get the factors of number1 and number2
    number1_factors = get_factors(number1)
    number2_factors = get_factors(number2)
    index = 0 # Keep track of which factor we are on.
    # Check which list is shorter.
    if len(number1_factors) > len(number2_factors):
        shorter_list = number2_factors[:]
    else:
        shorter_list = number1_factors[:]
    # Start the for loop.
    for e in shorter_list:
        # Append the current factor if the factors are common
        if number1_factors[index] == number2_factors[index]:
            common_factors.append(number2_factors[index])

        index += 1 # Increse the value of index so it dosent remain 0.
    return common_factors

def get_common_multiples(number1, number2, number_of_multiples):
    """Returns common multiples of 2 given numbers."""
    # Set up the variables.
    common_multiples = []
    # Keep track var
    index = 1
    # Start the while loop.
    while not len(common_multiples) == number_of_multiples:
        number1_multiple = get_multiples(number1, index+1, from_=index)
        number2_multiple = get_multiples(number2, index+1, from_=index)
        if number1_multiple == number2_multiple:
            common_multiples.append(number2_multiple)

    return common_multiples