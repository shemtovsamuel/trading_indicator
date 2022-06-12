#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## undefined
## File description:
## main.py
##

import sys

from src.check import *
from src.calc_temperature import *
from src.loop import *

def main(av):
    value = []
    check_error(len(av), av)
    period = int(av[1])
    loop(period, value)

if __name__ == "__main__":
    main(sys.argv)
