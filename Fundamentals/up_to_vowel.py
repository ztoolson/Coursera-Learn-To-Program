def up_to_vowel(s):
    ''' (str) -> str

    Return a substring of s from index 0 up to but not
    including the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>>  up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''
    i = 0
    #count up to a vowel from the beginning of the string
    while i < len(s) and s[i] not in 'aeiouAEIOU':
        i = i + 1
    return s[:i]

def get_answer(prompt):
    ''' (str) -> str

    Use promt to ask the user for a "yes" or "no"
    answer and continue asking until the user
    gives a valid response. Return the answer.
    '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer
                   
    
