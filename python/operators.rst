Operátory a datové typy
-----------------------

(Nejen aritmetické) operátory slouží k operacím nad hodnotami. Funkce
jednotlivých operatorů je samovysvětlující, některé jsou trochu více nezvyklé,
ale jasné:

+-------------+---------------+-----------------------------------------------+
|**Symbol**   |**Příklad**    |**Popis**                                      |
+=============+===============+===============================================+
| +, -, \*, / | 1 + 1         | Základní aritmetika                           |
+-------------+---------------+-----------------------------------------------+
| \-          | -5            | Negace                                        |
+-------------+---------------+-----------------------------------------------+
| //; %       | 7 // 2; 7 % 2 | Dělení se zbytkem (celočíselné dělení); zbytek|
+-------------+---------------+-----------------------------------------------+
| \*\*        | 3**2          | Umocnění (3 na druhou)                        |
+-------------+---------------+-----------------------------------------------+


Příklady toho jak fungují operátory nad různými datovými typy:

.. code-block:: python

    >>> 1 + 1
    2

    >>> 'Ahoj ' + 'světe!'
    'Ahoj světe!'

    >>> 1 - 1
    0

    >>> 'Ahoj ' - 'světe!'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for -: 'str' and 'str'

    >>> print("Už nikdy nebudu psát kód 2x\n" * 100)
    Už nikdy nebudu psát kód 2x
    Už nikdy nebudu psát kód 2x
    Už nikdy nebudu psát kód 2x
    Už nikdy nebudu psát kód 2x
    ...

    >>> 7%2
    1

    >>> 9**9
    387420489

Další důležité operátory jsou operátory porovnávací

=========== =============== ==================================
Symbol      Příklad         Popis
=========== =============== ==================================
==, !=      1 == 1, 1 != 1  Je rovno, není rovno
<, >        3 < 5, 3 > 5    Větší než, menší než
<=, >=      3 <= 5, 3 >= 5  Větší nebo rovno, menší nebo rovno
=========== =============== ==================================

Výsledkem porovnávání je booleanovská hodnota `True` nebo `False`
(pravda/nepravda).

Příklady logických operátorů:

.. code-block:: python

        >>> 1 < 1
        False

        >>> a = 1
        >>> b = 5
        >>> a = b   # POZOR - přirazení - a teď obsahuje hodnotu 5
        print(a, b)

        >>> a = 1
        >>> a == b
        False
        >>> a != b
        True

Datové typy
-----------
Počítače potřebují k uložní čísel a řetězců určité množstí paměti. Proto,
abychom mohli V programovacích jazycích a databázích proměnné a data efektivně
ukládat, jsou zavedeny různé *datové typy*, které zabírají optimální množství
paměti v počítači.

    * Nejméně paměti zabere booleanovská hodnota Pravda/Nepravda nebo-li `True` a
      `False`
    * Dalším datovým typem je *celé číslo* `integer`
    * Dále *číslo s plovoucí desetinnou čárkou* `float`
    * *Textový řetězec* nebo-li `string` zabírá ještě více místa

.. note:: Datových typů je více a v různých programovacích jazycích a databázích
        jsou různé. Formát DBF je omezen na číslo, číslo desetinné a text,
        databáze PostgreSQL `rozlišuje celou řadu datových typů
        <http://www.postgresql.org/docs/9.4/static/datatype.html>`_.

Python nám dává nástroje (funkce) pro převod mezi datovými typy, některé už jsme
viděli `float(), int()` a `int()`:

.. code-block:: python

    >>> int(3.3) # nezaokrouhluje - vždy odstraní hodnotu za desetinnou tečkou
    3

    >>> str(1)

    >>> float('pí je 3.14')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: could not convert string to float: pi je 3.14

    >>> float('3.14')
    3.14

S dalšími více komplexními datovými typy se budeme seznamovat postupně dále.


Jaký má proměnná datový typ zjistíte rychle pomocí funkce `type()`:

.. code-block:: python

    >>> type(1)
    <class 'int'>

    >>> a = 'elce pelce'
    >>> type(a)
    <class 'str'>
