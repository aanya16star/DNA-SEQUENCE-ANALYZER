#DNA Sequence Analyzer
#----------------------
#This is a beginner-friendly Python project that analyzes a DNA sequence.

CODON_TABLE = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
}

COMPLEMENT = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

def is_valid_dna(sequence):
    for base in sequence:
        if base not in 'ATGC':
            return False
        return True
def count_nucleotides(sequence):
    return {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C'),
    }

def gc_content(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    total = g + c
    if total == 0:
        return 0.0
    return round((g + c) / total * 100, 2)

def complementary_strand(sequence):
    return ''.join(COMPLEMENT[base] for base in sequence)

def reverse_complement(sequence):
    return complementary_strand(sequence)[::-1]

def transcribe_to_mrna(sequence):
    return sequence.replace('T', 'U')

def translate_to_protein(mrna_sequence):
    protein = []
    for i in range(0, len(mrna_sequence) - 2, 3):
        codon = mrna_sequence[i:i + 3]
        amino_acid = CODON_TABLE.get(codon, '???')
        if amino_acid == 'Stop':
            break
        protein.append(amino_acid)
    return '-'.join(protein)

def search_pattern(sequence, pattern):
    positions = []
    pattern_len = len(pattern)
    for i in range(len(sequence) - pattern_len + 1):
        if sequence[i:i + pattern_len] == pattern:
            positions.append(i)
    return positions

def display_menu():
    print("\n===== DNA SEQUENCE ANALYZER =====")
    print("1. Enter/Load DNA sequence")
    print("2. Show nucleotide count")
    print("3. Show GC content")
    print("4. Show complementary strand")
    print("5. Show reverse complement strand")
    print("6. Transcribe to mRNA")
    print("7. Translate to Protein")
    print("8. Search for a pattern")
    print("9. Exit")

def main():
    sequence = ""

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            seq_input = input("Enter DNA sequence (A, T, G, C only): ").strip().upper()
            if is_valid_dna(seq_input) and len(seq_input) > 0:
                sequence = seq_input
                print(f"Sequence loaded successfully! Length: {len(sequence)} bases")
            else:
                print("Invalid sequence! Only A, T, G, C characters are allowed.")

        elif choice == '2':
            if sequence:
                counts = count_nucleotides(sequence)
                print(f"Nucleotide Counts: {counts}")
            else:
                print("Please load a sequence first (option 1).")

        elif choice == '3':
            if sequence:
                print(f"GC Content: {gc_content(sequence)}%")
            else:
                print("Please load a sequence first (option 1).")

        elif choice == '4':
            if sequence:
                print(f"Complementary Strand: {complementary_strand(sequence)}")
            else:
                print("Please load a sequence first (option 1).")

        elif choice == '5':
            if sequence:
                print(f"Reverse Complement: {reverse_complement(sequence)}")
            else:
                print("Please load a sequence first (option 1).")

        elif choice == '6':
            if sequence:
                print(f"mRNA Sequence: {transcribe_to_mrna(sequence)}")
            else:
                print("Please load a sequence first (option 1).")

        elif choice == '7':
            if sequence:
                mrna = transcribe_to_mrna(sequence)
                protein = translate_to_protein(mrna)
                print(f"Protein Sequence: {protein if protein else '(no amino acids found)'}")
            else:
                print("Please load a sequence first (option 1).")

        elif choice == '8':
            if sequence:
                pattern = input("Enter pattern to search: ").strip().upper()
                if is_valid_dna(pattern) and len(pattern) > 0:
                    positions = search_pattern(sequence, pattern)
                    if positions:
                        print(f"Pattern found at position(s): {positions}")
                    else:
                        print("Pattern not found in the sequence.")
                else:
                    print("Invalid pattern! Only A, T, G, C characters are allowed.")
            else:
                print("Please load a sequence first (option 1).")

        elif choice == '9':
            print("Thank you for using DNA Sequence Analyzer. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1-9.")

if __name__ == "__main__":
    main()