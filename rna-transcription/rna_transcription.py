def to_rna(dna_strand):
    x = "GCTA"
    y = "CGAU"
    mytable = dna_strand.maketrans(x, y)
    return dna_strand.translate(mytable)
