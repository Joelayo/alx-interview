#!/usr/bin/python3
"""
Minimum OPerations
"""


def minOperations(n):
    if not isinstance(n, int) or n < 1:
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0 or n % done != 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        else:
            # paste
            done += clipboard
            ops_count += 1
    return ops_count
