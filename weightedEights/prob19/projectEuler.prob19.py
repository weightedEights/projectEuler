#!/usr/bin/python

from __future__ import print_function

"""

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

"""

Approach is this: Using the built-in "calendar" module, count Sundays if and only if they fall on the 1st. The calendar
module will handle leap days, etc. Note, weekday indices are: 0 is Monday, 6 is Sunday

"""

import calendar

def main():

    loadprob()

    sunCount = parseShit()

    displayResult(sunCount)


def loadprob():
        # with open(file, 'r') as fin:
        #
        #     listVals = [map(int, num.split()) for num in fin]
        #
        # return listVals[::-1]

    pass

def parseShit():

    sunCount = 0

    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            if calendar.monthrange(year, month)[0] == 6:
                sunCount += 1

    return sunCount

def displayResult(data):

    print(data)


if __name__ == main():
    main()
