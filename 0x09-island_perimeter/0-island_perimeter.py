#!/usr/bin/python3
"""
module: 0-island_perimeter
returns: the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a given grid.

    Parameters:
        grid (List[List[int]]): A 2D grid representing the island.
        Each element in the grid is either 0 or 1,
        where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
