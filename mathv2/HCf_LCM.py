import multiples_factors as mf

def get_hcf(number1, number2):
    """Returns HCF of 2 given numbers."""
    # Give error if either of the params are not int.
    if not number == int or not factor_to_check == int:
        raise ValueError("Can only except 'int'")
    else:
        # Get the common factors
        common_factors = mf.get_common_factors(number1, number2)

        return max(common_factors)