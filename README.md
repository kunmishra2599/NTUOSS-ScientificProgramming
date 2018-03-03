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
Now this is cool. This string is a **nucleotide sequence**, or more specifically, an **mRNA sequence**. mRNA stands for messenger Ribonucleic Acid (yes, it's a mouthful to say sometimes). 
