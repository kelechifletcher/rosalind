"""
title: Computing GC Content
description: ROSALIND, Bioinformatics Stronghold
author: Kelechi K. Fletcher
data: 12.25.2016
"""


from pyfasta import Fasta


def gc_content(seq):
    """
    gc_content
        Calculates gc content of dna sequence.

    :param seq: dna sequence
    :return: (number of 'c' + number of 'g') / length of seq
    """
    return ((str(seq).count('C') + str(seq).count('G')) / len(seq))*100


def main():
    """
    main
        Identifies dna sequence with highest gc content.

    :return:
    """

    seq_dict = Fasta('../test/in/rosalind_gc.txt')
    out_file = open('../test/out/rosalind_gc_solution.txt', 'w')
    max_id = ''
    max_gc = 0.0

    for id in sorted(seq_dict.keys()):
        gc = gc_content(seq_dict[id])
        if gc > max_gc:
            max_id = id
            max_gc = gc

    out_file.write('%s\n%f\n' % (max_id, max_gc))
    print('%s\n%f\n' % (max_id, max_gc))

    out_file.close()

    return 0


if __name__ == '__main__':
    main()