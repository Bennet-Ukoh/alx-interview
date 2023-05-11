#!/usr/bin/python3

"""Reads stdin line by line and computes metrics."""

import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

# Define signal handler for CTRL+C


def signal_handler(sig, frame):
    """Handler for the SIGINT signal.

    Args:
        sig (int): The signal number.
        frame (frame): The interrupted stack frame.
    """
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Define function to print metrics


def print_stats():
    """Prints statistics from the beginning of the program.

    Args:
        total_size (int): The total file size.
        status_codes (dict): contains the count of lines for each status code.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        if count > 0:
            print("{}: {}".format(code, count))

# Read from stdin line by line
for line in sys.stdin:
    line_count += 1

    # Parse line and update metrics
    parts = line.split()
    if len(parts) == 9:
        try:
            status_code = int(parts[7])
            file_size = int(parts[8])
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_file_size += file_size
        except ValueError:
            pass

    # Print metrics every 10 lines
    if line_count == 10:
        print_stats()
        line_count = 0

# Print final metrics
print_stats()
