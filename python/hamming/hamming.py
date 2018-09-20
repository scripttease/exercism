def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("{strand_a}! is not the same length as {strand_b}!")
    else:
        lc = [i == j for i, j in zip(strand_a, strand_b)]
        return lc.count(False)
# note I could just use i != j and sum the resulting list because True sums to 1 but that is not as clear I think.
