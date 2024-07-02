#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game after x rounds
    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing the upper limit of
the range of numbers for each round
    Returns:
        str: The name of the player that won
the most rounds ("Maria" or "Ben").
        None: If the winner cannot be determined.
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)
    # Sieve of Eratosthenes to find all primes up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False
    for start in range(2, int(max_num ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_num + 1, start):
                is_prime[multiple] = False
    # Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Determine the winner for each game
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
