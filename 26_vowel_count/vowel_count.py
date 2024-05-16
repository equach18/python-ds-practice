def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    undercased_phrase = phrase.lower()
    return {ltr: undercased_phrase.count(ltr) for ltr in set(undercased_phrase) if ltr in 'aeiou'}