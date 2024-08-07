#!/usr/bin/python3
"""
module: 0-prime_game

function: isWinner
"""


def isWinner(x, nums):
    """
    Determines the winner of a game based on a list of numbers.

    Args:
        x (int): The number of players in the game.
        nums (List[int]): A list of numbers representing the game.

    Returns:
        str or None: The name of the winner ("Maria" or "Ben")
        if there is a winner, None otherwise.
    """
    def is_prime(n):
        """
        Determines if a given integer is prime.

        Args:
            n (int): The integer to check.

        Returns:
            bool: True if the integer is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Generates a list of prime numbers up to the given number `n`.

        Parameters:
            n (int): The upper limit for the prime numbers.

        Returns:
            List[int]: A list of prime numbers between 2 and `n` (inclusive).
        """
        return [i for i in range(2, n + 1) if is_prime(i)]

    def play_game(n):
        """
        Determines if the number of prime numbers up to a
        given number `n` is odd.

        Parameters:
            n (int): The upper limit for the prime numbers.

        Returns:
            bool: True if the number of prime numbers is odd, False otherwise.
        """
        primes = get_primes(n)
        return len(primes) % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
