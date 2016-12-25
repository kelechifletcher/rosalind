import sys


def main():
    dna = sys.stdin.readline()
    rna = dna.replace('T', 'U')

    print(rna)

if __name__ == '__main__':
    main()