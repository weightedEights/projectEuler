#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""


A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


"""

"""

Approach is this: Build list of abundant numbers less that 28123. The largest divisors can only be less than
sqrt(28123), so build that list and search for divi

"""


def main():

    # loadprob("p022_names.txt")

    upperLimit = 24

    parsedSum = listAbundants(upperLimit)

    displayResult(parsedSum, upperLimit)


def loadprob(file):
    with open(file, 'r') as fin:
        nameList = [name.split(",") for name in fin]

    parsedList = [name[1:-1] for name in nameList[0]]

    return parsedList


def isAbundant(num):

    return num


def listAbundants(upperLim):

    abundants = [x for x in xrange(1, upperLim +1) if isAbundant(x)]

    return abundants


def displayResult(sumDiv, upperLim):

    print(sumDiv, upperLim)


if __name__ == main():
    main()