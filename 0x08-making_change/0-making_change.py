#!/usr/bin/python3
"""
makeChange Module
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the dp array
    dp = [float('inf') for _ in range(total+1)]
    dp[0] = 0

    for c in coins:
        for j in range(c, total+1):
            if j >= c:
                dp[j] = min(dp[j], dp[j-c] + 1)

    return dp[total] if dp[total] < float('inf') else -1
