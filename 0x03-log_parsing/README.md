# Log Parsing Script
This is a Python script that reads log data from standard input (stdin) and computes metrics based on the input format. The input format is as follows:

```<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>```

After every 10 lines of input and/or a keyboard interruption (CTRL + C), the script prints the following statistics from the beginning:

- Total file size: the sum of all previous file sizes
- Number of lines by status code: counts for each of the possible status codes (200, 301, 400, 401, 403, 404, 405, and 500) that appear in the input data

## Requirements
- Python 3.4.3
- PEP 8 style (version 1.7.x)
- Executable permissions for all script files

## Usage
To use this script, simply pipe log data into it from the command line:

``` $ ./log_parsing.py < access.log ```

The script will begin reading and parsing log data from standard input. It will output statistics to the console after every 10 lines of input and/or a keyboard interruption (CTRL + C). To stop the script, use the keyboard interruption command.

## Author
This script was written by Bennet Ukoh. 
- Feel free to contact me with any questions or feedback.
