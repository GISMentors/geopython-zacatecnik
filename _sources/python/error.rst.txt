Chyby, jak je číst a interpretovat
==================================

Do souboru `printing.py` napište následující řádky a spusťte jej. Jaké chyby se
vyskytly a proč? Zkuste je odstranit

.. code-block:: python

        #!/usr/bin/env python3

        print(1)
        print(1, 2, 3)
        print(1 + 1)
        print(3 * 8)
        print(10 - 2.2)
        print(3 + (4 + 6) * 8 / 2 - 1)
        print('*' * 80)
        print("Ahoj" + " " + "PyLadies!")
        print("Součet čísel 3 a 8 je", 3 + 8)
        print('Máma má mísu')
        print(V míse je maso.)


Při běhu souboru byla až zcela na konci nalezena *Chyba Syntaxe* - soubor ani
nešel spustit. 

.. code-block:: python

          File "/tmp/printing.py", line 13
            print(V míse je maso.)
                       ^
        SyntaxError: invalid syntax

Python vypíše jméno souboru, číslo řádku a pozici na řádku, kde našel chybu.
Dále napíše, jakého druhu chyba je. Pokud se jedná o chybu vnořenou ve větší
hloubi kódu, bývá vypsán celý "stack" (sloupec) -- řetězec vyvolaných *výjimek*,
jak se chyba projevila a kde všude nadělala paseku. Proto *je výhodné začít s
hledáním chyby od spodu* ve výpisu.

Pokud zkusíme experimentovat a např. sečteme *číslo a řetězec* nebo zkusíme
*dělit nulou*, dostaneme odlišné chyby.

Jak funguje Program
===================

Je to zatím docela jednoduché: příkazy se provádějí jeden po druhém, odshora
dolů. Program je jako recept: seznam instrukcí.

Pro zatím máme pouze jeden jasný směr, jak jsou programy vykonávány. Časem ale
přibudou odbočky a smyčky, které přehlednost poněkud zkomplikují.
