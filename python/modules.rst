Moduly
======
Síla programovacího jazyka není pouze v jeho syntaxi, ale především ve funkcích,
které už někdo naprogramoval před vámi a vy je musíte jenom použít.

Python používá systém *modulů* - v podstatě se jedná o soubory, ve kterých jsou
funkce uloženy a do vašeho programu je musíte *naimportovat*. Heslem Pythonu je
*"batterries included"* a znamená to, že opravdu spousta věcí je už hotová a
dostupná.

Čím více modulů budete importovat, tím více vám váš program bude zabírat v
paměti a jeho spouštění bude o něco pomalejší - neimportujte něco, co
nepotřebujete.

Vyzkoušíme si např. některé funkce z modulu `math`

.. code-block:: python

    import math

    print(math.sqrt(10))

Funkce :func:`sqrt` není standardně v základu Pythonu přítomna.  Program by skončil
výjimkou

.. code-block:: python

        NameError: name 'math' is not defined

Modul `math` obsahuje celou řadu zajímavých věcí, např. číslo `PI`

.. code-block:: python

    print(math.pi)
    print(math.e)

Importovat můžete buď celé moduly, jako v předchozím příkladě, nebo jenom
jednotlivé fukce, např. :func:`sin`.

.. code-block:: python

    from math import sin

    print(sin(math.pi/2))

Nyní něco ze světa prostorových dat

.. code-block:: python

        from shapely.geometry import Point

        centroid = Point(0.0, 0.0) # vytvoříme nový objekt třídy "Point"
        patch = centroid.buffer(10.0) # zavoláme jeho metodu buffer
        print(patch.area) # a tiskneme jeho plochu

V předchozím příkladu jsme z modulu `shapely`, který nám umožňuje pracovat s
vektorovými geometriemi naimportovali třídu :class:`Point`, vytvořili jsme nový
bod, okolo něj buffer o velikosti 10 a vytiskli plochu výsledné obalové zóny.

Trochu jsme tím nakoukli do světa objektově-orientovaného programování, blíže se
s ním seznámíme v další části.

Nyní zkusíme ještě vytisknout vytvořený buffer ve formátu GeoJSON:

.. code-block:: python

    import json
    from shapely.geometry import mapping

    print(json.dumps(mapping(patch)))

V předchozím příkladu jsme na posledním řádku použili jako vstup pro funkci
:func:`print` výstup z funkce :func:`json.dumps`, která zase dostala výstup z
funkce :func:`mapping` - není to moc přehledné, ale podobné konstrukce se
používají často.

Dokumentace k modulům
---------------------
Je na čase, seznámit se s příkazem `pydoc` (nebo `pydoc3`), který jako parametr
dostane modul a provede vás jeho dokumentací

.. code-block:: bash

    $ pydoc shapely


    Help on package shapely.geometry in shapely:
    
    NAME
        shapely.geometry - Geometry classes and factories
    
    FILE
        /home/jachym/.local/lib/python2.7/site-packages/shapely/geometry/__init__.py
    
    PACKAGE CONTENTS
        base
        collection
        geo
        linestring
        multilinestring
        multipoint
        multipolygon

    ...

Google vám vždycky dobře poradí, pokud správně hledáte a seznam modulů
distribuovaných spolu s jazykem Python najdete na `dokumentační stránce jazyka
Python <https://docs.python.org/3.4/library/index.html>`_

Vlastní moduly
--------------
Uložíte-li program do souboru, stává se tímto váš soubor modulem, který lze
použít a naimportovat.

Vytvoříme soubor :file:`buffer.py` s následujícím obsahem:

.. code-block:: python

    from shapely.geometry import Point
    from shapely.geometry import mapping, shape

    def udelej_buffer(geometry, velikost):
        """Vrátí buffer ve formátu GeoJSON pro zadanou geometrii
        """

        geometrie = shape(geometry)
        buffer = geometrie.buffer(velikost)
        return  mapping(buffer)

Nyní můžeme v jiném programu (nebo přímo v interpretu) náš modul použít:

.. code-block:: python

    >>> import buffer
    >>> muj_bod = {"type": "Point", "coordinates": [0.0, 0.0]}
    >>> buffer.udelej_buffer(muj_bod, 3)
    {
        'type': 'Polygon',
        'coordinates': ((
            (3.0, 0.0),
            (2.9855541800165906, -0.29405142098868153),
            (2.9423558412096917, -0.5852709660483842),
            (2.8708210071966267, -0.8708540317633864),
            (2.771638597533861, -1.1480502970952682),
            (2.6457637930450657, -1.4141902104779915),
            (2.4944088369076365, -1.6667106990588052),
            (2.3190313600882124, -1.903179852490935),
            (2.1213203435596446, -2.1213203435596406),
            (1.903179852490939, -2.319031360088209),
            (1.6667106990588092, -2.4944088369),
            ...
        ))
    }

Moduly nám tedy umožňují uklidit spolu související části programu do logických
celků, rozsekat rozsáhlé programy do menších souborů a strukturovat tak kód pro
přehlednější použití.
