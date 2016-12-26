"""
title: Transcribing DNA into RNA
description: ROSALIND, Bioinformatics Stronghold
author: Kelechi K. Fletcher
date: 12.25.2016
"""


def main():
    """
    main
        Transcribes DNA into RNA sequence

    :return: 0
    """

    in_file = open('../in/rosalind_rna.txt', 'r')
    out_file = open('../out/rosalind_rna_solution.txt', 'w')

    dna = in_file.readline()
    rna = dna.replace('T', 'U')

    out_file.write(rna)
    print(rna)

    in_file.close()
    out_file.close()


if __name__ == '__main__':
    main()
