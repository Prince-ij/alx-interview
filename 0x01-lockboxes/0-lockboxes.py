#!/usr/bin/python3
"""
Module for determining if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    :param boxes: List of lists, where each sublist contains key
    s for other boxes.
    :type boxes: list
    :return: True if all boxes can be unlocked, otherwise False.
    :rtype: bool
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is initially unlocked
    keys = [0]  # Start with the keys from the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
