#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    # Set of boxes that have been unlocked
    unlocked = {0}
    # Stack of boxes to check
    stack = [0]

    # Repeat the process until all boxes have been checked
    while stack:
        # Get the next box to check
        box = stack.pop()
        # Check if the box contains any keys
        for key in boxes[box]:
            if key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    # Return whether all boxes have been unlocked
    return len(unlocked) == len(boxes)
