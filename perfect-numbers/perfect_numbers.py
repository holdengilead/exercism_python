def factors(n):
    return set(
        factor
        for i in range(1, int(n ** 0.5) + 1)
        if n % i == 0
        for factor in (i, n // i)
    )


def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum = sum(factors(number)) - number
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    return "deficient"
