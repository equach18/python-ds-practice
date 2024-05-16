def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if len(parens) % 2 != 0 or parens[0] == ')':
        return False
    elif len(parens) % 2 != 0:
        for i in range(len(parens)/2):
            if parens[i] == parens[-i-1]:
                return False
    return True
