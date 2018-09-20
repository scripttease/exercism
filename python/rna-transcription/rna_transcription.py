def to_rna(dna_strand):
    DNAtoRNA = {'C': 'G', 'A': 'U', 'T': 'A', 'G': 'C'}
    rna = list(map(lambda x: DNAtoRNA[x], dna_strand))
    return "".join(rna)
