#!/usr/bin/python3
"""
This module has a kind of function that calculates
and then returns the island's perimetr that was
described in the grid
"""


def island_perimeter(grid):
    """The island's function that prints the outputs
    of the perimetr of the island that was described
    by the grid"""
    perimetr = 0
    the_grids_lengt = len(grid)
    for roww in range(the_grids_lengt):
        for colummn in range(len(grid[roww])):
            if grid[roww][colummn] == 1:
                if roww - 1 < 0 or grid[roww - 1][colummn] == 0:
                    perimetr += 1

                if colummn - 1 < 0 or grid[roww][colummn - 1] == 0:
                    perimetr += 1

                if colummn + 1 >= len(grid[roww]) or grid[roww][colummn + 1] == 0:
                    perimetr += 1

                if roww + 1 >= the_grids_lengt or grid[roww + 1][colummn] == 0:
                    perimetr += 1
    return perimetr
