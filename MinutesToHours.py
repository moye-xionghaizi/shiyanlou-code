#! /usr/bin/env python3
import sys
def Hours(minute):
    # if minute is less than 0 ,raise Exception
    if minute < 0:
        raise ValueError("Input number cannot be negative")
    else:
        hour,min = divmod(minute,60)
        print("{} H ,{} M".format(hour,min))

try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")
