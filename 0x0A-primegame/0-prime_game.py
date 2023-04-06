#!/usr/bin/python3
""" prime game"""


def isWinner(x, nums):
    """ returns the winner of the primegame"""
    mariaWins = 0
    benWins = 0
    Round = 0
    while (Round < x):
        winner = playPrime(nums[Round])
        if winner == 'Ben':
            benWins += 1
        if winner == 'Maria':
            mariaWins += 1
        Round += 1
    if benWins > mariaWins:
        return 'Ben'
    if benWins < mariaWins:
        return 'Maria'
    else:
        return None


# play primegame
def playPrime(n):
    """ initiates play"""
    turn = 0
    nums = []
    if n == 1:
        return 'Ben'
    for i in range(1, n + 1):
        nums.append(i)
    for j in nums[:]:
        # first move maria
        if turn == 0 and j == 2:
            turn += 1
            for i in nums[:]:
                if i % j == 0:
                    nums.remove(i)
        elif turn == 0 and j > 2:
            # marias turn
            if j % 2 != 0:
                for i in nums[:]:
                    if i % j == 0:
                        nums.remove(i)
                        turn += 1
        elif turn == 1:
            # bens turn
            if j % 2 != 0:
                for i in nums[:]:
                    if i % j == 0:
                        nums.remove(i)
                        turn -= 1
    if turn == 0:
        return 'Ben'
    if turn == 1:
        return 'Maria'
