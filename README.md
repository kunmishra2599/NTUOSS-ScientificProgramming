# NTUOSS-ScientificProgramming
Workshop for NTUOSS AY2017-2018



## Section 1 - Working with Matplotlib - Charts, Axes and Nucleotide Sequences

### Step 1 - Importing libraries and setting up the sequence
To start off, we need to import a few libaries for our use. Create a python file called `sequence.py`. Add the following lines to the top of your code:

```
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np
```
Alot of these libraries will become relevant quite soon. The first import is for `pyplot`, which helps, you know, plot data. There are many different types of graphs you can plot, and you can check out a full list of them [here](https://matplotlib.org/tutorials/index.html).
The second `ticker` import will help us format the x and y axes on the graphs we're about to generate. The last imports the module `numpy`, which we'll get into soon. 

Following this, add the following line of code to your file:
```
sequence="acauuugcuucugacacaacuguguucacuagcaaccucaaacagacaccauggugcaucugacuccugaggagaagucugccguuacugcccuguggggcaaggugaacguggaugaaguugguggugaggcccugggcaggcugcugguggucuacccuuggacccagagguucuuugaguccuuuggggaucuguccacuccugaugcuguuaugggcaacccuaaggugaaggcucauggcaagaaagugcucggugccuuuagugauggccuggcucaccuggacaaccucaagggcaccuuugccacacugagugagcugcacugugacaagcugcacguggauccugagaacuucaggcuccugggcaacgugcuggucugugugcuggcccaucacuuuggcaaagaauucaccccaccagugcaggcugccuaucagaaagugguggcugguguggcuaaugcccuggcccacaaguaucacuaagcucgcuuucuugcuguccaauuucuauuaaagguuccuuuguucccuaaguccaacuacuaaacugggggauauuaugaagggccuugagcaucuggauucugccuaauaaaaaacauuuauuuucauugc"
```
### Step 2 - Learning a bit of Molecular Biology
Now this is cool. This string is a **nucleotide sequence**, or more specifically, an **mRNA sequence**. mRNA stands for messenger Ribonucleic Acid (yes, it's a mouthful to say sometimes).

Running `print(len(sequence))` tells us that there are 626 base pairs in this sequence.

Before we proceed any further, let's address some basics. 

The image below illustrates the **Central Dogma of Molecular Biology**.
![Central Dogma](images/centraldogma.png)

mRNA is made of four bases: Adenine, Uracil, Guanine, Cytosine.
mRNA sequence analysis reveals alot about the proteins that can be formed, and can be aided using tools such as [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi). Here, we're going to do a very simplistic analysis of nucleotide sequences using fragments and histograms, and hopefully learn a bit about `Matplotlib` and `Modern Scientific Techniques`. 

This particular mRNA sequence codes for the β subunit of Haemoglobin in Humans. Haemoglobin is a transport protein that helps bring oxygen around the body.

Now, generally, such sequences are unknown, and scientists probe the sequence using chemical and biological reagents to analyse the fragments generated and the size of the fragments. One such method is **Gel Electrophoresis**, an example of which is shown below:

![Gel Electrophoresis](images/gelelectrophoresis.png)

### Step 3 - Doing a base pair analysis

To seperate the strand into fragments, we're going to mimic the activity of **RNAse T1**, a common endoribonuclease that quite literally, splices nucleotide sequences into fragments after Guanine Residues. Before we do that, lets visualise the base pair composition of the sequence. Add the following lines of code to your file:
```
def bp_analysis(seq):

    counter = [0,0,0,0]
  
    for x in seq:
        if x == 'a':
            counter[0] += 1
        elif x == 'u':
            counter[1] += 1
        elif x == 'g':
            counter[2] += 1
        else:
            counter[3] += 1

    x_ax = np.arange(4)
  
    plt.bar(x_ax, counter)
    plt.xticks(x_ax, ('Adenine', 'Uracil', 'Guanine', 'Cytosine'))
    
    plt.xlabel('Nitrogenous Bases')
    plt.ylabel('Frequency')
    plt.title('Base Pair Composition')
    
    plt.grid(True)
    plt.show()
```
Ah, this piece of code serves as the first foray into `Matplotlib`.The first part of the code increases a `counter` everytime a particular base is encountered, giving us the following list: `[137, 167, 165, 157]`, in the following order: A, U, G, C. 
The line `x_ax` helps create a numpy array for each of our nitrogenous bases. 

The next line, `plt.bar(x_ax, counter)` calls the `bar()` function unto our data set, and the following line helps us define the labels for each of the bases. 
`Matplotlib` allows us quite a bit of formatting and modification options. The three lines demonstrate the simplicity of adding axis labels and a title to the graph. And finally, the last two lines help us to visualise the graph. Calling `bp_analysis(sequence)` generates the following graph. 

![1.3](images/1.3.png)

Yay! We've achieved liftoff. We can see roughly the composition of the four bases relative to each other. However, analytically speaking this doesn't give us much. The sequence shows that there's alot of Guanine residues present, but nothing whatsoever about the position of the residues. It could very well be `ggggggggggggggggggggggggggg`, `ggggggguuuuggguguguguguguug` or `aggagagagauuugag`.

We need to take this one step further and _cleave_ the mRNA sequence using our artificial RNAse T1. 

### Step 4 - Cleaving the sequence and analysing the fragments

Add the following lines of code to your file.
```
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
```
These lines are quite similar to the previous function `bp_analysis`. Running `len(t1_digested)` tells us that there are a total of 166 digested fragments. Dividing the fragments by size, we can generate a histogram using `plt.hist`. The object of focus here, however is in these few lines:
```
    minorLocator = MultipleLocator(2)
    majorLocator = MultipleLocator(2)
    majorFormatter = FormatStrFormatter('%d')

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_major_formatter(majorFormatter)

    ax.xaxis.set_minor_locator(minorLocator)
```
These let us format the major and minor 'ticks' on the graph generated. The `Locator` function defines how often a tick is placed, and in this case, it's every 2 units. The line `ax = plt.subplot(111)` creates a subplot, giving us access to more advanced formatting options in `Matplotlib`. The next few lines define the axis with the desired formatting options. 

Running `t1_digestion(sequence)` gives us the following graph:

![1.4](images/1.4.png)

This graph gives us a bit more information about the distribution of Guanine residues along the sequence. Most fragments are between 1-6 base pairs long, and most likely this means that guanine residues are distributed roughly quite evenly throughout the sequence. Now that we know some more information about this sequence, let's try visually comparing it against a sequence that codes for another protein: Myglobin.

### Step 5 - Unknown Protein Comparison

Add the following sequence to your file:
```
myoglobin="aaaccccagcuguuggggccaggacacccagugagcccauacuugcucuuuuugucuucuucagacugcgccauggggcucagcgacggggaauggcaguuggugcugaacgucugggggaaguccucaucaggcucuuuaagggucacccagagacucuggagaaguuugacaaguucaagcaccugaagucagaggacgagaugaaggcaucugaggacuuaaagaagcauggugccacugugcucaccgcccuggguggcauccuuaagaagaaggggcaucaugaggcagagauuaagccccuggcacagucgcaugccaccaagcacaagauccccgugaaguaccuggaguucaucucggaaugcaucauccagguucugcagagcaagcaucccggggacuuuggugcugaugcccagggggccaugaacaaggcccuggagcuguuccggaaggacauggccuccaacuacaaggagcugggcuuccagggcuaggccccugccgcucccacccccacccaucugggccccggguucaagagagagcggggucugaucucguguagccauauagaguuugcuucugagugucugcuuuguuuaguagaggugggcaggaggagcugaggggcuggggcugggguguugaaguuggcuuugcaugcccagcgaugcgccucccugugggaugucaucacccugggaaccgggaguggcccuuggcucacuguguucugcaugguuuggaucugaauuaauuguccuuucuucuaaaucccaaccgaacuucuuccaaccuccaaacuggcuguaaccccaaauccaagccauuaacuacaccugacaguagcaauugucugauuaaucacuggccccuugaagacagcagaaugucccuuugcaaugaggaggagaucugggcugggcgggccagcuggggaagcauuugacuaucuggaacuugugugugccuccucaggt"
```
Through this exercise, we'll hopefully learn more about Myoglobin. ~~Well, I know about myoglobin, but this should help you guys learn more about it haha.~~ 
This sequence is 989 base pairs long. We'll skip on the base pair analysis and directly compare it against the known fragments from the Haemoglobin sequence.

Add this function to your code.
```
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
```
This code isn't quite hard to make sense of actually. It performs the same operation on both the sequences and then plots them. Calling `h_comparison(sequence, myoglobin)` gives the following plot:

![1.5](images/1.5.png)

On analysing the graph, you can see that though the fragment frequencies are larger in Myoglobin(owing to the larger sequence length), the cleavage pattern is similar to Haemoglobin, and this tell us that the two proteins are quite similar in shape, and as it follows in molecular biology, function as well. In fact, both Haemoglobin and Myoglobin are oxygen transporters / storers. Myoglobin stores oxygen in muscles and has a very high affinity for Oxygen. The two proteins(I call them **H&M**) look like this:

![handm](images/handm.png)

Interesting? [Here](http://www.sbs.ntu.edu.sg/prospective/undergraduate/MinorinLifeSciences/Pages/Home.aspx)'s a link outlining the Life Sciences Minor at NTU haha.


