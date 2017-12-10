.. _rasterio-reklasifikace:

Reklasifikace
-------------

Reklasifickace je proces nahrazení hodnot pixelů vstupní mapy novými hodnotami
na základě pravidel.

V našem případě si reklasifikujeme naši mapu NDVI indexů, kterou jsme si udělali
v předchozím příkladu :ref:`ndvi-algebra`. 

V našem příkladu chceme dále rozdělit NDVI do tříd podle hodnoty. NDVI nabývá
hodnot od -1 do 1, rozdělíme je na 3 skupiny "od oka":

+---+----------------+---------------+
| 1 | Vegetace       | 1 - 0.3       |
+---+----------------+---------------+
| 2 | Suchá půda     | 0.3 - -0.35   |
+---+----------------+---------------+
| 3 | Voda           | -0.35 - -1    |
+---+----------------+---------------+

.. literalinclude:: ../../_static/skripty/rasterio-reclass.py
   :language: python

Výsledný soubor obsahuje pouze 3 hodnoty reprezentující jednotlivé povrchy.

.. figure:: ../images/ndvi-classes.png
    
    Výsledný soubor se třemi povrchy.
