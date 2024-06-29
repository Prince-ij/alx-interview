#!/usr/bin/python3
"""
Script to read stdin line by line and compute metrics:
- Total file size
- Number of lines by status code
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the computed statistics.
    :param total_size: The total size of files.
    :type total_size: int
    :param status_codes: Dictionary of status codes and their counts.
    :type status_codes: dict
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


def log_parsing():
    """
    Reads stdin line by line and computes metrics.
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                    405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) > 6:
                try:
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])
                    total_size += file_size

                    if status_code in status_codes:
                        status_codes[status_code] += 1

                except ValueError:
                    continue

                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    log_parsing()
