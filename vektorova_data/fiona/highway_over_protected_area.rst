Dálnice přes České středohoří
-----------------------------

.. note:: Nová dálnice přes CHKO České středohoří

        Najděte oblasti, kterých se bezprostředně dotkla výstavba dálnice D8 z
        Prahy do Drážďan. Předpokládejme, že se jedná o oblast 200m od dálnice.
        O jak velké území se jedná?

.. figure:: ../../images/highways_areas.png

        Dálniční síť České republiky spolu s mapou chráněných krajinných
        oblastí.

Potřebné kroky pro vyřešení úlohy

#. Otevření obou datových zdrojů
#. Převod na společný souřadnicový systém
#. Vytvoření obalové zóny okolo dálnic
#. Zjištění průniku všech geometrií


Načtení datových zdrojů
^^^^^^^^^^^^^^^^^^^^^^^

Nejprve oba soubory otevřeme pomocí klasického `fiona.open()`. Použijeme buď
klauzuli `with` nebo nesmíme nakonec zapomenout sobory uzavřít.

.. literalinclude:: ../../_static/skripty/highway-example.py
   :language: python
   :lines: 1-2,9-10

Společný souřadnicový systém
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Data jak můžeme ověřit, data jsou v různých souřadnicových systémech.

.. note:: Zjistěte, v jakých souřadnicových systémech jsou dálnice a chráněné
        krajinné oblasti.

Pro další práci proto musíme data převézt na jednotný souřadnicový systém.

Na transformaci jednotlivých geometrí můžeme použít např. funkci
`trasnform_geom`

.. code-block:: python

        from fiona.transform import transform_geom

        wgs84 = "EPSG:4326"
        jtsk = {"init": "epsg:5514"}

        geom_transformed = transform_geom(wgs84, jtsk, feature["geometry"])

Vytvoření obalové zóny okolo dálnic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pro každý prvek v dálniční síti, nejprve vyfiltrujeme pouze prvky se jménem
dálnice D8, transformujeme geometrii na S-JTSK a vytvoříme obalovou zónu:

.. literalinclude:: ../../_static/skripty/highway-example.py
   :language: python
   :lines: 12-23

.. note:: Zrychlení topologických operací

        Modul `shapely.speedups` obsahuje zrychlení některých operací optimalizovaných v
        jazyce C. Pokud během instalace byla dostupná knihovan GEOS a pokud byl dostupný
        kompilátor jazyka C, jsou tyto optimalizace automaticky zavedeny.

        Ověřit jejch přítomnost, případně je explicitně povolit, můžeme modulem
        `speedups`::

                >>> from shapely import speedups
                >>> print(speedups.available)
                True
                >>> speedups.enable()

Průnik geometrií
^^^^^^^^^^^^^^^^

Pro každou chráněnou krajinnou oblast musíme nejprve zjistit, jestli se
geometrie CHKO a obalové zóny okolo dálnice protínají - teprve potom má smysl
pokračovat s interkací.

.. literalinclude:: ../../_static/skripty/highway-example.py
   :language: python
   :lines: 24-34

Spojení do jedné geometrie
^^^^^^^^^^^^^^^^^^^^^^^^^^

V tuto chvíli máme data rozkouskovaná, bylo by ale vhodné je spojit do jednoho
geometrického objektu.

.. note:: Spojení geometrií do jednoho objektu

        Navrhněte postup, jak spojit více geometrií do jedné.


Zápis do souboru - OGC GeoPackage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pokud potřebujeme uložit některý z binárních typů vektorových souborů (ESRI
Shapefile, OGC GeoPackage, ...) musíme nejprve nadefinovat datové schéma -
atributy a typ geometrií.

.. code-block:: python
        
        schema = {
                'properties': {
                        'highway': 'str'
                },
                'geometry': 'MultiPolygon'
        }

Následně můžeme otevřít nový soubor pro zápis a uložit do něj námi vytvořenou
geometrii.

.. code-block:: python

        with fiona.open("chko_x_highway.gpkg", "w", driver="GPKG", crs="EPSG:5514", schema=schema) as out:
                feature = {
                        'type': 'Feature',
                        'properties': {
                                'highway': 'D8'
                        },
                        'geometry': mapping(one_geometry)
                }
                out.write(feature)

Zápis do souboru - GeoJSON
^^^^^^^^^^^^^^^^^^^^^^^^^^
