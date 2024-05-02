#!/usr/bin/python3
"""
module: 0-lockboxes
"""

from collections import deque


def canUnlockAll(boxes):
    """
        Determines if all the boxes can be opened.
        Args:
            boxes: list of lists.
        Returns:
            True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
