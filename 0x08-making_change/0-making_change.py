#!/usr/bin/python3
'''
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given total total.
'''

def makeChange(coins, total):
    """
    For a given few coins

    Args:
        coins: List of coin denominations available.
        total: Integer value for the target total.

    Returns:
        Integer: The fewest number of coins needed to meet the total.
        If the total is 0 or less, return 0.
        If the total cannot be met by any number of coins available, return -1.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value and update the dp list
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the value at the total amount is still infinity, it means the amount cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]
