Geometrie geoprvků a knihovna Shapely
-------------------------------------

V této části se blíže seznámíme jak pracovat s geometrií vektorových
prvků.

Knihovna `Shapely <https://github.com/Toblerity/Shapely>`__ (stejného
autora jako Fiony) nám umožňuje pracovat s geometrickou složkou popisu
geoprvků opět ve stylu jazyka Python. Stejně jako Fiona, převádí
Shapely geometrické vlastnosti na objekty typu JSON.

Shapely
^^^^^^^

Shapely obsahuje i některé funkce pro modifikaci geometrií, například
generalizaci, obalovou zónu (buffer) nebo porovnání dvou
geometrií. Shapely využívá pro manipulaci s geometriemi knihovnu `GEOS
<https://libgeos.org/>`__, která je zase re-implementací nástroje JTS
(Java Topoology Suite) do jazyka C, a používá se například v
databázové nadstavbě PostGIS. GEOS a JTS odpovídají specifikaci OGC
Simple Feature. Knihovna Shapely nám umožní řešit například úlohy
typu:

* Jakou výměru má plošný prvek?
* Překrývají se dva prvky?
* Jak vypadá společný průnik více prvků?
* Vytvořit obalovou zónu okolo prvku.

Pro práci s geometriemi proto potřebujeme převést data na struktury
Shapely:

.. literalinclude:: ../../_static/skripty/fiona-example.py
   :language: python
   :lines: 47-51

.. code-block:: python

    (-683329.1875, -993228.75, -681265.625, -991528.0)

.. tip:: V prostředí Jupyter notebook můžeme geometrii vizualizovat
    prostě tak, že obsah proměnné s geometrií necháme vypsat, např.::

        geom = shape(chko[54]["geometry"])
        geom

.. todo:: Příklad vykreslení geometrie pomocí matplotlib
          https://deparkes.co.uk/2015/03/11/how-to-plot-polygons-in-python/

Nyní se můžeme vypsat celou řadu metadat o daném geometrickém objektu

.. code-block:: python

    print(geom.type)
    print(geom.area)
    ...

.. task:: Zjistěte, jaký má naše geometrie obvod a najděte souřadnice
   jejího centroidu. Jaká metoda se použije pro vytvoření obalové
   zóny a jak funguje?

.. note:: Kompletní ukázkový příklad na využití knihoven Fiona a
   Shapely `zde <../../_static/skripty/fiona-example.py>`__.
   
Převod geometrie zpět na formát JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Na převod zpět  do formátu JSON použijeme funkci ``mapping`` z modulu
``shapely.geometry``.

Jako příklad si vytvoříme "ručně" celý nový vektorový objekt


.. code-block:: python

    new_feature = {
        "type": "Feature",
        "properties": {
            "NAZEV": "prvek s obalovou zonou 100m",
        },
        "geometry": mapping(geom.buffer(100))
    }
