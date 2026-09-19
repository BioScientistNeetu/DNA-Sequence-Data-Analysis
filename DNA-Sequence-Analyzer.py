print("=== DNA SEQUENCE ANALYZER ===")
dna = input("Enter DNA sequence:").upper()

valid_bases = "ATGC"
if all(base in valid_bases for base in dna):
    print("valid DNA sequence")
    print("DNA Length:", len(dna))
else:
    print("invalid DNA sequence")

from collections import Counter
length = len(dna)
count = Counter(dna)
print(count)
print("A:", count["A"])
print("T:", count["T"])
print("G:", count["G"])
print("C:", count["C"])

gc_content = (count["G"]+ count["C"])/ length * 100
print("GC Countent:", gc_content)
at_content = (count["A"] + count["T"])/length * 100
print("AT Countent:",at_content)

complementary = ""
complement_map = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

for base in dna:
    if base in complement_map:
        complementary += complement_map[base]

print("Complementary DNA:", complementary)

reverse_dna = dna[::-1]
print("Reverse DNA:", reverse_dna)

reverse_complement = complementary[::-1]
print("Reverse Complement:",reverse_complement)

transcription_rule = {'A': 'U', 'T':'A', 'C':'G', 'G':'C'}
mrna_seq =""


for base in dna:
    mrna_seq += transcription_rule[base]
    
print("mRNA Sequence:",mrna_seq)


codons = []

for i in range(0, len(mrna_seq), 3):
    codon = mrna_seq[i:i+3]
    codons.append(codon)

print("codons list:", codons)

codon_table = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "CCU": "Proline",
    "CCC": "Proline",
    "CCA": "Proline",
    "CCG": "Proline",
    
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Isoleucine",
    "ACU": "Threonine",
    "ACC": "Threonine",
    "ACA": "Threonine",
    "ACG": "Threonine",
    
    "GUU": "Valine",
    "GUC": "Valine",
    "GUA": "Valine",
    "GUG": "Valine",
    "GCA": "Alanine"
}

protein = ""

for codon in codons:
    if codon in codon_table:
        protein += codon_table[codon]

print("protein:", protein)

print("codons:")

for i, codon in enumerate(codons,start=1):
    print(i, codon)

stop_codons = ["UAA","UAG","UGA"]

for codon in codons:
    if codon in stop_codons:
        print(codon, "is a STOP codon")

invalid_base =[]

for base in dna:
    if base not in valid_bases:
        invalid_base.append(base)

if invalid_base:
    print("invalid bases:", invalid_base)
else:
    print("DNA sequence is valid")

print("\n===== FINAL DNA ANALYSIS=====")

print("DNA sequence:", dna)
print("DNA length:", length)
print("A Count:", count["A"])
print("T Count:", count["T"])
print("G Count:", count["G"])
print("C Count:", count["C"])
print("GC Content:", gc_content)
print("AT Content:", at_content)
print("complementary DNA:", complementary)
print("reverse DNA:", reverse_dna)
print("reverse complement:", reverse_complement)
print("mRNA Sequence:", mrna_seq)
print("codona:", codons)
print("Protein:", protein)