"""
title: Mendel's First Law
description: ROSALIND, Bioinformatics Stronghold
author: Kelechi K. Fletcher
date: 12.28.2016
"""


def main():
    """
    Calculates total probability of producing phenotypically dominant offspring

    :return:
    """
    in_file = open('../../test/in/rosalind_iprb.txt', 'r')
    out_file = open('../../test/out/rosalind_iprb_solution.txt', 'w')

    data = in_file.readline().split(' ')
    k, m, n = int(data[0]), int(data[1]), int(data[2])
    population = k + m + n
    prob = 0.0

    prob += (k/population)*((k-1)/(population-1))           # k/k
    prob += (k/population)*(m/(population-1))               # k/m
    prob += (k/population)*(n/(population-1))               # k/n
    prob += (k/population)*(m/(population-1))               # m/k
    prob += (3/4)*((m/population)*((m-1)/(population-1)))   # m/m
    prob += (1/2)*((m/population)*(n/(population-1)))       # m/n
    prob += (k/population)*(n/(population-1))               # k/n
    prob += (1/2)*((m/population)*(n/(population-1)))       # m/n

    out_file.write(str(prob))
    print(prob)

    in_file.close()
    out_file.close()

    return 0


if __name__ == '__main__':
    main()