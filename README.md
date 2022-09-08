# python-delimiter-test
<br />
<br />
PT_BR: Função para verificar se todos os delimitadores são correspondentes e fechados. 
<br />
<br />
EN: Function to check that all delimiters are matched and closed
<br />
<br />


Testes automatizados.
<br />

+    """
+    >>> test_delim('{(blabla)5555}[1123123(testestesteste)999]')
+    True
+    >>> test_delim('{ (altoqi) } [')
+    False
+    >>> test_delim('[ { ] }')
+    False
*    >>> test_delim('')
*    True
+    """


Para executar testes automatizados da função, recomendo o xdoctest
<br />

$ pip install xdoctest
<br />
<br />

$ python -m xdoctest delim.py
<br />
<br />
