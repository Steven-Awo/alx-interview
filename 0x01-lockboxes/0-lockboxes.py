#!/usr/bin/python3
"""the method that's to determine if all the boxes could
actually be opened"""


def canUnlockAll(boxes):

    if (type(boxes) is not list):
        return False

    if (len(boxes) == 0):
        return False

    keyys = [0]
    for k in keyys:
        for b in boxes[k]:
            if b not in keyys and b != k and b < len(boxes) and b != 0:
                keyys.append(b)
    if len(keyys) == len(boxes):
        return True
    else:
        return False
