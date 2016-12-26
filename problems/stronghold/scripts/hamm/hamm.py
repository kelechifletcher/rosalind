"""
title: Counting Point Mutations
description: ROSALIND, Bioinformatis Stronghold
author: Kelechi K. Fletcher
date: 12.25.2016
"""


def main():
    """
    main
        Calculates hamming distance between two sequences.

    :return: 0
    """

    in_file = open('../../test/in/rosalind_hamm.txt', 'r')
    out_file = open('../../test/out/rosalind_hamm_solution.txt', 'w')

    seq1 = in_file.readline()
    seq2 = in_file.readline()
    dist = 0

    for i in range(0, len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1

    out_file.write(str(dist))
    print(dist)

    in_file.close()
    out_file.close()

    return 0


if __name__ == '__main__':
    main()
