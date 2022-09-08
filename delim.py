def test_delim(source):
    """
    >>> test_delim('{(blabla)5555}[1123123(testestesteste)999]')
    True

    >>> test_delim('{ (altoqi) } [')
    False

    >>> test_delim('[ { ] }')
    False

    >>> test_delim('')
    True

    """
    #delimiters = ['[', ']', '(', ')', '{', '}']
    #delimiters_map = {']':'[', ')':'(', '}':'{'}


    delimiterPairs = [('[', ']'), ('(', ')'), ('{', '}')]
    delimOpens = set(o for o,c in delimiterPairs)
    delimCloseToOpen = dict((c,o) for o,c in delimiterPairs)


    delimStack = ['testel']
    for c in source :
        if c in delimOpens :
            delimStack.append(c)
        elif c in delimCloseToOpen :
            if delimCloseToOpen[c] != delimStack.pop() :
                return False
    return (len(delimStack) == 1)



    working_set = []
    for i,v in enumerate(source):
        if v not in delimiters:
            continue
        if v in delimiters_map: # end of a delimiter:
            if (not working_set) or (working_set[-1] != delimiters_map[v]):
               return False
            else:
               working_set.pop(-1)
        elif v in delimiters:
            working_set.append(v)

    if len(working_set) > 0:
       return False
    else:
       return True


print( test_delim(']') )
print ( test_delim('0]') )