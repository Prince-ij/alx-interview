#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.
    :param grid: A list of list of integers where 0
    represents water and 1 represents land.
    :type grid: list of list of int
    :return: The perimeter of the island.
    :rtype: int
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides
                if i == 0 or grid[i-1][j] == 0:  # Top
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1

    return perimeter
