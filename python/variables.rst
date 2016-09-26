Proměnné a tisk
===============

Výrazy můžeme spojovat a kombinovat například pomocí čárky.

.. code-block:: python

        print('Obvod čtverce se stranou 356 cm je', 4 * 356, 'cm')
        print('Obsah čtverce se stranou 356 cm je', 356 * 356, 'cm2')

::

   Obvod čtverce se stranou 356 cm je 1424 cm
   Obsah čtverce se stranou 356 cm je 126736 cm2

.. note:: Místo čárky pro kombinaci výrazů je vhodnější použít
          formátování pomocí funkce ``format()``. Výraz výše uvedený
          by mohl vypadat následovně:

          .. code-block:: python

             print('Obvod čtverce se stranou 356 cm je {} cm'.format(4 * 356))
             
          V návodem také můžete narazit na formátovací znak ``%``:

          .. code-block:: python

             print('Obvod čtverce se stranou 356 cm je %d cm' % (4 * 356))
   
Můžeme také spočítat obvod menšího čtverce

.. code-block:: python

        print('Obvod čtverce se stranou 112 cm je', 4 * 112, 'cm')
        print('Obsah čtverce se stranou 112 cm je', 112 * 112, 'cm2')

::
           
   Obvod čtverce se stranou 112 cm je 448 cm
   Obsah čtverce se stranou 112 cm je 12544 cm2

Nyní je vhodná chvíle na zavedení *proměnných*. Proměnné nám umožňují definovat
na jednom místě určité hodnoty, se kterými se dále v programu
pracuje. Můžeme si být jisti, že proměnná se "sama od sebe" nezmění, neuděláte
chybu při věčném opisování čísel a textů.

V následujícím programu zavedeme proměnnou *strana* a nastavíme jí hodnotu 123.
Následně provedeme výpočet charakteristik čtverce jak to již umíme:


.. code-block:: python

        strana = 123
        print('Obvod čtverce se stranou', strana, 'cm je', 4 * strana, 'cm')
        print('Obsah čtverce se stranou', strana, 'cm je', strana * strana, 'cm2')

::
        
   Obvod čtverce se stranou 112 cm je 492 cm
   Obsah čtverce se stranou 112 cm je 15129 cm2

Proměnná je reprezentována nami zvoleným slovem (tzv. názvem
proměnné), pod kterým budeme přistupovat k její hodnotě.  Název
proměnné může být v podstatě libovolný. Nesmí ale začínat na číslici
či se shodovat s jedním z vyhrazených slov, které jsou používány přímo
interpretem jazyka Python, např. `print, import, if` a podobně.

Hodnotu proměnné *přiřadíme* znakem ``=`` (rovná se).

.. note:: Ve většině programovacích jazyků se znak *rovná se* ``=``
        používá pro *přirazení* proměnné a nikoliv k *porovnávání*
        výrazů. Pro porovnávání se používají znaky ``==`` - více o
        porovnávání se dozvíme v další části.

To nás vede k jedné ze základních programátorských zásad: "neopakuj
se" (anglicky *Don't repeat yourself, DRY*). Pokud se v programu
opakuje stejná hodnota, stejný výraz, nebo stejný kus kódu použijeme
správně proměnou či funkci. Často se totiž stává, že je program
potřeba změnit - buď je v něm chyba, nebo se změní zadání. A potom je
mnohem jednodušší změnu udělat jen na jednom místě.

Proměnné si můžete vytvořit podle potřeby *kdekoliv v kódu, kde to zrovna
potřebujete*. Bývá ale dobrým zvykem, proměnné *deklarovat* na začátku funkce
nebo na začátku programu.

.. code-block:: python

        r = 123
        pi = 3.14
        h = 3
        jednotky = 'm'

        print('Objem válce s poloměrem', r, jednotky, 'a výškou', h, jednotky,
              'je', pi*r*r*h, jednotky+'3')
