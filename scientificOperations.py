import math


def scientific_calculate(operation, num1):
    """
    Performs the given scientific operation on the given number, which may be either an integer or a float.

    args:
        - operation: the operation to perform (sin, cos, tan, ln)
        - num1: the number to perform the operation on

    returns:
        - the result of the operation on the given number
    """

    if operation == 'sin':
        return math.sin(num1)

    elif operation == 'cos':
        # TODO: finish this statement
        # - should return the cosine of num1
        math.cos(num1)

    elif operation == 'tan':
        # TODO: finish this statement
        # - should return the tangent of num1
        math.tan(num1)

    elif operation == 'ln':
        # TODO: finish this statement
        # - should return the natural log of num1
        math.ln(num1)

    else:
        raise ValueError(
            'Invalid Operation: Scientific Operations are (sin, cos, tan, ln, sqrt, !, ^, and %)')
