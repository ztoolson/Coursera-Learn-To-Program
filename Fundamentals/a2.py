def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)



def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return len(dna1) > len(dna2)



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    count = 0
    for nuc in dna:
        if nuc == nucleotide:
            count += 1
    return count
    



def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    return dna2 in dna1


def is_valid_sequence(dna):
    ''' (str) -> bool

    The parameter is a potential DNA sequence. This method returns True if and
    only if the DNA sequence is valid( that is, it contains no characters other
    than 'A', 'T', 'C', 'G'). Lowercase characters are NOT valid

    >>> is_valid_sequence('ATCCGGTCG')
    True
    >>> is_valid_sequence('ATCGa')
    False
    >>> is_valid_sequence('This is a bad test')
    False
    '''
    non_valid_count = 0
    
    for char in dna:
        if char not in 'ATCG':
            non_valid_count += 1
            
    return non_valid_count == 0


def insert_sequence(dna1, dna2, index):
    ''' (str, str, int) -> str

    The first two parameters are DNA sequences and the third parameter is an index.
    This function returns the DNA sequence obtained by inserting the second DNA sequence
    into the first DNa sequence at a given index.

    Preconditon: Assume the index, and DNA sequences are valid

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 0)
    ATCCGG
    >>> insert_sequence('CCGG', 'AT', 4)
    CCGGAT
    '''
    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nucleotide):
    ''' (str) -> str

    Parameter is a nucleotide ('A', 'T', 'C', 'G')
    Precondition: The parameter nucleotide is a corrent nucleotide.
    
    This method returns the nucleotide's complement. If precondition is not met, method returns None

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    
    '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'


def get_complementary_sequence(dna):
    ''' (str) -> str

    The parameter is a DNA sequence.

    Return the DNA sequence that is complementary to the given DNA sequence.


    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CG')
    'GC'
    
    '''
    complementary_dna = ''
    
    for nucleotide in dna:
        complementary_dna += get_complement(nucleotide)
        
    return complementary_dna
