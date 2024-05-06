#!/usr/bin/python3
"""Validating if data is a UTF-8"""


def validUTF8(data):
    """
    This method that helps to determine if that the given data set
    actually represents a actual valid UTF-8 encoding
    """
    numbbytes = 0

    bb1 = 1 << 7
    bb2 = 1 << 6

    for d in data:
        bb = 1 << 7
        if numbbytes == 0:
            while bb & d:
                numbbytes += 1
                bb = bb >> 1
            if numbbytes == 0:
                continue
            if numbbytes == 1 or numbbytes > 4:
                return False
        else:
            if not (d & bb1 and not (d & bb2)):
                return False
        numbbytes -= 1
    return numbbytes == 0
