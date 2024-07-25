#!/usr/bin/python3
"""
module: 0-making_change

holds one function: makeChange
"""


def makeChange(coins, total):
    """
    Given a list of coins and a total amount, return the minimum number of
    coins needed to make the total.

    Args:
        coins (list): List of positive integers representing the coins.
        total (int): Total amount to be made.

    Returns:
        int: Minimum number of coins needed to make the total.
        If the total cannot be made, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize dp array with a value > the possible number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
