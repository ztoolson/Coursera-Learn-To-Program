def second_index(s1, s2):
    '''
    (str, str) => int

    Return the index of the second occurance of s2 in the string s1. If there
    in no second occurance, the function returns -1
    
    >>> second_index('the big banana', 'ana')
    11
    >>> second_index('That cat', 'at')
    6
    >>> second_index('Chicken', 'ick')
    -1
    '''
    first_index = s1.find(s2)
    return s1.find(s2, first_index + 1)


