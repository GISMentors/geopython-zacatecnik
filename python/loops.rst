Smyčky, cykly
=============

Další důležitou koponentou programovacích jazyků jsou tzv. *smyčky* nebo
*cykly*. Jsou to opakující se části kódu  a pomáhají programátorovi vytvořit
konstrukci typu *"pro každý prvek z množiny prvků vykonej ..."* nebo *"opakuj
... dokud není splněna podmínka, že ..."*.

Smyčka for
-----------

Zkusme si v praxi následující příklady:

.. code-block:: python

        for cislo in range(5):
            print(cislo)


a

.. code-block:: python

        for pozdrav in 'Ahoj', 'Hello', 'Hola', 'Hei', 'SYN':
            print(pozdrav + '!')

Nová užitečná funkce :func:`range()` vrátí pole indexů, které velikostně odpovídá
zadanému číslu. :func:`range(5)` vrátí pole `[0, 1, 2, 3, 4]`.

Pomocí smyčky `for` vytvoříme novou loklání proměnnou `cislo` nebo `pozdrav`, do
které budou postupně ukládány hodnoty prvků ze vstupního pole a v těle smyčky se
bude s touto proměnnou dále pracovat (v našem případě se pouze zavolá funkce
:func:`print()`.

Oblast platnosti proměnných
---------------------------

Vidíme, že proměnná `cislo` nebo `pozdrav` je definována při vzniku smyčky. Její
oblast platnosti (... je definována pro ...) platí pouze v těle smyčky. Můžeme
ale vzít jinou proměnnou definovanou výše a přistupovat k její hodnotě

.. code-block:: python

    suma = 0

    for i in range(10):
        suma = suma + i

    print(suma)

Smyčka typu while
-----------------
Na rozdíl od smyčky `for`, která pracuje s prvky z existujícího pole, smyčka
typu `while` provádí blok kódu, dokud není splněna nějaká podmínka:

.. code-block:: python

    dny = ['pondeli', 'utery', 'streda', 'cvrtek', 'patek', 'sobota', 'nedele']

    den = 0

    while den < 5:
        print(dny[den] + ': Musim do Kolbenky :-(')
        den = den + 1

    print('Vikend!')

Brzda break
-----------

Smyčka `while` může být zrádná v tom, že pokud není podmínka splněna, může běžet
i nekonečně dlouho

.. code-block:: python

    from random import randrange

    while True:
            print('Číslo je', randrange(10000))
            print('(Počkej, než se počítač unaví...)')

Tento cyklus musíme přerušit uměle (např. klávesovou zkratkou `Ctrl+C`).

Pokud chceme z nějaké smyčky (`for` nebo `while`) náhle vyskočit, použijeme
brzdu `break`. V následující ukázce uvidíme, jak zajistit, že vstup od uživatele
bude opravdu správný:


.. code-block:: python

    while True:
            odpoved = input('Řekni Ááá! ')
            if odpoved == 'Ááá':
                break
            print('Špatně, zkus to znovu')

     print('Hotovo, ani to nebolelo.')
