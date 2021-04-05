"""A module to work with Multiples and Factors."""

def get_factors(number):
    """Returns all the factors of a number."""
    # Give error if either of the params are not int.
    if not number == int or not factor_to_check == int:
        raise ValueError("Can only except 'int'")
    else:
        # Set up the variables.
        factors = []
        # Start the for loop.
        for number_to_divide in range(1, number+1):
            # Check if the number is divisible by the current number.
            if number % number_to_divide == 0:
                factors.append(number_to_divide)

        return factors

def get_multiples(number, till):
    """Returns all the multiples of a given number till a given number."""
    # Give error if either of the params are not int.
    if not number == int or not factor_to_check == int:
        raise ValueError("Can only except 'int'")
    else:
        # Set up the variables.
        multiples = []
        # Start the for loop.
        for number1 in range(1, till+1):
            multiple = number1 * number
            multiples.append(multiple)

        return multiples

def check_factor(number, factor_to_check):
    """Gives true if the given number is a factor of another given number."""
    # Give error if either of the params are not int.
    if not number == int or not factor_to_check == int:
        raise ValueError("Can only except 'int'")
    else:
        return number % factor_to_check == 0

def check_multiple(number, multiple_to_check):
    """Gives true if the given number is a multiple of another given number."""
    # Give error if either of the params are not int.
    if not number == int or not multiple_to_check == int:
        raise ValueError("Can only except 'int'")
    else:
        return multiple_to_check % number == 0

def is_prime(number):
    """Returns true if the number given is prime."""
    # Give error if either of the param is not int.
    if not number == int:
        raise ValueError("Can only except 'int'")
    else:
        return len(get_factors(number)) == 2

def get_common_factors(number1, number2):
    """Returns the common factors of both the numbers."""
    # Give error if either of the params are not list.
    if not number1 == int or not number2 == int:
        raise ValueError("Can only except 'list'")
    else: # Else return common factors
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