#!/usr/bin/python3
"""
Module for determining the fewest number of
coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet the given total.
    :param coins: A list of the values of the coins in possession.
    :type coins: list of int
    :param total: The total amount to be met.
    :type total: int
    :return: Fewest number of coins needed to meet the
total, or -1 if the total cannot be met.
    :rtype: int
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum coins
    # for each amount up to the total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
