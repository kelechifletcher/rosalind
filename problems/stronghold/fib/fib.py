"""
title: Rabbits and Recurrence Relations (ROSALIND: Bioinformatics Stronghold)
author: Kelechi K. Fletcher
date: 12.25.2016
"""


def fib(n, k):
    """
    fib
        Calculates resulting number of rabbits from pairs that
        produce k rabbits per month after n months.

    :param n: number of months
    :param k: number of rabbits produced by each pair
    :return: total number of rabbits
    """

    if n == 1:
        return 1

    elif n == 2:
        return k

    f1 = fib(n-1, k)
    f2 = fib(n-2, k)

    if n <= 4:
        return f1 + f2

    return f1 + (f2 * k)


def main():
    """
    main
        Calculates number of waskly wabbits.

    :return: 0
    """

    inFile = open('../in/rosalind_fib.txt', 'r')
    outFile = open('../out/rosalind_fib_solution.txt', 'w')

    data = inFile.readline().split(' ')

    total = fib(int(data[0]), int(data[1]))

    outFile.write(str(total))
    print(total)

    return 0

if __name__ == '__main__':
    main()