#!/usr/bin/python

from __future__ import print_function

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt , a 15K text file containing a triangle with one-hundred rows.

"""

"""

Approach is this: Start at the bottom and "compare/add" the smallest 3-element triangles. So, from the small example,
answer the question: compare 8 to 5, add greater to 2. compare 5 to 9, add greater to 4. compare 9 to 3, add.. etc.

Pyramid should "flatten" from the bottom up, with the largest sum emerging from the top.

"""


def main():

    pyraList = loadprob("p067_triangle.txt")

    topSum = compAdd(pyraList)

    displayResult(topSum)


def loadprob(file):
        with open(file, 'r') as fin:

            listVals = [map(int, num.split()) for num in fin]

        return listVals[::-1]


def compAdd(array):

    for i, row in enumerate(array):
        for j, val in enumerate(row[:-1]):
            array[i+1][j] += max((row[j], row[j+1]))

    return array


def displayResult(data):

    print(data[-1])


if __name__ == main():
    main()

