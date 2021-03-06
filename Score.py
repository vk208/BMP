__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'

# Finally, we can compute Score(Motifs) by first constructing Consensus(Motifs) and then summing
# the number of symbols in the j-th column of Motifs that do not match the symbol in position j
# of the consensus string. We leave this task to you as an exercise.


# Sample Input:

# AACGTA
# CCCGTT
# CACCTT
# GGATTA
# TTCCGG

# Sample Output:

# 14

from Consensus import consensus
from count import count

def Score(Motifs):

    count = 0
    L = consensus(Motifs)
    for i in Motifs:
        for chr1, chr2 in zip(i,L):
            if chr1 != chr2:
                count += 1

    return count