"""
title: Complementing a Strand of DNA
description: ROSALIND, Bioinformatics Stronghold
author: Kelechi K. Fletcher
date: 12.25.2016
"""


def main():
    """
    main
        Calculates the reverse complement strand of given dna sequence

    :return: 0
    """

    in_file = open('../../test/in/rosalind_revc.txt', 'r')
    out_file = open('../../test/out/rosalind_revc_solution.txt', 'w')

    dna = in_file.readline()
    complement = str()

    for base in dna[::-1]:
        if base == 'A':
            complement += 'T'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'
        elif base == 'T':
            complement += 'A'

    out_file.write(complement)
    print(complement)

    in_file.close()
    out_file.close()

    return 0


if __name__ == '__main__':
    main()
