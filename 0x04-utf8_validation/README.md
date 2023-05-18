# UTF-8 Validation
This repository contains a Python script developed as a project for Holberton School. The script implements a method for determining if a given data set represents a valid UTF-8 encoding.

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- The code should follow the PEP 8 style guidelines (version 1.7.x)
- All files must be executable

## Task
0. UTF-8 Validation
Write a method called validUTF8(data) that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: def validUTF8(data)
- Return: True if the data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, so you only need to handle the 8 least significant bits of each integer

Example usage:

    validUTF8 = __import__('0-validate_utf8').validUTF8

    data = [65]
    print(validUTF8(data))  # Output: True

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # Output: True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # Output: False

### Repository
GitHub repository: [alx-interview](https://github.com/Bennet-Ukoh/alx-interview)
Directory: 0x04-utf8_validation
File: 0-validate_utf8.py
This project was completed as part of the curriculum at [Holberton School](https://www.holbertonschool.com/). Feel free to explore the code and use it as needed!
