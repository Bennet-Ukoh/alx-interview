# Island Perimeter

The "island_perimeter" script is a Python program that calculates the perimeter of an island described in a given grid.

## Usage

To use the script, follow these steps:

1. Make sure you have Python 3 installed on your system.
2. Save the "island_perimeter.py" file to your desired location.
3. Open a terminal or command prompt.
4. Navigate to the directory where the "island_perimeter.py" file is located.
5. Run the script by executing the following command:

./island_perimeter.py

6. The script will calculate and display the perimeter of the island based on the provided grid.

## Grid Format

The grid is represented as a list of lists, where each inner list represents a row of the grid. The elements of the inner lists can be either 0 or 1, where:

- 0 represents water
- 1 represents land

The grid should satisfy the following conditions:

- The cells are square, with a side length of 1.
- The cells are connected horizontally or vertically (not diagonally).
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

## Example

Here's an example usage of the script:

grid = [
 [0, 1, 0, 0],
 [1, 1, 1, 0],
 [0, 1, 0, 0],
 [1, 1, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 16
In this example, the grid represents an island where land cells are marked with 1 and water cells with 0. The script will calculate and output the perimeter of the island, which is 16 units.
