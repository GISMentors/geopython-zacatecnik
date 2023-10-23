Práce s datových zdrojem
------------------------

V této části si blíže popíšeme, jak otevřít a načíst vektorový soubor
a jak manipulovat s jednotlivými objekty (tj. vektorovými geoprvky -
*features*).

Datovou vrstvu otevřeme pomocí funkce ``open()``, ta vytvoří objekt
tvz. *kolekce* geoprvků:

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 1-11
                      

Následně můžeme zjišťovat vlastnosti této kolekce geoprvků, viz
`dokumentace knihovny <https://fiona.readthedocs.io/en/latest/>`__.

.. code-block:: python

    >>> # driver
    >>> chko.driver
    'ESRI Shapefile'

    >>> # souřadnicový systém
    >>> chko.crs
    'PROJCS["S_JTSK_Krovak_East_North",GEOGCS["GCS_S-JTSK",DATUM["System_of_the_Unified_Trigono...'

    >>> # jméno souboru
    >>> chko.path
    'data/chko.shp'

    >>> # jméno vrstvy
    >>> chko.name
    'chko'

    >>> # hraniční souřadnice
    >>> chko.bounds
    (-891817.1765, -1209945.3889999986, -440108.9158999994, -943075.1875)

    >>> # všechna metadata pohromadě
    >>> chko.meta
    {'driver': 'ESRI Shapefile', 'schema': {'properties': {'gml_id': 'str:80', 'OBJECTID': ... }

Prvky uložené v kolekci můžeme standardním postupem iterovat a
zpracovávat je prvek po prvku. Nejprve ale zjistíme jejich počet:

.. code-block:: python

    >>> len(chko)
    5626

Souřadnicové systémy
--------------------

Na pozadí Fiony se používají nástroje knihovny `GDAL
<http://www.gdal.org>`_, proto ani práce se souřadnicovými systémy
není o tolik zjednodušena, jak by možná bylo potřeba. Pokud je
souřadnicový systém datové vrstvy definován pomocí kódu EPSG, je tento
kód dále využit, v našem případě se jedná o :epsg:`4326`.

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 31-32

.. code-block:: python

   EPSG:4326

Při vytvoření nového geoprvku s definicí souřadnicového systému je postupováno
analogicky (zde S-JTSK, :epsg:`5514`):

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 34-35

.. code-block:: python

   EPSG:5514

Fiona těmito funkcemi pouze mapuje jednotlivé parametry souřadnicového
systému a stará se o jejich převod do textového řetězce a z textových
řetězců.


