#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-CNA-410-PAR-4-1-groundhog-samuel.shemtov
## File description:
## calc_temperature.py
##

import sys
import math

def temperatureIncreadeAverage(value, i, period):
    g = 0
    index = len(value) - period
    while (index != len(value)):
        x = value[index] - value[index - 1]
        g += x if x > 0 else 0
        index += 1
    try:
        g /= period
    except ZeroDivisionError:
        g = 0
    return g

def relativeTemperatureEvolution(value, i, period):
    lastr = 0
    r = 0
    if (r != "nan"):
        lastr = r
    x = value[len(value) - period - 1]
    y = value[-1]
    if (x == 0):
        r = int(0)
    else:
        r = int((round((y - x) / x * 100)))
    return r

def standardDeviation(value, i , period):
    s = 0
    end = len(value)
    x = 0
    y = 0

    for i in range (end - period, end):
        x = x + value[i]
        y = y + pow(value[i], 2)
    s = math.sqrt(y / period - pow(x / period, 2))
    return s

def temperatureSwitches(currentr, lastr):
    if (lastr > 0 and currentr < 0):
        return True
    elif (lastr < 0 and currentr > 0):
        return True
    else:
        return False

def display(period, value, tabr, nbSwitches, i):
    g = float(0)
    r = float(0)
    s = float(0)
    switch = False

    print("g=", end = "")
    if (i < period):
        print("nan", end = "")
    else:
        g = temperatureIncreadeAverage(value, i, period)
        print('{:.2f}'.format(g), end = "")
    print("\t\tr=", end = "")
    if (i < period):
        print("nan%", end = "")
    else:
        r = relativeTemperatureEvolution(value, i , period)
        print(r, end = "%")
    print("\t\ts=", end = "")
    if (i + 1 < period):
        print("nan")
    else:
        s = standardDeviation(value, i, period)
        tabr.append(r)
        if (len(tabr) > 0 and temperatureSwitches(tabr[len(tabr) - 1], tabr[len(tabr) - 2]) == True):
            print('{:.2f}'.format(s), "\t\ta switch occurs")
            nbSwitches += 1
        else:
            print('{:.2f}'.format(s))
    return nbSwitches
