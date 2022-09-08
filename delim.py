#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    paresDelimitadores = [('[', ']'), ('(', ')'), ('{', '}')]
    delimAbertos = set(o for o,c in paresDelimitadores)
    delimFechadoParaAberto = dict((c,o) for o,c in paresDelimitadores)


    delimArray = ['']
    for c in source :
        if c in delimAbertos :
            delimArray.append(c)
        elif c in delimFechadoParaAberto :
            if delimFechadoParaAberto[c] != delimArray.pop() :
                return False
    return (len(delimArray) == 1)




print( test_delim(']') )
print ( test_delim('0]') )