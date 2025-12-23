with open("rna.fna", "r") as rna_file:
   # rna_lines = rna_file.read()
    rna_sequence = ""
    for line in rna_file:
        if not line.startswith(">"):# skips fasta header
            rna_sequence += line.strip() # adds sequence letters only

with open ("protein.faa", "r") as protein_file:
    protein_sequence = ""
    for line in protein_file:
        if not line.startswith(">"):# skips fasta header
            protein_sequence += line.strip() # adds sequence letters only
    # https://github.com/T101J/Translating_RNA_to_Protein
codon_table = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
           "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
           "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
           "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
           "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
           "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
           "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
           "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }

def translate_mrna(mrna_seq):
    protein = "" # empty string to store the protien
    mrna_seq =  mrna_seq.upper() # changes every input to uppercase
    for i in range(0, len(mrna_seq), 3):# looping through the M=mRNA 3 string at a time
        codon = mrna_seq[i:i+3]
        if len(codon) < 3: # if last codon isnt complete (up to 3 codons, Break)
            break
        amino_acid = codon_table.get(codon,'')
        if amino_acid == "STOP":
           break
        protein += amino_acid
    return protein


rna_mrna = rna_sequence
rna_result = translate_mrna(rna_mrna)
print("protein sequencefor rna:", rna_result)



protein_mrna = protein_sequence
protein_result = translate_mrna(protein_mrna)
print("protein sequencefor protein:", protein_result)
