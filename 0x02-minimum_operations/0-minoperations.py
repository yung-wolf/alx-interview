#!/usr/bin/python3
"""
module: checkPrime
This program holds two functions.

is_prime: Determines if a given number is prime.

minOperations: Calculates the prime factors of a given number.
"""


def is_prime(num):
    """
    Determines if a given number is prime.

    Args:
        num (int): The number to check for primality.

    Returns:
        0 if number is prime.
        1 if number is NOT prime.
    """
    number_to_check = num
    for x in range(2, num + 1):
        if number_to_check % x == 0 and x != number_to_check:
            return 1
    return 0


def minOperations(num):
    """
    Calculates the minimum operations required to find the n chars using the
    prime factors of a given number (n).

    :param num: The number to calculate the prime factors of.
    :type num: int
    :return: A sum of prime factors.
    :rtype: int
    """
    # Initialize variables for the function
    number_to_get_factors = num
    prime_factors = []

    # if num is impossible return 0
    if num <= 1:
        return 0

    # If the number is prime, return a list with the number itself
    check = is_prime(num)
    if check == 0:
        return num

    # If the number is not prime, iterate through numbers from 2 to the
    # given number (inclusive)
    for x in range(2, num + 1):
        # Check if the number is divisible by x and x is not equal to the
        # number
        if number_to_get_factors % x == 0 and x != number_to_get_factors:
            # Check if x is prime
            check = is_prime(x)
            # If x is prime, append it to the prime_factors list
            if check == 0:
                prime_factors.append(x)
                # Divide the number by x repeatedly until it is no longer
                # divisible by x
                number = number_to_get_factors
                while (number / x) % x == 0:
                    prime_factors.append(x)
                    number = number / x

    # Return the list of prime factors
    return sum(prime_factors)
