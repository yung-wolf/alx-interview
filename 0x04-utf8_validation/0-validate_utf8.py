#!/usr/bin/python3
"""
module: 0-validate_utf8

Holds one function: validUTF8(data)
"""


def validUTF8(data):
    """
    Determine if the given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes.
    :return: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    # Masks to check if the most significant bit is set or not
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Get the binary representation of the current byte
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1 bits
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # If n_bytes is 0, it means it is a 1-byte character
            if n_bytes == 0:
                continue

            # If the number of bytes is more than 4 or 1
            # (which is invalid as per UTF-8 standard)
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte follows the pattern 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    # If we finished processing and n_bytes is not 0, then it's invalid
    return n_bytes == 0
