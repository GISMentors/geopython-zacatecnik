.. _ndvi-algebra:

Rasterová algebra
-----------------

Nástroj srovnatelný s topologickými překryvnými operacemi vektorových dat.
Umožňuje kombinovat rastrové vrstvy pomocí různých matematických operací.
Tyto matematické operace se vykonávají buď na jedné nebo více
vrstvách a jejich výstupem je vrstva nová. Rastrová algebra se často používá pro
prostorové modelování a analýzu.

*Operátory* dělíme na matematické, statistické, relační a logické
operátory (+, -, \*, /, >, <, >=, <=, <>, mod, div, and, or, not,
...).

*Funkce* se dělíme na:

    Lokální
        na individuální buňce, nová hodnota vzniká z jedné rastrové buňky jedné nebo více vrstev.
    Fokální
        v definovaném okolí, nová hodnota vzniká v rámci definovaného okolí buňky
        (např. jako výsledek operace nad "oknem" 3x3 pixely)
    Zonální
        na specifické oblasti, nová hodnota vzniká ze zóny definované v jiné vrstvě.
    Globální
        používají se všechny buňky informační vrstvy (např. analýzy povrchů).

RasterIO využívá pro uložení datový typ `NumPy
<http://www.numpy.org/>`__, což nám umožňuje s těmito datovými
strukturami pracovat standardním způsobem a využívat i pokročilé
nástroje pro analýzu obrazu, jako je `Sciktit Image
<http://scikit-image.org/>`__, `Matplot lib
<https://matplotlib.org/users/image_tutorial.html>`__, `OpenCV
<https://docs.opencv.org/3.0-last-rst/doc/py_tutorials/py_tutorials.html>`__
a další.

V našem příkladu si ukážeme jednoduchou analýzu - **výpočet indexu
NDVI ze satelitních dat**.

.. note:: :wikipedia-en:`Normalizovaný vegetační index
    <Normalized_Difference_Vegetation_Index>` je poměr mezi viditelným
    červeným kanálem a blízkým infračerveným kanálem satelitních dat.

    .. math::
        
         NDVI = (NIR - VIS) / (NIR  + VIS)

Rastr z předchozího příkladu obsahuje barevné kanály (první je černený
kanál, druhý infračervený). Na základě těchto dat vytvoříme nový
soubor s vypočteným NDVI.

Neprve vytvoříme novou matici pro výsledné hodnoty, následně do tohoto
pole uložíme výsledek výpočtu pro každý pixel. Pracujeme v prostředí
NumPy, které práci s poli významně usnadňuje.

.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 16-18

.. code-block:: python

    -0.94444442, 0.97435898

Výsledek uložíme do nově vytvořeného souboru. Data budou zkomprimována
pomocí LWZ komprese a uložena v číselném formátu `float64` (rastrový
soubor obsahuje čísla s plovoucí desetinnou čárkou a záporné
hodnoty). Výsledný soubor ve formátu GeoTIFF bude mít pouze jeden
kanál.

.. literalinclude:: ../../_static/skripty/rasterio-example.py
   :language: python
   :lines: 20-23

.. figure:: ../images/ndvi.png
    
    Výsledný soubor s NDVI indexem.
