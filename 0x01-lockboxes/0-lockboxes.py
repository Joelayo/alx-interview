#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    checked = set()
    stack = [0]

    while stack:
        box = stack.pop()
        checked.add(box)
        for key in boxes[box]:
            if key not in checked:
                stack.append(key)

    return len(checked) == len(boxes)
