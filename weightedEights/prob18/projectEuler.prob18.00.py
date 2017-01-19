#!/usr/bin/python

from __future__ import print_function

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

"""

"""

Approach is this: Start at the bottom and "compare/add" the smallest 3-element triangles. So, from the small example,
answer the question: compare 8 to 5, add greater to 2. compare 5 to 9, add greater to 4. compare 9 to 3, add.. etc.

Pyramid should "flatten" from the bottom up, with the largest sum emerging from the top.

"""


def main():

    pyraList = loadprob("p18.test.txt")

    displayResult(pyraList)


def loadprob(file):
        with open(file, 'r') as fin:
            listVals = [num.rstrip() for num in fin.readlines()]

        pyraVals = []

        return pyraVals


def displayResult(data):

    print(data)


if __name__ == main():
    main()

