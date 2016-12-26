"""
title: Rabbits and Recurrence Relations
description: ROSALIND, Bioinformatics Stronghold
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

    # Base case: one month, one rabbit
    if n == 1:
        return 1

    # Base case: two months, k rabbits
    elif n == 2:
        return k

    # fibonacci, f1 and f2 generations
    f1 = fib(n-1, k)
    f2 = fib(n-2, k)

    # Base case: less than four months, f1 + f2 rabbits
    if n <= 4:
        return f1 + f2

    # Return fibonacci f1 + (f2*k)
    return f1 + (f2 * k)


def main():
    """
    main
        Calculates number of waskly wabbits.

    :return: 0
    """

    # Open input and output files
    in_file = open('../../test/in/rosalind_fib.txt', 'r')
    out_file = open('../../test/out/rosalind_fib_solution.txt', 'w')

    # Read in data
    data = in_file.readline().split(' ')

    # Calculate total from fibonacci sequence
    total = fib(int(data[0]), int(data[1]))

    # Write to output file and standard out
    out_file.write(str(total))
    print(total)

    # Close input and output files
    in_file.close()
    out_file.close()

    return 0


if __name__ == '__main__':
    main()
