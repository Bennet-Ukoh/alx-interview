# Star Wars Characters Script

This script retrieves and prints the names of all characters from a Star Wars movie using the Star Wars API and the request module.

## Prerequisites

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var
- requests module

## Installation

1. Clone this repository or download the script file (`0-star_wars_characters.js`) to your local machine.
2. Install the `requests` module

## Usage

Run the script by providing a movie ID as the argument. The movie ID corresponds to a specific Star Wars movie.

Example usage:

./0-starwars_characters.js 3


Replace `3` with the desired movie ID. The script will retrieve the characters' names for that movie and display them on separate lines.

## Notes

- The script uses the Star Wars API to retrieve movie and character data.
- If a character's data fails to be retrieved, an error message will be displayed.
