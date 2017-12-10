Vektorizace rastrových dat
--------------------------

Převod rastru na vektor - ohraničení pixelů o stejné hodnotě.

Protože používáme `numpy <http://www.numpy.org/>`_ struktury, můžeme využít více
nástrojů.

Vektorize pomocí rasterio
^^^^^^^^^^^^^^^^^^^^^^^^^

Modul `rasterio.features <https://mapbox.github.io/rasterio/api/rasterio.features.html>`_
obsahuje nástroje pro převod rastru na vektor. K dispozici je funkce `shapes <https://mapbox.github.io/rasterio/api/rasterio.features.html#rasterio.features.shapes>`_, která převede sousedící
pixely o stejné hodnotě na vektor (formát GeoJSON).

Hodit se může i např. funkce `sieve <https://mapbox.github.io/rasterio/api/rasterio.features.html#rasterio.features.sieve>`_, kterou můžeme použít na odfiltrování příliš malých ploch.

Jedním z podstatným vstupů je také transformační matice, která převede vektorová
data ze souřadnic obrázku (pixely) na souřadnice geografické.

.. literalinclude:: ../../_static/skripty/rasterio-vectorize.py
   :language: python


.. figure:: ../images/ndvi-classes.png
    
    Výsledný soubor ve vektorech

Vektorize pomocí potrace
^^^^^^^^^^^^^^^^^^^^^^^^

Další možností je vektorize pomocí knihovny `pypotrace <https://pythonhosted.org/pypotrace/>`_.
`Potrace <http://potrace.sourceforge.net/>`_ se používá v množství dalších programů
(např. Inkscape). Má jiné možnosti vektorize, ale musí se trochu pracovat s
převodem do geografických souřadnic.

.. todo:: Příklad s Potrace. Jedním z problémů pypotrace je, že funguje pouze v
        Python 2.x.

Rasterizace vektorových dat
---------------------------
.. todo:: Modul `rasterio.features <https://mapbox.github.io/rasterio/api/rasterio.features.html>`_
