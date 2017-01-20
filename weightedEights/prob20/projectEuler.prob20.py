#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


"""

"""

Approach is this:

"""

import math

def main():

    loadprob()

    parseShit()

    displayResult()


def loadprob():
        # with open(file, 'r') as fin:
        #
        #     listVals = [map(int, num.split()) for num in fin]
        #
        # return listVals[::-1]

    pass

def parseShit():

    pass

def displayResult():

    numStr = str(math.factorial(100))

    numSum = [int(c) for c in numStr if c != "0"]

    print(sum(numSum))


if __name__ == main():
    main()
