#Different Approaches to determine whether a string is a palindrome

#approach 1
def is_palindrome_v1(s):
    ''' (str) -> bool

    Return True if and only if s is a palindrome. This is case sensitive.

    1. reverse the string
    2. compare the reversed string to the original string

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    '''
    return s == reverse(s)

#approach 2
def is_palindrome_v2(s):
    ''' (str) -> bool
    Return True if and only if s is a palindrome. This is case sensitive.
    
    1. split the string into to halves
        example:
        noon -> no | on
        racecar -> rac | e | car (ignore the middle letter if the string is odd)
    2. reverse the second half
    3. compare the first hald to the reversed second half

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    '''
    mid = len(s) - len(s) // 2
    
    first_half = s[:mid]
    second_half = s[mid:]
    
    
    return first_half == reverse(second_half)


#approach 3
def is_palindrome_v3(s):
    
    '''(str) -> bool

    Return True if and only if s is a palindrome. This is case sensitive.

    1. Compare the 1st character to the last character
    2. Compare the 2nd character to the second last character
    ...
    Stop when the middle of the string is reached. This is case sensitive.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    '''
    for index in range(len(s)):
        if s[index] != s[-(index + 1)]:
            return False
    return True

#approach 4 -> recursive implementation of is_palindrome_v3
def is_palindrome_v4(s):
    '''(str) -> bool

    Return True if and only if s is a palindrome. This is case sensitive.

    1. Compare the 1st character to the last character
    2. Compare the 2nd character to the second last character
    ...
    Stop when the middle of the string is reached. This is case sensitive.

    >>> is_palindrome_v4('noon')
    True
    >>> is_palindrome_v4('racecar')
    True
    >>> is_palindrome_v4('dented')
    False
    '''
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome_v4(s[1:-1])

def reverse(s):
    ''' (str) -> str

    Return a reversed version of s.
    
    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    '''
    rev = ''
    
    #for each char in s, add that char to the beginning of rev
    for char in s:
        rev = char + rev

    return rev
