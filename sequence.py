# This is the RNA sequence that codes for the Beta subunit of Haemoglobin in Humans.
# This sequence is transcribed into an mRNA transcript, which is then translated into a subunit to form the beta subunit

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np


sequence="acauuugcuucugacacaacuguguucacuagcaaccucaaacagacaccauggugcaucugacuccugaggagaagucugccguuacugcccuguggggcaaggugaacguggaugaaguugguggugaggcccugggcaggcugcugguggucuacccuuggacccagagguucuuugaguccuuuggggaucuguccacuccugaugcuguuaugggcaacccuaaggugaaggcucauggcaagaaagugcucggugccuuuagugauggccuggcucaccuggacaaccucaagggcaccuuugccacacugagugagcugcacugugacaagcugcacguggauccugagaacuucaggcuccugggcaacgugcuggucugugugcuggcccaucacuuuggcaaagaauucaccccaccagugcaggcugccuaucagaaagugguggcugguguggcuaaugcccuggcccacaaguaucacuaagcucgcuuucuugcuguccaauuucuauuaaagguuccuuuguucccuaaguccaacuacuaaacugggggauauuaugaagggccuugagcaucuggauucugccuaauaaaaaacauuuauuuucauugc"

myoglobin="aaaccccagcuguuggggccaggacacccagugagcccauacuugcucuuuuugucuucuucagacugcgccauggggcucagcgacggggaauggcaguuggugcugaacgucugggggaaguccucaucaggcucuuuaagggucacccagagacucuggagaaguuugacaaguucaagcaccugaagucagaggacgagaugaaggcaucugaggacuuaaagaagcauggugccacugugcucaccgcccuggguggcauccuuaagaagaaggggcaucaugaggcagagauuaagccccuggcacagucgcaugccaccaagcacaagauccccgugaaguaccuggaguucaucucggaaugcaucauccagguucugcagagcaagcaucccggggacuuuggugcugaugcccagggggccaugaacaaggcccuggagcuguuccggaaggacauggccuccaacuacaaggagcugggcuuccagggcuaggccccugccgcucccacccccacccaucugggccccggguucaagagagagcggggucugaucucguguagccauauagaguuugcuucugagugucugcuuuguuuaguagaggugggcaggaggagcugaggggcuggggcugggguguugaaguuggcuuugcaugcccagcgaugcgccucccugugggaugucaucacccugggaaccgggaguggcccuuggcucacuguguucugcaugguuuggaucugaauuaauuguccuuucuucuaaaucccaaccgaacuucuuccaaccuccaaacuggcuguaaccccaaauccaagccauuaacuacaccugacaguagcaauugucugauuaaucacuggccccuugaagacagcagaaugucccuuugcaaugaggaggagaucugggcugggcgggccagcuggggaagcauuugacuaucuggaacuugugugugccuccucaggt"

#print('Number of Base Pairs: '+str(len(sequence)))


# Digestion by RNAse T1 - cleaves after Guanine Residues

def bp_analysis(seq):

    counter = [0,0,0,0]
    x_ax = np.arange(4)

    for x in seq:
        if x == 'a':
            counter[0] += 1
        elif x == 'u':
            counter[1] += 1
        elif x == 'g':
            counter[2] += 1
        else:
            counter[3] += 1

    plt.bar(x_ax, counter)
    plt.xticks(x_ax, ('Adenine', 'Uracil', 'Guanine', 'Cytosine'))
    plt.xlabel('Nitrogenous Bases')
    plt.ylabel('Frequency')
    plt.title('Base Pair Composition')
    plt.grid(True)
    plt.show()

def t1_digestion(seq):
    t1_pre_digested = seq.split('g')
    t1_digested = []
    for x in t1_pre_digested:
        if x == '':
            x = 'g'
            t1_digested.append(x)
        else:
            t1_digested.append(x)

    print('Digested fragments: '+ str(t1_digested))
    print('Number of Fragments: '+str(len(t1_digested)))

    plotme = []

    #getting fragment sizes
    for x in t1_digested:
        plotme.append(len(x))

    #plotting and formatting graph
    plt.xlabel('Fragment Sizes (no of b.p)')
    plt.ylabel('Frequency')
    plt.title('Fragments generated on digestion with T1 RNAse')

    minorLocator = MultipleLocator(2)
    majorLocator = MultipleLocator(2)
    majorFormatter = FormatStrFormatter('%d')

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_major_formatter(majorFormatter)

    ax.xaxis.set_minor_locator(minorLocator)
    plt.grid(True)
    plt.hist(plotme)
    plt.show()

    # plot shows that most fragments are between 1-8 base pairs long. This shows that there is a frequent occurence of Guanine residues in the sequence.

def h_comparison(seq1, seq2):
    t1_pre_digested1 = seq1.split('g')
    t1_digested1 = []
    for x in t1_pre_digested1:
        if x == '':
            x = 'g'
            t1_digested1.append(x)
        else:
            t1_digested1.append(x)

    plotme1 = []

    for x in t1_digested1:
        plotme1.append(len(x))

    t1_pre_digested2 = seq2.split('g')
    t1_digested2 = []
    for x in t1_pre_digested2:
        if x == '':
            x = 'g'
            t1_digested2.append(x)
        else:
            t1_digested2.append(x)


    plotme2 = []


    for x in t1_digested2:
        plotme2.append(len(x))

    #plotting and formatting graph
    plt.xlabel('Fragment Sizes (no of b.p)')
    plt.ylabel('Frequency')
    plt.title('Fragment Comparison with Haemoglobin')

    minorLocator = MultipleLocator(2)
    majorLocator = MultipleLocator(2)
    majorFormatter = FormatStrFormatter('%d')

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_major_formatter(majorFormatter)

    ax.xaxis.set_minor_locator(minorLocator)
    plt.grid(True)
    plt.hist(plotme1, alpha=0.5, label='Haemoglobin')
    plt.hist(plotme2, alpha=0.5, label='Myoglobin')
    plt.legend(loc='upper right')

    plt.show()

h_comparison(sequence, myoglobin)
