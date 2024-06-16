#!/usr/bin/python3
"""Creating a prime game's winner for determination"""


def isWinner(x, nums):
    """A function that returns the prime's game
    winner determination"""
    if x < 1 or not nums:
        return None

    maxi_wins = 0

    bb_wins = 0

    n = max(nums)

    primesWin = [True] * (n + 1)

    primesWin[0] = primesWin[1] = False

    for a in range(2, int(n**0.5) + 1):
        if primesWin[a]:
            for b in range(a**2, n + 1, a):
                primesWin[b] = False

    for n in nums:
        counterr = sum(primesWin[2:n+1])

        bb_wins += counterr % 2 == 0

        maxi_wins += counterr % 2 == 1

    if maxi_wins == bb_wins:
        return None

    return 'Maria' if maxi_wins > bb_wins else 'Ben'
