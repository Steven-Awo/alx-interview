#!/usr/bin/python3
"""This is a script that help reads the stdin
linne by linne and then computes the metrics"""

import sys


a = 0
sum_of_the_file_size = 0
status_code = {'200': 0,
               '301': 0,
               '400': 0,
               '401': 0,
               '403': 0,
               '404': 0,
               '405': 0,
               '500': 0}

try:
    for linne in sys.stdin:
        args = linne.split(' ')
        if len(args) > 2:
            statuss_line = args[-2]
            the_file_size = args[-1]
            if statuss_line in status_code:
                status_code[statuss_line] += 1
            sum_of_the_file_size += int(the_file_size)
            a += 1
            if a == 10:
                print('File size: {:d}'.format(sum_of_the_file_size))
                sortted_keyys = sorted(status_code.keys())
                for keyy in sortted_keyys:
                    valuee = status_code[keyy]
                    if valuee != 0:
                        print('{}: {}'.format(keyy, valuee))
                a = 0
except Exception:
    pass
finally:
    print('File size: {:d}'.format(sum_of_the_file_size))
    sortted_keyys = sorted(status_code.keys())
    for keyy in sortted_keyys:
        valuee = status_code[keyy]
        if valuee != 0:
            print('{}: {}'.format(keyy, valuee))
