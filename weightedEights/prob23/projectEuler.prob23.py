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

Approach is this: Generate list of abundant numbers up to 28123/2. Generate new list of the combination of sums of the
abundant numbers. Sum the numbers from 0-28123 which are not on the abundant sum list. 

"""


def main():

    # loadprob("p022_names.txt")

    upper_limit = 48

    divisor_list = [{x: list_divisors(x)} for x in range(upper_limit + 1) if x % 2 == 0 and x != 0]

    abundants_list = [x for x in divisor_list if is_abundant(x)]

    display_result(upper_limit, divisor_list, abundants_list)


def loadprob(file):
    with open(file, 'r') as fin:
        name_list = [name.split(",") for name in fin]

    parsed_list = [name[1:-1] for name in name_list[0]]

    return parsed_list


def list_divisors(num):
    # divisors cannot be greater than the number / 2
    # it is only divisor if mod = 0
    div_list = [x for x in range(num / 2 + 1) if x != 0 and num % x == 0]

    return div_list


def is_abundant(div_dict):

    for k, v in div_dict.items():
        if sum(v) == k:
            return True
        else:
            return False


def display_result(upper_lim, div_list, result_list):

    print(upper_lim)
    print(div_list)
    print(result_list)


if __name__ == main():
    main()