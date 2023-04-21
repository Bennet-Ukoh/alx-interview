#!/usr/bin/python3
"""
0-pascal_triangle

"""

def pascal_triangle(n):
    """
    Generate the first n rows of Pascal's triangle.

    Args:
        n: The number of rows to generate.

    Returns:
        A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        # If n is less than or equal to 0, return an empty list.
        return []

    # Create a list to store the rows of Pascal's triangle.
    triangle = [[1]]

    # Loop through each row of Pascal's triangle, starting with the second row.
    for i in range(1, n):
        # Create a list to store the current row of Pascal's triangle.
        row = [1]

        # Loop through each element in the current row, except for the first and last elements.
        for j in range(1, i):
            # Calculate the value of the current element by adding the two elements above it in the previous row.
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)

        # Add the last element of the current row (which is always 1).
        row.append(1)

        # Add the current row to the triangle.
        triangle.append(row)

    # Return the triangle.
    return triangle

