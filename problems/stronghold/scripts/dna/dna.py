"""
title: Counting DNA Nucleotides
description: ROSALIND, Bioinformatics Stronghold
author: Kelechi K. Fletcher
date: 12.25.2016
"""


def main():
    """
    main
        Calculates number of nucleotides and generates report.

    :return: 0
    """

    # Open input and output files
    in_file = open('../../test/in/rosalind_dna.txt', 'r')
    out_file = open('../../test/out/rosalind_dna_solution.txt', 'w')

    # Read in DNA sequence
    dna = in_file.readline()
    a, c, g, t = 0, 0, 0, 0

    # Count nucleotides
    for base in dna:
        if base == 'A':
            a += 1
        elif base == 'C':
            c += 1
        elif base == 'G':
            g += 1
        elif base == 'T':
            t += 1

    # Write to output file and standard out
    out_file.write('%i %i %i %i' % (a, c, g, t))
    print('%i %i %i %i' % (a, c, g, t))

    # Close input and output files
    in_file.close()
    out_file.close()

    return 0


if __name__ == '__main__':
    main()
