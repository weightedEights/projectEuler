#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to
obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?


"""

"""

Approach is this:

"""


def main():

    nameList = loadprob("p022_names.txt")

    parsedList = parseShit(nameList)

    displayResult(parsedList)


def loadprob(file):
    with open(file, 'r') as fin:
        nameList = [name.split(",") for name in fin]

    parsedList = [name[1:-1] for name in nameList[0]]

    return parsedList


def parseShit(nameList):

    alphaList = [name for name in sorted(nameList)]

    nameSum = 0

    for i, name in enumerate(alphaList):
        nameSum += (i+1) * len(name)
        print(i, name, (i+1) * len(name), nameSum)

    return nameSum

def displayResult(data):

    print(data)


if __name__ == main():
    main()