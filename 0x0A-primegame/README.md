# Prime Game

This is a Python program that implements the Prime Game. In this game, Maria and Ben take turns selecting prime numbers from a set of consecutive integers and removing them and their multiples from the set. The player who cannot make a move loses the game. The program determines the winner of each round based on the given set of numbers.

## Requirements

- Allowed editors: vi, vim, emacs
- All files are interpreted/compiled on Ubuntu 14.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- All files must be executable
- Code should use the PEP 8 style (version 1.7.x)
- The program does not import any packages

## Usage

To use the program, follow these steps:

1. Clone the repository: `git clone https://github.com/Bennet-Ukoh/alx-interview`
2. Navigate to the project directory: `cd 0x0A-primegame`
3. Run the program: `./0-prime_game.py`
4. Modify the `x` and `nums` variables in the code to specify the number of rounds and the array of numbers for each round.
5. Save the changes.
6. Execute the program: `./0-prime_game.py`
7. The program will output the name of the player who won the most rounds or "None" if the winner cannot be determined.

## Example

Here is an example usage of the program:

```python
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))

Output:

Ben

In the example above, there are three rounds with the given numbers. The program determines that Ben wins the first and third rounds, while Maria wins the second round.

## Limitations
- The program assumes that the input values n and x will not exceed 10000.
- The program does not handle invalid input or error conditions.

## Author: Bennet Ukoh
