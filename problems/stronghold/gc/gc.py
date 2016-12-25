from pyfasta import Fasta


def gc_content(seq):
    return ((str(seq).lower().count('c') + str(seq).lower().count('g')) / len(seq))*100


def main():
    seq_dict = Fasta('../in/rosalind_gc.txt')
    outFile = open('../out/rosalind_gc_solution.txt','w')
    max_id = ''
    max_gc = 0.0

    for id in sorted(seq_dict.keys()):
        gc = gc_content(seq_dict[id])
        if gc > max_gc:
            max_id = id
            max_gc = gc

    outFile.write('%s\n%f\n' % (max_id, max_gc))


if __name__ == '__main__':
    main()