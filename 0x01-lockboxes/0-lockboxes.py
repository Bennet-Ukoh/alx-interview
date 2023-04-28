#!/usr/bin/env python3

"""
Module for solving the "Lockboxes" interview question.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked given a list of boxes, where each
    box contains keys to other boxes, and the first box is initially unlocked.
    A key with the same number as a box opens that box. Returns True if all
    boxes can be opened, else returns False.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)
    return all(visited)
