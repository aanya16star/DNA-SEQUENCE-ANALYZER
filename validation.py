def is_valid_dna(sequence):
    if len(sequence) == 0:
        return False
    for base in sequence:
        if base not in "ATGC":
            return False
    return True
