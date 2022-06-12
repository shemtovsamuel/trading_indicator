#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## undefined
## File description:
## check.py
##

import sys

def helper():
    print("SYNOPSIS")
    print("    ./groundhog period\n")
    print("DESCRIPTION")
    print("    period    the number of days defining a period")

def check_error(ac, av):
    if ac != 2:
        sys.exit(84)
    if av[1] == "-h":
        helper();
        sys.exit(0)
    if av[1].isdigit() == False:
        sys.exit(84)
    if int(av[1]) <= 0:
        sys.exit(84)

def check_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
