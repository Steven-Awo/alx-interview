#!/usr/bin/python3
"""
Making an algotithm that makes coin change
"""


def makeChange(coins, total):
    """Calculating up the fewest needed number to meet the
    given total of amount.
    Args:
        coins ([list]): A list of all the coin's values thats
        available.
        total ([number]): The amount to reach
    Return: The fewest number of the coins thats needed to be able
    to reach the given total, or -1 if isnt possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    n, numb_coins = (0, 0)
    cpy_the_total = total
    length_of_coins = len(coins)

    while(n < length_of_coins and cpy_the_total > 0):
        if (cpy_the_total - coins[n]) >= 0:
            cpy_the_total -= coins[n]
            numb_coins += 1
        else:
            n += 1

    checking = cpy_the_total > 0 and numb_coins > 0
    return -1 if checking or numb_coins == 0 else numb_coins
