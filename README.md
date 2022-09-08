# python-delimiter-test
<br />
<br />
- PT_BR: Função para verificar se todos os delimitadores são correspondentes e fechados. 
<br />
<br />
- EN: Function to check that all delimiters are matched and closed
<br />
<br />

![#1589F0](https://via.placeholder.com/15/1589F0/1589F0.png) Testes automatizados:


<br />
```
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

```
Para executar testes automatizados da função, recomendo o xdoctest
<br />

$ pip install xdoctest
<br />
<br />

$ python -m xdoctest delim.py
<br />
<br />

o resultado será:

```
=====================================
_  _ ___  ____ ____ ___ ____ ____ ___
 \/  |  \ |  | |     |  |___ [__   |
_/\_ |__/ |__| |___  |  |___ ___]  |

=====================================

Start doctest_module('delim.py')
Listing tests
gathering tests
running 1 test(s)
====== <exec> ======
* DOCTEST : delim.py::test_delim:0, line 3 <- wrt source file
DOCTEST SOURCE
1 >>> test_delim('{(blabla)5555}[1123123(testestesteste)999]')
  True
4 >>> test_delim('{ (altoqi) } [')
  False
7 >>> test_delim('[ { ] }')
  False
10 >>> test_delim('')
  True
DOCTEST STDOUT/STDERR
False
False
DOCTEST RESULT
* SUCCESS: delim.py::test_delim:0
====== </exec> ======
============
=== 1 passed in 0.09 seconds ===
```


