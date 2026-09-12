def to_rna(dna_strand):
    rna = ""
    for item in dna_strand:
        if item == "G":
            rna += "C"
        elif item == "C":
            rna += "G"
        elif item == "T":
            rna += "A"
        elif item == "A":
            rna += "U"
        elif item == "":
            rna += ""
    return rna

