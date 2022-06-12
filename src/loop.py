#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-CNA-410-PAR-4-1-groundhog-samuel.shemtov
## File description:
## loop.py
##

import sys
import statistics
import math

from src.check import *
from src.calc_temperature import *

def loop(period, value):
    i = 0
    tabr = []
    nbSwitches = int(0)
    while 1:
        value_user = input()    
        if check_float(value_user):
            value.append(float(value_user))
            nbSwitches = display(period, value, tabr, nbSwitches, i)
            i += 1
        elif value_user == "STOP":
            if len(tabr) <= 0:
                sys.exit(84)
            else:
                display_end(period, value, tabr, nbSwitches, i)
        else:
            sys.exit(84)

def get_weirdest(period, value, tabr):
    del tabr[0];
    calc = []
    highest = []
    weirdest = []

    if len(tabr) < 5:
        sys.exit(0)
    for i in range (0, len(value)):
        calc.append(abs(value[i] - statistics.median(value)))
        highest.append(abs(value[i] - statistics.median(value)))
    highest.sort()
    highest = highest[-5:]
    for i in range (0, 5):
        weirdest.append(value[calc.index(highest[i])])
    print("5 weirdest values are", weirdest)
    sys.exit(0)

def display_end(period, value, tabr, nbSwitches, i):
    tabWeird = []
    print("Global tendency switched", nbSwitches, "times")
    get_weirdest(period, value, tabr)
