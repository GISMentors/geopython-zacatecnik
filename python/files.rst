Práce se soubory
----------------

Soubory jsou velice důležité, protože obsahují data. Jako soubor se chovají i
některá vstupní a výstupní zařízení, síťová připojení a podobně.

Základní operace se soubory jsou *otevření, zápis* a *zavření*. Při otevírání
vznikne nový objekt, se kterým dále pracujeme.

.. code-block:: python

    data_soubor = open('data.txt', 'r')

    data = data_soubor.read()

    data_soubor.close()


Tento příklad - vytvořil novou proměnnou typu :type:`file` v režimu *read*, na
dalším řádku ze souboru přečetl *všechna data* a uložil do proměnné :var:`data`
a nakonec soubor uzavřel.

Lepší je ale využít konstrukci s blokem ``with``, která soubor automaticky
uzavře (i pokud mezitím např. dojde k výjimce) - konečné :func:`close()` pak již
není potřeba.

.. code-block:: python

    with open('data.txt', 'r') as data_soubor:
        data = data_soubor.read()


Pojďme vytvořit soubor typu JSON, který bude obsahovat jeden bod ve formátu
GeoJSON:

.. code-block:: python

    import json
    from shapely.geometry import Point, mapping

    # vytvoříme bod a uložíme do struktury JSON
    bod = Point(100, 100)
    data = mapping(bod)

    # vytvoříme nový objekt typu soubor a uložíme do něj json jako textový
    # řetězec
    with open('/tmp/output.json', 'w') as file_out: # soubor otevřeme v režimu "write"
        file_out.write(json.dumps(data))

Výsledný soubor si můžeme prohlédnout v programu QGIS.

.. note:: Vhodnější by jinak bylo použít funkci json.dump(), která jako parametr
        potřebuje práve file-like objekt, do kterého data zapíše přímo
        `json.dump(file_out, data)`

Režimy otevření souborů
-----------------------
Soubory můžeme otevřít ve 3 režimech: *read*, *write*, *append* - tedy v režimu
pro čtení, zápis a *přidávání* obsahu na konec souboru. Odpovídající parametry
pro funkci `open()` jsou `r, w, a`.

.. code-block:: python

    pridat_na_konec = open('soubor.txt', 'a')
    pridat_na_konec.write('text, ktery bude az na konci souboru\n')
    pridat_na_konec.close()

nebo lépe

.. code-block:: python

    with open('soubor.txt', 'a') as pridat_na_konec:
        pridat_na_konec.write('text, ktery bude az na konci souboru\n')

.. note:: funkce souboru `write()` na rozdíl od `print()` nevkládá znak pro nový
        řádek na konec řádku a musíte ho tam vložit sami (proto `\\n` nakonci)


Zavírání souborů
----------------

Je čisté (a z pohledu souborového systému i bezpečné) soubor na konci práce s
ním uzavřít funkcí `close()`. Někdy je výhodnější kompatní zápis, kdy soubor
bude otevřen jenom v rámci daného bloku kódu:

.. code-block:: python

    with file_out as open('/tmp/output.json', 'w'):
        file_out.write(json.dumps(data))

V tomto případě je soubor automaticky uzavřen na konci bloku uvozeného slovem
`with`.

Bezpečné čtení ze souboru
-------------------------
Funkce `read()` načte *veškerý obsah souboru* - bez ohledu na jeho velikost, na
velikost vaší paměti, na jeho obsah. Používejte proto tuto funkci s rozmyslem.

Pokud načítáte textové soubory, zvažte použití funkce `readlines()`, která načte
soubor po řádcích:

.. code-block:: python

    for line in soubor.readlines():
        # pracuj s řádkem

Funkce `read()` také umožňuje přidat jeden nepovinný parametr - velikost (v
bytech) načtených dat. Můžete tedy zpracovávat soubor postupně:

.. code-block:: python

    size = 1024
    data = soubor.read(size)
    while data:
        # pracuj s proměnnou data
        ...
        data = soubor.read(size) # načti další kusanec

A nebo si na začátku určit maximální velikost dat a vyhodit výjimku, pokud je
soubor větší.

.. code-block:: python

    max_size = 1024
    data = soubor.read(max_size)

    if soubor.read(1): # zkus načíst ještě malý kousek
        raise Exception("Tenhle soubor je nějak velký, kašlu na to")

.. note:: V tomto příkladě jsme si ukázali vyhození vlastní výjimky pomocí
        klíčového slova `raise`
