Proměnné a tisk
===============

Výrazy můžeme spojovat a kombinovat například pomocí čárky.

.. code-block:: python

        print('Obvod čtverce se stranou 356 cm je', 4 * 356, 'cm')
        print('Obsah čtverce se stranou 356 cm je', 356 * 356, 'cm2')

        Obvod čtverce se stranou 356 cm je 1424 cm
        Obsah čtverce se stranou 356 cm je 126736 cm2


Můžeme také spočítat obvod menšího čtverce

.. code-block:: python

        print('Obvod čtverce se stranou 112 cm je', 4 * 112, 'cm')
        print('Obsah čtverce se stranou 112 cm je', 112 * 112, 'cm2')

        Obvod čtverce se stranou 112 cm je 448 cm
        Obsah čtverce se stranou 112 cm je 12544 cm2

Nyní je vhodná chvíle na zavedení *proměnných*. Proměnné nám umožňují definovat
na jednom místě v programu určité hodnoty, se kterými se dále v programu
pracuje. Můžeme si být jisti, že proměnná se "sama od sebe" nezmění, neuděláte
chybu při věčném opisování čísel a textů.

V následujícím programu zavedeme proměnnou *strana* a nastavíme jí číslo 123.
Následně provedeme výpočet charakteristik čtverce jak to již umíme:


.. code-block:: python

        strana = 123
        print('Obvod čtverce se stranou', strana, 'cm je', 4 * strana, 'cm')
        print('Obsah čtverce se stranou', strana, 'cm je', strana * strana, 'cm2')

        Obvod čtverce se stranou 112 cm je 492 cm
        Obsah čtverce se stranou 112 cm je 15129 cm2

Proměnná je námi zvolené slovo, pod kterým budeme přistupovat k její hodnotě.
Slovo může být v podstatě libovolné, ale nesmí být stejné jako některé ze slov
vyhrazených, které jsou používány přímo interpretem jazyka python, např. `print,
import, if` a podobně.

Hodnotu proměnné *přiřadíme* znakem `=`.

.. note:: Ve většině programovacích jazyků se znak *rovná se* '=' používá pro
        *přirazení* proměnné ne k *porovnávání* výrazů. Pro porovnávání se
        používají znaky `==` - více o porovnávání se dozvíme v další části.

To nás vede k jedné ze základních programátorských zásad: "neopakuj se"
(anglicky *Don't repeat yourself, DRY*). Když se někde opakuje stejná hodnota,
stejný výraz, nebo stejný kus kódu, dobrá programátorka ten kus programu
pojmenuje a pak používá jen jméno. Často se totiž stává, že je program potřeba
změnit – buď je v něm chyba, nebo se změní zadání. A potom je mnohem jednodušší
změnu udělat jen na jednom místě.

Proměnné si můžete vytvořit podle potřeby *kdekoliv v kódu, kde to zrovna
potřebujete*.Bývá ale dobrým zvykem, proměnné *deklarovat* na začátku funkce
nebo na začátku programu.

.. code-block:: python

        r = 123
        pi = 3.14
        h = 3
        jednoky = 'm'

        print('Objem válce s poloměrem', r, jednotky, 'a výškou', h, jednotky,
              'je', pi*r*r*h, jednotky+'3')
