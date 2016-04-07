Načítání vstupu
---------------

Jak zařídit, aby číslo nemuselo být zapsáno v programu, ale
aby ho mohl uživatel zadat sám.

Stejně jako pro výstup používáme *funkci* `print` pro vstup použijeme funkci
`input`.

Protože ale ze vstupu jsou načítány *textové řetězce*, musíme je nejprve převézt
na *číslo* a k tomu použijeme funkci `float` (tedy převod na číslo s plovoucí
desetinnou čárkou).

Hotový program může vypadat takto:

.. code-block:: python

        # Tento program počítá obvod a obsah čtverce.

        strana = input('Zadej stranu v centimetrech: ')
        strana = float(strana) # převod na číslo

        # výstup
        print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
        print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')

Výstup jedné funkce můžeme poslat na vstup do druhé funkce - můžeme je za sebou
řetězit:


.. code-block:: python

        strana = float(input('Zadej stranu v centimetrech: '))

A pro větší čitelnost (pokud je řádek příliš dlouhý) můžem i logicky mezi
závorkami zalomit:

.. code-block:: python

        strana = float(
            input('Zadej stranu v centimetrech: ')
        )
