def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    """
    Returns multiple values (not a list) of all starting positions (1-based)
    where dna_string2 appears as a substring in dna_string1.
    """
    positions = []

    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i + len(dna_string2)] == dna_string2:
            positions.append(i + 1)  # convert to 1-based

    return tuple(positions)  # return multiple parameters


def validate_dna_string(dna):
    # must be > 8 and <= 16
    return 8 < len(dna) <= 16


def validate_dna_substring(sub):
    # must be exactly 4 characters
    return len(sub) == 4
