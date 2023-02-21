#!/usr/bin/python3
"""
defines validUTF8 function
"""


def validUTF8(data):
    """
    validates UTF8 encoding.
    Return: True if data is valid UTF-8 encoding, else return False.
    """
    countOfBytes = 0
    oneVer = 1 << 7
    secondVer = 1 << 6

    for i in data:
        mask_n_bytes = 1 << 7
        if countOfBytes == 0:
            while mask_n_bytes & i:
                countOfBytes += 1
                mask_n_bytes = mask_n_bytes >> 1
            if countOfBytes == 0:
                continue
            if countOfBytes == 1 or countOfBytes > 4:
                return False
        else:
            if not (i & oneVer and not (i & secondVer)):
                return False
        countOfBytes -= 1
    if countOfBytes == 0:
        return True
    return False
