import sys


def main():
    dna = sys.stdin.readline()
    r_dna = dna[::-1]
    com = str()

    for base in r_dna:
        if base == 'A':
            com += 'T'

        elif base == 'C':
            com += 'G'

        elif base == 'G':
            com += 'C'

        elif base == 'T':
            com += 'A'

    print(com)

    out = open('.\out\solution.txt', 'w+')
    out.write(com)

if __name__ == '__main__':
    main()
