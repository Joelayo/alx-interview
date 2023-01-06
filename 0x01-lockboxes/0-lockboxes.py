#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    # Set of boxes that have been checked
    checked = set()
    # Stack of boxes to check
    stack = [0]

    # Repeat the process until all boxes have been checked
    while stack:
        # Get the next box to check
        box = stack.pop()
        # Add the box to the set of checked boxes
        checked.add(box)
        # Check if the box contains any keys
        for key in boxes[box]:
            # If the key corresponds to an unchecked box, add it to the stack
            if key not in checked:
                stack.append(key)

    # Return whether all boxes have been checked
    return len(checked) == len(boxes)
