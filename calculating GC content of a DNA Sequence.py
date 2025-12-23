dna_sequence = "AATGCTCGAGGTGCCTTGGTAA"
mrna_sequence = "AUG CCA GUG ACU UCA GGG ACG AAU GAC UUA"
G=0
C=0
A=0
T=0

for base in dna_sequence:
    if base == 'A':
        A+=1
    elif base == 'T':
        T+=1
    elif base == 'G':
        G+=1
    elif base == 'C':
        C+=1
        
def calculate_gc_content(dna_seq):
   A = dna_seq.count('A')
   T = dna_seq.count('T')
   G = dna_seq.count('G')
   C = dna_seq.count('C')
    
    
   gc_content = ((G+C) / (A +T+G+C)) * 100
   return gc_content
    

gc_percentage = calculate_gc_content(dna_sequence)
gc_percentage_mrna = calculate_gc_content(mrna_sequence)
print("GC percentage: ", gc_percentage)
print("GC percentage: ", gc_percentage_mrna)