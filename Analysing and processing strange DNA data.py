import matplotlib.pyplot as plt
import re
from collections import Counter
#############################################
#function to read sequence from  a FASTA file
#############################################
def read_fasta(filepath):
    '''
    'it reads a FASTA file and returns the sequence as a single string.
    headears that starts with (>) are ignored'
    '''
    sequence = ""
    with open(filepath, "r") as file:
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence


###################
# Read sequences
###################
dna_sequence = read_fasta("gene_a.fa")
rna_sequence = read_fasta("rna_a.fa")
protein_sequence = read_fasta("protein_a.fa")
gene_b_dna_sequence = read_fasta("gene_b.fa")


########################################
# Task 1 — Nucleotide count / visualization
########################################


#### cleaning DNA sequence#####
'''
removes ambigous nucleotide 'N' from DNA and RNA for analysis
'''
clean_dna =  dna_sequence.replace("N", "")
clean_b_dna = gene_b_dna_sequence.replace("N", "")
clear_rna = rna_sequence.replace("N", "")
# prints cleaned DNA sequence lengths
print("Cleaned DNA length:", len(clean_dna))
print("Cleaned RNA length:", len(clear_rna),'\n')


###### counting nucleotides frequencies########
dna_counts = Counter(dna_sequence)
rna_counts = Counter(rna_sequence)
gene_b_dna_sequence_count = Counter(gene_b_dna_sequence)

#prints nucleotide counts
print("DNA Nucleotide Count: ", dna_counts)
print("Rna nucleotide Count: ", rna_counts)
print("Gene b DNA nucleotide Count: ", gene_b_dna_sequence_count,"\n")


# Check whether cleaned DNA and RNA sequences align in length
if len(clean_dna) != len(rna_sequence):
    print("WARNING: DNA and RNA still do not match in length!")
else:
    print("Lengths match. Proceeding with transcription key discovery.\n")




# Visualization
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
#DNA nucleotide distribution
axes[0].bar(dna_counts.keys(), dna_counts.values(), color='blue')
axes[0].set_title("DNA Nucleotide Distribution")
axes[0].set_xlabel("Nucleotides")
axes[0].set_ylabel("Count")

#RNA nucleotide distribution
axes[1].bar(rna_counts.keys(), rna_counts.values(), color='green')
axes[1].set_title("RNA Nucleotide Distribution")
axes[1].set_xlabel("Nucleotides")
axes[1].set_ylabel("Count")

plt.tight_layout()


########################################
# Task 2 — Discover Transcription Key
########################################
pair_counts = Counter() # counts the frequency of each DNA pair
mapping = {}            # maps each DNA base to possible RNA bases
# Using the cleaned DNA for transcription rule discovery
for d, r in zip(clean_dna, rna_sequence):
# zip(clean_dna, rna_sequence) pairs the 1st DNA letter with the 1st RNA letter, 2nd with 2nd, etc.
    pair_counts[(d, r)] += 1 # count this specific DNA - RNA pair
    if d not in mapping: 
        mapping[d] = set()  #if this DNA letter has not been seen yet, creates an empty set for it
    mapping[d].add(r)       #Add RNA letter to set of possible mappings for the DNA letter


########################################
# Print the transcription key
########################################
print("\n=== DNA → RNA Transcription Key ===")
for dna_base in sorted(mapping.keys()):
    rna_outputs = ", ".join(sorted(mapping[dna_base]))
    print(f"{dna_base} → {rna_outputs}")

print("\n=== Pair Frequency Table ===")
for (d, r), count in pair_counts.most_common():
   print(f"{d} → {r}: {count}\n")


########################################
#Task 3 - Determine codon lenght
########################################
# Step 1: Split protein into residues (each element symbol)
protein_residues = re.findall(r'[A-Z][a-z]?', protein_sequence)
num_residues = len(protein_residues)
mRNA = rna_sequence
# Step 2: RNA length
rna_length = len(mRNA)

# Step 3: Compute codon length
codon_length = rna_length / num_residues

print("Number of protein residues:", num_residues)
print("Length of mRNA sequence:", rna_length)
print("Computed codon length:", codon_length)

########################################
#Task 4 - Create a look up table
########################################

# Step 1: spliting RNA into codons of discovered length (2)
#with each codon represnting one amino acid
codons = [mRNA[i:i+2] for i in range(0, len(mRNA), 2)]

# Ensuring codon list and protein residues have same length
min_len = min(len(codons), len(protein_residues))
codons = codons[:min_len]
protein_residues = protein_residues[:min_len]

# Step 2: Creating mapping dictionary
codon_table = {} # stores mapping of codon - amino acid
conflicts = {}   # receods any codons that map to multiple amino acids

#populating codon table and pairing each codon with corresponding protein residue
for codon, residue in zip(codons, protein_residues):
    
    # if codon has not been seen before, add it to the table
    if codon not in codon_table:
        codon_table[codon] = residue
    else:
        #if the same codon maps to a different residue, record a conflict
        if codon_table[codon] != residue:
            # record conflicts for reporting
            if codon not in conflicts:
                conflicts[codon] = {codon_table[codon]}
                #add the confliciting residue to the set
            conflicts[codon].add(residue)
########################################
# Task 4 Output
########################################

print("\n=== CODON → RESIDUE LOOKUP TABLE ===")
for c in sorted(codon_table.keys()):
    print(f"{c} → {codon_table[c]}")

if conflicts:
    print("\n⚠ WARNING: Some codons mapped to multiple residues:")
    for codon, options in conflicts.items():
        print(f"{codon}: {', '.join(options)}")
else:
    print("\nNo conflicts detected. Mapping is clean\.n")
    
########################################
# Task 5 Dna to mRNA sequence
########################################
# converting the dicovered mapping (sets) into a single output DNA base
transcription_key = {base: list(outputs)[0] for base, outputs in mapping.items()}
print("transcription key used for Gene b")
for base in sorted(transcription_key.keys()):
    print(f"{base} - {transcription_key[base]}")

#transcription fuction using my discovered transcription key
def transcribe_custom(dna_seq, transcription_key):
    return "".join(transcription_key[base] for base in dna_seq)
    
#outut mRNA for gene_b
b_mrna_sequence = transcribe_custom(clean_b_dna, transcription_key)

print("\nGenerated mRNA for gene_b", "and the lenght is: ",len(b_mrna_sequence))
print(b_mrna_sequence)
    


########################################
# Task 5.2 gene_b mRNA to protein
########################################
#spliting into my discovered codon lenght (2)
b_codons = [b_mrna_sequence[i:i+2] for i in range(0,len(b_mrna_sequence),2)]

# Remove any incomplete codon at the end (defensive programming)
b_codons = [c for c in b_codons if len(c) == 2]

#translating codon into protein sequence
b_protein = "".join(codon_table[codon] for codon in b_codons)
print("\nprotein sequence for gene_b:")
print(b_protein)

