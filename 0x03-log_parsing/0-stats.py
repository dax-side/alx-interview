#!/usr/bin/python3
""" reads from std """
import sys


def print_status(sdict, fsize):
    """ prints format """
    print("File size: {}".format(fsize))
    for key in sorted(sdict.keys()):
        if sdict[key] != 0:
            print("{}: {}".format(key, sdict[key]))


def log_parsing():
    """ print logs"""
    count = 0
    fsize = 0
    status_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line in sys.stdin:
            if count != 0 and count % 10 == 0:
                print_status(status_dict, fsize)

            File = line.split()
            count += 1

            try:
                fsize += int(File[-1])
            except Exception:
                pass
            try:
                if File[-2] in status_dict.keys():
                    status = File[-2]
                    status_dict[status] += 1
            except Exception:
                pass
        print_status(status_dict, fsize)

    except KeyboardInterrupt:
        print_status(status_dict, fsize)
        raise


log_parsing()
