#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    checked = set()
    # Queue of boxes to check
    queue = [0]

    # Repeat the process until all boxes have been checked
    while queue:
        # Get the next box to check
        box = queue.pop(0)
        # Add the box to the set of checked boxes
        checked.add(box)
        # Check if the box contains any keys
        for key in boxes[box]:
            # If the key corresponds to an unchecked box, add it to the queue
            if key not in checked:
                queue.append(key)

    # Return whether all boxes have been checked
    return len(checked) == len(boxes)
