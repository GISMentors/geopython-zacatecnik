Výjimky
=======

Když se v Pythonu něco fatálně nepovede, nestane se to, že by program
nekontrolovatelně spadnul. Na místo toho "vyhodí" *výjimku* a dá vám možnost na
ni reagovat. Můžete například pokračovat dál v jiné konfiguraci, smazat dočasné
soubory a program ukončit čistě a tak podobně.

Výjimek je mnoho typů a ve vlastních programech si můžete vytvářet vlastní.
Můžete tak reagovat na mimořádné události (jako například špatně zadaný
uživatelský vstup, nefunkční internetové připojení, neexistující soubor a tak
dál).

Následující kód uložte do souboru :file:`deleni.py`

.. code-block:: python
    
    #!/usr/bin/env python3

    def deleni(delenec, delitel):
        """Vydeli jedno cislo druhym
        """

        return delenec/delitel

    print(deleni(10, 0))

A soubor spusťe:

.. code-block:: bash
        $ python3 deleni.py

        Traceback (most recent call last):
          File "deleni.py", line 9, in <module>
            print(deleni(10/0))
        ZeroDivisionError: division by zero

Nemůžeme dělit nulou - program vyhodil výjimku a navedl nás na řádek 9 v souboru
:file:`deleni.py`. Program vyhodil speciální ``ZeroDivisionError`` výjimku, kterou
můžeme zachytit a zareagovat na ni.

Odchycení výjimky
-----------------

Předchozí kód upravíme následujícím způsobem:

.. code-block:: python
    
    #!/usr/bin/env python3

    def deleni(delenec, delitel):
        """Vydeli jedno cislo druhym
        """

        try:
            return delenec/delitel
        except (ZeroDivisionError, error):
            print('Dělitel nesmí být nula!')
            return None

    print(deleni(10/0))

Blok kódu, který hrozí výjimkou (v našem případě pouze jeden řádek) jsme
uzavřeli mezi klíčová slova ``try`` a ``except``, tedy *zkus* a *kdyby to nedopadlo,
tak*

Jako parametr *except* se předá *typ výjimky* a název proměnné, do které bude
uložena, abychom s ní případně mohli dál pracovat.
